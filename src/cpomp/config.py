from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = REPO_ROOT / "configs" / "analysis.yaml"


def load_config(path: str | Path | None = None) -> dict[str, Any]:
    cfg_path = Path(path) if path else DEFAULT_CONFIG
    with cfg_path.open() as handle:
        data = yaml.safe_load(handle) or {}
    data["_config_path"] = str(cfg_path)
    data["_repo_root"] = str(REPO_ROOT)
    return data
