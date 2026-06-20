# Frullania Morphometric Analysis (PCA)

This repository contains the data analysis pipeline used to quantify morphological differentiation between *Frullania delangeii* and *Frullania rostrata*.

## Overview

We evaluate morphological variation across two distinct groups of characters: a branching character dataset and a leaf character dataset. The branching characters are internal length, terminal length, and the deviation for both. The leaf characters are base-apex count, orthogonal count, base-apex distance, orthogonal distance, leaf median cell length and width, leaf lobule length and width, oilbody length and width, styli length and width, and underleaf length and width. 

## Methodology
### Data Preparation
Raw morphological measurements across various files were placed in standardized spreadsheets containing specimen IDs, species names, and corresponding character measurements. The process involved data validation, removing missing entries, and proper formatting. Three spreadsheets were created: one with 68 specimens for leaf characters, one with 24 specimens for leaf characters, and one with 25 specimens for branching characters.

### Analysis
The analysis pipeline uses Principal Component Analysis, or PCA, to reduce the high-dimensional datasets into two-dimensional components, allowing the identification of the relatedness of *F. delangeii* and *F. rostrata* based on the formation of clusters. Furthermore, PCA facilitates the identification of the major characters driving separation between the species. 

1. **Standardization:**   StandardScaler   was applied to ensure that traits with larger absolute scales would not disproportionaly influence result, transforming all features to a mean of 0 and a variance of 1. 
2. **Dimensionality Reduction:** `scikit-learn` was used to compute the principal components. By focusing on the first two components (PC1 and PC2), the specimens can be grouped in the morphospace.
3. **Loading Analysis:** We examined the **loadings**—the correlation coefficients between each original trait and the principal components. Traits with the highest absolute loading values are identified as the primary diagnostic characters for the genus.

## Repository Contents

