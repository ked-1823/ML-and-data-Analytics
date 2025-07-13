import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load dataset
df = pd.read_csv("automobileEDA.csv")

# Initial inspection
print(df.head(10))
print(df['peak-rpm'].dtypes)

# Correlation among selected columns
cols = ['bore', 'stroke', 'compression-ratio', 'horsepower']
print(df[cols].corr())

print("newline")
print(df[['highway-mpg', 'price']].corr())
print(df[['stroke', 'price']].corr())

# Boxplot of price by drive-wheels
sns.boxplot(x='drive-wheels', y='price', data=df)

# Summary of categorical data
print(df.describe(include=['object']))

# Value counts of drive-wheels
print("value count", df['drive-wheels'].value_counts())
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts = drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'})
print(drive_wheels_counts)
print(df['drive-wheels'].unique())

# Convert price to numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Group by drive-wheels and calculate mean price only
df_group_one = df[['drive-wheels', 'price']].dropna()
grouped_result = df_group_one.groupby(['drive-wheels'], as_index=False).mean()
#print(grouped_result)
df_gptest=df[['drive-wheels','body-style','price']]
grouped_test1=df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
#print("gptest: ",grouped_test1)
pivot1=grouped_test1.pivot(index='drive-wheels',columns='body-style')
#print("pivot1: ",pivot1)x
gp=pivot1.fillna(0)
#print("gp: ",gp)
gptest2=df[['price','body-style']]
res=gptest2.groupby(['body-style'],as_index=False).mean()
print("res:",res)

group_test2=df_gptest[['drive-wheels','price']].groupby(['drive-wheels'])
print(group_test2.head(2))
group_test2.get_group(('4wd',))['price']
f_value, p_value = stats.f_oneway(group_test2.get_group(('fwd',))['price'], group_test2.get_group(('rwd',))['price'], group_test2.get_group(('4wd',))['price'])
print("ANOVA results: F=", f_value, ", P =", p_value)
f_val,p_val=stats.f_oneway(group_test2.get_group(('fwd',))['price'],group_test2.get_group(('rwd',))['price'])
print("ANOVA results 2: F=", f_val, ", P =", p_val)
f_val,p_val=stats.f_oneway(group_test2.get_group(('4wd',))['price'],group_test2.get_group(('rwd',))['price'])
print("ANOVA results 3: F=", f_val, ", P =", p_val)
f_val,p_val=stats.f_oneway(group_test2.get_group(('4wd',))['price'],group_test2.get_group(('fwd',))['price'])
print("ANOVA results 4: F=", f_val, ", P =", p_val)

