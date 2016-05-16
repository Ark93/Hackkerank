#!/usr/bin/py
import numpy as np

def printTransactions(actions):
    print len(actions)
    for action in actions:
        print action
    return 0

def create_TrainingTable(K,F,data):
    datahx = np.zeros((K,F))
    infohx = []
    yx = np.zeros((K,1))
    i=0
    for a in data: 
        datahx[i][:F] = a[:-1]
        yx[i] = a[-1]
        i+=1
    return datahx,yx  
    
def create_TestTable(K,F,data):
    datahx = np.zeros((K,F))
    yx = np.zeros((K,1))
    i=0
    for a in data: 
        datahx[i][:F] = a[1:]
        yx[i] = a[-1]
        i+=1
    return datahx,yx

def getW(datahx,yx):
    datahx_T = datahx.transpose()
    datahx_TInv = np.linalg.inv(np.dot(datahx_T,datahx))
    datahx_y = np.dot(datahx_T,yx)
    w = np.dot(datahx_TInv,datahx_y)
    return w

def getPreds(W,K,F,prices):
    hxtest,last_prices = create_TestTable(K,F,prices)
    hxtest_T = hxtest.transpose()
    y_test = np.dot(hxtest,W)
    return y_test,last_prices

#change to lambda function
def transaction(y,K):
    Action = []
    sell = 'SELL'
    buy = 'BUY'
    for stock in xrange(K):
        if(y[stock]<0):
            Action.append(sell)
        else:
            Action.append(buy)
    return Action

def cuantities(K,actions,names,owned,last_prices,M):
    transaction = []
    for stock in xrange(K):
        if(actions[stock]=='SELL' and owned[stock]>0):
            transaction.append(names[stock] + ' SELL ' + str(int(owned[stock])))
        elif (actions[stock]=='BUY' and last_prices[stock]<M):
            transaction.append(names[stock] + ' BUY ' + str(int(np.floor(M/last_prices[stock]))))
            M = M%last_prices[stock]
    return transaction


if __name__ == '__main__':
    M, K, D = [float(i) for i in raw_input().strip().split()]#money,stocks,days
    K = int(K)
    D = int(D)
    names = []#name of stock
    owned = []#amount of stocks owned
    prices = []#prices of the stock the 5 last days
    for data in range(K):
        temp = raw_input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])


max_record = 10
#training to predict the last day
record = []
if(len(record) == max_record):
    record = np.append(record[:][:-1],n[-1])
elif(len(record)!=0):
    record = np.append(record[:][:-1],n[-1])
else:
    record = prices
F=len(record[0])-1

datahx,yx = create_TrainingTable(K,F,record)

W = getW(datahx,yx)
#test

y,last_prices = getPreds(W,K,F,record)
actions = transaction(y,K)

actions = cuantities(K,actions,names,owned,last_prices,M)
      
printTransactions(actions)
