# Medulloblastoma: Human Specific Genes Contributions
Repository for the project of Laboratory of Biological Data Mining (M.Sc. in Quantitative and Computational Biology, 2023-2024).

## Overview
This repository contains the analysis pipeline and results from a study investigating the role of Human Specific Genes (HSGs) in medulloblastoma (MB), a prevalent malignant brain tumor in childhood. The study focuses on identifying MB-related HSGs, exploring their functions, and assessing their potential as biomarkers and therapeutic targets.

## Project Objectives
- Differential Expression Analysis: Identify differentially expressed genes (DEGs) between MB cases and controls, and across the four MB subgroups (WNT, SHH, Group 3, Group 4).
- HSG Contribution: Explore the contribution of HSGs to MB development and progression.
- Network and Functional Analysis: Analyze gene networks and functional roles of significant DEGs, with a focus on identifying key pathways and potential biomarkers.
  
## Data and Methods
Datasets:
- GSE155446: Single-cell RNA sequencing data from MB cases.
- GSE118068: Reference dataset from normal postnatal mouse hindbrain samples.
  
Tools and Libraries:
- Quality Control & Analysis: Scanpy, NumPy, SciPy, ggplot2
- Gene Networks: NetworkX, STRING
- Functional Analysis: Enrichr, Reactome
  
## Key Findings
- Identified several HSGs significantly associated with MB, including MAOA, ALOX5, CNTNAP2, RAB3A, and PPIP5K2.
- The functional analysis confirmed the involvement of these genes in brain-related processes and cancer pathways, suggesting their potential as MB biomarkers.
- Network analysis revealed key interactions among these genes, highlighting their relevance in MB subtypes.
