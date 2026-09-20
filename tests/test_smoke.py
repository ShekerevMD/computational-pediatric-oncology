from pathlib import Path

from cpomp.config import REPO_ROOT, load_config
from cpomp.io import read_expression, read_metadata
from cpomp.matrix import pca_svd


def test_config_and_toy_pca():
    cfg = load_config()
    expr = read_expression(cfg["year01"]["expression_csv"])
    meta = read_metadata(cfg["year01"]["metadata_csv"])
    assert expr.shape[0] >= 8
    assert set(expr.columns) == set(meta.index)
    pca = pca_svd(expr.T, n_components=2)
    assert pca["scores"].shape == (expr.shape[1], 2)
    assert Path(REPO_ROOT, "README.md").exists()
