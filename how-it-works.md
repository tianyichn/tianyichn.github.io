---
title: How it works
permalink: /how-it-works/
---
<div class="wrap page prose" markdown="1">

# How it works

## From request to results

1. **Submit a request.** Use the [request form]({{ '/request/' | relative_url }}) to describe your material, the measurement you need, how many samples, and your deadline.
2. **Feasibility and quote.** We review the request, may ask a few questions, and email a quote within 3 business days.
3. **Agreement and purchase order.** Oregon State University handles billing. A purchase order, a service agreement or a contract are the preferred ways to set up the work.
4. **Ship samples.** We send shipping instructions with the quote.
5. **Measurement.** We run the work and keep you updated if anything changes.
6. **Results and invoice.** We send your data and a short summary by email and share the files through cloud storage. OSU invoices you after the work is complete.

## Ways to work with us

**Full service.** Our team runs the measurements and delivers data.

**Collaborative research.** For problems that need method development or interpretation, we can work with you as research collaborators, which may lead to joint publications.

## Radioactive and nuclear samples

ATOM Lab is licensed under ORE90005 to receive, process and ship radioactive materials. The lab is authorized to handle radioactive materials up to 750 mR/h on contact. Contact us if you need to work with higher-activity materials or materials with atomic number greater than 84; these are approved case by case.

Please contact us **before** shipping any radioactive sample.

## Rates

Work is billed at Oregon State University's published external fee rates. Instrument time and staff time are charged separately, so a quote combines the instrument hours and the labor needed for your samples.

<table class="rates">
<thead><tr><th>Service</th><th>Rate (general users)</th></tr></thead>
<tbody>
{% for rate_row in site.data.rates.items %}<tr><td>{{ rate_row.label }}</td><td>{{ rate_row.rate }} per {{ rate_row.unit }}</td></tr>
{% endfor %}</tbody>
</table>

Lower rates apply to government users for some services. Rates are set by OSU and may change; the current figures are in the [OSU fee book]({{ site.data.rates.source_url }}) under index ENS201. Last checked against the fee book on {{ site.data.rates.checked | date: "%B %-d, %Y" }}.

## Data and confidentiality

Data and a short summary are sent by email, with the full files shared through cloud storage. We keep your samples, data and results confidential, and we can sign a non-disclosure agreement (NDA) on request.

## Acknowledging our work

If our data appear in a publication or report, please include this acknowledgment:

> Part of this work was performed at the Advanced Thermophysical and Operando Mechanics (ATOM) Lab in the School of Nuclear Science and Engineering at Oregon State University.

## Frequently asked questions

**Do you work with industry?** Yes. Industry, national laboratory and academic users are all welcome.

**Do you accept non-radioactive samples?** Yes. Most of our instruments are used for both radioactive and non-radioactive materials, and non-radioactive work needs no special approval. Every sample leaving our facility is rigorously surveyed for radiological contamination before it is released and returned to the customer.

**How much does it cost?** See the [rates](#rates) above. Your quote will state the estimated instrument and staff hours for your samples.

**Can I attend the measurement?** Yes. You are welcome to attend; let us know when you request a quote so we can schedule it.

</div>
