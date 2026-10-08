#!/usr/bin/env python3
"""Build self-contained Odoo skills from shared sources (Python 3.9+, stdlib)."""

import argparse
import json
from pathlib import Path
import sys

VERSIONS = (14, 16, 18, 19, 20)
FAMILIES = {
    "guidelines": (
        "Backend",
        "Desarrollo backend compatible con Odoo {v}",
        "Desarrolla o modifica addons backend para Odoo {v}.0: Python, ORM, "
        "campos, vistas, datos, controladores y pruebas. Úsala cuando el destino "
        "sea Odoo {v}; para archivos static utiliza la especialidad web de esa versión.",
    ),
    "web-guidelines": (
        "Web",
        "JavaScript, templates y assets de Odoo {v}",
        "Desarrolla o modifica frontend de addons para Odoo {v}.0: JavaScript, "
        "widgets/componentes, templates cliente, SCSS, assets y pruebas web. "
        "Úsala cuando el destino sea Odoo {v}; excluye imágenes y librerías vendorizadas.",
    ),
    "review": (
        "Revisión",
        "Revisión de addons y cambios para Odoo {v}",
        "Revisa diffs, commits, PRs o módulos destinados a Odoo {v}.0, "
        "contrastando comportamiento, compatibilidad, backend, frontend y seguridad. "
        "Úsala para una revisión de código con destino Odoo {v}.",
    ),
    "security": (
        "Seguridad",
        "Auditoría de permisos y seguridad Odoo {v}",
        "Audita seguridad de addons destinados a Odoo {v}.0: permisos, "
        "compañías, RPC, sudo, controladores, SQL, dominios y XSS. Úsala en una "
        "auditoría o al evaluar un límite de confianza concreto en Odoo {v}.",
    ),
}


def read(root, relative):
    return (root / relative).read_text(encoding="utf-8").strip()


def expected_files(root):
    """Return relative path -> UTF-8 content; does not mutate the filesystem."""
    result = {}
    context = read(root, "common/context.md")
    for v in VERSIONS:
        rows = []
        for family, (label, short, description) in FAMILIES.items():
            name = f"odoo-v{v}-{family}"
            folder = Path(f"v{v}") / name
            body = read(root, f"common/{family}.md")
            header = (
                f"---\nname: {name}\n"
                f"description: {json.dumps(description.format(v=v), ensure_ascii=False)}\n"
                f"metadata:\n  odoo-version: \"{v}.0\"\n  specialty: {family}\n---\n"
            )
            result[folder / "SKILL.md"] = (
                header + f"\n# Odoo {v}.0: {label}\n\n" + context + "\n\n" + body + "\n"
            )
            prompt = f"Usa ${name} para trabajar en este addon de Odoo {v}.0."
            ui = {
                "display_name": f"Odoo {v} · {label}",
                "short_description": short.format(v=v),
                "default_prompt": prompt,
            }
            result[folder / "agents/openai.yaml"] = "interface:\n" + "".join(
                f"  {key}: {json.dumps(value, ensure_ascii=False)}\n"
                for key, value in ui.items()
            )
            result[folder / "references/version.md"] = read(root, f"profiles/v{v}.md") + "\n"
            result[folder / "references/security-audit.md"] = read(
                root, "common/references/security-audit.md"
            ) + "\n"
            domains = []
            if family in ("guidelines", "review"):
                domains.append("guidelines")
            if family in ("web-guidelines", "review"):
                domains.append("web")
            for domain in domains:
                for source in sorted((root / "common/references" / domain).glob("*.md")):
                    result[folder / "references" / domain / source.name] = source.read_text(
                        encoding="utf-8"
                    )
            if family == "review":
                # Indices move one level down: rewrite their local reference prefix.
                for source, target in (("guidelines", "backend-index"), ("web-guidelines", "web-index")):
                    result[folder / f"references/{target}.md"] = (
                        read(root, f"common/{source}.md").replace(
                            "(references/", "("
                        ) + "\n"
                    )
            rows.append(f"| `{name}` | {label} | [{name}/SKILL.md]({name}/SKILL.md) |")
        result[Path(f"v{v}/README.md")] = (
            f"# Skills Odoo {v}.0\n\n"
            "Cada carpeta de skill es autónoma y su nombre incluye la versión. "
            "Puedes copiar una especialidad o las cuatro al directorio de skills "
            "de tu agente. No copies sólo SKILL.md.\n\n"
            "| Skill | Especialidad | Entrada |\n| --- | --- | --- |\n"
            + "\n".join(rows)
            + "\n\nGenerado desde `common/` y `profiles/`; modifica esas fuentes y ejecuta "
            "`python3 scripts/build_library.py` en la raíz de la biblioteca.\n"
        )
    return result


def generated_paths(root):
    return {
        path.relative_to(root)
        for version in VERSIONS
        for path in (root / f"v{version}").rglob("*")
        if path.is_file() or path.is_symlink()
    }


def differences(root, expected):
    issues = []
    for relative, content in expected.items():
        path = root / relative
        if not path.is_file():
            issues.append(f"Falta: {relative}")
        elif path.read_text(encoding="utf-8") != content:
            issues.append(f"Desactualizado: {relative}")
    for relative in sorted(generated_paths(root) - expected.keys()):
        issues.append(f"Archivo ajeno a la generación (revisar): {relative}")
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="Check freshness without writing")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        expected = expected_files(root)
        # Reject symlinks even for --check: generated folders must be portable copies.
        for relative in expected:
            path = root / relative
            if any(item.is_symlink() for item in (path, *path.parents) if item != root and root in item.parents):
                raise ValueError(f"Enlace simbólico en salida generada: {relative}")
        if not args.check:
            for relative, content in expected.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                if not path.exists() or path.read_text(encoding="utf-8") != content:
                    path.write_text(content, encoding="utf-8")
        issues = differences(root, expected)
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    print(f"OK: {len(VERSIONS) * len(FAMILIES)} skills, {len(expected)} archivos generados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
