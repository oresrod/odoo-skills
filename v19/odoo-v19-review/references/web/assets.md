# Bundles y recursos

Consulta la declaración de assets del perfil y los bundles reales de la serie.
En Odoo 14 comprueba herencia XML y la clave `qweb`; desde 16 usa el diccionario
`assets` del manifest y operaciones de ordenación sólo cuando hagan falta.
No supongas que website, backend, POS y tests comparten bundle.

Comprueba dependencias entre módulos, orden de carga y exports; los comodines
pueden incorporar archivos no deseados. Valida con assets de desarrollo y con el
modo habitual de empaquetado del proyecto si la modificación afecta carga.

Incluye recursos y licencias de terceros según la política del proyecto. No cambies
vendored/minificados por preferencias de estilo. Los recursos remotos requieren
una razón funcional y considerar disponibilidad y privacidad, no una prohibición
universal para cualquier integración.
