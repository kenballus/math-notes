from matplotlib import pyplot as plt
import math
import pandas as pd

df = pd.read_csv("data.csv")
r = df["Resistance (Ohms)"]
v = df["Voltage (V)"]
i = [v[i]/r[i] for i in range(len(v))]

# plt.xscale("log")
# plt.yscale("log")

print(i)
print(list(v))

plt.plot(i, v, marker='o', linewidth=0)
plt.xlabel('Current (A)', fontsize=14)
plt.ylabel('Voltage (V)', fontsize=14)
plt.grid(True)
plt.show()
