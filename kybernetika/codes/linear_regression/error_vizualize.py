import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.metrics import mean_squared_error

# ------------------------------------
# 1️⃣ Dataset (same as before)
# ------------------------------------
np.random.seed(42)
x = np.linspace(0, 10, 20)
y = 2.0 * x + 1.0 + np.random.normal(0, 2, size=20)
n = len(x)

# ------------------------------------
# 2️⃣ Compute optimal parameters analytically
# ------------------------------------
a_opt = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - (np.sum(x))**2)
b_opt = (np.sum(y) - a_opt * np.sum(x)) / n

# ------------------------------------
# 3️⃣ Create a **wider grid** of a, b values
# ------------------------------------
a_vals = np.linspace(-2, 6, 200)   # much wider slope range
b_vals = np.linspace(-10, 15, 200) # wider intercept range
A, B = np.meshgrid(a_vals, b_vals)

# ------------------------------------
# 4️⃣ Compute MSE for each (a, b)
# ------------------------------------
MSE = np.zeros_like(A)
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        y_pred = A[i, j] * x + B[i, j]
        MSE[i, j] = mean_squared_error(y, y_pred)

# ------------------------------------
# 5️⃣ 3D Surface Plot (Zoomed Out)
# ------------------------------------
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A, B, MSE, cmap='viridis', alpha=0.85)
ax.set_xlabel('a (slope)')
ax.set_ylabel('b (intercept)')
ax.set_zlabel('MSE')
ax.set_title('3D Error Surface for Linear Regression (Zoomed Out)')

ax.scatter(a_opt, b_opt,
           mean_squared_error(y, a_opt * x + b_opt),
           color='red', s=70, label='Minimum (a,b)')
ax.legend()


# ------------------------------------
# 6️⃣ 2D Contour Plot (Zoomed Out)
# ------------------------------------
plt.figure(figsize=(8, 6))
cp = plt.contour(A, B, MSE, levels=40, cmap='viridis')
plt.clabel(cp, inline=True, fontsize=8)
plt.scatter(a_opt, b_opt, color='red', label='Minimum (a,b)')
plt.xlabel('a (slope)')
plt.ylabel('b (intercept)')
plt.title('MSE Contour Plot (Zoomed Out)')
plt.legend()
plt.grid(True)
plt.show()
