# Enter your code here. Read input from STDIN. Print output to STDOUT#expected value E[X] it's the mean value
#Pearson correlation = covariance(X,Y) / sdt_x * std_y
from __future__ import division
from decimal import Decimal
import math


X = []
Y = []
Z = []

N = int(raw_input())
for n in xrange(N):
    temp = raw_input().strip().split('\t')
    X.append(int(temp[0]))
    Y.append(int(temp[1]))
    Z.append(int(temp[2]))
    
#create function to get covariance

fixed = Decimal(10)**-2

def getCOV(X,Y,x_mean,y_mean):
    n = len(X)
    sum12 = 0
    for i in xrange(n):
        sum12 += (X[i]-x_mean)*(Y[i]-y_mean)
    covariance = (sum12) / n
    return covariance

#create function to get mean

def getMean(X):
    return (sum(X)/len(X))

#create function to get standar deviation

def getSTD(X,mean):    
    x_2 = [0]*len(X)
    for i in xrange(len(X)):
        x_2[i] = pow(X[i]-mean,2)
    variance = sum(x_2)/len(X)
    std = math.sqrt(variance)
    return std

#create function to get the Pearson correlation 
def getPearsonCOR(X,Y):
    #first, get Mean, then std and cov
    x_mean = getMean(X)
    y_mean = getMean(Y)
    x_std = getSTD(X,x_mean)
    y_std = getSTD(Y,y_mean)
    cov = getCOV(X,Y,x_mean,y_mean)
    return cov/(x_std*y_std)

#create arrs 

print Decimal(getPearsonCOR(X,Y)).quantize(fixed)
print Decimal(getPearsonCOR(Y,Z)).quantize(fixed)
print Decimal(getPearsonCOR(X,Z)).quantize(fixed)


