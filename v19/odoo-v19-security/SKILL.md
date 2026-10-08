---
name: odoo-v19-security
description: "Audita seguridad de addons destinados a Odoo 19.0: permisos, compañías, RPC, sudo, controladores, SQL, dominios y XSS. Úsala en una auditoría o al evaluar un límite de confianza concreto en Odoo 19."
metadata:
  odoo-version: "19.0"
  specialty: security
---

# Odoo 19.0: Seguridad

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

## Auditoría de seguridad

Lee [la guía de auditoría](references/security-audit.md) y la sección de seguridad
del perfil. Identifica actores, entradas controlables y operaciones privilegiadas.
Revisa ACL/reglas, compañías, controladores, métodos públicos, SQL, dominios,
HTML, ficheros y evaluación dinámica en el alcance solicitado.

Una coincidencia de búsqueda no es una vulnerabilidad: sigue el flujo hasta el
efecto y comprueba las defensas en la versión instalada. Informa gravedad,
archivo/línea, actor y precondiciones, reproducción mínima y corrección. Señala
los límites de la revisión. Para validar acceso usa usuarios representativos sin
`sudo()`; no pruebes cambios de seguridad sobre producción.
