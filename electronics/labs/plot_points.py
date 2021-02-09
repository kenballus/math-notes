from matplotlib import pyplot as plt

x = [-1, -.8, -.4, 0, .4, .8, 1]
y = [-.5, -.4, -.2, 0, .2, .4, .5]

plt.plot(x, y, color='red', marker='o')
plt.xlabel('Vin', fontsize=14)
plt.ylabel('Vout', fontsize=14)
plt.grid(True)
plt.show()
