# Computational Pediatric Oncology Molecular Pathology

Personal multi-year workspace for **computational pediatric oncology molecular pathology**: Physofia-style mathematics, reproducible omics analysis, digital pathology, and translational reporting.

Owner: [Ivan Shekerev](https://github.com/ShekerevMD) (`ShekerevMD`)

This repository is the working companion to a 5-year curriculum assuming ≥4 hours of daily deep work. It is structured so Year 1 can start immediately on a local workstation (Dell Pro Max 18 Plus class machine) without committing restricted data.

## What this repo is

- Curriculum map and quarterly project templates
- A small Python package (`cpomp`) for shared I/O, QC, and figures
- Starter notebooks-as-scripts for linear algebra on expression matrices and a TARGET/OpenPedCan-style landscape sketch
- Pointers to public pediatric cancer resources (no raw BAM/FASTQ/WSI in git)
- Reproducibility defaults: environment file, CI smoke test, analysis config, report template

## What this repo is not

- A dump of patient-level sequencing or whole-slide images
- A replacement for clinical validation, CAP/CLIA processes, or official molecular sign-out
- A claim of affiliation with TARGET, OpenPedCan, St. Jude Cloud, or COG

## Quick start

```bash
git clone https://github.com/ShekerevMD/computational-pediatric-oncology.git
cd computational-pediatric-oncology
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest -q
python notebooks/year01/01_linear_algebra_on_expression.py
```

Optional omics extras later:

```bash
pip install -e ".[omics]"
```

## Repository map

```text
curriculum/     year-by-year outcomes, weekly rhythm, capstones
docs/           math stance, data access, resources, hardware notes
src/cpomp/      shared Python utilities
notebooks/      executable Year 1 scripts (no giant binaries)
projects/       one folder per analysis; start from templates/
pipelines/      Nextflow / Snakemake notes (empty until Year 2)
data/           local-only payloads; git keeps README + .gitkeep
reports/        molecular-report and journal-club templates
configs/        analysis.yaml defaults
tests/          smoke tests so the workspace cannot silently rot
```

## Daily deep-work block (suggested)

| Block | Minutes | Focus |
| --- | ---: | --- |
| Math (Physofia) | 60–90 | Derive one object; apply it to a toy pediatric matrix |
| Code | 90–120 | Pipeline, figure, or test on this machine |
| Clinic + papers | 30–60 | One entity or one method paper; write 10 lines of notes |

Protect the block with recovery data you already collect (sleep, HRV, nutrition). Four hours is enough only if it is repeatable.

## Year 1 north star

Process a **public** pediatric bulk-expression / mutation summary end-to-end and write a short integrated note on one histology (default sketch: neuroblastoma). See `curriculum/year-01/README.md` and `projects/year01-target-landscape/`.

## Data policy

1. Never commit FASTQ, BAM/CRAM, VCF with sample IDs, or WSI files.
2. Store local paths in `.env` (gitignored). Copy `.env.example`.
3. Prefer OpenPedCan / PedcBioPortal / TARGET *open* summaries until dbGaP access is in place.
4. Treat any real-world case material as PHI even if de-identified poorly.

## License

Code and original notes: MIT (`LICENSE`). Cited papers, WHO texts, and consortium data remain under their own terms.
