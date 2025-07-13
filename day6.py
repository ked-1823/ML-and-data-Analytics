import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
df=pd.read_csv('automobileEDA.csv')
print(df.head())
sns.scatterplot(x='engine-size',y='price',data=df)
plt.xlabel('engine-size')
plt.ylabel('price')
plt.show()