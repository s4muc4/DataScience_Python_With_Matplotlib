import matplotlib.pyplot as plt
import random

vector = []

for i in range(10):
	random_number = random.randint(0,1000)
	vector.append(random_number)

plt.boxplot(vector);
plt.title("My Boxplot")
plt.show()