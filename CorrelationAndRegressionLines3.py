#expected value E[X] it's the mean value
#Pearson correlation = covariance(X,Y) / sdt_x * std_y
#http://www.dummies.com/how-to/content/how-to-calculate-a-regression-line.html
#slope = corr(y_std/x_std)
from __future__ import division
from decimal import Decimal
import math

#create function to get covariance

fixed = Decimal(10)**-1

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
def getPearsonCOR(X,Y,x_,y_,x_s,y_s):
    #first, get Mean, then std and cov
    cov = getCOV(X,Y,x_,y_)
    return cov/(x_s*y_s)

#create function to get the slope
def getSlope(X,Y):
    x_ = getMean(X)
    y_ = getMean(Y)
    x_s = getSTD(X,x_)
    y_s = getSTD(Y,y_)
    cor = getPearsonCOR(X,Y,x_,y_,x_s,y_s)
    return cor*(y_s/x_s)

#create function to get the 'y' intercept:

def getIntercept(X,Y):
    slope = getSlope(X,Y)    
    x_ = getMean(X)
    y_ = getMean(Y)
    return y_-(x_*slope)

#create function to get a Prediction

def getPredict(X,Y,x_Score):
    slope = getSlope(X,Y)
    intercept = getIntercept(X,Y)
    return (slope*x_Score) + intercept

#create Arrays

phy_Xscr = [15,12,8,8,7,7,7,6,5,3]
his_Yscr = [10,25,17,11,13,17,20,13,9,15]

print Decimal(getPredict(phy_Xscr,his_Yscr,10)).quantize(fixed)

