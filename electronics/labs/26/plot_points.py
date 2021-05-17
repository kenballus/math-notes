from matplotlib import pyplot as plt
import math
import pandas as pd

df = pd.read_csv("data.csv")
x = df['Frequency']
vin = df['Vin']
vout = df['Vout']

# plt.xscale("log")
# plt.yscale("log")

plt.plot([math.log10(f) for f in x], [20 * math.log10(vout[i]/vin[i]) for i in range(len(vin))]) # marker='o' will make dots on the graph, linewidth=0 will not draw a line between the dots
plt.xlabel('log(Frequency)', fontsize=14)
plt.ylabel('Gain (dB)', fontsize=14)
plt.grid(True)
plt.show()
