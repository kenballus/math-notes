from matplotlib import pyplot as plt
import math
import pandas as pd

df = pd.read_csv("data.csv")

# x = [thing / 100 for thing in range(0, 746)]
# y = [.343 if thing > 5.40 else 5.42 for thing in x]

x = df["vin"]
y = df["n"]

# plt.xscale("log")
# plt.yscale("log")

plt.plot(x, y, marker='o', linewidth=0) # marker='o' will make dots on the graph, linewidth=0 will not draw a line between the dots
plt.xlabel('Vin', fontsize=14)
plt.ylabel('Number of Steps Until Comparator Switch', fontsize=14)
plt.grid(True)
plt.show()
