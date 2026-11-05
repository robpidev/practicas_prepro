# AGENTS.md — practicas-prepro

Prácticas de preprocesado (error analysis & calibration) for a physics lab course.

## Project structure

| Path | What it is |
|---|---|
| `data/*.csv` | Measurement data (caliper, thermometer, gauge blocks). Referenced with relative path `data/` from notebook working dir. |
| `Pide de rey calibracion (Practica).ipynb` | Main practice: caliper calibration with error propagation using sympy. |
| `Pide de rey calibracion (Test).ipynb` | Test variant of the above (same structure, same data). |
| `Regresion de temperatura.ipynb` | Thermometer calibration regression with sklearn. |
| `inf/` | LaTeX report ("Informe de prácticas"), compiled with latexmk + biber (APA style, Spanish). |
| `bernier/` | LaTeX document on measurement error theory (Bernier formalism). |
| `main.py` | Stub — real work lives in the notebooks. |

## Setup

```sh
uv sync          # install deps into .venv (Python ≥3.14 required)
source .venv/bin/activate
```

## Running notebooks

The notebooks must be run from the repo root so that `data/*.csv` relative paths resolve.

```sh
jupyter notebook          # full UI
jupyter nbconvert --to notebook --execute <name>.ipynb   # headless run
```

## Dependencies

pandas, numpy, matplotlib, scikit-learn, sympy, IPython (all pinned in `uv.lock`).

## LaTeX compilation

```sh
cd inf && latexmk main.tex                 # builds main.pdf into inf/build/
cd bernier && latexmk -pdf bernier.tex -outdir=build
```

Do **not** run bare `latexmk` in `inf/`: it also tries to compile the
`c1*.tex` fragments as standalone documents and exits non-zero.

- `inf/.latexmkrc` configures pdf mode, nonstop mode, biber backend, output to `build/`.
- Build artifacts in `build/` are gitignored (`.gitignore` has `**build/`).

## Git

- Branches: `main` (default), `ai` (experimental, currently same as main).
- No CI or pre-commit hooks configured.

## Notes

- All prose/documentation is in **Spanish**; code identifiers are in English.
- `README.md` is empty — doc happens in LaTeX files and notebooks.
- No test framework exists (exercises are notebooks, not unit tests).