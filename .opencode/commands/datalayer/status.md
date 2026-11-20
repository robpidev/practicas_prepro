---
description: Muestra la conexión con Jupyter, los notebooks y los kernels
---

Informa del estado de la conexión con Jupyter, de forma breve.

Pasos:

1. Llama a `tools.jupyter.list_notebooks` y di a cuántos notebooks se puede
   llegar y cuál está activo.
2. Llama a `tools.jupyter.list_kernels` e indica qué kernels están en marcha.
3. Si alguna llamada falla por conexión, di exactamente qué error se produjo y
   recuerda que hay que arrancar JupyterLab desde la raíz del repositorio con
   `.venv/bin/jupyter lab --port 8888 --IdentityProvider.token practicas-prepro-local`;
   no reintentes la llamada.

Que ocupe pocas líneas. Esto es una comprobación de estado, no un informe.
