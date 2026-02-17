#!/usr/bin/env python3
"""
Build a static website (output-only notebook rendering) + Colab links.

Usage:
  python tools/build_site.py

This will:
  - Convert all notebooks in ./content to HTML (inputs hidden)
  - Write pages into ./site (GitHub Pages artifact)
"""
from __future__ import annotations

import html
import shutil
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter

REPO_SLUG = "Uddiptaatwork/astro-ii-ss2026-ethz"
BRANCH = "main"

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
SITE = ROOT / "site"

DESC = {
    "00_hubble_reenactment": "Recreate the logic behind the first Hubble diagram by computing redshifts and distances from observables, then fitting H₀ and exploring systematics.",
    "01_comoving_coordinates": "Build intuition for comoving vs proper coordinates, Hubble flow, and peculiar velocity using interactive visualisations.",
    "02_cosmic_fate": "Explore Friedmann cosmology by numerically evolving a(t) under different Ω parameters and classifying the Universe’s fate.",
}

CSS = """
:root { --fg:#111; --muted:#555; --bg:#fff; --link:#0b57d0; --card:#f6f7f9; --border:#e5e7eb; }
@media (prefers-color-scheme: dark){
  :root { --fg:#eaeaea; --muted:#b7b7b7; --bg:#0b0c10; --link:#7ab7ff; --card:#141622; --border:#2a2d3a; }
}
body{ margin:0; font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; background:var(--bg); color:var(--fg); line-height:1.55;}
header{ padding:28px 20px; border-bottom:1px solid var(--border); background:linear-gradient(180deg,var(--card),var(--bg));}
.container{ max-width: 1000px; margin: 0 auto; padding: 0 16px;}
h1{ margin:0 0 6px 0; font-size: 28px;}
p.lead{ margin: 0; color: var(--muted); }
main{ padding: 22px 0 60px 0;}
.grid{ display:grid; grid-template-columns: repeat(auto-fit,minmax(260px,1fr)); gap:14px;}
.card{ border:1px solid var(--border); background:var(--card); border-radius:14px; padding:16px;}
.card h2{ margin:0 0 6px 0; font-size:18px;}
.card p{ margin:0 0 12px 0; color:var(--muted);}
a{ color:var(--link); text-decoration:none;}
a:hover{ text-decoration:underline;}
.btnrow{ display:flex; gap:10px; flex-wrap:wrap;}
.btn{ display:inline-block; padding:8px 12px; border-radius:10px; border:1px solid var(--border); background:var(--bg); }
.btn.primary{ background: var(--link); color: white; border-color: transparent; }
footer{ border-top:1px solid var(--border); padding: 18px 0; color: var(--muted); font-size: 13px;}
.nav{ display:flex; gap:12px; align-items:center; margin: 14px 0; }
.badge img{ height: 20px; vertical-align: middle; }
"""

def title_from_stem(stem: str) -> str:
    words = stem.replace("_", " ").title()
    return words

def main() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "labs").mkdir(parents=True, exist_ok=True)
    (SITE / "assets").mkdir(parents=True, exist_ok=True)
    (SITE / "assets" / "style.css").write_text(CSS, encoding="utf-8")

    exporter = HTMLExporter()
    exporter.exclude_input = True
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True
    exporter.embed_images = True

    labs = []
    for nb_path in sorted(CONTENT.glob("*.ipynb")):
        nb = nbformat.read(nb_path, as_version=4)
        body, _resources = exporter.from_notebook_node(nb)
        title = nb.metadata.get("title") or title_from_stem(nb_path.stem)
        colab_url = f"https://colab.research.google.com/github/{REPO_SLUG}/blob/{BRANCH}/content/{nb_path.name}"

        wrapped = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{html.escape(title)} — Astro II SS2026</title>
<link rel="stylesheet" href="../assets/style.css"/>
</head>
<body>
<header>
  <div class="container">
    <div class="nav">
      <a class="btn" href="../index.html">← Course home</a>
      <a class="btn primary" href="{colab_url}" target="_blank" rel="noopener">Open in Google Colab</a>
      <span class="badge"><a href="{colab_url}" target="_blank" rel="noopener">
        <img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/>
      </a></span>
    </div>
    <h1>{html.escape(title)}</h1>
    <p class="lead">Interactive lab notebook (rendered view). Use Colab link above to run and modify code.</p>
  </div>
</header>
<main>
  <div class="container">
    {body}
  </div>
</main>
<footer>
  <div class="container">Astro II (SS2026), ETH Zürich — maintained by Uddipta Bhardwaj.</div>
</footer>
</body>
</html>"""
        (SITE / "labs" / f"{nb_path.stem}.html").write_text(wrapped, encoding="utf-8")
        labs.append((nb_path.stem, title, f"labs/{nb_path.stem}.html", colab_url))

    # index.html
    def nice_lab_title(stem: str, title: str) -> str:
        if stem.startswith("00_"): return "Lab 0: " + title.replace("00 ", "")
        if stem.startswith("01_"): return "Lab 1: " + title.replace("01 ", "")
        if stem.startswith("02_"): return "Lab 2: " + title.replace("02 ", "")
        return title

    cards = []
    for stem, title, view, colab in labs:
        desc = DESC.get(stem, "Interactive lab notebook.")
        cards.append(f"""
      <div class="card">
        <h2>{html.escape(nice_lab_title(stem, title))}</h2>
        <p>{html.escape(desc)}</p>
        <div class="btnrow">
          <a class="btn" href="{view}">View (static)</a>
          <a class="btn primary" href="{colab}" target="_blank" rel="noopener">Open in Colab</a>
        </div>
      </div>
        """.strip())

    index = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Astro II — SS2026 (ETH Zürich) | Interactive Cosmology Labs</title>
<link rel="stylesheet" href="assets/style.css"/>
</head>
<body>
<header>
  <div class="container">
    <h1>Astro II — SS2026 (ETH Zürich)</h1>
    <p class="lead">Interactive cosmology labs (static web pages + one-click Google Colab notebooks).</p>
  </div>
</header>

<main>
  <div class="container">
    <div class="card" style="margin-bottom:14px;">
      <h2>How to use this site</h2>
      <p>Each lab is available in two formats:</p>
      <ul>
        <li><strong>View</strong>: a clean, static HTML rendering (no code shown, outputs + explanations only).</li>
        <li><strong>Open in Colab</strong>: run the notebook interactively in your own Google account (recommended).</li>
      </ul>
      <p><em>Tip:</em> In Colab, use <code>Runtime → Run all</code> to execute everything, then play with the sliders.</p>
    </div>

    <div class="grid">
      {"".join(cards)}
    </div>
  </div>
</main>

<footer>
  <div class="container">
    Maintainer: Uddipta Bhardwaj · ETH Zürich · Repo: <a href="https://github.com/{REPO_SLUG}" target="_blank" rel="noopener">{REPO_SLUG}</a>
  </div>
</footer>
</body>
</html>
"""
    (SITE / "index.html").write_text(index, encoding="utf-8")
    print(f"Built site into: {SITE}")

if __name__ == "__main__":
    main()
