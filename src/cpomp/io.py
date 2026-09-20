from __future__ import annotations

from pathlib import Path

import pandas as pd

from .config import REPO_ROOT


def _resolve(path: str | Path) -> Path:
    path = Path(path)
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def read_expression(path: str | Path) -> pd.DataFrame:
    """Genes x samples numeric matrix."""
    frame = pd.read_csv(_resolve(path), index_col=0)
    return frame.apply(pd.to_numeric, errors="coerce")


def read_metadata(path: str | Path) -> pd.DataFrame:
    """Sample metadata; first column is sample_id."""
    return pd.read_csv(_resolve(path), index_col=0)
