import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. Load and prepare data
# Ensure the filename matches your specific dataset (e.g., 'Caitlin_Data.csv' or 'Jeff_Data.csv')
df = pd.read_csv('Data for figures.xlsx - w_o styli or underleaves.csv')
features = df.drop(['ID', 'Species'], axis=1)
X = StandardScaler().fit_transform(features)

# 2. PCA
pca = PCA(n_components=2)
coords = pca.fit_transform(X)
loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2'], index=features.columns)

# 3. Save Scatterplot
sns.set_style("whitegrid")
plt.figure(figsize=(10, 7))
sns.scatterplot(x=coords[:, 0], y=coords[:, 1], hue=df['Species'], 
                palette=["#4857ff", "#ff617b"], s=120, alpha=0.8, edgecolor='black')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%})', fontsize=12, fontweight='bold')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%})', fontsize=12, fontweight='bold')
plt.title('PCA of 68 specimens of F. delangeii and F. rostrata', fontsize=14, fontweight='bold', pad=20)
plt.legend(title='Species', title_fontsize='11', fontsize='10')
plt.tight_layout()
plt.savefig('Jeff_PCA_Scatterplot.png', dpi=300)
print("Saved: Jeff_PCA_Scatterplot.png")

# 4. Save PC1 and PC2 Loadings TOGETHER
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle('Contribution of Leaf Characters to PCA of F. delangeii and F. rostrata', fontsize=14, fontweight='bold')

loadings['PC1'].sort_values().plot(kind='barh', ax=axes[0], color='skyblue', edgecolor='black')
axes[0].set_title('Drivers of PC1', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Loading Magnitude')

loadings['PC2'].sort_values().plot(kind='barh', ax=axes[1], color='salmon', edgecolor='black')
axes[1].set_title('Drivers of PC2', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Loading Magnitude')

plt.tight_layout()
plt.savefig('Jeff_PCA_Loadings_Combined.png', dpi=300)
print("Saved: Jeff_PCA_Loadings_Combined.png")
plt.show()

# 5. Print analytical summary to console
print("\n--- Summary of Drivers ---")
print("Top drivers for PC1 (Primary Separation):")
print(loadings.abs().sort_values(by='PC1', ascending=False)['PC1'])
print("\nTop drivers for PC2 (Secondary Variation):")
print(loadings.abs().sort_values(by='PC2', ascending=False)['PC2'])