#!/usr/bin/env python
"""Simple QC language on the toy matrix: ranges, separation, outliers."""

from __future__ import annotations

import sys

from cpomp.config import load_config
from cpomp.io import read_expression, read_metadata


def main() -> int:
    cfg = load_config()
    expr = read_expression(cfg["year01"]["expression_csv"])
    meta = read_metadata(cfg["year01"]["metadata_csv"])
    print("shape_genes_x_samples", expr.shape)
    print("gene_means")
    print(expr.mean(axis=1).sort_values(ascending=False).head(6).to_string())
    nb = meta.index[meta["histology"] == "neuroblastoma"]
    all_s = meta.index[meta["histology"] == "B-ALL"]
    print("MYCN_NB_mean", float(expr.loc["MYCN", nb].mean()))
    print("MYCN_ALL_mean", float(expr.loc["MYCN", all_s].mean()))
    print("PAX5_NB_mean", float(expr.loc["PAX5", nb].mean()))
    print("PAX5_ALL_mean", float(expr.loc["PAX5", all_s].mean()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
