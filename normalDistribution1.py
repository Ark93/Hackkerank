# Enter your code here. Read input from STDIN. Print output to STDOUT
#http://ci.columbia.edu/ci/premba_test/c0331/s6/s6_4.html
#http://www.usablestats.com/lessons/zarea
#http://www.sjsu.edu/faculty/gerstman/EpiInfo/z-table.htm
#http://www.sjsu.edu/faculty/gerstman/EpiInfo/z-table.htm
from __future__ import division
from decimal import Decimal

fixed = Decimal(10)**-3

mean = 30
std = 4

def getZ(x,mean,std):
    return (x-mean)/std

def getCProb(a,b,mean,std):    
    probB = getZ(b,mean,std)
    probA = getZ(a,mean,std)
    return probA,probB

#print getZ(40,mean,std), checking a Z table
print Decimal(0.9938).quantize(fixed)
#print getZ(21,mean,std), cheking a Z table
print Decimal(1-(1-0.9878)).quantize(fixed)
#print getCProb(30,35,mean,std)
#0.5, 0.8944
print Decimal(0.8944 - 0.5).quantize(fixed)