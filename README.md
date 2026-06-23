# Frullania Morphometry Principal Component Analysis

This repository contains the data analysis pipeline used to quantify morphological differentiation between *Frullania delangeii* and *Frullania rostrata*.

## Overview

We evaluate morphological variation across two distinct groups of characters: a branching character dataset and a leaf character dataset. The branching characters include internal length, terminal length, and their respective deviations. The leaf characters are base-apex count, orthogonal count, base-apex distance, orthogonal distance, leaf median cell length and width, leaf lobule length and width, oilbody length and width, styli length and width, and underleaf length and width. 

## Methodology
### Data Preparation
Raw morphological measurements across various files were placed in standardized spreadsheets containing specimen IDs, species names, and corresponding character measurements. The process involved data validation, removing missing entries, and proper formatting. Three spreadsheets were created: a full leaf-character dataset (n = 68), a reduced leaf-character subset containing specimens with complete trait coverage (n = 24), and a branching-character dataset (n = 25).

### Analysis
The analysis pipeline uses Principal Component Analysis (PCA) to reduce the high-dimensional datasets into two-dimensional components, allowing visualization of morphological similarity and separation of *F. delangeii* and *F. rostrata* through cluster formation. Furthermore, PCA facilitates the identification of the major characters driving separation between the species. 

1. **Standardization:**   StandardScaler   was applied to ensure that traits with larger absolute scales would not disproportionately influence the results, transforming all features to a mean of 0 and a variance of 1. 
2. **2D Dimensionality:** `scikit-learn` was used to compute the principal components. By focusing on the first two components (PC1 and PC2), the specimens can be grouped in the morphospace.
3. **Loading Analysis:** Loadings, or the correlation coefficients between each original trait and PC1 and PC2 respectively, were identified. Traits with the highest absolute loading values are identified as the primary diagnostic characters driving differences between *F. delangeii* and *F. rostrata*.

## Results
PCA of the leaf morphology characters demonstrated strong separation between *F. delangeii* and *F. rostrata*; the species formed distinct clusters along PC1 in both the full (n = 68) and recduced (n = 24) datasets. Leaf characters—mainly stem leaf, oilbody, and leaf lobule dimensions—contributed most strongly to species differentiation and clustering. PCA of branching morphology, however, showed weaker separation, although some clustering remained, suggesting that branching morphology captures morphological variation but provides less support for separating species in practice. The formation of clusters in PCA for both character sets supports the presence of measurable morphological variation between the two groups of plants, reinforcing classification as separate species. 

## Repository Contents
1. `/Cleaned Data`: Contains cleaned `.csv` data separated by character immediately usable for morphometric analysis.
2. `/Scripts`: Contains the Python analysis pipelines (`branching_architecture.py`, `leaf_morphology.py`) used to process data and generate PCA models.
3. `/Figures`: Contains graph outputs, including PCA scatterplots and trait contribution loading profiles.

