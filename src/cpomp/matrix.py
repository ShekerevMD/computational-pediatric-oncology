from __future__ import annotations

import numpy as np
import pandas as pd


def center(matrix: pd.DataFrame, axis: int = 1) -> pd.DataFrame:
    """Center genes (axis=1) or samples (axis=0)."""
    return matrix.sub(matrix.mean(axis=axis), axis=0 if axis == 1 else 1)


def pca_svd(matrix: pd.DataFrame, n_components: int = 3) -> dict[str, np.ndarray]:
    """PCA via SVD on a samples x features matrix.

    Expects rows = samples, columns = genes (so transpose an expression genes x samples table first).
    """
    x = np.asarray(matrix, dtype=float)
    x = x - x.mean(axis=0, keepdims=True)
    u, s, vt = np.linalg.svd(x, full_matrices=False)
    n = min(n_components, u.shape[1])
    scores = u[:, :n] * s[:n]
    var = (s**2) / max(x.shape[0] - 1, 1)
    explained = var / var.sum() if var.sum() else var
    return {
        "scores": scores,
        "loadings": vt[:n].T,
        "singular_values": s[:n],
        "explained_variance_ratio": explained[:n],
    }
