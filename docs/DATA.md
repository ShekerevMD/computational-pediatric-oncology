# Data sources (pointers only)

Do not vendor large restricted files into this git repository.

## Open / semi-open starting points

- Open Pediatric Cancer (OpenPedCan) analysis and merged summaries  
  https://github.com/d3b-center/OpenPedCan-analysis
- PedcBioPortal  
  https://pedcbioportal.kidsfirstdrc.org/
- NCI pediatric Molecular Targets Platform
- TARGET program pages and open-access summaries  
  https://ocg.cancer.gov/programs/target
- St. Jude Cloud / PeCan (account + data-use terms required for many files)
- Kids First Data Resource Portal

## Local layout

```text
data/raw/         downloads you fetched (gitignored payloads)
data/processed/   matrices, figures, tables you generated
data/external/    third-party checksums, manifests, citation notes
```

Record accession, version, download date, and license in the project README before analysis.

## Year 1 default

Use the toy matrices committed under `data/raw/` (`toy_expression.csv`, `toy_metadata.csv`) until a public summary matrix is cached locally. Replace paths in `configs/analysis.yaml`.
