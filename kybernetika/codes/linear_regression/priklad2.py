import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------
# Generování dat
# -------------------------------
np.random.seed(42)
n = 50
x1 = np.random.uniform(0, 10, n)  # hodiny studia
x2 = np.random.uniform(0, 5, n)   # počet opakování

# Skutečný lineární vztah + šum
y = 1.5 * x1 + 2.0 * x2 + 3.0 + np.random.normal(0, 2, n)

# -------------------------------
# 🎨 Vizualizace vstupních dat (barevně)
# -------------------------------
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Barvy podle hodnoty y
scatter = ax.scatter(x1, x2, y, c=y, cmap='viridis', s=60, edgecolors='k')
fig.colorbar(scatter, ax=ax, label='Body z testu (y)')

ax.set_xlabel('Hodiny studia (x1)')
ax.set_ylabel('Počet opakování (x2)')
ax.set_zlabel('Body z testu (y)')
ax.set_title('Generovaná data pro lineární regresi (2 proměnné) – barevná mapa')
plt.show()

# -------------------------------
# Výpočet koeficientů
# -------------------------------
X = np.column_stack((x1, x2, np.ones(n)))
a = np.linalg.inv(X.T @ X) @ X.T @ y
a1, a2, b = a
print(f"Rovnice: y = {a1:.2f}x1 + {a2:.2f}x2 + {b:.2f}")

# -------------------------------
# Predikce + metriky
# -------------------------------
y_pred = X @ a
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"MSE  = {mse:.3f}")
print(f"RMSE = {rmse:.3f}")
print(f"MAE  = {mae:.3f}")
print(f"R²   = {r2:.3f}")

# -------------------------------
# 🌈 3D vizualizace s regresní rovinou
# -------------------------------
x1_grid, x2_grid = np.meshgrid(np.linspace(0, 10, 30), np.linspace(0, 5, 30))
y_grid = a1 * x1_grid + a2 * x2_grid + b

fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111, projection='3d')

# Data body – barevné podle skutečných hodnot
scatter = ax.scatter(x1, x2, y, c=y, cmap='viridis', s=60, edgecolors='k', label='Skutečná data')

# Regresní rovina – poloprůhledná
ax.plot_surface(x1_grid, x2_grid, y_grid, color='red', alpha=0.5)

# Popisky
ax.set_xlabel('Hodiny studia (x1)')
ax.set_ylabel('Počet opakování (x2)')
ax.set_zlabel('Body z testu (y)')
ax.set_title('Lineární regrese (2 proměnné) – model a data')
fig.colorbar(scatter, ax=ax, label='Body z testu (y)')
plt.show()
