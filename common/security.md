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
