import numpy as np 
import math
import matplotlib.pyplot as plt


class Process:
    def time_step(self):
        dw=np.random.normal(0, math.sqrt(self.delta_t))
        ds= self.drift*self.delta_t*self.current_price + self.volatility*self.current_price*dw
        self.asset_price.append(self.current_price + ds)
        self.current_price = self.current_price + ds #accounting new change 



    def __init__(self, drift, volatility, delta_t, initial_price):
        self.drift = drift
        self.volatility = volatility
        self.delta_t = delta_t
        self.current_price=initial_price
        self.asset_price=[initial_price]
        
processes = []
for i in range(0, 100):
    processes.append(Process(.2, .3, 1/365, 300))


for process in processes:
    tte = 1
    while((tte - process.delta_t)>0):
        process.time_step()
        tte = tte - process.delta_t 

print(processes[0].asset_price)

x=plt.plot(np.arange( 0, len(processes[0].asset_price)), processes[0].asset_price)
plt.show()