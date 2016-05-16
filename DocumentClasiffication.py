# Enter your code here. Read input from STDIN. Print output to STDOUT

from __future__ import division
from collections import Counter
import numpy as np
import math 

#first, readdata
yx = []
hx = []
with open('trainingdata.txt') as file:
    num = file.readline()
    for line in file:
        data = line.split(' ')
        yx = int(data[0])
        hx = Counter(data[1:])
    file.close()

#second, create the logistic funcion and log likelihood
#W its Beta, the features coefficients

#logistic function to predict probability of be a member of the class
def logisticFunction(x):
	return  1.0/(1 + math.exp(-x))

#function to get the Score of the data
def getScore(x_i,W):
	return np.dot(x_i,W)

def getPrediction(X,W):
	return logisticFunction(getScore(X,W))


#function to get the individual log likelihood
def logistic_log_likelihood_i(x_i,y_i,W):
	#given the real category y_i
	if y_i ==1:
		#if it must be true
		return math.log(logistic(getScore(x_i,W)))
    else:
    	#if it must be false
    	return math.log(1-logistic(getScore(x_i,W)))

#function to get the log likelihood, ¿product or sum?
def logistic_log_likelihood(x,y,W):
	return sum(logistic_log_likelihood_i(x_i,y_i,W) for x_i,y_i in zip(x,y)))

#getting the gradient

def logistic_log_partial_ij(x_i,y_i,W,j):
	return  (y_i - logistic (getScore(x_i,W))) * x_i[j]

def logistic_log_gradient_i(x_i,y_i,W):
	return [logistic_log_partial_ij(x_i,y_i,W,j) for j,_ in enumerate(W)]

def logistic_log_gradient(X,Y,W):
	return logistic_log_gradient_i(x_i,y_i,W) for x_i,y_i in zip(x,y)

random.seed(0)
x_train = hx[:100]
x_test = hx[100,110]
y_train = yx[:100]
y_test = yx[100:110]

fn= partial()
