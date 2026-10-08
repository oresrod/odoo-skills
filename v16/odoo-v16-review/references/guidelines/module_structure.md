# Estructura de addons

- Usa `models/`, `views/`, `security/`, `data/`, `controllers/`, `static/` y, cuando
  proceda, `wizard/`, `report/`, `tests/`. No crees directorios vacíos por convención.
- Importa paquetes Python en `__init__.py` y pruebas en `tests/__init__.py`.
- Sigue la granularidad y los nombres del repositorio; un modelo por archivo
  (`res_partner.py`) suele facilitar la herencia. No dividas una extensión pequeña
  sólo para satisfacer una preferencia del core.
- Los CSV de seguridad dependen de [la versión](../version.md). Grupos y reglas
  XML deben cargarse antes de las referencias que los usan.
- Distingue informes estadísticos (`_auto = False`) de informes QWeb imprimibles.
  No añadas convenciones de `populate` del core a un módulo que no las necesita.
