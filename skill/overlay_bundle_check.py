"""只读校验配套运行文件，不加载 Overlay。"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath

def check(root):
    root = Path(root).resolve()
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    records = manifest["files"]
    if not isinstance(records, dict) or not records:
        raise ValueError("Empty manifest")
    errors, names = [], set()
    for name, record in records.items():
        posix = PurePosixPath(name)
        if posix.is_absolute() or ".." in posix.parts or "\\" in name or ":" in name:
            errors.append("unsafe path: " + name)
            continue
        if name.casefold() in names:
            errors.append("case collision: " + name)
        names.add(name.casefold())
        target = (root / name).resolve()
        if root not in target.parents or not target.is_file():
            errors.append("missing or escaped file: " + name)
            continue
        data = target.read_bytes()
        if len(data) != record["bytes"] or hashlib.sha256(data).hexdigest() != record["sha256"]:
            errors.append("mismatch: " + name)
    return {"files": len(records), "ok": not errors, "errors": errors}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    try:
        result = check(args.root)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result = {"ok": False, "errors": [str(exc)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["ok"] else 1)
