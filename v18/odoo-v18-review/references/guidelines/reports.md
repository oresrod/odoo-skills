# Informes

En un reporte personalizado, `_get_report_values` debe proporcionar `docs`,
`doc_ids` y `doc_model` si la plantilla los necesita. Revisa permisos, compañía,
idioma, moneda y zona horaria de los datos entregados.

Para bloques traducidos usa `t-call` con `t-lang`; vuelve a obtener registros con
el idioma adecuado cuando leas campos traducibles. Comprueba HTML/PDF, formato de
papel, assets y motor configurado en el proyecto. No presupongas que la misma
instalación de renderizado sirve para todas las versiones.

En modelos SQL (`_auto = False`) evita IDs inestables/duplicados, duplicación por
joins y agregados incorrectos. El SQL no aplica automáticamente las reglas de
los modelos fuente: analiza acceso y compañías del informe por separado.
