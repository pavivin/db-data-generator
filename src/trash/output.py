import matplotlib.pyplot as plt
import numpy as np
from faker import Faker

fig, ax = plt.subplots()  # Create a figure containing a single axes.

fake = Faker()
a = []
for i in range(10_000):
    a.append(np.random.normal())


ax.scatter([i for i in range(10_000)], a)
# Plot some data on the axes.
plt.show()


a = []
for i in range(10_000):
    a.append(np.random.lognormal())


fig.scatter([i for i in range(10_000)], a)
# Plot some data on the axes.
plt.show()
