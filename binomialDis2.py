# Enter your code here. Read input from STDIN. Print output to STDOUT
#get combinations:
from __future__ import division
import math
from  decimal import *
#getcontext()
f = math.factorial

fixed = Decimal(10)**-3

p = 1.09/(1+1.09)
q = 1/(1+1.09)

def combinations(n,x):
    return f(n) / float((f(x)*f(n-x)))

def get_binomProb(n,x,p,q):
    return combinations(n,x) * (pow((p),x) * (pow(q,(n-x))))


#the success data is over hit, so if we want to know the probability of X fails, we have to compute the numbers of sucesss 
print Decimal((get_binomProb(6,3,p,q))).quantize(fixed) + Decimal((get_binomProb(6,4,p,q))).quantize(fixed) + Decimal((get_binomProb(6,5,p,q))).quantize(fixed) + Decimal((get_binomProb(6,6,p,q))).quantize(fixed) 
