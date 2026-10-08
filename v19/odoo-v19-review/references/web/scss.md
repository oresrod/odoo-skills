# Estilos

Sigue las convenciones de la base y limita estilos al módulo/componente, normalmente
con clases `o_<modulo>_*`. Evita selectores por ID o cadenas frágiles que acoplen
la extensión a la estructura interna del padre.

Comprueba variables, mixins, utilidades y versión de Bootstrap realmente incluidos.
No copies utilidades CSS de 20 a 14 sin verificarlas. Reutiliza tokens existentes y
evita `!important` salvo necesidad justificada. Valida los estados afectados,
ancho reducido y temas que el proyecto soporte.

Usa variables SCSS o CSS según compilación y alcance dinámico; las convenciones
internas del core no obligan a renombrar variables de una librería externa.
