
import pandas as pd

df=pd.DataFrame({"names":["kedar","rohan","shubham","nilesh"],"marks":[90,43,87,45]})
print(df)

newdata=df.rename(columns={"names":"NAMES"}, inplace=True)
print("updated dataframe:")
print(df)
print(len(df))
df['zeros']=[0 for i in range(len(df))]
print("added zero :")
print(df)
print(df.info())
df.to_csv("newdata.csv",index= False)
pd1=pd.DataFrame({"names":["kedar","rohan","shubham","nilesh"],"marks":[90,43,87,45]})
pd2=pd.DataFrame({"names":["kashish","richa","shivani"],"marks":[56,34,98]})
og_data=pd.concat([pd1,pd2])
print(og_data)
