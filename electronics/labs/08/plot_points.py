from matplotlib import pyplot as plt
import math
import pandas as pd

mA = [0, 10, 50, 100, 150, 200, 250, 300, 350, 400, 450]
V = [0,0.67,0.77,0.80,0.81,0.82,0.83,0.83,0.84,0.84,0.84]

# plt.xscale("log")
# plt.yscale("log")

plt.plot(V, mA, marker='o')
plt.xlabel('V', fontsize=14)
plt.ylabel('mA', fontsize=14)
plt.grid(True)
plt.show()