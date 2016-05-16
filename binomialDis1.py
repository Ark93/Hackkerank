# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://onlinecourses.science.psu.edu/stat414/node/69
from __future__ import division
import math
from  decimal import *

f = math.factorial

fixed = Decimal(10)**-3

#we want to know about reject pistons, so a piston rejected is a success
p = 0.12
q = 1-p

def combinations(n,x):
    return f(n) / float((f(x)*f(n-x)))

def get_binomProb(n,x,p,q):
    return combinations(n,x) * (pow((p),x) * (pow(q,(n-x))))

def get_AcumBinomProb(n,a,b,p,q):
    #b is always +1, because it's inclusive
    #a is always normal because the xrange is not inclusive, so the last number is excluded
    a_ = min(a,b)
    b_ = max(a,b)
    aCProb = sum(get_binomProb(n,x_,p,q) for x_ in xrange(a))
    bCProb = sum(get_binomProb(n,x_,p,q) for x_ in xrange(b+1))
    return bCProb - aCProb

#sometimes we have to roundDown
print Decimal(get_AcumBinomProb(10,0,2,p,q)).quantize(fixed,rounding=ROUND_DOWN)
print Decimal(get_AcumBinomProb(10,2,10,p,q)).quantize(fixed,rounding=ROUND_DOWN)
