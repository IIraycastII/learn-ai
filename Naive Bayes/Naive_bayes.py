import numpy as np
import pandas as pd

dataset = np.array([
    ["Temperature", "hot", "cool", "cool", "hot", "cool", "cool"],
    ["Weather", "rainy", "sunny", "sunny", "sunny", "rainy", "rainy"],
    ["Ice_cream", "yes", "yes", "no", "yes", "yes", "no"]
])

print(pd.DataFrame(dataset))

input_1 = input("Enter the condition (temprature(hot/cool), weather(rainy/sunny): ")
list_parameters = list(input_1.split())

list_temprature = []
list_weather = []
list_ice_cream = []

probability_yes_count = 0
probability_no_count = 0
probability_hot_yes_count = 0
probability_cool_yes_count = 0
probability_cool_no_count = 0
probability_hot_no_count = 0
probability_rainy_yes_count = 0
probability_rainy_no_count = 0
probability_sunny_yes_count = 0
probability_sunny_no_count = 0

for i in range(1, len(dataset[0])):
    list_temprature.append(dataset[0][i])
    list_weather.append(dataset[1][i])
    list_ice_cream.append(dataset[2][i])

#P(yes | temprature, weather) = P(yes) * P(temprature|yes) * P(weather|yes)
#P(no | temprature, weather) = P(no) * P(temprature|no) * P(weather|no)

for i in range(len(list_ice_cream)):
    if list_ice_cream[i] == "yes":
        probability_yes_count += 1
    elif list_ice_cream[i] == "no":
        probability_no_count += 1

    if list_parameters[0] == "hot" and list_ice_cream[i] == "yes":
        probability_hot_yes_count += 1
    elif list_parameters[0] == "cool" and list_ice_cream[i] == "yes":
        probability_cool_yes_count += 1
    elif list_parameters[0] == "cool" and list_ice_cream[i] == "no":
        probability_cool_no_count += 1
    elif list_parameters[0] == "hot" and list_ice_cream[i] == "no":
        probability_hot_no_count += 1

    if list_parameters[1] == "rainy" and list_ice_cream[i] == "yes":
        probability_rainy_yes_count += 1
    elif list_parameters[1] == "rainy" and list_ice_cream[i] == "no":
        probability_rainy_no_count += 1
    elif list_parameters[1] == "sunny" and list_ice_cream[i] == "yes":
        probability_sunny_yes_count += 1
    elif list_parameters[1] == "sunny" and list_ice_cream[i] == "no":
        probability_sunny_no_count += 1

# Probabilities
P_yes = probability_yes_count / len(list_ice_cream)
P_no = probability_no_count / len(list_ice_cream)

if list_parameters[0] == "hot":
    P_temp_given_yes = probability_hot_yes_count / probability_yes_count
    P_temp_given_no = probability_hot_no_count / probability_no_count
elif list_parameters[0] == "cool":
    P_temp_given_yes = probability_cool_yes_count / probability_yes_count
    P_temp_given_no = probability_cool_no_count / probability_no_count

if list_parameters[1] == "sunny":
    P_weather_given_yes = probability_sunny_yes_count / probability_yes_count
    P_weather_given_no = probability_sunny_no_count / probability_no_count
elif list_parameters[1] == "rainy":
    P_weather_given_yes = probability_rainy_yes_count / probability_yes_count
    P_weather_given_no = probability_rainy_no_count / probability_no_count

P_yes_given_input = P_yes * P_temp_given_yes * P_weather_given_yes
P_no_given_input = P_no * P_temp_given_no * P_weather_given_no

print(f"probaility of yes ice cream is {[P_yes_given_input]}")
print(f"probaility of no ice cream is {[P_no_given_input]}")

if P_yes_given_input > P_no_given_input:
    print(f"in a {list_parameters[0]} temprature and {list_parameters[1]} weather, the person will buy ice cream")
else:
    print(f"in a {list_parameters[0]} temprature and {list_parameters[1]} weather, the person will not buy ice cream")
