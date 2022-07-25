import matplotlib.pyplot as plt
import numpy as np

x = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
y = [0, 1, 1, 0, -1, -1, 1, 1, -1, -1, 1, 1, 0, 0]
plt.plot(x, y)
plt.title('Square Wave')
plt.xlabel('X : axis')
plt.ylabel('Y : axis')
plt.show()