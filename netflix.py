import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/netflix_titles.csv")
df.columns = df.columns.str.strip()  # Clean column names

print("✅ Dataset Loaded:")
print(df.shape)
print("columns:", df.columns.tolist())
print(df.info())
print(df.describe(include='all'))
print(df.isnull().sum())

# Clean data
df = df.dropna(subset=['director', 'cast', 'country'])
df['rating'] = df['rating'].fillna("unknown")
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')

# Show insights
print(df['type'].value_counts())
indian_content = df[df['country'] == 'India']
print("Indian content:", indian_content.head(10))
print(df['listed_in'].value_counts().head(10))
print("Top 5 directors:", df['director'].value_counts().head(5))

# Plot and save
plt.figure(figsize=(6, 4))
df['type'].value_counts().plot(kind='bar', title="Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("movies_vs_tv_show.png")
df.to_csv("cleaned_netflix_titles.csv", index=False)
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/netflix_titles.csv")
df.columns = df.columns.str.strip()  # Clean column names

print("✅ Dataset Loaded:")
print(df.shape)
print("columns:", df.columns.tolist())
print(df.info())
print(df.describe(include='all'))
print(df.isnull().sum())

# Clean data
df = df.dropna(subset=['director', 'cast', 'country'])
df['rating'] = df['rating'].fillna("unknown")
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')

# Show insights
print(df['type'].value_counts())
indian_content = df[df['country'] == 'India']
print("Indian content:", indian_content.head(10))
print(df['listed_in'].value_counts().head(10))
print("Top 5 directors:", df['director'].value_counts().head(5))

# Plot and save
plt.figure(figsize=(6, 4))
df['type'].value_counts().plot(kind='bar', title="Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("movies_vs_tv_show.png")
df.to_csv("cleaned_netflix_titles.csv", index=False)

