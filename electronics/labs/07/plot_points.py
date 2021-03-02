from matplotlib import pyplot as plt
import math
import pandas as pd

df = pd.read_csv("data.csv")
f = df['f']
vin = df['Vin']
vout = df['Vout']

# plt.xscale("log")
# plt.yscale("log")

vout_over_vin = [vout[i] / vin[i] for i in range(len(vin))]
print(max(vout_over_vin))
plt.plot(f, vout_over_vin, marker='o', linewidth=0)
plt.xlabel('Frequency (kHz)', fontsize=14)
plt.ylabel('Vout/Vin ', fontsize=14)
plt.grid(True)
plt.show()