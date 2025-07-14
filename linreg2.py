import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import root_mean_squared_error

data = {
    'ad_budget': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    'sales': [14, 28, 35, 45, 52, 60, 68, 74, 80, 85]
}
df=pd.DataFrame(data)
x=df[['ad_budget']]
y=df[['sales']]
model=LinearRegression()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model.fit(x_train,y_train)
ypred=model.predict(x_test)
print('predicted sale:',model.predict([[23]]))
print('r2 score:',r2_score(y_test,ypred))
print('mean square error:',mean_squared_error(y_test,ypred))
print('root mean square error:',root_mean_squared_error(ypred,y_test))
