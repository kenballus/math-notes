from matplotlib import pyplot as plt
import math
import pandas as pd

df = pd.read_csv("data1.csv")
current = [count * 5.08/220 for count in df["220s"]]
v = df["Output"]
v1 = df["Gate"]

# plt.xscale("log")
# plt.yscale("log")

plt.plot(current, v, marker='o', linewidth=0)
plt.plot(current, v1, marker='o', linewidth=0)
plt.xlabel('Current (A)', fontsize=14)
plt.ylabel('Voltage (V)', fontsize=14)
plt.grid(True)
plt.show()
