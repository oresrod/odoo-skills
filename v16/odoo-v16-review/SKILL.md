---
name: odoo-v16-review
description: "Revisa diffs, commits, PRs o módulos destinados a Odoo 16.0, contrastando comportamiento, compatibilidad, backend, frontend y seguridad. Úsala para una revisión de código con destino Odoo 16."
metadata:
  odoo-version: "16.0"
  specialty: review
---

# Odoo 16.0: Revisión

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

## Revisión

1. Delimita diff/base/head, commit o módulo solicitado. Trabaja con el código
   correspondiente a esa revisión; no cambies la rama de trabajo para revisar si
   puedes leerla sin mutaciones. Si sólo recibes un parche, revisa lo demostrable
   y señala qué contexto falta. Lee los manifests afectados.
2. Revisa cada archivo con las referencias pertinentes: [backend](references/backend-index.md),
   [web](references/web-index.md) y [seguridad](references/security-audit.md).
   No conviertas una preferencia de estilo del core en un defecto de un addon.
3. Contrasta las API con el perfil y el core de destino. Sigue overrides,
   XML IDs, imports y productores/consumidores en los addons disponibles.
   Revisa otro repositorio sólo cuando el cambio realmente tenga dependencias allí.
4. Busca un escenario concreto de fallo: recordsets vacíos o múltiples, empresas,
   zonas horarias, redondeo, concurrencia, segundo intento, permisos y actualización
   de una base existente. Comprueba que una prueba de regresión detectaría el fallo.
5. Informa hallazgos accionables ordenados por impacto, con archivo/línea,
   escenario, efecto y corrección propuesta. Distingue los riesgos no verificados
   de los defectos demostrados. Si no hay hallazgos, dilo y explica el alcance
   comprobado. No modifiques código por el mero hecho de revisarlo.

En migraciones, contrasta origen y destino además de la versión declarada: cambiar
el manifest no adapta vistas, permisos, assets, hooks, nombres ni datos.
