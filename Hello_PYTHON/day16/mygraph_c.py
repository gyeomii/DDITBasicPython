import matplotlib.pyplot as plt
from day16.stocksyncdao import StockSyncDao
import numpy as np

sd = StockSyncDao()

arr_code = sd.selectCode()

arr_price = []

for i in arr_code:
    arr_price.append(sd.selectPrice(i))

length = len(arr_price[0])

x = np.zeros(length)

y = []

for i in range(length):
    y.append(i)

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

for idx, z in enumerate(arr_price):
    z_n = np.array(z)
    percentage = z_n/z_n[0]
    ax.plot(x + idx, y, percentage)

plt.show()