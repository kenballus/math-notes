from matplotlib import pyplot as plt
import math
import pandas as pd

df = pd.read_csv("data.csv")
x = df['x_label']
y = df['y_label']

# plt.xscale("log")
# plt.yscale("log")

plt.plot(x, y) # marker='o' will make dots on the graph, linewidth=0 will not draw a line between the dots
plt.xlabel('The X Axis', fontsize=14)
plt.ylabel('The Y Axis', fontsize=14)
plt.grid(True)
plt.show()
