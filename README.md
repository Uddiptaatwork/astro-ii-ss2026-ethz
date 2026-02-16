# Astro II — Interactive Cosmology Labs (JupyterLite)

This repo contains two lightweight, fully in-browser interactive notebooks suitable for **static hosting** (e.g. GitHub Pages) via **JupyterLite**.

## Included notebooks
1. **Comoving coordinates explorer** — proper vs comoving views of an expanding FLRW-like universe.
2. **Cosmic fate explorer** — vary Ωm, ΩΛ (and implied Ωk) and see a(t), fate classification, and key timescales.

## Deploy to GitHub Pages (recommended)
1. Create a GitHub repo and push this folder.
2. In GitHub, enable Pages for the `gh-pages` branch (Settings → Pages).
3. The included GitHub Action builds a static JupyterLite site and publishes it to `gh-pages`.

Your site will be available at:

`https://<your-username>.github.io/<repo-name>/`

## Local build (optional)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install jupyterlite
jupyter lite build --contents content --output-dir dist
python -m http.server --directory dist 8000
```

## Notes
- The notebooks use only **NumPy + Matplotlib + ipywidgets** (no SciPy), so they run comfortably in Pyodide.


## Why `environment.yml`?
This deployment uses the **xeus-python** kernel so that packages like `ipywidgets` can be **pre-installed** at build time (and the matching JupyterLab extensions are bundled automatically). This is the most reliable way to make widgets work in a static JupyterLite site.
