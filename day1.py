import numpy as np
import pandas as pd
df=pd.read_csv('titanic.csv')


df['Age']=df['Age'].fillna(df['Age'].mean())
print(df.columns)
print(df['Age'].isnull().sum())
df['Cabin']=df['Cabin'].fillna('Unknown')
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
print(df.head())
print(df['Embarked'].isnull().sum())




