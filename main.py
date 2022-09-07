import numpy as np
import csv
import matplotlib.pyplot as plt

# Using linspace so that the endpoint of 360 is included
actual = np.radians(np.linspace(0.5, 360, 720))
expected = np.arange(0, 180.5, 0.5)

r, theta = np.meshgrid(expected, actual)
f = open('raw.csv','r')
rdr = csv.reader(f)
values = list(rdr)
f.close()

fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
ax.contourf(theta, r, values)

plt.show()