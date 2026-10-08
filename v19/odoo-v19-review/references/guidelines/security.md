# Permisos

Lee la sección Seguridad de [la versión](../version.md) antes de crear ACL o reglas.
Odoo 14/16/18/19 usan `ir.model.access` e `ir.rule`; el checkout 20.0 contrastado
usa `ir.access`. No son ficheros ni semánticas intercambiables.

Comprueba cada operación CRUD por separado, grupos efectivos, usuario público,
portal, usuario interno y aislamiento entre empresas. La ausencia de permiso de
lectura no demuestra que la escritura esté bloqueada. Una vista o menú oculto no
es una barrera de autorización.

Valida el resultado con un usuario sin elevación, incluyendo un acceso permitido
y otro denegado. Consulta [auditoría](../security-audit.md) para RPC, `sudo`, SQL y
exposición indirecta de campos.
