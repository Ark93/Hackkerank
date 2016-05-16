import numpy as np
from scipy import stats
from decimal import *

fixed = Decimal(10)**-1

T = input()
arr = map(int,raw_input().split(' ')) 
m = np.mean(arr)
s = (np.std(arr))
print m
print np.median(arr)
print stats.mode(arr)[0][0]
print Decimal(s).quantize(fixed)
coef = 1.9
trust_val = 0.95
trustBound = 1.96* float(float(s) / (np.sqrt(len(arr))))
up_tB = m+trustBound
lo_tB = m-trustBound
print Decimal(lo_tB).quantize(fixed), Decimal(up_tB).quantize(fixed)