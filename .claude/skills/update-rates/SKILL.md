---
name: update-rates
description: Refresh the service rates on the ATOM Lab website from the OSU fee book (fees.oregonstate.edu). Use when the owner asks to update, check, sync or add costs, prices, rates or fee items, or mentions fee book IDs.
---

# Update rates from the OSU fee book

The rates table on the "How it works" page is generated from `_data/rates.json`.
`tools/update_rates.py` reads the public OSU fee book and rewrites only the
`rate`, `unit` and `checked` fields in that file. Never type a rate by hand.

## Steps

1. From the repository root, compare without saving:
   `python3 tools/update_rates.py`
2. Show the owner every `CHANGED` line (old rate, new rate, fee book title).
   If nothing changed, say so and stop unless they want the "last checked" date refreshed.
3. Save: `python3 tools/update_rates.py --write`
4. Run `jekyll build` (or use the running preview) and confirm the table on
   `/how-it-works/#rates` shows the new figures.
5. Do not commit or push unless the owner asks.

## Adding, removing or changing a row

Edit the `items` list in `_data/rates.json`, then run the steps above.

- `fee_id`: the fee book ID the owner gives you.
- `label`: the wording shown on the site. Ask the owner; do not copy the fee book title blindly.
- `pick`: `"high"` or `"low"`, which end of a range such as `$120.00 - $300.00/Hour` to show.
  The owner's default is the higher (general user) rate.
- `role`: use instead of `pick` for the hourly worker rates fee (16587), whose description
  lists `$N/Hr for <role>`. The value must match the role name in the fee description.

Leave `rate` and `unit` out of a new item; the script fills them in.

## If the script reports a problem

It saves nothing when any fee cannot be read. Typical causes: a fee ID was retired or
renumbered, the description of fee 16587 was reworded so a `role` no longer matches, or
the fee book page layout changed. Open
`https://fees.oregonstate.edu/Public/BrowseExternal.aspx?ID=<fee id>` to see the current
entry, tell the owner what you found, and fix `_data/rates.json` or the parser in
`tools/update_rates.py` accordingly. Do not guess a rate.
