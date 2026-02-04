# sergio1817.github.io

Personal academic website for Sergio Edgardo Urzúa Correa.

## Features
- About/Bio, Projects, Publications, and Contact sections
- Modern, responsive design with dark mode toggle
- Downloadable PDF CV
- Automated publication updates from ORCID and GitHub activity
- SEO meta tags, favicon, and analytics

## Setup
1. Clone the repo and install Ruby, Bundler, and Jekyll.
2. Run `bundle install` to install dependencies.
3. Serve locally with `bundle exec jekyll serve`.

## Updating Content
- Edit Markdown files for About, Projects, Publications, etc.
- Update navigation and publications in `_data/`.
- To update publications from ORCID, run `python scripts/fetch_orcid.py`.
- To update GitHub activity, run `python scripts/fetch_github_activity.py`.

## Deployment
- Site auto-deploys via GitHub Actions on push to `main`.
- Data updates run weekly via GitHub Actions.

## Customization
- CSS in `assets/css/custom.css`
- Favicon in `assets/icons/favicon.svg`
- Add your PDF CV to `assets/` and link in navigation.

## License
MIT