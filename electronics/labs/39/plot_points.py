from matplotlib import pyplot as plt
import math
import pandas as pd

df = pd.read_csv("data.csv")
y = df['temps']
x = list(range(len(y)))
print(len(y))
# plt.xscale("log")
# plt.yscale("log")

plt.plot(x, y) # marker='o' will make dots on the graph, linewidth=0 will not draw a line between the dots
plt.xlabel('Time', fontsize=14)
plt.ylabel('Temperature', fontsize=14)
plt.grid(True)
plt.show()
