# Astro II (SS2026, ETH Zürich) — Interactive Cosmology Labs

This repository contains interactive Jupyter notebooks for **Astro II: Extragalactic Astronomy & Cosmology** (ETH Zürich, Spring Semester 2026).

Student-facing access is provided in two ways:

1. **Static web pages (recommended for reading):** clean output-only HTML renderings (markdown + plots; no code cells).
2. **Google Colab (recommended for interaction):** one-click Colab links so students can run and modify notebooks in their own Google accounts.

---

## Live website

After deployment, the site is available at:

`https://Uddiptaatwork.github.io/astro-ii-ss2026-ethz/`

The landing page links to each lab in both formats (View / Open in Colab).

---

## Labs

- **Lab 0 — Hubble reenactment:** compute redshifts and distances from observables, then build a velocity–distance diagram and fit \(H_0\).
- **Lab 1 — Comoving coordinates:** proper vs comoving distance, Hubble flow vs peculiar velocity.
- **Lab 2 — Cosmic fate explorer:** integrate Friedmann evolution \(a(t)\) under different \(\Omega\) parameters and classify outcomes.

Notebooks live in `content/`.

---

## How the website is built

On each push to `main`, GitHub Actions:

1. converts notebooks in `content/` to output-only HTML,
2. writes pages into `site/`,
3. deploys `site/` to GitHub Pages.

The build script is:

- `tools/build_site.py`

If you want to build locally:

```bash
python -m pip install nbconvert nbformat jinja2
python tools/build_site.py
```

---

## Repository layout

```
content/            # notebook sources (.ipynb)
tools/build_site.py # converts notebooks -> static HTML pages
site/               # generated static site (Pages artifact)
.github/workflows/  # CI deployment to GitHub Pages
```

---

## Maintainer

Uddipta Bhardwaj (ETH Zürich)
