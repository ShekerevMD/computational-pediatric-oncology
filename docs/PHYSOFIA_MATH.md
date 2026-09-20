# Physofia mathematical stance

Work from objects and maps, not from memorized recipes.

## Recurring translations

| Mathematical object | Pediatric molecular-pathology reading |
| --- | --- |
| Vector / point in R^n | A cell, a bulk sample, or a slide tile in feature space |
| Change of basis | PCA / NMF / ICA on expression or methylation |
| Eigenvectors of a covariance | Directions of cohort variance (batch vs biology — always ask which) |
| SVD | Low-rank tumor + stroma + batch decomposition |
| Gradient of a loss | Force on parameters; backprop is chain rule |
| Probability measure | Ensemble of clones, cells, or patients |
| Entropy / KL | Mutational process uncertainty; methylation disorder |
| Graph / DAG | Pathways, copy-number adjacency, lineage, causal sketches |
| Survival function | Event-free and overall survival; competing late effects |

## Year 1 derivation list

Write these by hand once, then code them without a library first:

1. Projection of a vector onto a subspace.
2. Covariance matrix and the PCA eigenproblem.
3. SVD and why it solves the same problem as PCA on centered data.
4. Gradient of squared error and of logistic loss.
5. Bayes rule for a binary classifier on a molecular marker.
6. Multiple-testing language: family-wise error vs FDR (Benjamini–Hochberg idea).

Keep notes in `curriculum/year-01/math/`.
