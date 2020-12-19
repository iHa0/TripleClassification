import os
import sys
import random
import numpy as np
count1 = 0
count2 = 0
# f1 = open('/Users/ihao/Desktop/wn18rr_data/rel.txt', 'r')
# f2 = open('/Users/ihao/Desktop/wn18rr_data/rel_new.txt', 'w')
f1 = open('/Users/ihao/Desktop/wn18rr_data/N1_0.01/rel.txt', 'r')
f2 = open('/Users/ihao/Desktop/wn18rr_data/N1_0.01/rel_new.txt', 'w')
for line in f1:
    f2.write(line.replace('], [', '\n'))
    count1 += 1
print(count1)
print('=======')
# print(count2)
f1.close()
f2.close()