#!/usr/bin/py
import numpy as np
import os.path

def delete_record():
    target = open('record.txt', 'w')
    target.truncate()
    target.close()

def print_Record(record):
    target = open('record.txt', 'w')
    target.truncate()
    for row in record:
        for num in row:
            target.write(str(num) + ' ')
        target.write('\n')
    target.close()
    
def read_Record(K):
    record = []
    if(os.path.isfile('record.txt')): 
        target = open('record.txt', 'r')
        for a in xrange(K):
            temp = target.readline().strip().split()
            record.append([float(i) for i in temp])
    return record

def printTransactions(actions,f,max_record,d):
    if ((f!=max_record) or d==1):
        print 0
    else:
        print len(actions)
        for action in actions:
            print action
        return 0

# to get the rises or dows
def normalize_data(record):
    norm_record = []
    for row in record:
        i=0
        row_temp = []
        for i in xrange(len(row)-1):
            row_temp = np.append(row_temp,(row[i+1]-row[i]))
        norm_record.append(row_temp)
    return norm_record
    
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
    pen_l2 = 1
    eye = pen_l2 *np.eye(len(datahx[0]))
    datahx_T = datahx.transpose()
    datahx_TInv = np.linalg.inv(np.dot(datahx_T,datahx) + (eye))
    datahx_y = np.dot(datahx_T,yx)
    w = np.dot(datahx_TInv,datahx_y)
    return w

def getPreds(W,K,F,prices):
    hxtest,last_prices = create_TestTable(K,F,prices)
    hxtest_T = hxtest.transpose()
    y_test = np.dot(hxtest,W)
    return y_test,last_prices

def getPreds2(W,K,F,prices,y1):
    for row in xrange(len(prices)):
        prices[row] = np.append(prices[row][1:],y1[row]) 
    hxtest,last_prices = create_TestTable(K,F,prices)
    hxtest_T = hxtest.transpose()
    y_test = np.dot(hxtest,W)
    return y_test

#function to choose between wait or not wait to make the trade
def wait_day(K,y1,y2):
    move_today = []
    for stock in xrange(K):
        if(y1 < 0):
            if(y2<0):
                move_today.append(0)
            else:
                move_today.append(1)
        else:
            if(y2>0):
                move_today.append(0)
            else:
                move_today.append(1)
    return move_today

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

def sort_actions(names,owned,move_today,actions,act_prices):    
#add a function to sort actions,name,owned,last_price
    stock_tuple = []
    for stock in xrange(K):
        stock_tuple.append((names[stock],owned[stock],move_today[stock],actions[stock],act_prices[stock]))     
    stock_tuple = sorted(stock_tuple,key=lambda stock : stock[2],reverse = False)
    actionsS=[]
    namesS=[]
    ownedS=[]
    move_todayS=[]
    act_pricesS=[]
    for stock in stock_tuple:
        actionsS.append(stock[3])
        namesS.append(stock[0])
        ownedS.append(stock[1])
        move_todayS.append(stock[2])
        act_pricesS.append(stock[4])        
    return actionsS,namesS,ownedS,move_todayS,act_pricesS

def cuantities(K,actions,move_today,names,owned,last_prices,M):
    transaction = []
    max_bought = 10000
    for stock in xrange(K):
        if(actions[stock]=='SELL' and owned[stock]>0 and move_today[stock] ):
            transaction.append(names[stock] + ' SELL ' + str(int(owned[stock])))
        elif (actions[stock]=='BUY' and last_prices[stock]<M and move_today[stock]):
            to_buy = int(np.floor(M/last_prices[stock]))
            #if(to_buy >max_bought ):
            #    to_buy = max_bought
            transaction.append(names[stock] + ' BUY ' + str(to_buy))
            M -= (to_buy*last_prices[stock])
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


max_record = 17
#training to predict the last day
record = []
record = read_Record(K)
act_prices = []

if(len(record)!=0):
    rec_temp=[]
    i=0
    for row in record:
        if(len(row)==max_record):
            rec_temp.append(np.append(row[1:],prices[i][-1]))
        else:
            rec_temp.append(np.append(row,prices[i][-1]))        
        i+=1
    record = rec_temp
    F=len(record[0])-2
else:
    F=3
    record = prices
    
for row in prices:
    act_prices.append(row[-1])
    
print_Record(record)

record = normalize_data(record)
datahx,yx = create_TrainingTable(K,F,record)

W = getW(datahx,yx)
#test
y1,last_rises = getPreds(W,K,F,record)
y2 = getPreds2(W,K,F,record,y1)

actions = transaction(y1,K)

#wait_t = wait_turn(actions,y1,y2)

actionsS,namesS,ownedS,move_todayS,act_pricesS = sort_actions(names,owned,last_rises,actions,act_prices)

#actions = cuantities(K,actions,names,owned,last_prices,M)
if(D==2):
    actionsS =[]
    for k in xrange(K):
        actionsS.append('SELL')
actions = cuantities(K,actionsS,move_todayS,namesS,ownedS,act_pricesS,M)
printTransactions(actions,F,max_record-2,D)
