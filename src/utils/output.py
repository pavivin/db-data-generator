from classes import Human
from faker import Faker
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

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
