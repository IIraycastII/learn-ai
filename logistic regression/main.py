import math
import random
import matplotlib.pyplot as plt

x_original = [random.randint(80, 100) for _ in range(100)]
y_original = [random.randint(80, 100) for _ in range(100)]

weight = 1
bias = 0
e = math.e
threshold = 0.5

z_x = [weight * x + bias for x in x_original]
z_y = [weight * y + bias for y in y_original]
z_combined = [(weight * z_x[i]) + (weight * z_y[i]) + bias for i in range(len(z_x))]

z_min, z_max = min(z_combined), max(z_combined)
z_scaled = [((z - z_min) / (z_max - z_min)) * 20 - 10 for z in z_combined]

sigmoid_combined = [1 / (1 + e ** -z) for z in z_scaled]

z_sorted, sigmoid_sorted = zip(*sorted(zip(z_scaled, sigmoid_combined)))

plt.figure(figsize=(8, 5))
plt.plot(z_sorted, sigmoid_sorted, color='blue', label='Sigmoid(z_combined)')
plt.axhline(threshold, color='red', linestyle='--', label='Threshold = 0.5')
plt.title('Proper Sigmoid Curve')
plt.xlabel('z (scaled)')
plt.ylabel('σ(z)')
plt.legend()
plt.grid(True)
plt.show()

plt.scatter(x_original, y_original, color='orange')
plt.title("Original Random Points")
plt.show()
