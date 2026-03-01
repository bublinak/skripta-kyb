import numpy as np
import matplotlib.pyplot as plt

# --- 1. Vytvoření dat ---
np.random.seed(0)
X = np.random.multivariate_normal(mean=[0, 0], cov=[[3, 2], [2, 2]], size=100)

# --- 2. Centrovaní dat ---
X_centered = X - np.mean(X, axis=0)

# --- 3. Kovarianční matice ---
cov = np.cov(X_centered.T)

# --- 4. Vlastní čísla a vektory ---
eigvals, eigvecs = np.linalg.eig(cov)

# Seřazení podle velikosti
idx = np.argsort(eigvals)[::-1]
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

# --- 5. Projekce dat na 1. dvě hlavní komponenty ---
Z = X_centered @ eigvecs

# --- 6. Vizualizace ---
plt.figure(figsize=(7, 7))
plt.scatter(X[:, 0], X[:, 1], alpha=0.3, label="Původní data")
origin = np.mean(X, axis=0)

for i in range(2):
    vec = eigvecs[:, i] * np.sqrt(eigvals[i]) * 3
    plt.arrow(origin[0], origin[1], vec[0], vec[1],
              head_width=0.2, head_length=0.3, color='red' if i == 0 else 'orange',
              length_includes_head=True)
    plt.text(origin[0] + vec[0]*1.1, origin[1] + vec[1]*1.1,
             f"PC{i+1}", color='red' if i == 0 else 'orange', fontsize=12)

plt.axis('equal')
plt.title("PCA – hlavní komponenty")
plt.xlabel("x₁")
plt.ylabel("x₂")
plt.legend()
plt.grid(True)
plt.show()
