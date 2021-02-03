from matplotlib import pyplot as plt

x = [1.00, 1.99, 2.99, 4.05, 5.01]
y = [10.1, 20.4, 30.6, 41.4, 51.4]
# x = [0.01, 0.09, 0.20, 0.60, 1.11, 1.78, 2.48, 3.21, 5.07, 7.01, 8.97, 10.99, 13.01, 14.08]
# y = [0.2, 5.1, 9.8, 16.1, 20.4, 25.6, 30.4, 35.0, 45.8, 54.4, 62.3, 69.8, 76.8, 80.5]

plt.plot(x, y, color='red', marker='o')
plt.xlabel('V', fontsize=14)
plt.ylabel('mA', fontsize=14)
plt.grid(True)
plt.show()