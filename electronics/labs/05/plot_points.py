from matplotlib import pyplot as plt
import math
import pandas as pd

df = pd.read_csv("data.csv")
f = df['Frequency']
vout = df["Vout"]
vin = df["Vin"]
db = [20 * math.log10(vout[i] / vin[i]) for i in range(len(vout))]
print(db)
phase = df["PhaseShift"]

plt.xscale("log")
# plt.yscale("log")

plt.plot(f, db, marker='o', linewidth=0)
plt.xlabel('Frequency (Hz)', fontsize=14)
plt.ylabel('Phase Shift (°) ', fontsize=14)
plt.grid(True)
plt.show()