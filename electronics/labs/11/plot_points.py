from matplotlib import pyplot as plt
import math
import pandas as pd

df = pd.read_csv("data.csv")
V = df['V']
mA = df['mA']

# plt.xscale("log")
# plt.yscale("log")

plt.plot(V, mA, marker='o', linewidth=0)
plt.xlabel('V_{GS} (V)', fontsize=14)
plt.ylabel('I_{DS} (mA)', fontsize=14)
plt.grid(True)
plt.show()