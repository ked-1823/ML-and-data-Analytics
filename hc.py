import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

try:
    df = pd.read_csv(url)
    print("✅ Dataset loaded successfully")
    print(df.head())
except Exception as e:
    print("❌ Failed to load dataset:")
    print(e)
print(df['species'].value_counts())
sns.pairplot(df,hue='species')
plt.show()

