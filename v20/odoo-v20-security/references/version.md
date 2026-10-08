# Perfil Odoo 20.0

Usa este perfil únicamente para el destino 20.0. Verificación: 2026-10-07, core
`43300b310feb054e14d6b90dcba55cec9d7e5017`. Las skills originales procedían de
reglas orientadas a `master`; este perfil las contrasta con 20.0. `master` puede
avanzar a otra serie y no es sinónimo permanente de 20.

## Backend

- Usa exports públicos y verifica la implementación en `odoo/orm/`.
  `fields.Domain`, `fields.Command`, `models.Constraint`, `models.Index` y
  `models.UniqueIndex` están disponibles. Constraints/índices son atributos cuyo
  nombre empieza por `_`; `_sql_constraints` no está soportado en esta revisión.
- Para agregados backend usa `_read_group`, con tuplas y recordsets en grupos
  relacionales. **`read_group` existe, pero su contrato cambió:** recibe
  `domain, groupby, aggregates, having, ...` y devuelve tuplas con IDs
  serializables. No le pases `fields, groupby, lazy` ni desempaquetes diccionarios
  del API antiguo. Para resultados formateados revisa `formatted_read_group`.
- Usa `display_name`/`_compute_display_name`, `self.env._` y `@api.private` según
  el contrato. Verifica overrides, métodos de búsqueda de campos y API de
  consultas; las internals de `_search`/Query/TableSQL pueden cambiar entre series.

## Vistas y QWeb

Usa `list`, `view_mode="list,form"` y expresiones directas de modificadores;
no `attrs`/`states`. En QWeb servidor usa `t-out`: los compiladores de `t-esc`
y `t-raw` antiguos no están en esta revisión. No extiendas esa conclusión a
14/16/18/19 ni a toda variante de Owl sin comprobar el compilador correspondiente.

## Seguridad

El modelo unificado es `ir.access`, en `security/ir.access.csv`, con columnas
`id,name,model_id,group_id/id,operation,domain`. En estos CSV `model_id` contiene
el nombre técnico, por ejemplo `library.book`, mientras que `group_id/id` usa el
XML ID del grupo. No pegues la referencia `model_library_book` de una ACL antigua
en esa columna. `operation` es un conjunto de letras `crud`:
`r`, `cru`, `crud`, etc.; `u` representa escritura.

- Con grupo, una fila concede permisos sobre su dominio; las concesiones se unen.
- Sin grupo, es una restricción que se intersecta con el acceso concedido.
  **Una fila sin grupo no concede acceso**, al contrario que una ACL antigua.
- Sin concesiones, se deniega. `base.group_everyone` incluye usuarios públicos
  y portal: revisa cualquier concesión y especialmente modificaciones.
- Una restricción sólo limita las operaciones declaradas. Una restricción de
  lectura no evita escrituras autorizadas por otra fila.
- Para multiempresa usa restricciones de compañía; incluye registros sin
  compañía sólo cuando el negocio los admita y verifica el contexto disponible.

No migres ACL/reglas antiguas renombrando sólo el CSV. Reproduce las concesiones
y restricciones efectivas con pruebas por actor y operación. Los comandos x2many
bajo `sudo` pueden afectar comodelos; revisa el mecanismo `_allow_sudo_commands`
sin asumir que reemplaza la validación de payloads.

## Controladores

El paquete HTTP está dividido en `odoo/http/`. Rutas `http`, `jsonrpc` y `json2`
según dispatcher. `auth='bearer'` exige `bearer_scope` en la revisión contrastada.
Verifica alcance del token y exposición real. Vuelve a decorar overrides y
comprueba restricciones al cambiar `type`/`readonly`; no dependas de advertencias
o mecanismos de compatibilidad como contrato universal.

## Frontend y pruebas

El Owl incluido en el checkout es **3.0.0-alpha.49**. Comprueba los exports y
ejemplos de ese commit; no trasplantes reactividad, hooks, servicios ni templates
de Owl 2 mecánicamente. `computed` está disponible aquí, pero no es una regla
aplicable a todas las versiones. El patch mantiene `patch(target, extension)`
con `super` nativo. Usa bundles del manifest y pruebas HOOT del subsistema.

Los tests backend parten de `standard, post_install`. Para ejecutar al instalar
usa `@tagged('at_install', '-post_install')` cuando se requiera. Comprueba helpers
`BaseCommon`/usuarios demo y colección de métodos heredados en la revisión antes
de usarlos; definir una subclase no garantiza que corran los tests heredados.

## Fuentes de la revisión

- [Release](https://github.com/odoo/odoo/blob/43300b310feb054e14d6b90dcba55cec9d7e5017/odoo/release.py)
- [ORM y nuevo read_group](https://github.com/odoo/odoo/blob/43300b310feb054e14d6b90dcba55cec9d7e5017/odoo/orm/models.py)
- [Permisos unificados](https://github.com/odoo/odoo/blob/43300b310feb054e14d6b90dcba55cec9d7e5017/odoo/addons/base/models/ir_access.py)
- [Rutas](https://github.com/odoo/odoo/blob/43300b310feb054e14d6b90dcba55cec9d7e5017/odoo/http/routing_map.py)
- [Owl incluido](https://github.com/odoo/odoo/blob/43300b310feb054e14d6b90dcba55cec9d7e5017/addons/web/static/lib/owl/owl.js)
- [Pruebas](https://github.com/odoo/odoo/blob/43300b310feb054e14d6b90dcba55cec9d7e5017/odoo/tests/common.py)
