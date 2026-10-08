# Campos

- `Many2one` suele terminar en `_id`; `One2many`/`Many2many`, en `_ids`.
  Revisa comodel, inverse, `required`, `ondelete` y moneda de campos Monetary.
- Usa `active`, `company_id` y los campos reservados cuando quieras su semántica.
  Comprueba `_check_company_auto` y `check_company=True` para relaciones que deban
  respetar compañía; no sustituyen a las reglas de acceso.
- Un campo sensible necesita `groups` y permisos del servidor, no sólo invisibilidad
  en una vista. Los related se computan habitualmente con privilegios; comprueba
  `compute_sudo`/`related_sudo` en la rama y desactívalo cuando exponga datos.
- No encadenes x2many en un related esperando una agregación. Define un compute
  explícito para ese contrato. Compartir inverse entre campos puede causar lecturas
  protegidas como `False`; evita depender de ellas.
- Indexa según búsquedas reales, distribución y coste de escritura. Un índice
  parcial sobre un estado puede ser útil; no descartes todos los índices sobre
  campos de baja cardinalidad. Tipos de índice y objetos SQL dependen de la versión.
- Un campo y un método comparten namespace. Un cambio de tipo, almacenamiento o
  nombre necesita evaluar datos existentes y consumidores.
