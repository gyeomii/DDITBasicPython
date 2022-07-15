import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day14.stockdao import StockDao
import numpy as np

sd = StockDao()

arrx = np.zeros(23)

arry = list(range(23))

print(arry)

arr_name = ["삼성전자","LG","SK"]

arrz = []
arrz.append(sd.select(arr_name[0]))
arrz.append(sd.select(arr_name[1]))
arrz.append(sd.select(arr_name[2]))


fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot(arrx    ,arry   ,arrz[0])
ax.plot(arrx+1  ,arry   ,arrz[1])
ax.plot(arrx+2  ,arry   ,arrz[2])

plt.show()