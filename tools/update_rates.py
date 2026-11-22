#!/usr/bin/env python3
"""Refresh _data/rates.json from the OSU fee book.

    python3 tools/update_rates.py           # compare only, change nothing
    python3 tools/update_rates.py --write   # save the new rates

Each item in _data/rates.json names a fee book ID and how to read it:

    "pick": "high" | "low"   which end to show when the fee book gives a range
                             (a single amount is used as is)
    "role": "Professor"      instead of the amount, read "$N/Hr for <role>"
                             from the fee description (hourly worker rates)

Only "rate", "unit" and "checked" are rewritten. Labels are never touched.
To add a row, add an item with "fee_id", "label" and "pick" or "role".
Uses only the Python standard library.
"""
import datetime
import html
import json
import pathlib
import re
import sys
import urllib.request

DATA = pathlib.Path(__file__).resolve().parent.parent / "_data" / "rates.json"
MONEY = r"\$\s*([\d,]+(?:\.\d+)?)"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def text(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def parse_fees(page):
    """Return {fee_id: {title, description, amount}} for every fee on the page."""
    fees = {}
    for block in page.split('class="groupedFeeListGroup"')[1:]:
        fee_id = re.search(r'class="groupCode">\s*(\d+)\s*:', block)
        title = re.search(r'class="groupTitle">(.*?)</span>\s*</span>', block, re.S)
        desc = re.search(r'class="groupDescription">(.*?)</div>', block, re.S)
        cell = re.search(r'class="feedetail".*?<td[^>]*>(.*?)</td>', block, re.S)
        if fee_id and cell:
            fees[int(fee_id.group(1))] = {
                "title": text(title.group(1)) if title else "",
                "description": text(desc.group(1)) if desc else "",
                "amount": text(cell.group(1)),
            }
    return fees


def money(value):
    number = float(value.replace(",", ""))
    return f"${int(number):,}" if number == int(number) else f"${number:,.2f}"


def read_rate(item, fee):
    """Work out (rate, unit) for one table row from its fee book entry."""
    if "role" in item:
        found = re.search(MONEY + r"\s*/\s*(\w+)\s+for\s+" + re.escape(item["role"]),
                          fee["description"], re.I)
        if not found:
            raise ValueError(f'no "$N/Hr for {item["role"]}" in the fee description')
        unit = "hour" if found.group(2).lower() in ("hr", "hour") else found.group(2).lower()
        return money(found.group(1)), unit
    amounts = re.findall(MONEY, fee["amount"])
    unit = re.search(r"/\s*([A-Za-z ]+)$", fee["amount"])
    if not amounts or not unit:
        raise ValueError(f'cannot read the amount "{fee["amount"]}"')
    values = sorted(amounts, key=lambda a: float(a.replace(",", "")))
    chosen = values[0] if item.get("pick") == "low" else values[-1]
    return money(chosen), unit.group(1).strip().lower()


def main():
    write = "--write" in sys.argv[1:]
    data = json.loads(DATA.read_text(encoding="utf-8"))
    base = data["source_url"]

    fees = {}
    for fee_id in sorted({item["fee_id"] for item in data["items"]}):
        if fee_id not in fees:
            fees.update(parse_fees(fetch(f"{base}?ID={fee_id}")))

    changes, problems = 0, []
    for item in data["items"]:
        fee = fees.get(item["fee_id"])
        if fee is None:
            problems.append(f'{item["fee_id"]} ({item["label"]}): not found in the fee book')
            continue
        try:
            rate, unit = read_rate(item, fee)
        except ValueError as err:
            problems.append(f'{item["fee_id"]} ({item["label"]}): {err}')
            continue
        old = f'{item.get("rate")} per {item.get("unit")}'
        new = f"{rate} per {unit}"
        if old == new:
            print(f'  same     {item["fee_id"]}  {new:<24} {item["label"]}')
        else:
            changes += 1
            print(f'  CHANGED  {item["fee_id"]}  {old} -> {new}   {item["label"]}')
        print(f'           fee book: "{fee["title"]}", {fee["amount"]}')
        item["rate"], item["unit"] = rate, unit

    if problems:
        print("\nCould not read these fees; nothing was saved:")
        for problem in problems:
            print("  " + problem)
        return 2

    print(f"\n{changes} rate(s) changed.")
    if write:
        data["checked"] = datetime.date.today().isoformat()
        DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Saved {DATA.name}.")
    else:
        print("Nothing saved. Run again with --write to save.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
