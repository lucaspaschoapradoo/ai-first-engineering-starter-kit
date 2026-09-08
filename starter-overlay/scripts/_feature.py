from pathlib import Path

def find_feature(root: Path, explicit=None):
    if explicit:
        p = (root / explicit).resolve() if not Path(explicit).is_absolute() else Path(explicit).resolve()
        if not p.exists():
            raise FileNotFoundError(f"Feature directory not found: {p}")
        return p
    specs = root / "specs"
    if not specs.exists():
        raise FileNotFoundError("specs/ directory not found")
    candidates = [p for p in specs.iterdir() if p.is_dir() and (p / "spec.md").exists()]
    if not candidates:
        raise FileNotFoundError("No feature directory with spec.md found under specs/")
    return max(candidates, key=lambda p: (p / "spec.md").stat().st_mtime)
