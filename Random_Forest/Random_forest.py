import numpy as np
import math
import pandas as pd
import random

def generate_random_dataset():
    return np.array([
        [random.choice(["sunny", "rainy"]) for _ in range(6)],
        [random.choice(["cool", "hot"]) for _ in range(6)],
        [random.choice(["play tennis", "dont play"]) for _ in range(6)]
    ])

def decision_tree_run(dataset):
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

    for i in range(len(dataset[0])):
        if dataset[0][i] == "sunny":
            count_sunny += 1
        if dataset[0][i] == "sunny" and dataset[2][i] == "play tennis":
            count_sunny_play += 1
        if dataset[0][i] == "sunny" and dataset[2][i] == "dont play":
            count_sunny_dont_play += 1

    probability_sunny_play_tennis = count_sunny_play / count_sunny if count_sunny else 0
    probability_sunny_dont_play = count_sunny_dont_play / count_sunny if count_sunny else 0

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

    probability_rainy_play_tennis = count_rainy_play / count_rainy if count_rainy else 0
    probability_rainy_dont_play = count_rainy_dont_play / count_rainy if count_rainy else 0

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

    probability_cool_play_tennis = count_cool_play / count_cool if count_cool else 0
    probability_cool_dont_play = count_cool_dont_play / count_cool if count_cool else 0

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

    probability_hot_play_tennis = count_hot_play / count_hot if count_hot else 0
    probability_hot_dont_play = count_hot_dont_play / count_hot if count_hot else 0

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
    final_decision = ""

    if information_gain_temprature > information_gain_weather:
        print("path choosed of temprature")
        if entropy_hot == 0:
            print("leaf node achieved by hot temprature")
            final_decision = "dont play"
        elif entropy_cool == 0:
            print("leaf node achieved by cool temprature")
            final_decision = "play tennis"
        else:
            print("leaf node not achieved and changing input feature")
            final_decision = "play tennis"
    elif information_gain_weather > information_gain_temprature:
        print("path choosed of weather")
        if entropy_sunny == 0:
            print("leaf node achieved by sunny weather")
            final_decision = "play tennis"
        elif entropy_rainy == 0:
            print("leaf node achieved by rainy weather")
            final_decision = "dont play"
        else:
            print("leaf node not achieved and changing input feature")
            final_decision = "play tennis"

    print("input features exhausted")
    return final_decision


trees = []
for i in range(3):
    dataset = generate_random_dataset()
    print(f"\n--- Dataset for Decision Tree {i+1} ---")
    print(pd.DataFrame(dataset))
    print(f"--- Running Decision Tree {i+1} ---")
    decision = decision_tree_run(dataset)
    trees.append(decision)
    print("Tree", i+1, "decision:", decision)


print("\n--- Majority Voting ---")
print("All tree decisions:", trees)
final_output = max(set(trees), key=trees.count)
print("Final Random Forest Decision:", final_output)
