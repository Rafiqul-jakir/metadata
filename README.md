# ResearchMeta Data – static website (GitHub Pages)

## 1. Deploy
1. Create a GitHub repository (e.g. `researchmeta`). 2. Upload every file in this folder (keep the `es/ fr/ it/ de/ assets/` folders). 3. Settings → Pages → Source: "Deploy from a branch" → `main` / root → Save.
4. Your URL: user/organization site (repo named `USERNAME.github.io`) → `https://USERNAME.github.io`; project site (any other repo) → `https://USERNAME.github.io/REPO-NAME`. GitHub shows the final URL on the Pages settings screen.

## 2. Set the real URL (required for SEO)
Your site is configured for `https://rafiqul-jakir.github.io/metadata` (default in `build.py`), so you only need to re-run `python build.py` after edits. Keywords per language are in the `kw` lists in `build.py`.

Canonical, hreflang, Open Graph, JSON-LD, `sitemap.xml` and `robots.txt` contain a placeholder until you build. Run once with your real URL (no trailing slash):

    python build.py https://USERNAME.github.io/REPO-NAME

(or `python build.py https://USERNAME.github.io` for a user site). This regenerates all five pages, sitemap and robots.txt. Asset links are relative, so both deployment types work. Re-run the command after any edit to `build.py`.

## 3. Editing
- **Text/translations, prices display, stats, FAQ:** edit the `T` dictionary, `PRICES`, `RECS`, `STATS` in `build.py`, then rebuild. Email subject/body templates are in `T[lang]["subj"/"body"]`.
- **Package prices used in the generated email:** `P` object at the top of `script.js` (change it too).
- **Sample records + demo download:** run `python make_data.py your-file.csv` (comma-separated UTF-8 CSV). It writes `data.js` (the table) and `assets/sample-data.csv` (the download button file). Columns shown/downloaded are listed in `COLS` in `make_data.py`; if you change them, also change the header list in `build.py` (search `published_date`) and rebuild.
- **Default inquiry message:** `dm` key in `T`; used whenever the visitor leaves Message empty.
- **Contact email:** change `EMAIL` in `build.py` and rebuild.
- **Licensing/legal text:** `lic`, `disc`, `fd` keys in `T`.
- **Colors per language:** `[data-theme=xx]` variables in `styles.css`.

## 4. Inquiry system
The form only runs in the visitor's browser. It builds a subject and message, offers copy buttons and a `mailto:` link. Nothing is sent or stored; the visitor sends the email themselves.

## 5. Google Search Console
Search Console → Add property → "URL prefix" with your final URL → verify (HTML tag: paste the meta tag into the `<head>` template in `build.py`, rebuild, upload; or upload the HTML verification file) → Sitemaps → submit `sitemap.xml`. Rankings are not guaranteed.
