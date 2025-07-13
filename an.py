import pandas as pd
import numpy as np

import matplotlib.pyplot as plt



headers = [
    "symboling", "normalized-losses", "make", "fuel-type", "aspiration",
    "num-of-doors", "body-style", "drive-wheels", "engine-location",
    "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
    "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke",
    "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg",
    "price"
]

df = pd.read_csv("auto.csv", names=headers)

df.replace("?", np.nan, inplace=True)

missing = df.isnull()

for column in missing.columns.values.tolist():

     print(missing[column].value_counts())
     print("")
avg_norm_loss = df['normalized-losses'].astype('float').mean(axis=0)
#print("avg of norm_loss:",avg_norm_loss)
df['normalized-losses'].replace(np.nan, avg_norm_loss, inplace=True)
#print(df['normalized-losses'].head(10))
avg_bore = df['bore'].astype('float').mean(axis=0)
#print("avg of bore:",avg_bore)
df['bore'].replace(np.nan, avg_bore, inplace=True)
#print(df['bore'].head(10))
avg_stroke = df['stroke'].astype('float').mean(axis=0)
#print("avg of stroke:",avg_stroke)
df['stroke'].replace(np.nan, avg_stroke, inplace=True)
#print(df['stroke'].head(10))
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)
avg_peak_rpm = df['peak-rpm'].astype('float').mean(axis=0)
df['peak-rpm'].replace(np.nan, avg_peak_rpm, inplace=True)
df['num-of-doors'].value_counts()
#print(df['num-of-doors'].value_counts().idxmax())
df['num-of-doors'].replace(np.nan, 'four', inplace=True)
df.dropna(subset=['price'], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
#print(df.head(10))
df[['bore', 'stroke']] = df[['bore', 'stroke']].astype('float')
df[['normalized-losses']] = df[['normalized-losses']].astype('int')
df[['pr']] = df[['price']].astype('float')
df[['peak-rpm']] = df[['peak-rpm']].astype('float')
#print(df.dtypes)
df['city-L/100km'] = 235 / df['city-mpg']

print(df.head(10))
df['highway-L/100km'] = 235 / df['highway-mpg']
print(df.head(10))
df['length'] = df['length'] / df['length'].max()
df['height'] = df['height'] / df['height'].max()
df['width'] = df['width'] / df['width'].max()
a=df[['length','width','height']].head(10)
#print(a)
df['horsepower'] = df['horsepower'].astype(int,copy=True)
print(df['horsepower'].head(10))
plt.hist(df['horsepower'])
plt.xlabel('horsepower')
plt.ylabel('count')
plt.title('horsepower bins')
plt.show()
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)


