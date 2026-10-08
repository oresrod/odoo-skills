# Perfil Odoo 16.0

Usa este perfil únicamente para el destino 16.0. Verificación: 2026-10-07, core
`300925a48debae7c86cb15c17d1b2a6c6f82db8d`. No confundas 16.0 con versiones
Online 16.x ni asumas que todas sus novedades están en 16.0.

## Backend

- Usa `from odoo import api, fields, models, _`. `fields.Command` permite
  `Command.create`, `Command.link`, `Command.set`, etc.; `set` reemplaza la
  relación completa. En payloads RPC se siguen enviando tuplas/listas serializables.
- Compón dominios con `odoo.osv.expression.AND/OR`. No uses `fields.Domain`.
- Usa `_sql_constraints`; `models.Constraint`/`Index` no son la API de esta serie.
  `odoo.tools.SQL` tampoco debe importarse como en 18+.
- `read_group` devuelve diccionarios. El `_read_group` de 16.0 tiene firma antigua
  `(domain, fields, groupby, ..., lazy=True)`, no la de 18. No asumas que
  `search_fetch` de Online 16.2 ni `grouped` estén disponibles en 16.0.
- `name_get` sigue siendo válido. Traduce con `_`; no copies `self.env._` de 18.
  Los campos traducidos usan almacenamiento JSONB: no reutilices SQL sobre
  `ir.translation` de 14 para manipular sus traducciones.
- Algunos checkouts actualizados, incluido el contrastado, incorporan `api.private`.
  Verifica decorador y guardia RPC en el despliegue antes de depender de ese backport.

## Vistas y QWeb

Usa `tree`, `view_mode="tree,form"` y `attrs`/`states`. No migres a la sintaxis
de 18 sólo porque el cliente ya use Owl 2.

```xml
<tree>
    <field name="state"/>
    <field name="name" attrs="{'readonly': [('state', '=', 'done')]}"/>
</tree>
```

En QWeb servidor se prefiere `t-out`; `t-esc` todavía funciona en esta revisión.
`t-raw` es legado/deprecado, no una directiva universalmente inexistente.

## Seguridad y controladores

Usa ACL `ir.model.access` (`security/ir.model.access.csv`) y reglas `ir.rule` con
`domain_force`. Cabecera CSV:
`id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`.
Las ACL se suman; sin grupo conceden a todos. Reglas globales se intersectan,
reglas de grupos se unen; los flags `perm_*` de reglas indican cuándo se aplican,
no una denegación. Comprueba compañías y cada operación. No uses `ir.access`.

Rutas `type='http'` o `type='json'`, con `auth='user'/'public'/'none'` según uso.
No copies `jsonrpc`, `json2` ni `bearer_scope`. Usa las comprobaciones de acceso
presentes (`check_access_rights`, `check_access_rule`) cuando sean necesarias.

## Frontend

- Owl 2 y módulos ES marcados con `/** @odoo-module **/`, imports `@web/...`
  y `@odoo/owl` donde ese subsistema los soporte. Sigue legacy donde aún exista.
- Usa registries, servicios y hooks de esta rama, `useService('orm')` para modelos.
  No añadas `computed` o APIs de Owl 3.
- Firma de patch: `patch(obj, patchName, patchValue, options)`, con nombre único
  por módulo y `this._super`. Si necesitas el padre después de un `await`, conserva
  previamente su función enlazada; `_super` es temporal.

```javascript
/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
patch(Target.prototype, "my_module.target", {
    setup() {
        this._super(...arguments);
        // Inicialización específica de la extensión.
    },
});
```

`Target` representa la clase real importada del subsistema. No uses aquí la firma
de dos argumentos y `super` nativo de 18. Assets y templates cliente se declaran
en `assets` del manifest, en el bundle apropiado.

## Pruebas

`TransactionCase` integra la funcionalidad de savepoints; no añadas
`SavepointCase` deprecado a nuevas pruebas. Tags iniciales `standard, at_install`;
para post-instalación usa `@tagged('-at_install', 'post_install')`. Frontend:
QUnit y helpers/tours propios de 16; no copies tests HOOT de 18.

## Fuentes de la revisión

- [ORM](https://github.com/odoo/odoo/blob/300925a48debae7c86cb15c17d1b2a6c6f82db8d/odoo/models.py)
- [API y backports](https://github.com/odoo/odoo/blob/300925a48debae7c86cb15c17d1b2a6c6f82db8d/odoo/api.py)
- [Patch JavaScript](https://github.com/odoo/odoo/blob/300925a48debae7c86cb15c17d1b2a6c6f82db8d/addons/web/static/src/core/utils/patch.js)
- [Pruebas](https://github.com/odoo/odoo/blob/300925a48debae7c86cb15c17d1b2a6c6f82db8d/odoo/tests/common.py)
- [Documentación de la serie](https://www.odoo.com/documentation/16.0/)
