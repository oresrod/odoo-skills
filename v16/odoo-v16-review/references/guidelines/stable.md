# Compatibilidad, estabilidad y migraciones

Distingue dos contextos:

- **Contribución al core estable:** consulta su política vigente, mantén cambios
  mínimos y compatibilidad con bases que aún no hayan actualizado el módulo.
  Evita alterar contratos y términos traducibles por conveniencia.
- **OCA/Enterprise/custom:** aplica su política de mantenimiento. Una funcionalidad
  nueva o un campo persistente en un addon propio puede ser el objetivo legítimo,
  también en una serie estable. Planifica actualización y migración cuando hagan falta.

Para portar código identifica origen/destino, edición y addons instalados. Revisa
manifest, dependencias, hooks, ORM, vistas/XML IDs, assets/frontend, permisos y
datos. Preserva contratos consumidos por otros addons o adapta todos los
consumidores del alcance. Consulta scripts de upgrade o herramientas OCA sólo si
el proyecto las utiliza; portar código no equivale a migrar la base de datos.

Valida instalación limpia y actualización con datos representativos cuando el
cambio las afecte, incluyendo `noupdate`, traducciones, empresas y permisos.
No cambies el core para resolver una extensión propia salvo que esa sea la tarea.
