# Consultas por lotes

Evita `search`, `search_count` y `create` por cada elemento cuando el contrato
permita agrupar. Crea con una lista de diccionarios y calcula conteos con una
agregación por campo. Lee el perfil antes de elegir `read_group`/`_read_group` y
desempaquetar sus resultados: nombres parecidos no garantizan el mismo retorno.

Itera recordsets completos para conservar prefetch. No conviertas un lote en un
bucle de `browse(id)` y lecturas aisladas. Un lote no garantiza una sola sentencia
SQL; la mejora buscada es evitar trabajo proporcional innecesario.

Filtra en dominios cuando corresponda, reserva `filtered` para valores ya cargados
o condiciones no expresables en búsqueda. Preindexa resultados en dict/set para
evitar bucles cuadráticos. Mide con datos representativos y empresas/permisos reales.
Los lotes grandes pueden requerir límites por memoria y tiempo de transacción.

SQL directo necesita parámetros, flush e invalidación compatibles con la rama,
y una revisión explícita de permisos. `SQL` facilita composición, no autorización.
