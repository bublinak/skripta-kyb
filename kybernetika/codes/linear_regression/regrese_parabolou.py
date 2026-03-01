import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# -------------------------------
# Generování nelineárních dat
# -------------------------------
np.random.seed(42)

x = np.linspace(-5, 5, 40)
# Skutečný vztah (parabola) + šum
y = 2.0 * x**2 + 3.0 * x + 5.0 + np.random.normal(0, 5, len(x))

# -------------------------------
# Vizualizace vstupních dat
# -------------------------------
plt.figure(figsize=(8,5))
plt.scatter(x, y, color='blue', label='Data s šumem')
plt.title('Generovaná data pro kvadratickou regresi')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# -------------------------------
# Výpočet regresních koeficientů (a, b, c)
# -------------------------------
# Matice pro model y = a*x^2 + b*x + c
X = np.column_stack((x**2, x, np.ones(len(x))))

# Normální rovnice: θ = (XᵀX)^(-1) Xᵀy
theta = np.linalg.inv(X.T @ X) @ X.T @ y
a, b, c = theta

print(f"Rovnice paraboly: y = {a:.2f}x² + {b:.2f}x + {c:.2f}")

# -------------------------------
# Predikce a metriky přesnosti
# -------------------------------
y_pred = a * x**2 + b * x + c

mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"MSE  = {mse:.3f}")
print(f"RMSE = {rmse:.3f}")
print(f"MAE  = {mae:.3f}")
print(f"R²   = {r2:.3f}")

# -------------------------------
# Vizualizace výsledku
# -------------------------------
plt.figure(figsize=(8,5))
plt.scatter(x, y, color='blue', label='Skutečná data')
plt.plot(x, y_pred, color='red', linewidth=2, label=f'Model: y = {a:.2f}x² + {b:.2f}x + {c:.2f}')
plt.title('Kvadratická regrese (parabolický model)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
