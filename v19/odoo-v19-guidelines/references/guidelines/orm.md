# Recordsets y contratos

Usa recordsets y prefetch; `if records` expresa existencia. No leas un campo
escalar de varios registros como si fuese singleton. Conserva retornos y firma
de `super()` en CRUD y métodos heredados. Compón dominios mediante la API del
perfil; no introduzcas `Domain`, `Command`, `grouped` o firmas de `_read_group`
sin comprobar su disponibilidad. `_inherits` delega campos, no métodos.

Propaga contexto con `with_context`; evita que `default_*` o claves de un módulo
alteren creaciones ajenas. No uses `odoo.http.request` en lógica de modelos:
cron, shell y pruebas pueden ejecutarla sin petición HTTP.

# Computes y persistencia

Declara dependencias de todos los valores leídos por computes y asigna cada
resultado en todas las ramas. Valora coste y necesidad de `store=True`, contexto,
compañía y permisos. `onchange` es comportamiento de interfaz, no una validación
para imports/RPC. Aplica invariantes en ORM/SQL con la API del perfil.

Usa `@api.model_create_multi` para overrides de creación por lotes cuando el
contrato lo permita. Las constraints Python sólo se disparan bajo sus condiciones
de llamada; valida también campos ausentes cuando el negocio lo requiera. Las
garantías de unicidad concurrente necesitan una restricción de base de datos.

# Transacciones

El framework gestiona la transacción de una petición. No añadas commits o rollbacks
manuales para ocultar errores; usa savepoints para recuperación localizada y
captura excepciones específicas. Los cursores propios y API documentadas de cron
por lotes requieren analizar su contrato y reintentos. Evita efectos externos
duplicados si la transacción se reintenta.
