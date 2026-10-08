# Manifest y carga

- Declara `name`, licencia real y dependencias de los recursos usados. Incluye
  `base` cuando corresponda: no traslades la recomendación de omitirlo de un core
  concreto a cualquier addon. Una dependencia transitiva no sustituye a declarar
  una dependencia directa utilizada por tu código.
- Mantén el esquema de versión del proyecto; en OCA suele ser
  `<major>.0.<major-addon>.<minor>.<patch>`. El manifest por sí solo no prueba
  qué servidor ejecutará el módulo.
- Ordena `data`: grupos antes de ACL, acciones antes de menús y registros padre
  antes de referencias. `demo` no está garantizado en la instalación de destino.
- Usa `external_dependencies` para requisitos Python/binarios. `application`
  describe una aplicación; `auto_install` requiere una intención explícita de
  instalación automática y semántica compatible con la serie.
- Declara assets según el perfil: Odoo 14 usa herencia de bundles XML y `qweb`;
  las series modernas usan `assets`. No introduzcas claves de versiones nuevas.
- Antes de editar hooks de instalación/desinstalación, comprueba sus argumentos
  en el cargador de la serie; las firmas basadas en cursor/registry y Environment
  no son intercambiables.
