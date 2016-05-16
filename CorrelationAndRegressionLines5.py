#http://www.vitutor.com/estadistica/bi/recta_regresion.html
se busca obtener la varianza de Y mediante el conocimiento de las rectas de rectas de regresion
y el conocimiento de la desviacion de x (raiz de la varianza ).

para eso tenemos la ecuación de las rectas de regresion: (y-y_mean)= (cov)/(desviacion_y^2) * (x-x_mean)

despejando tenemos (desviacion_y^2) = ((cov)* (x-x_mean))/(y-y_mean)

tenemos conocimientio de la covarianza, pero no de el valor de x, y y sus medias, por lo que
se deben de obtener de las rectas de regresion

Para esto, la recta de y sobre x (4x – 5y + 33 =0) y la recta de X sobre Y ( 20x – 9y – 107 =0) 
se calculan sus despejes:

y= (4/5)x - 33/5
x= (9/20)y + 107/20

Una vez obtenida esta metrica, sabemos que los coeficientes para y,x son el valor de la covarianza 
sobre la varianza de la variable independiente, por lo cual

para y, (cov)/(desviacion_x^2) = 4/5
para x, (cov)/(desviacion_y^2) = 9/20

Como ya conocemos la covarianza, podemos realizar un despeje sobre la incognita de cov

(cov) = (desviacion_x^2) * (4/5) 
(cov) = (desviacion_y^2) * (9/20)

si hacemos una igualdad sobre cov entre ambas ecuaciones

(desviacion_x^2) * (4/5) = (desviacion_y^2) * (9/20)

Despejamos la incognita de la desviacion_y

(desviacion_y^2) = ((desviacion_x^2) * (4/5) )/(9/20)

sustituyendo la desviacion_x con 3

(desviacion_y^2) = ((3^2) * (4/5) )/(9/20) = (9 * 4/5 )/ (9/20) = 16

sqrt((desviacion_y^2)) = sqrt(3.24) = 4
