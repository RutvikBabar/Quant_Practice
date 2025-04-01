# for a sample space of 10000 simulating a success of predicting with 70% or higher probablity.

import numpy as np

total_repeats=[]
for i in range (0, 10000):
    repeats = []
    for j in range (0,100):
        r = np.random.random()
        if(r<=0.7):
            repeats.append(1)
        else:
            repeats.append(0)

    if(sum(repeats) >= 70):
        total_repeats.append(1)
    else:
        total_repeats.append(0)
print(np.average(total_repeats))


