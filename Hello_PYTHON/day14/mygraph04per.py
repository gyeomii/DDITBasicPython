import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day14.stockdao import StockDao

ds = StockDao()

arrx1 = []
arrx2 = [] 
arrx3 = []
arry1 = range(17)
arry2 = range(17)
arry3 = range(17)

arrz1 = ds.selects("삼성전자")
arrz2 = ds.selects("LG")
arrz3 = ds.selects("SK")

arrz1p =[]
arrz2p =[]
arrz3p =[]
for i in arrz1:
    arrz1p.append(i/arrz1[0])
for i in arrz2:
    arrz2p.append(i/arrz2[0])
for i in arrz3:
    arrz3p.append(i/arrz3[0])

for i in range(17):
    arrx1.append(-1)
    arrx2.append(0)
    arrx3.append(1)


fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot(arrx1,arry1,arrz1p)
ax.plot(arrx2,arry2,arrz2p)
ax.plot(arrx3,arry3,arrz3p)

plt.show()



