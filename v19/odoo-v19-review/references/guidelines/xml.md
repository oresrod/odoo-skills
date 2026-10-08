# Vistas y datos

Usa la raíz y modificadores del perfil: `tree`/`attrs`/`states` en 14/16 frente a
`list` y expresiones directas en 18/19/20. Comprueba también `view_mode`, subviews,
XPaths, templates kanban y claves consumidas por JavaScript. `invisible` en celdas
y `column_invisible` sobre la columna tienen contextos y efectos distintos.

Una vista heredada nueva tiene su propio XML ID y un `inherit_id` que apunta al
padre; no reutilices el XML ID completo del padre, pues actualizarías ese registro.
Algunos módulos usan el mismo nombre local en namespaces distintos: eso sigue
siendo otro XML ID. Usa `mode="primary"` sólo para una variante primaria real.

Ancla herencias en atributos estables y comprueba el XML padre de la serie exacta.
Si un campo aparece varias veces, usa un XPath que desambigüe. Evita posiciones
numéricas frágiles. Conserva los XML IDs existentes cuando haya consumidores.

Usa `noupdate` deliberadamente: afecta actualizaciones de bases existentes. No
asumas que un cambio XML se aplica al reiniciar; verifica instalación y actualización
del módulo. No elimines datos que otros registros referencian sin migración.

Escapa salidas QWeb con la directiva disponible en la serie. Las plantillas Owl
y QWeb del servidor no tienen necesariamente las mismas directivas.
