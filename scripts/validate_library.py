#!/usr/bin/env python3
"""Validate generated skills, metadata, portable links and source consistency."""

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from build_library import FAMILIES, VERSIONS, differences, expected_files


def validate_skill(folder):
    errors = []
    skill = folder / "SKILL.md"
    if not skill.is_file():
        return [f"Falta {skill}"]
    text = skill.read_text(encoding="utf-8")
    match = re.match(r"^---\nname: ([a-z0-9-]+)\ndescription: (.+)\n", text)
    if not match:
        return [f"Frontmatter no válido: {skill}"]
    name, description = match.groups()
    try:
        description = json.loads(description)
    except ValueError:
        description = ""
    if name != folder.name or len(name) > 64:
        errors.append(f"Nombre/carpeta no válido: {folder}")
    if not isinstance(description, str) or not 1 <= len(description) <= 1024:
        errors.append(f"Descripción no válida: {folder}")
    ui = folder / "agents/openai.yaml"
    if not ui.is_file():
        errors.append(f"Falta metadata UI: {folder}")
    else:
        fields = {}
        for line in ui.read_text(encoding="utf-8").splitlines()[1:]:
            try:
                key, value = line.strip().split(": ", 1)
                fields[key] = json.loads(value)
            except (ValueError, TypeError):
                errors.append(f"Metadata UI no válida: {ui}")
        if not 25 <= len(fields.get("short_description", "")) <= 64:
            errors.append(f"Longitud de descripción UI: {folder}")
        if f"${name}" not in fields.get("default_prompt", ""):
            errors.append(f"Prompt sin nombre de skill: {folder}")
    root = folder.resolve()
    for doc in sorted(folder.rglob("*.md")):
        for destination in re.findall(r"\[[^\]\n]+\]\(([^)\s]+)\)", doc.read_text(encoding="utf-8")):
            parsed = urlsplit(destination)
            if parsed.scheme or destination.startswith("#"):
                continue
            target = (doc.parent / unquote(parsed.path)).resolve()
            if root not in target.parents and target != root:
                errors.append(f"Referencia externa al paquete: {doc}: {destination}")
            elif not target.is_file():
                errors.append(f"Enlace roto: {doc}: {destination}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--skill", type=Path, help="Validate one copied skill independently")
    args = parser.parse_args()
    try:
        if args.skill:
            folders = [args.skill]
            errors = []
        else:
            root = args.root.resolve()
            expected = expected_files(root)
            errors = differences(root, expected)
            folders = [root / f"v{v}/odoo-v{v}-{family}" for v in VERSIONS for family in FAMILIES]
            found = set(root.glob("v*/**/SKILL.md"))
            if found != {folder / "SKILL.md" for folder in folders}:
                errors.append("El inventario de skills no coincide con las 20 especialidades esperadas.")
        for folder in folders:
            errors.extend(validate_skill(folder))
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK: {len(folders)} skills; nombres, metadata, referencias y consistencia válidos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
