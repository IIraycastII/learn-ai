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

# Gradient Descent Parameters
m = np.random.uniform(-2, 2)  # initial slope
learning_rate = 0.0001        # small step size
iterations = 500              # number of iterations
errors = []                   # store error at each step

# Gradient descent loop
for i in range(iterations):
    y_pred = m * x  # intercept c = 0
    residuals = y - y_pred
    avg_error = np.mean(residuals)  # same error as earlier
    errors.append(abs(avg_error))    # track absolute error

    # Gradient calculation (derivative of error w.r.t m)
    gradient = -np.mean(residuals * x)  # negative because we want to go downhill

    # Update slope
    m = m - learning_rate * gradient

# After gradient descent
best_m = m
lowest_error = errors[-1]

print(f"Gradient Descent Result: Best slope (m) = {best_m:.4f}, Lowest Average Residual Error = {lowest_error:.4f}")

# Plot dataset and best slope line
x_line = np.linspace(x_min - 50, x_max + 50, 500)
y_line = best_m * x_line

plt.figure(figsize=(12,6))

# Scatter plot of dataset
plt.scatter(x, y, color='orange', s=50, label='Data Points')

# Best slope line
plt.plot(x_line, y_line, color='red', linewidth=2, label=f'Best Slope Line (m={best_m:.2f})')

plt.title("100-Point Dataset with Best Slope Line (c = 0)")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

# Plot error decreasing over iterations
plt.figure(figsize=(10,5))
plt.plot(errors, color='blue', linewidth=2)
plt.title("Average Residual Error Decreasing During Gradient Descent")
plt.xlabel("Iteration")
plt.ylabel("Absolute Average Residual Error")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
