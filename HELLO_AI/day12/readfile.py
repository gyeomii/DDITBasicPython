import numpy as np
import os
from glob import glob
from tqdm import tqdm

file = '0_0_1_2.psq'
f = open(file,'r')
for idx, line in enumerate(f.read().splitlines()):
    print(idx, line)
    
    # if idx > 0 and idx < 87:
    #     x, y, t = np.array(line.split(','), np.int8)
    #     print(x,y)