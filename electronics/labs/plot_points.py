from matplotlib import pyplot as plt
import math

x = [10, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000, 25000, 50000, 75000, 100000]
# y = [1, 1, 1, 16.8/17.2, 15.8/17.2, 14.6/17.2, 9.8/17.8, 6.0/17.8, 3.92/17.8, 3.6/17.8, 1.22/17.8, .640/17.8, .460/17.6, .328/17.8]
# y = [10 * math.log10(thing) for thing in y]

y = [0.01, 0.01, 0.01, 15.1, 25.3, 30.2, 56.2, 70.7, 75.8, 79.2, 83.3, 80.2, 79.8, 82.0]

plt.xscale("log")
plt.yscale("log")

plt.plot(x, y, color='red', marker='o')
plt.xlabel('Frequency (Hz)', fontsize=14)
plt.ylabel('Phase difference (°) ', fontsize=14)
plt.grid(True)
plt.show()