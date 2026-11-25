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

## Servidor Jupyter para el MCP

El servidor MCP `jupyter` definido en `opencode.json` **no es autónomo**: necesita
un Jupyter Server escuchando en `http://localhost:8888` con el token configurado
en ese mismo archivo. Si no está levantado, el proceso MCP se queda esperando al
arrancar su kernel y OpenCode acaba mostrando
`mcp connect failed ... Request timed out` (≈30 s).

Para levantarlo, **desde la raíz del repositorio** (los paths `data/*.csv` y los
notebooks dependen de ello):

```sh
cd /home/drak/dev/practicas_prepro
TOKEN=$(python -c 'import json; print(json.load(open("opencode.json"))["mcp"]["servers"]["jupyter"]["environment"]["JUPYTER_TOKEN"])')
nohup .venv/bin/jupyter lab --no-browser --port=8888 \
  --ServerApp.root_dir=/home/drak/dev/practicas_prepro \
  --IdentityProvider.token="$TOKEN" > /tmp/jupyter-lab.log 2>&1 &
echo $! > /tmp/jupyter-lab.pid
```

El token se lee directamente de `opencode.json`: no copiarlo en comandos ni en
documentación. Verificar y reconectar OpenCode:

```sh
curl -s -o /dev/null -w 'HTTP %{http_code}\n' "http://localhost:8888/api/status?token=$TOKEN"
opencode mcp list    # debe mostrar ✓ jupyter connected
opencode reload      # si tras arrancar Jupyter sigue marcado como failed
```

Para detenerlo: `kill $(cat /tmp/jupyter-lab.pid)`.
Logs en `/tmp/jupyter-lab.log`, PID en `/tmp/jupyter-lab.pid`.

Opcional, para que el MCP conecte incluso con Jupyter caído: añadir
`"START_NEW_CODE_SANDBOX": "false"` al bloque `environment` de `opencode.json`
y fijar la versión del paquete (`jupyter-mcp-server==2.2.6` en lugar de
`@latest`). Así el fallo aparece como error de conexión en las herramientas, no
como timeout al arrancar.

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