import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# -------------------------------
# Generování  dat
# -------------------------------
np.random.seed(42)  # random seed (opakovaní náhody)

x = np.linspace(0, 10, 20)                # hodiny studia (0 až 10)
y = 2.0 * x + 1.0 + np.random.normal(0, 2, size=20)  # přibližný lineární vztah + šum

n = len(x)

# --------------------
# Vizualizacezadaných dat
# --------------------

plt.figure(figsize=(8,5))
plt.scatter(x, y, color='blue', label='Data s šumem')
plt.title('Generovaná data pro lineární regresi')
plt.xlabel('Hodiny studia')
plt.ylabel('Body z testu')
plt.legend()
plt.grid(True)
plt.show()

# -------------------------------
# Výpočet regresní přímky
# -------------------------------
a = (n * np.sum(x*y) - np.sum(x) * np.sum(y)) / (n*np.sum(x**2) - (np.sum(x))**2)
b = (np.sum(y) - a*np.sum(x)) / n

# Predikce.
y_pred = a * x + b

# -------------------------------
# Vyhodnocení přesnosti
# -------------------------------
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

# -------------------------------
# Výpis výsledků
# -------------------------------
print(f"Rovnice regresní přímky: y = {a:.2f}x + {b:.2f}")
print(f"MSE  = {mse:.3f}")
print(f"RMSE = {rmse:.3f}")
print(f"MAE  = {mae:.3f}")
print(f"R²   = {r2:.3f}")

# -------------------------------
# Vizualizace
# -------------------------------
plt.figure(figsize=(8,5))
plt.scatter(x, y, color='blue', label='Skutečná data')
plt.plot(x, y_pred, color='red', label=f'Model: y = {a:.2f}x + {b:.2f}')
plt.title('Lineární regrese pro větší množství dat')
plt.xlabel('Hodiny studia')
plt.ylabel('Body z testu')
plt.legend()
plt.grid(True)
plt.show()
