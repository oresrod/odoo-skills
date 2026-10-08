## Desarrollo web

Determina si trabajas en el webclient, website/portal, POS o un componente
embebido: sus puntos de extensión y bundles pueden diferir incluso en la misma
versión. Sigue el framework y las pruebas usados por ese subsistema.

| Referencia | Leer cuando |
| --- | --- |
| [JavaScript y plantillas](web/javascript.md) | Componentes, widgets, servicios, registries o patches |
| [Assets](web/assets.md) | Añades JS, XML, estilos, fuentes o librerías |
| [SCSS](web/scss.md) | Cambias estilos |
| [Auditoría](security-audit.md) | HTML dinámico, RPC o datos sensibles |

Comprueba carga del bundle, resolución de imports y plantillas, comportamiento y
ausencia de errores de consola en el cliente de destino. Ejecuta el runner de esa
serie y los tests relacionados si están disponibles. Un linter no valida el
registro de un componente ni el renderizado de una vista.
