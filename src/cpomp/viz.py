from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def scatter_pca(
    scores: pd.DataFrame,
    hue: pd.Series | None,
    title: str,
    outfile: str | Path,
    dpi: int = 150,
) -> Path:
    outfile = Path(outfile)
    outfile.parent.mkdir(parents=True, exist_ok=True)
    frame = scores.copy()
    if hue is not None:
        frame["group"] = hue.astype(str).values
        hue_col = "group"
    else:
        hue_col = None
    plt.figure(figsize=(6, 5))
    sns.scatterplot(data=frame, x="PC1", y="PC2", hue=hue_col, s=80)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(outfile, dpi=dpi)
    plt.close()
    return outfile
