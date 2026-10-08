# Perfil Odoo 19.0

Usa este perfil únicamente para el destino 19.0. Verificación: 2026-10-07, core
`774c073db8500170050b7fd82b6ae4eec4a4f5b9`. No tomes `master` ni 20.0 como
documentación implícita de esta serie.

## Backend

- ORM reorganizado en `odoo/orm/`; usa exports públicos `from odoo import api,
  fields, models`, no rutas internas por costumbre de una versión anterior.
- Dominios con `from odoo.fields import Domain`, operadores `&`, `|`, `~` y
  `Domain.AND/OR`; `odoo.osv` está deprecado. `fields.Command` para x2many.
- Constraints e índices como atributos privados: por ejemplo
  `_code_unique = models.Constraint('UNIQUE(code)', 'Code must be unique.')`.
  El checkout contrastado avisa que `_sql_constraints` ya no está soportado;
  migra y comprueba que la constraint exista en la base, no sólo que arranque.
- Usa `_read_group` para agregación backend. El `read_group` antiguo todavía
  existe en esta revisión, deprecado; no lo declares eliminado. Para salida
  formateada revisa `formatted_read_group` y su contrato.
- `display_name`/`_compute_display_name`, `self.env._`, `odoo.tools.SQL` y
  comprobaciones combinadas de acceso están disponibles. `@api.private` permite
  conservar un nombre Python público sin exponerlo por RPC.
- Revisa firmas de search de campos, operadores normalizados y overrides;
  no traslades el cuerpo de una implementación de 18 sin contrastarlo.

## Vistas

`list`, `view_mode="list,form"`, expresiones directas `invisible`, `readonly`,
`required`. No uses `attrs` ni `states`. Verifica templates `card` e herencias
kanban. QWeb servidor conserva `t-esc` y `t-raw` legado en esta revisión;
prefiere `t-out` y escape correcto, sin confundirlo con el comportamiento de 20.

## Seguridad

**19.0 todavía usa ACL `ir.model.access` y reglas `ir.rule`.** No generes
`ir.access.csv` copiando 20. Cabecera de `security/ir.model.access.csv`:
`id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`.
ACL por unión, sin grupo conceden a todos; reglas globales por intersección y
reglas de grupos por unión dentro del límite global. Un `perm_*` desactivado en
reglas excluye esa operación de la regla; no la deniega. Comprueba compañías y CRUD.

## Controladores e integraciones

Usa `type='jsonrpc'` para rutas JSON-RPC. `type='json'` es alias deprecado en
esta revisión; una alerta de deprecación no implica que la ruta no funcione.
`http` y autenticación `bearer` existen, pero no copies `bearer_scope` obligatorio
ni un dispatcher de controlador `json2` de 20.

La API externa JSON-2 de 19 es una interfaz de integración distinta de renombrar
un controlador a `type='json2'`. Antes de cambiar una integración confirma
autenticación, endpoints y semántica transaccional. No declares eliminadas las
API RPC antiguas sin contrastar la versión y la documentación vigente.

## Frontend y pruebas

Owl 2, assets en manifest, servicios/registries y `patch(target, extension)` con
`super` nativo. No uses `computed` u otros exports de Owl 3 sin soporte.
HOOT para pruebas JS modernas; respeta helpers de la rama y subsistema.

Backend: `TransactionCase`/`HttpCase`; tags iniciales `standard, at_install` en
el checkout verificado, no el valor por defecto de 20. No dependas de datos demo
sin declararlos o crearlos explícitamente.

## Fuentes de la revisión

- [ORM](https://github.com/odoo/odoo/blob/774c073db8500170050b7fd82b6ae4eec4a4f5b9/odoo/orm/models.py)
- [Construcción de modelos](https://github.com/odoo/odoo/blob/774c073db8500170050b7fd82b6ae4eec4a4f5b9/odoo/orm/model_classes.py)
- [ACL](https://github.com/odoo/odoo/blob/774c073db8500170050b7fd82b6ae4eec4a4f5b9/odoo/addons/base/models/ir_model.py)
- [HTTP](https://github.com/odoo/odoo/blob/774c073db8500170050b7fd82b6ae4eec4a4f5b9/odoo/http.py)
- [Pruebas](https://github.com/odoo/odoo/blob/774c073db8500170050b7fd82b6ae4eec4a4f5b9/odoo/tests/common.py)
- [JSON-2](https://www.odoo.com/documentation/19.0/developer/reference/external_api.html)
