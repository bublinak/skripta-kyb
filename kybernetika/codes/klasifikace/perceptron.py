import numpy as np
import matplotlib.pyplot as plt
import time

# --- 1. Generování 2D dat ---
np.random.seed(0)
X1 = np.random.randn(10, 2) + np.array([1, 1])  # Třída +1 (červené body)
X2 = np.random.randn(10, 2) + np.array([-1, -1])  # Třída -1 (modré body)

X = np.vstack((X1, X2))
y = np.hstack((np.ones(10), -np.ones(10)))  # cílové hodnoty (+1 / -1)

# --- 2. Inicializace perceptronu ---
w = np.random.randn(2) * 0.5  # náhodné váhy
b = 0.0  # bias
eta = 0.1  # learning rate


# --- 3. Pomocné funkce ---
def predict(x):
    """Vrátí znaménko (třídu) predikce."""
    return np.sign(np.dot(x, w) + b)


def plot_state(step, point=None):
    """Vykreslí aktuální stav rozhodovací hranice a dat."""
    plt.clf()
    plt.title(f"Krok {step}")

    # Data
    plt.scatter(X1[:, 0], X1[:, 1], color='red', label='Třída +1')
    plt.scatter(X2[:, 0], X2[:, 1], color='blue', label='Třída -1')

    # Zvýrazni právě zpracovávaný bod
    if point is not None:
        plt.scatter(point[0], point[1], s=200, edgecolor='k', facecolor='none', linewidths=2)

    # Rozhodovací přímka: w1*x + w2*y + b = 0 → y = (-w1*x - b)/w2
    x_vals = np.linspace(-5, 5, 100)
    if w[1] != 0:
        y_vals = (-w[0] * x_vals - b) / w[1]
        plt.plot(x_vals, y_vals, 'k--', label='Rozhodovací hranice')

    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.legend()
    plt.grid(True)
    plt.pause(0.3)  # krátká pauza, aby se graf zobrazil


# --- 4. Trénování perceptronu po jednotlivých krocích ---
plt.ion()  # zapne interaktivní režim (pro živou aktualizaci grafu)
step = 0
max_epochs = 10

for epoch in range(max_epochs):
    for i in range(len(X)):
        step += 1
        y_pred = predict(X[i])
        if y_pred != y[i]:  # Chyba → upravíme váhy
            w += eta * y[i] * X[i]
            b += eta * y[i]
        plot_state(step, point=X[i])

plt.ioff()  # vypne interaktivní režim
plt.show()  # finální zobrazení
