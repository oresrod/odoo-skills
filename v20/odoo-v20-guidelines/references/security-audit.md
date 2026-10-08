# Límites de confianza

Aplica la semántica de acceso de [la versión](version.md). Sigue las entradas
desde usuario, RPC, HTTP, importación y campos editables hasta su efecto. Un
patrón sospechoso requiere un escenario alcanzable para ser un hallazgo.

| Superficie | Comprobación |
| --- | --- |
| ACL y reglas | Operaciones independientes, grupos efectivos, dominios y compañías |
| `sudo`, `with_user`, `with_company` | Motivo, alcance mínimo, entradas e IDs controlables |
| Métodos públicos | Exposición RPC real, parámetros y registros no confiables |
| Rutas | Auth, métodos HTTP, CSRF, validación y autorización |
| SQL y dominios | Composición segura, permisos y límites del filtro |
| HTML dinámico | Escape, marcado seguro y sanitización |
| Ficheros y deserialización | Confinamiento, tamaño y contenido no confiable |
| Secretos | Permisos de campo, exposición indirecta y logs |

# Acceso y elevación

La autorización se aplica en el servidor. Comprueba lectura, creación, escritura
y borrado por separado; ocultar un menú o campo XML no protege el modelo.
No añadas `sudo()` para silenciar un error de permisos. Bajo elevación valida
modelo, registros, campos, valores y comandos x2many; éstos pueden modificar
comodelos. Verifica también acceso a adjuntos y cadenas de campos related.

Los campos `groups` protegen acceso al campo. Los related suelen computar con
privilegios; comprueba `compute_sudo`/`related_sudo` y las relaciones editables.
No presupongas `fields.NO_ACCESS` en ramas donde no existe. Un hash o token puede
ser sensible aunque no aparezca en formularios.

# RPC y HTTP

Los métodos públicos pueden exponerse a RPC sin validar automáticamente el caso
de negocio. Prefiere privados para helpers internos, pero conserva interfaces
necesarias y valida entradas. `@api.private` depende de la revisión, incluidos
backports: comprueba decorador y dispatcher. Un prefijo privado no hace segura
una llamada interna alimentada con datos del usuario.

Evita mutaciones de negocio por GET. Conserva CSRF en rutas HTTP con sesión;
los webhooks exigen autenticación/verificación propia. En JSON/JSON-RPC revisa
el dispatcher, sesión, Content-Type y CORS de la serie; que no se use un token
CSRF no demuestra seguridad por sí solo. La disponibilidad de JSON-2 no determina
los tipos permitidos en `@route`.

# SQL y dominios

Prefiere ORM. SQL directo omite reglas y otras garantías; parametriza valores y
compón identificadores con utilidades seguras de la rama, nunca con entradas
libres. `odoo.tools.SQL` sólo está disponible en las series indicadas en el perfil
y no añade permisos. No asumas que `_search()` tiene el mismo tipo de retorno
o nivel de validación en todas las versiones.

Compón un dominio impuesto por el servidor y otro recibido con `expression.AND`
o `Domain` según versión; nunca concatenes un filtro arbitrario esperando que
restrinja acceso. Limita campos, operadores y tamaño cuando el cliente controle
el filtro. Las reglas del servidor deben seguir protegiendo los datos.

# XSS y evaluación

Escapa texto al insertarlo en HTML. Odoo 14 usa `t-esc`; las series modernas
prefieren `t-out`. La disponibilidad/deprecación de `t-raw` y `t-esc` cambia entre
servidor y Owl: no declares roto un template antiguo válido sólo por su sintaxis.
No envuelvas entradas sin escapar en `Markup`, `markup`, `innerHTML` ni
`insertAdjacentHTML`. Construye HTML confiable desde literales con interpolación
que escape; sanitiza HTML no confiable según el uso. No presupongas helpers JS
de Owl 3 en Owl 1/2.

Usa JSON o `ast.literal_eval` para datos y limita tamaños según exposición.
`safe_eval` no es un parser inocuo: revisa capacidades y objetos accesibles,
incluidos métodos de modelos que devuelvan objetos ricos. No evalúes código ni
deserialices pickle no confiables. No presentes un nombre privado como sandbox.

# Ficheros, campos dinámicos y secretos

Para recursos de addons usa utilidades de lectura disponibles como `file_open`
y verifica su confinamiento en la revisión. Para otros ficheros valida la raíz
permitida y la ruta resuelta, enlaces incluidos; no asumas que un helper sirve
para cualquier carga o garantiza sólo lectura.

Con nombres dinámicos limita campos y usa `record[field_name]`; `getattr` puede
alcanzar atributos ajenos al contrato. Compara secretos con una función de tiempo
constante disponible, como `hmac.compare_digest`; una búsqueda en base de datos
no demuestra por sí sola resistencia a canales temporales. Evita secretos en
errores/logs y argumentos por defecto mutables entre peticiones.
