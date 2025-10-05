import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Generate 100 X values
x = np.linspace(10, 200, 100)

# Generate corresponding Y values with noise
y = 1.5 * x + 5 + np.random.normal(0, 20, size=100)

# Combine into dataset
dataset = np.column_stack((x, y))

# Store min and max values
x_min = np.min(dataset[:,0])
x_max = np.max(dataset[:,0])
y_min = np.min(dataset[:,1])
y_max = np.max(dataset[:,1])

data_range = {
    "x_min": x_min,
    "x_max": x_max,
    "y_min": y_min,
    "y_max": y_max
}

print("Data range:", data_range)

# Grid search for best slope (m) only, intercept c = 0
m_values = np.linspace(-2, 2, 500)  # slopes to try
best_m = None
lowest_error = float('inf')

# Search for the slope that minimizes average residual
for m in m_values:
    y_pred = m * x  # intercept = 0
    avg_error = np.mean(y - y_pred)
    abs_avg_error = abs(avg_error)
    if abs_avg_error < lowest_error:
        lowest_error = abs_avg_error
        best_m = m

print(f"Best slope (m) = {best_m:.4f}, Average Residual Error = {lowest_error:.4f}")

# Plotting the dataset and the best slope line
x_line = np.linspace(x_min - 50, x_max + 50, 500)
y_line = best_m * x_line  # intercept = 0

plt.figure(figsize=(10,6))
plt.scatter(x, y, color='orange', s=50, label='Data Points')
plt.plot(x_line, y_line, color='red', linewidth=2, label=f'Best Slope Line (m={best_m:.2f})')
plt.title("100-Point Dataset with Best Slope Line (c = 0)")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()
