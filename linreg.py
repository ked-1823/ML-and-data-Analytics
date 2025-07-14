import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
data = {
    'Area': [500, 750, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 2700],
    'Price': [15, 20, 25, 30, 38, 45, 49, 52, 60, 65]
}
df=pd.DataFrame(data)
x=df[['Area']]
y=df[['Price']]
model=LinearRegression()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model.fit(x_train,y_train)
ypred=model.predict(x_test)
print('r2 score:',r2_score(y_test,ypred))
print('mse:',mean_squared_error(y_test,ypred))
example=model.predict([[600]])
print('predicted price:',example[0][0])
plt.scatter(x,y,color='blue')
plt.plot(x_test,ypred,label='linear regression',color='red')
plt.title('linear regression')
plt.show()
