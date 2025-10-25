import numpy as np
import random
import math

dataset = np.array([[5.7, 4.3, 8.8, 2.5, 6.7, 3.0, 5.8],
                    [5.6, 7.4, 6.5, 3.2, 2.1, 6.4, 7.8]])

for i in range(len(dataset[0])):
    centroid_x_1 = random.choices(dataset[0])
    centroid_y_1 = random.choices(dataset[1])

    centroid_x_1 = list(map(float, centroid_x_1))
    centroid_y_1 = list(map(float, centroid_y_1))

    centroid_x_2 = random.choices(dataset[0])
    centroid_y_2 = random.choices(dataset[1])

    centroid_x_2 = list(map(float, centroid_x_2))
    centroid_y_2 = list(map(float, centroid_y_2))

    if centroid_x_2 == centroid_x_1 or centroid_y_2 == centroid_y_1:
        centroid_x_2 = random.choices(dataset[0])
        centroid_y_2 = random.choices(dataset[1])

        centroid_x_2 = list(map(float, centroid_x_2))
        centroid_y_2 = list(map(float, centroid_y_2))

x_coordinates = []
y_coordinates = []
distance_1 = []
distance_2 = []
new_data = []

for i in range(len(dataset[0])):
    x_coordinates.append(dataset[0][i])
    x_coordinates = list(map(float, x_coordinates))

    y_coordinates.append(dataset[1][i])
    y_coordinates = list(map(float, y_coordinates))

for i in range(len(x_coordinates)):
    distance_1.append(math.sqrt(((x_coordinates[i] - centroid_x_1[0]) ** 2) + ((y_coordinates[i] - centroid_y_1[0]) ** 2)))
    distance_2.append(math.sqrt(((x_coordinates[i] - centroid_x_2[0]) ** 2) + ((y_coordinates[i] - centroid_y_2[0]) ** 2)))

    if distance_1[i] > distance_2[i]:
        centroid_x_1 = [(centroid_x_1[0] + x_coordinates[i])/2]
        centroid_y_1 = [(centroid_y_1[0] + y_coordinates[i])/2]
        new_data.append("C1")
    elif distance_2[i] > distance_1[i]:
        centroid_x_2 = [(centroid_x_2[0] + x_coordinates[i])/2]
        centroid_y_2 = [(centroid_y_2[0] + y_coordinates[i])/2]
        new_data.append("C2")

dataset = np.vstack((dataset, new_data))

print(dataset)


