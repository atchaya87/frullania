# Frullania Morphometry PCA 

This repository contains the data analysis pipeline used to quantify morphological differentiation between *Frullania delangeii* and *Frullania rostrata*.

## Overview

We evaluate morphological variation across two distinct groups of characters: a branching character dataset and a leaf character dataset. The branching characters include internal length, terminal length, and their respective deviations. The leaf characters are base-apex count, orthogonal count, base-apex distance, orthogonal distance, leaf median cell length and width, leaf lobule length and width, oilbody length and width, styli length and width, and underleaf length and width. 

## Methodology
### Data Preparation
Raw morphological measurements across various files were placed in standardized spreadsheets containing specimen IDs, species names, and corresponding character measurements. The process involved data validation, removing missing entries, and proper formatting. Three spreadsheets were created: a leaf-character dataset containing all traits except styli and underleaf data (n = 68), a leaf-character dataset containing all traits except oilbodies (n = 24), and a branching-character dataset (n = 25).

### Analysis
The analysis pipeline uses Principal Component Analysis (PCA) to reduce the high-dimensional datasets into two-dimensional components, allowing visualization of morphological similarity and separation of *F. delangeii* and *F. rostrata* through cluster formation. Furthermore, PCA facilitates the identification of the major characters driving separation between the species. 

1. **Standardization:**   StandardScaler   was applied to ensure that traits with larger absolute scales would not disproportionately influence the results, transforming all features to a mean of 0 and a variance of 1. 
2. **2D Dimensionality:** `scikit-learn` was used to compute the principal components. By focusing on the first two components (PC1 and PC2), the specimens can be grouped in the morphospace.
3. **Loading Analysis:** PCA loadings quantify the contribution of each character to the observed variation along PC1 and PC2. High absolute loading values indicate that a trait is a primary diagnostic character for species differentiation. Directionally, as specimens shift further toward the positive end of the PC1 axis, they are more likely to exhibit traits with the highest positive loadings. As specimens shift further to the negative end of the PC1 axis, the traits with the highest absolute value of their negative loadings are more likely to be displayed by these specimens. If the specimens form clusters by species, then, characteristic hallmarks of the species are identifiable and serve as differentiatiors between the two species. The sign of the values are displayed on the loading graphs, but magnitudes are used in the reported tables.

## Results
### PCA: Leaf Morphology Characters
PCA of the leaf morphology characters demonstrated strong separation between *F. delangeii* and *F. rostrata*; the species formed distinct clusters along PC1 in both the large (n = 68) and small (n = 24) datasets. The 68 specimen PCA scatterplot reveals two distinct clusters along the PC1 axis: the first group is largely comprised of *F. delangeii* specimens and the second group contains *F. rostrata* specimens. The PCA indicates that 62.4% of observed variation is explained by the first two principal components (PC1: 45.0%, PC2: 17.4%). The 24 specimen PCA scatterplot similarly reveals two distinct clusters along the PC1 axis, one of *F. delangeii* specimens and the other of strictly *F. rostrata*. 68.2% of variation is further explained by the first two principal components (PC1: 53.6%, PC2: 13.6%), supporting the pattern that the specimens belong to separate species. 

### PCA: Branching Morphology Characters
Further PCA analysis of branching characters, based on 25 specimens, shows that 80.7% of observed variation is explained by the first two principal components (PC1: 43.2%, PC2: 37.5%). Although no strong, separated clusters formed along the axes, *F. rostrata* specimens grouped close together while the *F. delangeii* specimens were spread further away. There existed some overlap between the specimens, indicating overall morphological similarities in terms of branching traits, but enough differences to produce slight separation on the principal component axes. 

### PCA Loadings
####
Directionally, as you move toward the right (positive) end of the PC1 axis, the traits with the highest positive loadings significantly increase in magnitude, which is what effectively pushes the clusters apart and distinguishes the two species and vice versa. PC2 captures secondary morphological variation that emerges within those distinct clusters. The tables report the absolute value, or magnitude, or each character's loading value.

#### n = 68, PC1 (Leaf)
| Character | Loading Magnitude |
| :--- | :--- |
| Base-apex distance um (stem leaves) | 0.440169 |
| Orthogonal count (stem leaves) | 0.433630 |
| Base-apex count (stem leaves) | 0.432616 |
| Orthogonal distance um | 0.431302 |
| Length um (oilbodies) | 0.317515 |
| Width um (oilbodies) | 0.273396 |
| Length um (leaf lobules) | 0.160982 |
| Length um (leaf median cells) | 0.143614 |
| Width um (leaf lobules) | 0.118212 |
| Width um (leaf median cells) | 0.094672 |

Steam leaf dimensions most strongly contribute to separation for PC1.

#### n = 68, PC2 (Leaf)
| Character | Loading Magnitude |
| :--- | :--- |
| Width um (leaf lobules) | 0.571426 |
| Length um (leaf lobules) | 0.478105 |
| Length um (leaf median cells) | 0.425173 |
| Width um (oilbodies) | 0.288339 |
| Length um (oilbodies) | 0.260158 |
| Width um (leaf median cells) | 0.206292 |
| Orthogonal distance um | 0.164430 |
| Orthogonal count (stem leaves) | 0.141689 |
| Base-apex distance um (stem leaves) | 0.128713 |
| Base-apex count (stem leaves) | 0.084011 |

Leaf lobule leaf dimensions and leaf median cell dimensions most strongly contribute to separation for PC2.

#### n = 25, PC1 (Branching)
| Character | Loading Magnitude |
| :--- | :--- |
| term_branchlength_dev | 0.68 |
| internal_branchlength_dev | 0.63 |
| term_branchlength_avg | -0.21 |
| internal_branchlength_avg | -0.30 |

Terminal branch length deviation and internal branch length deviation are the traits most strongly driving separation for PC1.

#### n = 25, PC2 (Branching)
| Character | Loading Magnitude |
| :--- | :--- |
| term_branchlength_avg | 0.66 |
| internal_branchlength_avg | 0.65 |
| internal_branchlength_dev | 0.32 |
| term_branchlength_dev | 0.19 |

Average terminal branch length and average internal branch length deviation are the traits most strongly driving separation for PC2.


## Repository Contents
1. `/Cleaned Data`: Contains cleaned `.csv` data separated by character immediately usable for morphometric analysis.
2. `/Scripts`: Contains the Python analysis pipelines (`branching_architecture.py`, `leaf_morphology.py`) used to process data and generate PCA models.
3. `/Figures`: Contains graph outputs, including PCA scatterplots and trait contribution loading profiles.

