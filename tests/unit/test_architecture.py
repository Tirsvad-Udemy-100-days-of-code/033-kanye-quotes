import ast
from pathlib import Path

import pytest

PACKAGE = "kanye_quotes"
SRC = Path(__file__).resolve().parents[2] / "src" / PACKAGE
LAYERS = ("domain", "application", "infrastructure", "presentation")


def _imports(path: Path) -> set[str]:
    names: set[str] = set()
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            names.add(node.module)
    return names


def _layer_files(layer: str) -> list[Path]:
    return sorted((SRC / layer).rglob("*.py"))


def _own_imports(imports: set[str]) -> set[str]:
    return {name for name in imports if name.split(".")[0] == PACKAGE}


def _layer_of(module: str) -> str | None:
    parts = module.split(".")
    return parts[1] if len(parts) > 1 and parts[1] in LAYERS else None


def _foreign_layers(layer: str, allowed: set[str]) -> list[str]:
    found: list[str] = []
    for path in _layer_files(layer):
        for module in _own_imports(_imports(path)):
            target = _layer_of(module)
            if target is not None and target != layer and target not in allowed:
                found.append(f"{path.name} imports {module}")
    return found


def test_layers_exist_when_source_is_scanned() -> None:
    assert all(_layer_files(layer) for layer in LAYERS)


def test_domain_imports_no_other_layer() -> None:
    assert _foreign_layers("domain", set()) == []


def test_application_imports_only_domain() -> None:
    assert _foreign_layers("application", {"domain"}) == []


@pytest.mark.parametrize("layer", ["domain", "application", "infrastructure"])
def test_inner_layer_does_not_import_tkinter(layer: str) -> None:
    offenders = [
        path.name
        for path in _layer_files(layer)
        if any(name.split(".")[0] == "tkinter" for name in _imports(path))
    ]
    assert offenders == []


def test_infrastructure_is_imported_only_by_main() -> None:
    offenders: list[str] = []
    for path in SRC.rglob("*.py"):
        if path.is_relative_to(SRC / "infrastructure") or path.name == "main.py":
            continue
        own = _own_imports(_imports(path))
        if any(_layer_of(module) == "infrastructure" for module in own):
            offenders.append(str(path.relative_to(SRC)))
    assert offenders == []
