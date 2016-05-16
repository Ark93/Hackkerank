import numpy as np
F,N = raw_input().split(' ')
F,N = [int(F),int(N)]

max_order = 3

def create_Table(F,N,data):
    datahx = np.zeros((N,F*4))
    yx = np.zeros((N,1))
    i=0
    for a in data: 
        datahx[i][:F] = a[:F]
        datahx[i][F:F*2] = np.power(a[:F],2)
        datahx[i][F*2:F*3] = np.power(a[:F],3)
        datahx[i][F*3:F*4] = np.power(a[:F],4)
        yx[i] = a[-1]
        i+=1
    return datahx,yx
    
observaciones = []
for a_i in xrange(N):
    data_temp = map(float,raw_input().strip().split(' '))
    observaciones.append(data_temp)

datahx,yx = create_Table(F,N,observaciones)

datahx_T = datahx.transpose()
datahx_TInv = np.linalg.inv(np.dot(datahx_T,datahx))

#print datahx_T.shape
datahx_y = np.dot(datahx_T,yx)
#print datahx_y.shape
w = np.dot(datahx_TInv,datahx_y)

T = int(input())
test=[]

for t_i in xrange(T):
    test_data = map(float,raw_input().strip().split(' '))
    test.append(test_data)

    
testhx,ytestx = create_Table(F,T,test)
testhx_T = testhx.transpose()
ytestx = np.dot(testhx,w)

for y in ytestx:
    print float(y)