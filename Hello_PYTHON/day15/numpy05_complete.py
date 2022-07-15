import matplotlib.pyplot as plt
from day15.stockdao import StockDao
import numpy as np

sd = StockDao()

arr_name = sd.selectName()
arr_price = []

for i in arr_name:
    arr_price.append(sd.selectPrice(i))

x = np.zeros(23)

y = []

for i in range(len(arr_price[0])):
    y.append(i)

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

for idx, z in enumerate(arr_price):
    ax.plot(x + idx, y, z)
plt.show()
