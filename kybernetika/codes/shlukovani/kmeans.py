import numpy as np
import matplotlib.pyplot as plt

# --- 1. Generování dat ---
np.random.seed(1)
cluster1 = np.random.randn(20, 2) + np.array([1, 1])
cluster2 = np.random.randn(20, 2) + np.array([5, 5])
cluster3 = np.random.randn(20, 2) + np.array([8, 1])
X = np.vstack((cluster1, cluster2, cluster3))

# --- 2. K-means algoritmus ---
def kmeans(X, K=3, max_iters=10):
    # náhodná inicializace centroidů
    idx = np.random.choice(len(X), K, replace=False)
    centroids = X[idx]

    for it in range(max_iters):
        # přiřazení bodů ke shluku
        labels = np.argmin(np.linalg.norm(X[:, None] - centroids[None, :], axis=2), axis=1)

        # vykreslení aktuálního stavu
        plt.clf()
        plt.title(f"K-means – iterace {it+1}")
        for k in range(K):
            plt.scatter(X[labels == k, 0], X[labels == k, 1], label=f"Shluk {k+1}")
            plt.scatter(*centroids[k], color='black', marker='x', s=200)
        plt.legend()
        plt.grid(True)
        plt.pause(5)

        # přepočet centroidů
        new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(K)])
        # pokud se centroidy nezmění -> konec
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids

    plt.ioff()
    plt.show()
    return centroids, labels

# --- 3. Spuštění ---
plt.ion()
final_centroids, final_labels = kmeans(X, K=3, max_iters=10)
