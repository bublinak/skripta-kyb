import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# === 1. Generování více 2D dat ===
np.random.seed(0)

# Tři třídy, každá v jiném rohu
class1 = np.random.randn(25, 2) + np.array([1.5, 1.5])
class2 = np.random.randn(25, 2) + np.array([-1.5, -1.5])
class3 = np.random.randn(25, 2) + np.array([1.5, -1.5])

X = np.vstack((class1, class2, class3))
y = np.hstack((
    np.ones(len(class1)),       # třída +1
    np.full(len(class2), -1),   # třída -1
    np.full(len(class3), 2)     # třída +2
))

# === 2. Funkce pro výpočet vzdálenosti a predikci ===
def euclid(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def knn_predict(X_train, y_train, x_query, k=5):
    # spočítej vzdálenosti od všech bodů
    dists = [(euclid(x_query, x), cls) for x, cls in zip(X_train, y_train)]
    dists.sort(key=lambda t: t[0])
    k_neigh = dists[:k]

    # hlasování sousedů
    votes = Counter(cls for _, cls in k_neigh)
    return votes.most_common(1)[0][0]

# === 3. Vizualizace rozhodovacích oblastí ===
def plot_knn_decision(X, y, k=5):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    grid = np.c_[xx.ravel(), yy.ravel()]

    preds = np.array([knn_predict(X, y, p, k=k) for p in grid])
    Z = preds.reshape(xx.shape)

    plt.figure(figsize=(7, 7))
    plt.contourf(xx, yy, Z, alpha=0.25, cmap='coolwarm')
    plt.scatter(X[y == +1, 0], X[y == +1, 1], color='red', label='Třída +1', edgecolor='k')
    plt.scatter(X[y == -1, 0], X[y == -1, 1], color='blue', label='Třída -1', edgecolor='k')
    plt.scatter(X[y == 2, 0], X[y == 2, 1], color='green', label='Třída +2', edgecolor='k')
    plt.title(f"k-NN klasifikace (k={k}, nevážené)")
    plt.xlabel("x₁")
    plt.ylabel("x₂")
    plt.legend()
    plt.grid(True)
    plt.show()

# === 4. Spuštění s různými hodnotami k ===
for k in [1, 3, 7, 15]:
    plot_knn_decision(X, y, k=k)
