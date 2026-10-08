# Python y traducciones

Sigue el linter y la versión de Python del proyecto; no presupongas `ruff.toml`
ni sintaxis del intérprete de Odoo 20. Separa stdlib, terceros, imports de Odoo y
addons. Conserva el estilo local en cambios pequeños.

Usa `_compute_*`, `_inverse_*`, `_search_*`, `_check_*` y `action_*` para expresar
el contrato. Un `action_*` no es necesariamente singleton: añade `ensure_one()`
sólo cuando la operación lo exige. Distingue registros de IDs en los nombres.

Traduce literales estáticos: nunca un f-string ni texto interpolado antes de la
búsqueda. Odoo 14/16 emplean `from odoo import _`; en 18/19/20 puede preferirse
`self.env._` dentro de modelos. Usa placeholders y formato admitidos por la rama.
El formato después de `_('literal')` es habitual en código antiguo; no lo declares
un error funcional sin comprobar el caso. No presupongas formato localizado de
listas disponible en todas las versiones.

No resuelvas traducciones al importar módulos. Usa las utilidades lazy existentes
en esa serie cuando haga falta. Los valores de campos traducibles se gestionan con
`translate`, no pasando su contenido dinámico por `_()`.
