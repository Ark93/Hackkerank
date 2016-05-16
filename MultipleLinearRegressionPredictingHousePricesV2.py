import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

F,N = raw_input().split(' ')
F,N = [int(F),int(N)]


def create_Table(F,N,data):
    datahx = np.zeros((N,F))
    yx = np.zeros((N,1))
    i=0
    for a in data: 
        datahx[i][:F] = a[:F]
        yx[i] = a[-1]
        i+=1
    return datahx,yx

#creamos polinomio
poly = PolynomialFeatures(degree=1)

observaciones = []
for a_i in xrange(N):
    data_temp = map(float,raw_input().strip().split(' '))
    observaciones.append(data_temp)
    
datahx,yx = create_Table(F,N,observaciones)

#ingresamos datos de entrenamiento (features)
X_pol = poly.fit_transform(datahx)

#creamos la regresion lineal
clf = linear_model.LinearRegression()

#realizamos la regresion lineal con los datos de entrenamiento (features and expected output)
clf.fit(X_pol, yx)
    
##leemos pruebas

T = int(input())
test=[]

for t_i in xrange(T):
    test_data = map(float,raw_input().strip().split(' '))
    test.append(test_data)

testData,y_t = create_Table(F,T,test)

#ingresamos valores de test que queremos usar para predecir (features of test)
for test in testData:
    predict_ = poly.fit_transform(test)
    print clf.predict(predict_)[0][0]
    #print test
