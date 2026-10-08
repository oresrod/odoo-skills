---
name: odoo-v18-guidelines
description: "Desarrolla o modifica addons backend para Odoo 18.0: Python, ORM, campos, vistas, datos, controladores y pruebas. Úsala cuando el destino sea Odoo 18; para archivos static utiliza la especialidad web de esa versión."
metadata:
  odoo-version: "18.0"
  specialty: guidelines
---

# Odoo 18.0: Backend

## Confirmar el destino

Lee primero [el perfil de esta versión](references/version.md). Identifica el core
que utiliza el proyecto mediante `odoo/release.py`, la rama y los manifests de los
addons afectados. El nombre de una carpeta o `master` no demuestra una versión.
Si sólo hay addons, contrasta el prefijo del manifest con CI, contenedor y
dependencias; si las señales discrepan, pide el destino antes de elegir una API.
En una migración identifica por separado origen y destino y aplica este perfil al
destino. No apliques simultáneamente perfiles de distintas versiones al mismo código.

El código de la revisión instalada prevalece sobre el perfil: los backports y
forks pueden modificar una API dentro de la misma serie. Confirma firmas,
exports, campos y XML IDs en ese checkout antes de usarlos. Consulta documentación
de la serie exacta cuando falte el core; declara lo que no puedas verificar.
No deduzcas requisitos de Python/PostgreSQL por memoria: revisa `release.py`,
`requirements.txt`, CI y la imagen del proyecto.

Estas instrucciones sirven para Community, Enterprise, OCA y addons propios.
Respeta las convenciones del repositorio y su alcance; no presupongas una segunda
mitad Enterprise, módulos instalados, datos demo ni herramientas privadas de Odoo.
La política de contribución al core estable no prohíbe nuevas funcionalidades en
un addon propio para esa misma versión.

Lee sólo las referencias de los dominios afectados. Al terminar, indica la versión
y los cambios o hallazgos relevantes, las comprobaciones ejecutadas y las
limitaciones reales. No presentes una comprobación estática como prueba de
instalación o ejecución en Odoo.

## Desarrollo backend

Implementa el comportamiento solicitado conservando los contratos de herencia,
datos y seguridad del proyecto. Comprueba los consumidores en los `addons_path`
disponibles antes de cambiar nombres, firmas o XML IDs. Usa la variante de API
del perfil, no una traducción mecánica del código de otra versión.

| Referencia | Leer cuando |
| --- | --- |
| [Estructura](references/guidelines/module_structure.md) | Creas o reorganizas un addon |
| [Manifest](references/guidelines/manifest.md) | Cambias dependencias, datos o assets |
| [Python y traducciones](references/guidelines/python.md) | Escribes Python |
| [ORM](references/guidelines/orm.md) | Cambias búsquedas, computes, CRUD o transacciones |
| [Campos](references/guidelines/fields.md) | Defines o modificas campos |
| [Controladores](references/guidelines/controllers.md) | Defines o extiendes rutas |
| [XML](references/guidelines/xml.md) | Vistas, acciones y datos |
| [Informes](references/guidelines/reports.md) | QWeb o informes SQL |
| [Permisos](references/guidelines/security.md) | ACL, reglas o datos sensibles |
| [Rendimiento](references/guidelines/performance.md) | Consultas en bucles, lotes o agregaciones |
| [Pruebas](references/guidelines/tests.md) | Regresión y validación de comportamiento |
| [Comentarios](references/guidelines/comments.md) | Documentas una decisión o un mensaje |
| [Compatibilidad y migración](references/guidelines/stable.md) | Actualizaciones, portabilidad o core estable |
| [Auditoría](references/security-audit.md) | Cambias un límite de confianza o investigas seguridad |

Para JavaScript, plantillas Owl y SCSS utiliza la especialidad web de esta misma
versión, si está instalada. Esta skill contiene todas sus referencias backend y
puede instalarse por separado.
