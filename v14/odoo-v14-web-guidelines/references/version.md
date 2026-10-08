# Perfil Odoo 14.0

Usa este perfil únicamente para el destino 14.0. Verificación: 2026-10-07, core
`cc0060e889603eb2e47fa44a8a22a70d7d784185`. Los backports requieren comprobar
el checkout del proyecto. Una carpeta `v14` no sustituye esa identificación.

## Backend

- Imports públicos tradicionales: `from odoo import api, fields, models, _`.
  Compón dominios con `from odoo.osv import expression` y
  `expression.AND([domain_a, domain_b])` / `expression.OR(...)`.
- Relaciones x2many: tuplas de comandos; no presupongas `fields.Command`.
  Ejemplos: `(0, 0, vals)` crea, `(4, record_id, 0)` enlaza y
  `(6, 0, ids)` reemplaza todos los enlaces. Un reemplazo no equivale a añadir.
- Declara `_sql_constraints = [('code_unique', 'unique(code)', 'Code must be unique.')]`.
  No uses `models.Constraint`, `models.Index`, `fields.Domain` ni `odoo.tools.SQL`.
- `read_group(domain, fields, groupby, ..., lazy=True)` devuelve diccionarios;
  un grupo Many2one suele llegar como `(id, display_name)` o `False`. No uses
  el contrato moderno de `_read_group` con tuplas/recordsets.
- `name_get` y `name_search` son puntos de extensión válidos. No reemplaces
  automáticamente overrides por `_compute_display_name` de series nuevas.
- Usa `_('Literal')` para traducciones; no copies `self.env._` ni APIs de
  agrupación/prefetch modernas sin verificar soporte.

## Vistas y QWeb

Raíz `tree`, acciones `view_mode="tree,form"`, modificadores dinámicos `attrs`
y `states` donde corresponda. Los campos usados por los modificadores deben
estar disponibles en la vista.

```xml
<tree>
    <field name="state"/>
    <field name="name" attrs="{'readonly': [('state', '=', 'done')]}"/>
</tree>
```

El QWeb clásico usa `t-esc` para texto. `t-raw` existe pero puede introducir XSS;
no lo marques como sintaxis inexistente ni copies `t-out` moderno sin soporte.

## Seguridad

Usa `security/ir.model.access.csv` con cabecera
`id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`.
Las ACL conceden permisos por unión; una ACL sin grupo concede a todos los usuarios.
Las reglas son registros `ir.rule` con `domain_force`: globales se intersectan,
reglas de grupos aplicables se unen dentro del límite global. No hay denegaciones
por poner un permiso ACL a cero; un `perm_*` de regla desactivado significa que
esa regla no se aplica a la operación. Sin regla aplicable, una ACL puede bastar.
Aplica dominios de compañía a las operaciones necesarias. No uses `ir.access`.

## Controladores

Rutas `type='http'` o `type='json'`. Autenticación habitual `user`, `public`, `none`;
no presupongas `bearer`, `bearer_scope`, `jsonrpc` ni `json2`.
Vuelve a decorar overrides. Para comprobar acceso explícito, revisa
`check_access_rights` y `check_access_rule`; no copies `check_access` moderno.

## Frontend y pruebas

- Predominan `odoo.define(..., function (require) { ... })`, widgets legacy y
  QWeb; hay Owl temprano. Sigue el subsistema concreto, no presupongas `@web`,
  `@odoo/owl` ni el sistema de servicios/registries de 16.
- Assets JS/SCSS mediante herencia de bundles XML (por ejemplo
  `web.assets_backend`) cargada en `data`; templates cliente en `qweb` del
  manifest. No uses el diccionario moderno `assets`.
- Extensiones legacy con `.extend`/`.include` según su contrato; no trasplantes
  `@web/core/utils/patch`. Revisa `_super` y el ciclo de vida del widget.
- Backend: `TransactionCase` y `SavepointCase` tienen diferencias reales;
  tags iniciales `standard, at_install`. Para post-instalación:
  `@tagged('-at_install', 'post_install')`. JS: QUnit y tours de esta rama.

## Fuentes de la revisión

- [ORM y agregaciones](https://github.com/odoo/odoo/blob/cc0060e889603eb2e47fa44a8a22a70d7d784185/odoo/models.py)
- [Campos y comandos](https://github.com/odoo/odoo/blob/cc0060e889603eb2e47fa44a8a22a70d7d784185/odoo/fields.py)
- [Manifest web](https://github.com/odoo/odoo/blob/cc0060e889603eb2e47fa44a8a22a70d7d784185/addons/web/__manifest__.py)
- [Pruebas](https://github.com/odoo/odoo/blob/cc0060e889603eb2e47fa44a8a22a70d7d784185/odoo/tests/common.py)
- [Documentación de la serie](https://www.odoo.com/documentation/14.0/)
