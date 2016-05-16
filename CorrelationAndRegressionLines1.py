#expected value E[X] it's the mean value
#Pearson correlation = covariance(X,Y) / sdt_x * std_y
from __future__ import division
from decimal import Decimal
import math

#create function to get covariance

fixed = Decimal(10)**-3

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

phy_Xscr = [15,12,8,8,7,7,7,6,5,3]
his_Yscr = [10,25,17,11,13,17,20,13,9,15]

print Decimal(getPearsonCOR(his_Yscr,phy_Xscr)).quantize(fixed)

