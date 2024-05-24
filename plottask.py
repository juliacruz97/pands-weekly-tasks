import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
number = np.random.normal(loc=5, scale=2, size=1000)

labelx = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
labely = labelx ** 3


plt.xlabel('Values')
plt.ylabel('Frequency / h(x)')
plt.title('Histogram of Normal Distribution and Plot of h(x)=x^3')

plt.hist(number, color = 'pink')
plt.plot(labely)
plt.show()
