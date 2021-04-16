from matplotlib import pyplot as plt
import math
import pandas as pd

df = pd.read_csv("data1.csv")
x = df['Frequency (Hz)']
y = df['Vout (mV P-P)']
y = [y[i] / 1940 for i in range(len(y))]
print(y)
exit()

# plt.xscale("log")
# plt.yscale("log")

plt.plot(x, y) # marker='o' will make dots on the graph, linewidth=0 will not draw a line between the dots
plt.xlabel('Frequency (Hz)', fontsize=14)
plt.ylabel('Vout/Vin', fontsize=14)
plt.grid(True)
plt.show()
