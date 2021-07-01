import numpy as np
f = np.polyfit(x,y,3) #x is predictor, y is prediction, 3 is degree of polynomial
p = np.poluid(f) 
print (p) #to print the model

#Multipolynomial regression

# Pipeline to construct scaling, polynomial function and regression after

Input = [('scale',StandardScaler()), ('polynomial'), Polynomial_fetures(degree=2),..('model', LinearRegression())]
pipe = Pipeline(Input)
Pipe.train(X['param1', 'param2',...,'paramN'],y)
yhat = Pipe.predict(X['param1', 'param2',...,'paramN'],y)
