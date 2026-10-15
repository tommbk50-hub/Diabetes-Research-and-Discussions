# Diabetes Research and Discussions

**Live website:** https://tommbk50-hub.github.io/Diabetes-Research-and-Discussions/

This repository holds the files for a small website about Type 1 Diabetes (T1D) research, written by Thomas Knight.

## How this repo becomes a webpage

The repo uses **GitHub Pages**, GitHub's free website hosting service.

1. **The files are the website.** Every file in this repo can be reached on the web.
   - `index.md` is the home page. It holds the article "The Future of GLP-1 Research" along with its styling.
   - `_config.yml` tells GitHub Pages which site title, description and theme (`jekyll-theme-minimal`) to use.
   - The other `.html` files are separate pages linked from the home page:
     - `breakthrough_t1d_pre_award.html`: grant pre-award instructions
     - `breakthrough_t1d_post_award.html`: post-award instructions and FAQs
     - `grant_roadmap.html`: a visual timeline of the grant lifecycle
     - `cv.html` / `cv.pdf`: the author's CV
   - The images and GIFs (`.jpg`, `.png`, `.gif`) appear on these pages.
2. **GitHub builds the site.** When a change is pushed, GitHub Pages runs a tool called **Jekyll**. Jekyll turns the Markdown and HTML files into a finished website.
3. **The site goes live.** Jekyll publishes the result at the address above, usually within a minute or two.

To update the site, edit a file and commit it. You don't have to run a server or build anything yourself.

### Bonus: automated clinical trial alerts

The repo also has a background job that is separate from the webpage:

- `.github/workflows/scraper.yml` runs `scraper.py` every day at 08:00 UTC through GitHub Actions. You can also start it by hand.
- The script searches the NIHR [Be Part of Research](https://bepartofresearch.nihr.ac.uk/) site for trials that match "Type 1 Diabetes", "VX-880" and "Tegoprubart".
- It posts the trials it finds to a Discord channel. The Discord webhook address is stored in a repository secret named `DISCORD_WEBHOOK_URL`.

## Why the site is useful to diabetes researchers

- **Clear summaries of new therapies.** The site explains GLP-1 drugs in plain language: how they work, their structure, new oral versions and the status of small-molecule drugs as of 2026. It also covers newer T1D approaches, such as stem-cell-derived islet cells (Vertex's VX-880), encapsulated islets and teplizumab.
- **Grant guidance in one place.** Pre-award instructions, post-award FAQs, a grant lifecycle roadmap and a link to the grant handbook are gathered together. This helps applicants and research offices work with Breakthrough T1D funding.
- **Routes into research.** The site links to Breakthrough T1D UK, to clinical trial information and to pages where people can check whether they can join a trial.
- **Easy to share.** Every article has a "Save as PDF" button, so it can be printed or circulated.
- **Up-to-date trial monitoring.** The daily scraper flags relevant UK trials without anyone having to search by hand.
