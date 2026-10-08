# Skills para Odoo 14, 16, 18, 19 y 20

Biblioteca especializada por versión para desarrollar y revisar addons Community,
Enterprise, OCA y propios. Conserva las cuatro especialidades de la biblioteca
original de `v20`, separando las reglas comunes de las API de cada serie.

```text
odoo/
├── common/                 # Fuente compartida: flujos y referencias por dominio
├── profiles/               # Diferencias verificadas de cada versión
├── scripts/                # Generación reproducible y validación
├── v14/odoo-v14-*/          # Cuatro skills autónomas
├── v16/odoo-v16-*/
├── v18/odoo-v18-*/
├── v19/odoo-v19-*/
└── v20/odoo-v20-*/
```

Cada versión contiene `guidelines` (backend), `web-guidelines`, `review` y
`security`. Por ejemplo: `odoo-v18-guidelines`, `odoo-v18-web-guidelines`,
`odoo-v18-review` y `odoo-v18-security`. Los nombres únicos permiten instalar
varias versiones sin colisiones. Cada skill incluye perfil, referencias y
metadata `agents/openai.yaml`; no necesita otras skills ni rutas de esta máquina.

## Instalación y uso

Copia **las carpetas completas** de las skills que necesites al directorio de
skills admitido por tu agente. No copies `common/` o `profiles/` como skills ni
el directorio `v18` como si fuese una única skill. Ejemplo en un proyecto que
utiliza `.agents/skills/`, sustituyendo las rutas por las de tu instalación:

```bash
mkdir -p /ruta/al/proyecto/.agents/skills
cp -R /ruta/a/esta/biblioteca/v18/odoo-v18-* /ruta/al/proyecto/.agents/skills/
```

Antes de copiar sobre una instalación existente, revisa si contiene cambios
locales. La ubicación global y el mecanismo de recarga dependen del agente.
No se instala ni modifica ninguna configuración global automáticamente.

Ejemplos de invocación:

- `Usa $odoo-v14-guidelines para crear este módulo en Odoo 14.`
- `Usa $odoo-v16-web-guidelines para extender este componente.`
- `Usa $odoo-v18-review para revisar este diff.`
- `Usa $odoo-v19-security para auditar los permisos de este addon.`
- `Usa $odoo-v20-guidelines para portar este módulo de 19 a 20; identifica origen y destino.`

Las descripciones permiten selección automática por versión y tarea. Si el
destino no está claro, la skill pide identificarlo antes de elegir sintaxis.
En migraciones no se mezclan reglas de origen y destino sobre el mismo archivo.

## Diferencias que evitan contaminación entre versiones

| Área | 14 | 16 | 18 | 19 | 20 verificado |
| --- | --- | --- | --- | --- | --- |
| Listas/modificadores | `tree`, `attrs` | `tree`, `attrs` | `list`, expresiones | `list`, expresiones | `list`, expresiones |
| Permisos | ACL + `ir.rule` | ACL + `ir.rule` | ACL + `ir.rule` | ACL + `ir.rule` | `ir.access` |
| Componer dominios | `expression` | `expression` | `expression` | `Domain` | `Domain` |
| Constraints SQL | `_sql_constraints` | `_sql_constraints` | `_sql_constraints` | `models.Constraint` | `models.Constraint` |
| Ruta JSON-RPC | `json` | `json` | `json` | `jsonrpc` | `jsonrpc` |
| Assets | XML + `qweb` | manifest | manifest | manifest | manifest |
| Frontend principal | Legacy/Owl temprano | Owl 2 | Owl 2 | Owl 2 | Owl 3 del checkout |
| Pruebas JS modernas | QUnit | QUnit | HOOT | HOOT | HOOT |
| Fase backend por defecto | `at_install` | `at_install` | `at_install` | `at_install` | `post_install` |

La matriz es una orientación, no una garantía sobre forks o backports. Cada perfil
registra la revisión examinada y enlaza sus fuentes. El core que ejecuta el
proyecto es la referencia final; `master` no identifica una versión estable.

## Mantenimiento

Edita `common/` para reglas compartidas y `profiles/vNN.md` para diferencias de
versión. Después regenera y valida con Python 3.9+ (sólo biblioteca estándar):

```bash
python3 scripts/build_library.py
python3 scripts/build_library.py --check
python3 scripts/validate_library.py
python3 scripts/test_library.py
```

`--check` no escribe. La generación es determinista y no borra archivos ajenos;
si una referencia se retira de las fuentes, revisa y elimina sus copias obsoletas
que reporte el comando. Las ediciones manuales en `vNN/` se reemplazarán al
regenerar. Para comprobar un paquete copiado por separado:

```bash
python3 scripts/validate_library.py --skill /ruta/a/odoo-v18-review
```

La validación comprueba estructura, nombres, metadata, enlaces internos y
correspondencia con las fuentes. Las pruebas del generador verifican regeneración
sin cambios, copia aislada, referencias rotas y conservación de archivos ajenos.
No certifican instalación de addons ni ejecutan
Odoo. Los cambios de instrucciones se deben contrastar además con casos reales.

## Adaptación del material original

Las reglas originales de backend, web, revisión y seguridad se han reorganizado
en fuentes comunes. Se han sustituido dependencias entre skills por referencias
locales y añadido perfiles contrastados con los cinco checkouts. Las antiguas
carpetas `v20/odoo-*` pasan a `v20/odoo-v20-*`; al actualizar una instalación
antigua evita dejar activas ambas familias con instrucciones contradictorias.

Se han limitado al contexto adecuado las convenciones internas del core:
política estable, puntuación, organización y prohibición de patches. También se
han corregido el tratamiento de XML IDs heredados, las generalizaciones sobre
`t-esc`/`read_group`, la omisión universal de `base` y las API nuevas aplicadas
sin distinguir versiones. No se requiere Enterprise, Runbot ni una herramienta
de lint concreta para utilizar esta biblioteca.
