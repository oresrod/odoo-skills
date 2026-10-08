---
name: odoo-v14-web-guidelines
description: "Desarrolla o modifica frontend de addons para Odoo 14.0: JavaScript, widgets/componentes, templates cliente, SCSS, assets y pruebas web. Úsala cuando el destino sea Odoo 14; excluye imágenes y librerías vendorizadas."
metadata:
  odoo-version: "14.0"
  specialty: web-guidelines
---

# Odoo 14.0: Web

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

## Desarrollo web

Determina si trabajas en el webclient, website/portal, POS o un componente
embebido: sus puntos de extensión y bundles pueden diferir incluso en la misma
versión. Sigue el framework y las pruebas usados por ese subsistema.

| Referencia | Leer cuando |
| --- | --- |
| [JavaScript y plantillas](references/web/javascript.md) | Componentes, widgets, servicios, registries o patches |
| [Assets](references/web/assets.md) | Añades JS, XML, estilos, fuentes o librerías |
| [SCSS](references/web/scss.md) | Cambias estilos |
| [Auditoría](references/security-audit.md) | HTML dinámico, RPC o datos sensibles |

Comprueba carga del bundle, resolución de imports y plantillas, comportamiento y
ausencia de errores de consola en el cliente de destino. Ejecuta el runner de esa
serie y los tests relacionados si están disponibles. Un linter no valida el
registro de un componente ni el renderizado de una vista.
