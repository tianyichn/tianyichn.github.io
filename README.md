# ATOM Lab website

Static site for the Advanced Thermophysical and Operando Mechanics Lab,
built with Jekyll and hosted on GitHub Pages (no plugins, no build step to run yourself).

## Publish it
1. Create a GitHub repository and upload everything in this folder (except `_site/`).
2. Repository **Settings → Pages → Build and deployment**: Source = "Deploy from a branch", Branch = `main`, folder `/ (root)`.
3. If the repository is not named `<username>.github.io`, set `baseurl: "/<repo-name>"` in `_config.yml`.
4. The site appears at the URL shown on the Pages settings screen within a minute or two.

## Where to edit what
| To change… | Edit |
|---|---|
| Email, address, Scholar/LinkedIn links, request form | `_config.yml` |
| A service (specs, samples, turnaround, availability) | `_services/<name>.md` |
| Mark an instrument down or limited | `status:` and `status_note:` in its `_services` file |
| Add a new service | copy a file in `_services/`, change `title` and `order` |
| Group members and alumni | `_data/people.yml` |
| Research themes | `_data/research.yml` |
| Process, shipping, radioactive samples, FAQ | `how-it-works.md` |
| Homepage image | replace `assets/img/hero.jpg` (16:9, shown in grayscale) |

Search the project for `TODO` to find everything that still needs real content.

## Request form
Create a form (e.g. Microsoft Forms, Google Forms or Qualtrics through your OSU account)
that saves responses to a spreadsheet and notifies the shared lab inbox, then paste its
link into `request_form_url` in `_config.yml`. Until then, the page shows a pre-filled email button.

## Preview locally (optional)
`bundle exec jekyll serve` or `jekyll serve`, then open http://localhost:4000.
