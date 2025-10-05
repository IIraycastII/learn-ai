import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Generate 100 points along a base line y = 1.5*x + 5
x = np.linspace(10, 200, 100)  # elongated X range

# Increase noise to scatter the points more
y = 1.5 * x + 5 + np.random.normal(0, 20, size=100)  # higher std dev for more scatter

points = np.column_stack((x, y))
original_points = points.copy()

# Iterative midpoint process to get final point
points_mid = points.copy()
while len(points_mid) > 1:
    midpoints = []
    for i in range(len(points_mid) - 1):
        mid_x = (points_mid[i][0] + points_mid[i + 1][0]) / 2
        mid_y = (points_mid[i][1] + points_mid[i + 1][1]) / 2
        midpoints.append([mid_x, mid_y])
    points_mid = np.array(midpoints)

final_point = points_mid[0]

# Compute slope of the final line
slope = final_point[1] / final_point[0]

# Predicted y values on the midpoint line for each original x
y_pred = slope * original_points[:, 0]

# Compute residuals and average error
residuals = original_points[:, 1] - y_pred
average_error = np.mean(residuals)

print(f"Average Error (Actual - Predicted): {average_error:.3f}")
print(f"Residual Range: {np.min(residuals):.3f} to {np.max(residuals):.3f}")

# Plot
plt.figure(figsize=(10,6))
plt.scatter(original_points[:,0], original_points[:,1], color='orange', s=50, label='Original Points')
x_line = np.linspace(0, 250, 500)
plt.plot(x_line, slope*x_line, color='red', linewidth=2, label='Final Line (Infinite)')
plt.title("Midpoint Convergence Line with 100 Highly Scattered Points", fontsize=14)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()
