import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
df=pd.read_csv("automobileEDA.csv")
df.head()
lm=LinearRegression()
x=df[['highway-mpg']]
y=df['price']
lm.fit(x,y)
print("intercept:",lm.intercept_)
print("coefficient:",lm.coef_)
lm1=LinearRegression()
x1=df[['engine-size']]
y1=df['price']
lm1.fit(x1,y1)
print("intercept:",lm1.intercept_)
print("coefficient:",lm1.coef_)
pred=pd.DataFrame([[150]],columns=['engine-size'])
print("prediction:",lm1.predict(pred))
#multiple linear regression
z=df[['horsepower','curb-weight','engine-size','highway-mpg']]
r=df['price']
lm2=LinearRegression()
lm2.fit(z,r)
print("intercept:",lm2.intercept_)
print('coefficient:',lm2.coef_)

a=df[['normalized-losses','highway-mpg']]
b=df['price']
lm3=LinearRegression()
lm3.fit(a,b)
print("intercept:",lm3.intercept_)
print('coefficient:',lm3.coef_)

correlation=df[['peak-rpm','highway-mpg','price']].corr()
print(correlation)
width =12
height=10
plt.figure(figsize=(width,height))
sns.residplot(x='highway-mpg',y='price',data=df)
y_hat=lm2.predict(z)
plt.figure(figsize=(width, height))


ax1 = sns.kdeplot(df['price'], color="r", label="Actual Value")
sns.kdeplot(y_hat, color="b", label="Fitted Values" , ax=ax1)


plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')
plt.show()