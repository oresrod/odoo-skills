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
