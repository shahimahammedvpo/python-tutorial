
import matplotlib.pyplot as plt
x = [1, 2, 3]
y1 = [10, 20, 30]
y2 = [15, 25, 35]
plt.plot(x, y1, label='Line1')
plt.plot(x, y2, label='Line2')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Two Lines Plot')
plt.legend()
plt.show()
