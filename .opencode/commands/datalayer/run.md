---
description: Ejecuta una celda, o el notebook completo, en Jupyter
---

Ejecuta código en el notebook de Jupyter en el que estamos trabajando.

Pasos:

1. Si no hay notebook activo, ejecuta antes `/datalayer/notebook`.
2. Interpreta `$ARGUMENTS`:
   - un número — ejecuta esa celda con `tools.jupyter.execute_cell`;
   - `all` — lee el notebook y ejecuta las celdas de código en orden;
   - cualquier otra cosa — busca la celda que encaje con la descripción,
     muéstrala y confirma antes de ejecutarla.
3. Informa de lo que produjo cada celda. Si una celda falla, muestra el error y
   propón una solución en lugar de reintentar a ciegas.

Nunca edites una celda para hacerla pasar sin decir qué cambiaste y por qué.
