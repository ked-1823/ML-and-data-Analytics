import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: (optional in Replit, file already exists)
# os.system("wget https://raw.githubusercontent.com/ibm-developer-skills-network/DS0101EN-SkillsNetwork/master/labs/Module%202/data/automobileEDA.csv")

# Step 2: Load data
df = pd.read_csv("automobileEDA.csv")

# First model using highway-mpg
model = LinearRegression()
x = df[['highway-mpg']]
y = df['price']
model.fit(x, y)
yhat = model.predict(x)
print("Prediction from highway-mpg model:", yhat[0:5])
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)

# Second model using engine-size
lm1 = LinearRegression()
x = df[['engine-size']]
y = df['price']
lm1.fit(x, y)
yhat = lm1.predict(x)
print("Second prediction using engine-size:", yhat[0:5])
print("Intercept:", lm1.intercept_)
print("Coefficient:", lm1.coef_)

# Manual calculation
manual_yhat = -7963.34 + 166.86 * df['engine-size']
print("Manual Prediction (first 5):", manual_yhat.head())
