import matplotlib.pyplot as plt
from day14.stockdao import StockDao

sd = StockDao()

samsung = sd.select("삼성전자")
sk = sd.select("SK")
lg = sd.select("LG")

samPriceList = []
lgPriceList = []
skPriceList = []

x1 = []
x2 = []
x3 = []

y1 = []
y2 = []
y3 = []

for idx, i in enumerate(samsung):
    firstPrice = samsung[0].get('price')
    price = i.get('price')
    gap = price - firstPrice
    percent = gap/firstPrice*100
    samPriceList.append(percent)
    x1.append(0)
    y1.append(idx)
    

for idx, i in enumerate(lg):
    firstPrice = lg[0].get('price')
    price = i.get('price')
    gap = price - firstPrice
    percent = gap/firstPrice*100
    lgPriceList.append(percent)
    x2.append(1)
    y2.append(idx)
    
for idx, i in enumerate(sk):
    firstPrice = sk[0].get('price')
    price = i.get('price')
    gap = price - firstPrice
    percent = gap/firstPrice*100
    skPriceList.append(percent)
    x3.append(2)
    y3.append(idx)

fig = plt.figure()

ax = fig.add_subplot(1,1,1, projection='3d')       

ax.plot(x1, y1, samPriceList,'r')
ax.plot(x2, y2, lgPriceList,'g')
ax.plot(x3, y3, skPriceList,'b')

legend = plt.legend(["samsung", "sk", "lg"])
legend.set_title("Stock", prop = {'size':15})

# ax.set_xlim3d(-1, 3)
# ax.set_ylim3d(0, 30)
# ax.set_zlim3d(50000, 10000000)

plt.show()


