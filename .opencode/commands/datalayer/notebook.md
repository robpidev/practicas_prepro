---
description: Abre un notebook de Jupyter y trabaja en él
---

Conecta a un notebook del servidor Jupyter local y conviértelo en el notebook
de trabajo.

Pasos:

1. Llama a `tools.jupyter.list_notebooks` para ver a qué notebooks se puede
   llegar.
2. Si `$ARGUMENTS` está vacío, muestra la lista y pregunta cuál abrir. En caso
   contrario elige el notebook cuyo nombre o ruta encaje mejor con
   `$ARGUMENTS`; si hay varios candidatos, lístalos y pregunta en vez de
   adivinar.
3. Llama a `tools.jupyter.use_notebook` con un alias corto y estable y la ruta
   del notebook.
4. Llama a `tools.jupyter.read_notebook` en formato breve y resume su
   contenido: cuántas celdas tiene, de qué trata y dónde se detuvo la última
   ejecución.

No crees un notebook salvo que te lo pidan. Si nada coincide, dilo y muestra lo
disponible.
