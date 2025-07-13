import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

# Sample dataset
df = pd.DataFrame({
    'engine-size': [130, 152, 109, 136, 120, 150, 140, 160, 110, 128],
    'horsepower': [111, 154, 102, 115, 110, 160, 120, 170, 100, 108],
    'price': [13495, 16500, 13950, 17450, 15250, 18900, 16000, 21000, 14500, 14950]
})
x=df[['engine-size']]
y=df['price']

print(df)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=4)
print("train sample:",x_train.shape[0])
print("testing sample:",x_test.shape[0])
