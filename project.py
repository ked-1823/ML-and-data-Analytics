import numpy as np
import pandas as pd

df=pd.read_csv('matches.csv')
a=df.isnull().sum()
df=df.copy()
df['city']=df['city'].fillna('Unknown')
df['player_of_match']=df['player_of_match'].fillna('Unknown')
df['winner']=df['winner'].fillna('No result')
df['result_margin']=df['result_margin'].fillna('NA')
df['target_overs']=df['target_overs'].fillna('0')
df['target_runs']=df['target_runs'].fillna('0')
df['method']=df['method'].fillna('Unknown')

#print(df.isnull().sum())
toss=df['toss_winner'].value_counts()
print("most tosses won by: ",toss.idxmax())
print('most time toss losing team:',toss.idxmin())
toss_res=df[df['toss_winner']==df['winner']].shape[0]
total_match=df.shape[0]
toss_percentage=(toss_res/total_match )*100
print('toss win = match win % : ',toss_percentage)




