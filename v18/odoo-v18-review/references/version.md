# Perfil Odoo 18.0

Usa este perfil únicamente para el destino 18.0. Verificación: 2026-10-07, core
`545d87b1ac621ef9a8ae2b0072a8d66d8e6a1092`. Online 18.x y 19.0 incorporan APIs
que no debes trasladar automáticamente a 18.0.

## Backend

- `fields.Command` para x2many; dominios con `odoo.osv.expression.AND/OR`.
  No importes `fields.Domain` ni `models.Constraint` de 19.
- Declara `_sql_constraints`. Para SQL justificado existe `odoo.tools.SQL`;
  sigue aplicando autorización, flush e invalidación cuando corresponda.
- `_read_group(domain, groupby=(), aggregates=(), having=(), ..., order=None)`
  devuelve tuplas con recordsets en grupos relacionales. `read_group` conserva
  el formato antiguo de diccionarios; no mezcles los contratos.
- `search_fetch`, `fetch`, `grouped` y `self.env._` están disponibles.
  Usa `display_name`/`_compute_display_name`; no introduzcas overrides `name_get`
  de 14/16. Revisa `_search_display_name` y su firma al adaptar búsquedas.
- Para permisos combinados existen `check_access`, `has_access`, `_filtered_access`;
  comprueba qué valida cada operación. El campo agregado usa `aggregator` donde
  ramas antiguas usaban `group_operator`.
- `api.private` aparece en backports del checkout contrastado. Verifica el
  despliegue concreto antes de tratarlo como API universal de 18.0.

## Vistas y QWeb

Usa `list` y `view_mode="list,form"`. `attrs`/`states` ya no son el mecanismo de
modificadores: escribe expresiones directas y considera `parent`, `context` y
campos disponibles en cada subvista.

```xml
<list>
    <field name="state"/>
    <field name="name" readonly="state == 'done'"/>
</list>
```

Revisa XPaths que busquen `tree` y templates kanban: el template raíz moderno
es `card`, frente a `kanban-box` legado. No cambies sólo la etiqueta exterior.
QWeb servidor prefiere `t-out`; `t-esc` permanece en el checkout contrastado.

## Seguridad y controladores

Usa `ir.model.access` e `ir.rule`, no `ir.access`. Cabecera de
`security/ir.model.access.csv`:
`id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`.
ACL se suman y sin grupo conceden a todos; reglas globales se intersectan y
reglas de grupos se unen dentro del límite global. Los flags de reglas indican
aplicación a operaciones, no denegaciones. Verifica reglas de compañía.

Los controladores JSON siguen usando `type='json'`; `type='jsonrpc'` corresponde
a 19. La rama admite autenticación `bearer` y opciones como `readonly`, pero
comprueba sus contratos. No copies el requisito `bearer_scope` ni `type='json2'`
de 20.

## Frontend y pruebas

Owl 2, servicios y registries de `@web`, assets en manifest. No uses reactividad
Owl 3 por analogía. La firma de patch ya es de dos argumentos y usa `super` nativo:

```javascript
/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
patch(Target.prototype, {
    setup() {
        super.setup(...arguments);
        // Inicialización específica de la extensión.
    },
});
```

Importa la clase real en lugar de `Target`; no uses `this._super` ni nombre de
patch de 16. HOOT y `@web/../tests/web_test_helpers` son la base moderna de tests
JS; comprueba los imports exactos y legacy del subsistema. Backend:
`TransactionCase`, `HttpCase`, tags iniciales `standard, at_install`; cambia a
`@tagged('-at_install', 'post_install')` cuando proceda.

## Fuentes de la revisión

- [ORM](https://github.com/odoo/odoo/blob/545d87b1ac621ef9a8ae2b0072a8d66d8e6a1092/odoo/models.py)
- [HTTP](https://github.com/odoo/odoo/blob/545d87b1ac621ef9a8ae2b0072a8d66d8e6a1092/odoo/http.py)
- [Patch JavaScript](https://github.com/odoo/odoo/blob/545d87b1ac621ef9a8ae2b0072a8d66d8e6a1092/addons/web/static/src/core/utils/patch.js)
- [Pruebas](https://github.com/odoo/odoo/blob/545d87b1ac621ef9a8ae2b0072a8d66d8e6a1092/odoo/tests/common.py)
- [Vistas 18.0](https://www.odoo.com/documentation/18.0/developer/reference/user_interface/view_architectures.html)
