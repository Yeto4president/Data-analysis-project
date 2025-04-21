import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

# 1. Data Preparation
# Original data from the document
data = {
    'Year': [2010, 2012, 2014, 2016, 2018, 2020],
    'Total ASP produced': [0.486, 0.519, 0.539, 0.591, 0.63, 0.714],
    'GHG emissions': [96.4, 98.1, 104.2, 108.2, 113.9, 127.8],
    'Emission intensity': [196.5, 188.9, 193.4, 182.9, 180.8, 179.1],
    'Total ASP supply': [5.54, 5.6, 5.49, 5.71, 5.77, 6.21]
}

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Display original data
print("Original Transposed Data:")
display(df)

# 2. Basic Statistics
stats = pd.DataFrame({
    'Minimum': df.min(),
    'Maximum': df.max(),
    'Standard Deviation': df.std(),
    'Mean': df.mean()
})

print("\nBasic Statistics:")
display(stats)

# 3. Data Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)
X_scaled_df = pd.DataFrame(X_scaled, columns=df.columns, index=df.index)

print("\nStandardized Data (Centered and Reduced):")
display(X_scaled_df)

# 4. Correlation Matrix
correlation_matrix = X_scaled_df.corr()
print("\nCorrelation Matrix:")
display(correlation_matrix)

# 5. PCA Analysis
pca = PCA()
principal_components = pca.fit_transform(X_scaled_df)
explained_variance_ratio = pca.explained_variance_ratio_

# Eigenvalues
eigenvalues = pca.explained_variance_
print("\nEigenvalues:")
display(pd.DataFrame(eigenvalues, index=[f'λ{i+1}' for i in range(len(eigenvalues))], columns=['Value']))

# Variance explained by each axis
print("\nPercentage of Variance Explained:")
for i, ratio in enumerate(explained_variance_ratio):
    print(f"Axe {i+1}: {ratio*100:.4f}%")
print(f"Total variance explained (Axes 1+2): {sum(explained_variance_ratio[:2])*100:.4f}%")

# 6. Component Matrix (Loadings)
loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
loadings_df = pd.DataFrame(loadings[:, :2], index=df.columns, columns=['Axe 1', 'Axe 2'])

print("\nMatrix of Loadings (Saturations):")
display(loadings_df)

# 7. Correlation Circle
plt.figure(figsize=(8, 8))
for i, (x, y) in enumerate(loadings[:, :2]):
    plt.arrow(0, 0, x, y, color='b', alpha=0.5)
    plt.text(x*1.1, y*1.1, df.columns[i], color='b')
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title('Correlation Circle (Axes 1-2: 97.9749%)')
circle = plt.Circle((0, 0), 1, color='black', fill=False)
plt.gca().add_artist(circle)
plt.xlabel('Axe 1 (92.7375%)')
plt.ylabel('Axe 2 (5.2374%)')
plt.savefig('correlation_circle.png')
plt.close()

# 8. Principal Components
principal_components_df = pd.DataFrame(principal_components[:, :2], index=df.index, columns=['Axe 1', 'Axe 2'])
print("\nPrincipal Components Matrix:")
display(principal_components_df)

# 9. Quality of Representation (cos^2)
cos2 = np.square(principal_components[:, :2]) / np.sum(np.square(principal_components), axis=1, keepdims=True)
cos2_df = pd.DataFrame(cos2, index=df.index, columns=['Axe 1', 'Axe 2'])
print("\nQuality of Representation (cos^2):")
display(cos2_df)

# 10. Selection of Years
print("\nSelected Years:")
print("Axe 1: 2010, 2012, 2020 (high cos^2 values)")
print("Axe 2: 2016 (highest cos^2 value)")

# 11. Graphical Representation
plt.figure(figsize=(10, 6))
for year in principal_components_df.index:
    x, y = principal_components_df.loc[year]
    color = 'purple' if year in [2010, 2012, 2020] else 'orange' if year == 2016 else 'blue'
    plt.scatter(x, y, c=color, s=100)
    plt.text(x+0.05, y+0.05, year)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.title('Principal Components Plot (Axes 1-2)')
plt.xlabel('Axe 1 (92.7375%)')
plt.ylabel('Axe 2 (5.2374%)')
plt.savefig('principal_components_plot.png')
plt.close()

# 12. Conclusion
print("\nConclusion:")
print("Axe 1: Highlights the relationship between animal protein production, supply, and emission intensity over time.")
print("- 2010 and 2012 show lower animal protein production and supply compared to 2020.")
print("- 2020 shows significant increase in production and supply, but lower emission intensity, suggesting improved efficiency.")
print("Axe 2: Focuses on GHG emissions, with 2016 as an outlier with lower emissions.")
print("- The increase in production and consumption may strain natural resources, but reduced emission intensity suggests efforts toward sustainability.")
