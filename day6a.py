import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv('automobileEDA.csv')
print(df.head())

corr=df.corr(numeric_only=True)
sns.heatmap(corr,cmap='coolwarm')
price_cor=corr['price'].drop('price')
top_corr=price_cor.sort_values(ascending=False)
print("top correlation fetaures with price")
print(top_corr.head(5))
print(df[['price','highway-mpg','engine-size','horsepower']].describe())
