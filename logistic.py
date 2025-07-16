import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,recall_score,precision_score
from sklearn.datasets import load_breast_cancer
data=load_breast_cancer()
df=pd.DataFrame(data.data,columns=data.feature_names)
df['target']=data.target
print(df.head())
x=df[['mean radius','mean texture','mean perimeter']]
y=df['target']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LogisticRegression()
model.fit(x_train,y_train)
ypred=model.predict(x_test)
print('accuracy score:',accuracy_score(y_test,ypred))
print('confusion matrix:',confusion_matrix(y_test,ypred))
print('recall score:',recall_score(y_test,ypred))
print('precision score:',precision_score(y_test,ypred))