# UHNW Family Assistant Portfolio

This folder contains the BeverlyBella Fowler UHNW Family Assistant portfolio website and PDF packet for future UHNW/private family opportunities.

## Contents

- `index.html` - live portfolio website
- `CNAME` - GitHub Pages custom domain configuration for `beverlybella.com`
- `.nojekyll` - tells GitHub Pages to publish the static files exactly as they are
- `docs/UHNW_Family_Assistant_Portfolio.pdf` - portfolio packet
- `src/build_portfolio.py` - script used to build the PDF from the curated source images
- `src/make_contact_sheets.py` - helper script used during image review and curation
- `notes/portfolio_notes.md` - working notes, tone, and update guidance
- `assets/` - optional location for future selected portfolio images or design assets

## Portfolio Direction

The portfolio is intended to feel warm, discreet, capable, and polished. It presents hands-on household support across daily tasks, childcare support, meal preparation, organization, special projects, relocation support, closet organization, and property/lifestyle context.

Contact information is included in the website footer.

## Live Website

This repository is configured for GitHub Pages:

- Repository: `bevbevbella/portfolio`
- Publishing source: `main` branch, repository root
- Custom domain: `beverlybella.com`

Once DNS points to GitHub Pages, every pushed update to `main` will rebuild and update the live website automatically.

Required DNS records for `beverlybella.com`:

```text
Type  Name  Value
A     @     185.199.108.153
A     @     185.199.109.153
A     @     185.199.110.153
A     @     185.199.111.153
CNAME www   bevbevbella.github.io
```

Remove the old `A` record currently pointing to `66.223.49.89` before adding the GitHub Pages records. Large raw photo archives and downloaded Dropbox exports should stay out of the repository unless there is a specific reason to track them.
