# Notes for Claude when maintaining this site

- Jekyll site on GitHub Pages (default github-pages Jekyll 3.x). No plugins; keep Liquid compatible with Jekyll 3.
- Content lives in data files: `_config.yml` (contacts, links, form URL), `_services/*.md` (one per service,
  front matter drives the page), `_data/people.yml`, `_data/research.yml`, `_data/nav.yml`.
- Prefer editing data/front matter over editing layouts. Keep one shared style in `assets/css/style.css`.
- Service `status` must be one of: available, limited, offline.
- Do not invent specs, rates, turnaround times or license details; leave `TODO` and ask the owner.
- Liquid gotcha: includes share scope with the caller; never reuse a loop variable name inside an include.
- After changes, run `jekyll build` and check pages render before committing.
