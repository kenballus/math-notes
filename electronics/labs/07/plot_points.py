from matplotlib import pyplot as plt
import math
import pandas as pd

df = pd.read_csv("data.csv")
f = df['f']
vin = df['vin']
vout = df['vout']

# plt.xscale("log")
# plt.yscale("log")

plt.plot(f, [vout[i]/vin[i] for i in range(len(vin))], marker='o')
plt.xlabel('Frequency (Hz)', fontsize=14)
plt.ylabel('Phase difference (°) ', fontsize=14)
plt.grid(True)
plt.show()