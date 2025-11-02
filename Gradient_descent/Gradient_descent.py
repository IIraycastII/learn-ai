import numpy
import matplotlib.pyplot as plt

dataset = numpy.array([[10, 30, 20, 43, 23],
                       [23, 43, 55, 65, 23]])

m = 2.0
c = 4.0
m_list = [m]
c_list = [c]
learning_rate = 0.0001
y = []
difference_m = []
addition_m = []


for i in range(len(dataset[0])):
    y.append(m * dataset[0][i] + c)
    loss = ((y[i] - dataset[1][i]) ** 2) / len(dataset[1])

print(loss)

for i in range(len(dataset[0])):
    difference_m.append(dataset[1][i] - y[i])
    addition_m.append((dataset[0][i] * difference_m[i]))

addition_c = sum(difference_m)
sum_addition_m = sum(addition_m)

print(sum_addition_m)

input_1 = int(input("how many iterations: "))

for i in range(input_1):
    gradient_m = float(-2 * (sum_addition_m)/len(addition_m))
    gradient_c = float(-2 * (addition_c)/len(addition_m))
    print(gradient_m)
    print(gradient_c)

    m_list.append(m)
    c_list.append(c)
    m = m - learning_rate * gradient_m
    c = c - learning_rate * gradient_c

    m_list.append(m)
    c_list.append(c)

print(m_list)
print(c_list)

plt.plot(m_list, c_list, marker='o')
plt.title("Gradient Descent Progress (m vs c)")
plt.xlabel("m values")
plt.ylabel("c values")
plt.grid(True)
plt.show()
