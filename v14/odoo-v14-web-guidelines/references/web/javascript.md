# JavaScript, componentes y templates

Consulta el perfil antes de elegir imports, ciclo de vida, reactividad o extensiones.
Odoo 14 mezcla widgets legacy y Owl temprano; 16/18/19 usan Owl 2 en gran parte del
webclient; el checkout 20 incorpora Owl 3. No copies hooks o `computed` por nombre
sin verificar exports y ejemplos de ese subsistema.

Prefiere registries, servicios y puntos de extensión existentes. En addons propios
un patch puede ser la solución adecuada; usa su firma de versión y conserva el
contrato original. Comprueba cleanup y la llamada al padre, sobre todo con `await`.
No impongas la prohibición de patches del desarrollo del core a todas las extensiones.

Mantén JS, XML y estilos cercanos por funcionalidad siguiendo la organización local.
Usa nombres de template con namespace del módulo y carga el XML en el bundle
correcto. Distingue herencia de template Owl, QWeb servidor y vistas backend.

Usa el ORM del cliente para modelos y el mecanismo RPC del subsistema para rutas.
Gestiona errores, destrucción del componente y peticiones pendientes. Una condición
de interfaz no reemplaza una autorización del servidor. Renderiza texto con escape;
consulta [auditoría](../security-audit.md) para HTML dinámico.
