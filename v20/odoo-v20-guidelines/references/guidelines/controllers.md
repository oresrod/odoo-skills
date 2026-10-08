# Controladores

Extiende `http.Controller` y vuelve a decorar overrides con `@http.route()` para
conservar/publicar la ruta. Comprueba la combinación de opciones en la serie; no
dependas de auto-decoración o cambios de `type` que sólo algunas revisiones aceptan.

Elige `auth`, `type`, métodos HTTP y CSRF conforme al perfil. No copies `jsonrpc`,
`json2`, `bearer_scope` ni `readonly` a una versión sin soporte. La API externa
JSON-2 no implica por sí sola que un controlador de esa versión acepte `type='json2'`.

Valida IDs, campos y payloads antes de usarlos, aplica permisos con el usuario
efectivo y limita cualquier elevación. Los métodos HTTP seguros no deben mutar
estado de negocio. Para HTTP con sesión conserva CSRF; un webhook externo requiere
autenticación de su payload y control de repetición. Consulta
[auditoría](../security-audit.md) cuando cambies un límite de confianza.
