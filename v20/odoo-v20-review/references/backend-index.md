## Desarrollo backend

Implementa el comportamiento solicitado conservando los contratos de herencia,
datos y seguridad del proyecto. Comprueba los consumidores en los `addons_path`
disponibles antes de cambiar nombres, firmas o XML IDs. Usa la variante de API
del perfil, no una traducción mecánica del código de otra versión.

| Referencia | Leer cuando |
| --- | --- |
| [Estructura](guidelines/module_structure.md) | Creas o reorganizas un addon |
| [Manifest](guidelines/manifest.md) | Cambias dependencias, datos o assets |
| [Python y traducciones](guidelines/python.md) | Escribes Python |
| [ORM](guidelines/orm.md) | Cambias búsquedas, computes, CRUD o transacciones |
| [Campos](guidelines/fields.md) | Defines o modificas campos |
| [Controladores](guidelines/controllers.md) | Defines o extiendes rutas |
| [XML](guidelines/xml.md) | Vistas, acciones y datos |
| [Informes](guidelines/reports.md) | QWeb o informes SQL |
| [Permisos](guidelines/security.md) | ACL, reglas o datos sensibles |
| [Rendimiento](guidelines/performance.md) | Consultas en bucles, lotes o agregaciones |
| [Pruebas](guidelines/tests.md) | Regresión y validación de comportamiento |
| [Comentarios](guidelines/comments.md) | Documentas una decisión o un mensaje |
| [Compatibilidad y migración](guidelines/stable.md) | Actualizaciones, portabilidad o core estable |
| [Auditoría](security-audit.md) | Cambias un límite de confianza o investigas seguridad |

Para JavaScript, plantillas Owl y SCSS utiliza la especialidad web de esta misma
versión, si está instalada. Esta skill contiene todas sus referencias backend y
puede instalarse por separado.
