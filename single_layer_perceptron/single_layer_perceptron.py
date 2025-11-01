import numpy
import random

dataset = numpy.array([["Study Hours", 2, 4, 1, 5],
                       ["Attendence", 60, 75, 40, 80],
                       ["Results", "fail", "pass", "fail", "pass"],])

print(dataset)

weights_1 = 0.1
weights_2 = -0.3
bias = -0.2
learning_rate = 0.1

correct_count = 0
append_use = 0

list_study_hours = []
list_attendence = []
list_results = []

input_times = int(input("Enter the number of times to run this iteration: "))

for j in range(input_times):
    for i in range(len(dataset[2])):
        if dataset[2, i] == "fail":
            dataset[2, i] = 0
        elif dataset[2, i] == "pass":
            dataset[2, i] = 1

    if append_use == 0:
        for i in range(1, len(dataset[0])):
            list_study_hours.append(dataset[0][i])
            list_study_hours = list(map(int, list_study_hours))

            list_attendence.append((dataset[1][i]))
            list_attendence = list(map(int, list_attendence))

            list_results.append(dataset[2][i])
            list_results = list(map(int, list_results))

        append_use = 1

    for i in range(len(list_study_hours)):
        list_study_hours[i] = (list_study_hours[i] - min(list_study_hours)) / (max(list_study_hours) - min(list_study_hours))
        list_attendence[i] = (list_attendence[i] - min(list_attendence)) / (max(list_attendence) - min(list_attendence))

    for i in range(len(list_study_hours)):
        input_1 = list_study_hours[i]
        input_2 = list_attendence[i]
        input_3 = list_results[i]

        z = (weights_1 * input_1) + (weights_2 * input_2) + bias
        result = 0

        if z >= 0.3:
            result = 1
        else:
            result = 0


        if result == input_3:
            print(f"the predicted {result} and actual is {input_3} is the same")
            correct_count += 1
        elif result != input_3:
            weight_1 = weights_1 + learning_rate * (input_3 - result) * input_1
            weight_2 = weights_2 + learning_rate * (input_3 - result) * input_2
            bias = bias + learning_rate * (input_3 - result)
            print(weight_1, weight_2, bias)

    print(f"x1={input_1:.2f}, x2={input_2:.2f}, z={z:.3f}, predicted={result}, actual={input_3}")

print(f"out of {input_times} the model predicted correct {correct_count}")