import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Area': [1000, 1500, 2000, 2200, 2500, 1800, 2700, 3000, 3200, 3500],
    'Bedrooms': [2, 3, 3, 4, 4, 2, 4, 5, 5, 5],
    'Age': [5, 3, 10, 2, 7, 15, 5, 1, 3, 2],
    'Price': [50, 65, 70, 90, 100, 60, 110, 130, 135, 140]
}
df=pd.DataFrame(data)
x=df[['Area','Bedrooms','Age']]
y=df['Price']
model=LinearRegression()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model.fit(x_train,y_train)
ypred=model.predict(x_test)
print('predicted values',ypred)
print('coefficiency:',model.coef_)
print('intercept:',model.intercept_)
print(model.predict(pd.DataFrame([[2600,4,4]],columns=['Area','Bedrooms','Age'])))
print('r2 score:',r2_score(y_test,ypred))
print('mse:',mean_squared_error(y_test,ypred))
sns.regplot(x=y_test,y=ypred,color='blue')
plt.xlabel('actual price')
plt.ylabel('predicted price')
plt.show()
