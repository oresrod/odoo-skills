# Pruebas

Usa `TransactionCase` o `HttpCase` y helpers disponibles en la rama. Odoo 14
distingue `SavepointCase`; no traslades sus supuestos a versiones posteriores.
No dependas de usuarios demo, `BaseCommon` ni helpers recientes sin comprobarlos.
Crea fixtures mínimos y usa usuarios sin elevación para probar permisos.

Comprueba los tags del perfil: 14/16/18/19 parten de `standard, at_install` en
los checkouts contrastados; 20 parte de `standard, post_install`. Al cambiar fase,
añade una y elimina la otra. Importa archivos `test_*.py` desde `tests/__init__.py`
y comprueba la colección real, especialmente al heredar clases de pruebas.

Ejemplo de ejecución, adaptando ejecutable, configuración y base desechable:

```bash
./odoo-bin -c /ruta/odoo-test.conf -d base_pruebas -i mi_modulo --test-enable --test-tags /mi_modulo --stop-after-init
```

Usa `-u` para comprobar actualización sobre una base de pruebas donde el módulo
ya existe; no confundas esa prueba con una instalación limpia. No ejecutes este
ejemplo sobre producción. Asegura que el runner recoge y ejecuta los tests.

Verifica el fallo corregido y casos límite pertinentes; evita presupuestos rígidos
de conteo SQL en pruebas de negocio. Usa QUnit o HOOT según el perfil para JS y
tours del subsistema para flujos completos. No trasplantes opciones de tours de 20
a las series antiguas.
