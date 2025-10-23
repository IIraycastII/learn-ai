import numpy as np
import pandas as pd
import math

data = {
    "x": np.array([1, 2, 3, 4, 5, 6, 5, 3, 4, 6]),
    "y": np.array([2, 4, 1, 3, 6, 5, 6, 3, 2, 1]),
    "color": np.array(["red", "green", "red", "green", "red", "green", "green", "red", "red", "red"])
}

df = pd.DataFrame(data)

input_1 = input("Enter the values here: ")

list_1 = list(map(int, input_1.split()))

list_euclidean_dist = list(math.sqrt((list_1[0] - df["x"][i])**2 + (list_1[1] - df["y"][i])**2) for i in range(len(df["x"])))

print(list_euclidean_dist)

input_2 = int(input("Enter the number of min points to take: "))
list_min = []
index_list = []

n_green = 0
n_red = 0

for i in range(input_2):
    index = list_euclidean_dist.index(min(list_euclidean_dist))
    index_list.append(index)
    list_min.append(list_euclidean_dist[index])
    list_euclidean_dist.remove(list_euclidean_dist[index])
    list_choices = list(df["color"][index_list[i]] for i in range(len(index_list)))

    for j in list_choices:
        if j == "green":
            n_green += 1
        elif j == "red":
            n_red += 1

if n_green > n_red:
    print("green")
    n_green = 0
elif n_red > n_green:
    print("red")
    n_red = 0
elif n_green == n_red:
    print("50% chance of both")
    n_green = 0
    n_red = 0
