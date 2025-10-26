import numpy as np
import math
import pandas as pd

dataset = np.array([["sunny", "sunny", "rainy", "sunny", "sunny", "sunny"],
                    ["cool", "cool", "cool", "hot", "cool", "hot"],
                    ["play tennis", "play tennis", "dont play", "play tennis", "dont play", "dont play"]])

print(pd.DataFrame(dataset))

play_tennis_count = 0
dont_play_count = 0
count_sunny_play = 0
count_sunny_dont_play = 0
count_rainy_play = 0
count_rainy_dont_play = 0
count_sunny = 0
count_rainy = 0

for i in range(len(dataset[0])):
    if dataset[2][i] == "play tennis":
        play_tennis_count += 1
    elif dataset[2][i] == "dont play":
        dont_play_count += 1

probability_play_tennis = play_tennis_count / len(dataset[2])
probability_dont_play = dont_play_count / len(dataset[2])

entropy = 0
if probability_play_tennis > 0:
    entropy -= probability_play_tennis * math.log2(probability_play_tennis)
if probability_dont_play > 0:
    entropy -= probability_dont_play * math.log2(probability_dont_play)
print(entropy)

for i in range(len(dataset[0])):
    if dataset[0][i] == "sunny":
        count_sunny += 1
    if dataset[0][i] == "sunny" and dataset[2][i] == "play tennis":
        count_sunny_play += 1
    if dataset[0][i] == "sunny" and dataset[2][i] == "dont play":
        count_sunny_dont_play += 1

probability_sunny_play_tennis = count_sunny_play / count_sunny
probability_sunny_dont_play = count_sunny_dont_play / count_sunny

entropy_sunny = 0
if probability_sunny_play_tennis > 0:
    entropy_sunny -= probability_sunny_play_tennis * math.log2(probability_sunny_play_tennis)
if probability_sunny_dont_play > 0:
    entropy_sunny -= probability_sunny_dont_play * math.log2(probability_sunny_dont_play)

for i in range(len(dataset[0])):
    if dataset[0][i] == "rainy":
        count_rainy += 1
    if dataset[0][i] == "rainy" and dataset[2][i] == "play tennis":
        count_rainy_play += 1
    if dataset[0][i] == "rainy" and dataset[2][i] == "dont play":
        count_rainy_dont_play += 1

probability_rainy_play_tennis = count_rainy_play / count_rainy
probability_rainy_dont_play = count_rainy_dont_play / count_rainy

entropy_rainy = 0
if probability_rainy_play_tennis > 0:
    entropy_rainy -= probability_rainy_play_tennis * math.log2(probability_rainy_play_tennis)
if probability_rainy_dont_play > 0:
    entropy_rainy -= probability_rainy_dont_play * math.log2(probability_rainy_dont_play)

weighted_entropy_weather = ((count_sunny / len(dataset[2])) * entropy_sunny) + ((count_rainy / len(dataset[2])) * entropy_rainy)

count_cool = 0
count_cool_play = 0
count_cool_dont_play = 0
count_hot = 0
count_hot_play = 0
count_hot_dont_play = 0

for i in range(len(dataset[1])):
    if dataset[1][i] == "cool":
        count_cool += 1
    if dataset[1][i] == "cool" and dataset[2][i] == "play tennis":
        count_cool_play += 1
    if dataset[1][i] == "cool" and dataset[2][i] == "dont play":
        count_cool_dont_play += 1

probability_cool_play_tennis = count_cool_play / count_cool
probability_cool_dont_play = count_cool_dont_play / count_cool

entropy_cool = 0
if probability_cool_play_tennis > 0:
    entropy_cool -= probability_cool_play_tennis * math.log2(probability_cool_play_tennis)
if probability_cool_dont_play > 0:
    entropy_cool -= probability_cool_dont_play * math.log2(probability_cool_dont_play)

for i in range(len(dataset[1])):
    if dataset[1][i] == "hot":
        count_hot += 1
    if dataset[1][i] == "hot" and dataset[2][i] == "play tennis":
        count_hot_play += 1
    if dataset[1][i] == "hot" and dataset[2][i] == "dont play":
        count_hot_dont_play += 1

probability_hot_play_tennis = count_hot_play / count_hot
probability_hot_dont_play = count_hot_dont_play / count_hot

entropy_hot = 0
if probability_hot_play_tennis > 0:
    entropy_hot -= probability_hot_play_tennis * math.log2(probability_hot_play_tennis)
if probability_hot_dont_play > 0:
    entropy_hot -= probability_hot_dont_play * math.log2(probability_hot_dont_play)

weighted_entropy_temprature = ((count_cool / len(dataset[2])) * entropy_cool) + ((count_hot / len(dataset[2])) * entropy_hot)

information_gain_weather = entropy - weighted_entropy_weather
information_gain_temprature = entropy - weighted_entropy_temprature

print(information_gain_weather, information_gain_temprature)

path_taken = 0

if information_gain_temprature > information_gain_weather:
    if path_taken == 0:
        path_taken = 1
    elif path_taken == 1:
        path_taken = 2
    print("path choosed of temprature")
    if entropy_hot == 0:
        print("leaf node achieved by hot temprature")
    elif entropy_cool == 0:
        print("leaf node achieved by cool temprature")
    if entropy_hot != 0 and entropy_cool != 0:
        print("leaf node not achieved and changing input feature")
elif information_gain_weather > information_gain_temprature:
    if path_taken == 0:
        path_taken = 1
    elif path_taken == 1:
        path_taken = 2
    print("path choosed of weather")
    if entropy_sunny == 0:
        print("leaf node achieved by sunny weather")
    elif entropy_rainy == 0:
        print("leaf node achieved by rainy weather")
    if entropy_sunny != 0 and entropy_rainy != 0:
        print("leaf node not achieved and changing input feature")
if path_taken != 0:
    print("input features exhausted")
