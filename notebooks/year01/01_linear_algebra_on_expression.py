#!/usr/bin/env python
"""Year 1: PCA via SVD on the toy pediatric expression matrix."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

from cpomp.config import REPO_ROOT, load_config
from cpomp.io import read_expression, read_metadata
from cpomp.matrix import pca_svd
from cpomp.viz import scatter_pca


def main() -> int:
    cfg = load_config()
    y1 = cfg["year01"]
    expr = read_expression(y1["expression_csv"])
    meta = read_metadata(y1["metadata_csv"])

    missing = [s for s in expr.columns if s not in meta.index]
    if missing:
        raise SystemExit(f"Metadata missing for samples: {missing}")

    samples_x_genes = expr.T
    pca = pca_svd(samples_x_genes, n_components=int(y1["n_components"]))
    scores = pd.DataFrame(
        pca["scores"],
        index=samples_x_genes.index,
        columns=[f"PC{i+1}" for i in range(pca["scores"].shape[1])],
    )
    scores = scores.join(meta)

    fig_dir = REPO_ROOT / cfg["figures"]["outdir"]
    out = scatter_pca(
        scores[["PC1", "PC2"]],
        hue=scores["histology"],
        title="Toy cohort PCA (histology)",
        outfile=fig_dir / "year01_pca_histology.png",
        dpi=int(cfg["figures"]["dpi"]),
    )
    print("explained_variance_ratio", pca["explained_variance_ratio"])
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
