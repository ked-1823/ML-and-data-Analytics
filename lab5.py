import pandas as pd
from sklearn.model_selection import train_test_split
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/module_5_auto.csv'
df=pd.read_csv(url)

df.to_csv('module_5.csv')
df=df._get_numeric_data()
print(df.head())
new_data=df.drop(['price'],axis=1)
y_data=df['price']
print(new_data.head())

x_train,x_test,y_train,y_test=train_test_split(new_data,y_data,test_size=0.20,random_state=4)
print("number of test sample:",x_test.shape[0])
print("number of train sample:",x_train.shape[0])
