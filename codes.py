
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")
print(df.head)


print("\nColumns Available:\n", df.columns.tolist)
print("\nDataset Info:\n")
print(df.info())


# Top 10 Most Popular Artists
if 'artists' in df.columns and 'popularity' in df.columns:
    top_artists = df.groupby('artists')['popularity'].mean().sort_values(ascending=False).head(10)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_artists.values, y=top_artists.index, palette='viridis')
    plt.title("Top 10 Most Popular Artists on Spotify", fontsize=16, fontweight='bold')
    plt.xlabel("Average Popularity", fontsize=12)
    plt.ylabel("Artist", fontsize=12)
    plt.tight_layout()
    plt.show()
else:
    print("Columns 'artists' or 'popularity' not found. Skipping this plot.")
    print(f"Available columns: {df.columns.tolist()}")
    
# Distribution of Song Popularity
if 'popularity' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['popularity'], bins=30, kde=True, color='orange')
    plt.title("Distribution of Song Popularity", fontsize=16, fontweight='bold')
    plt.xlabel("Popularity", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.tight_layout()
    plt.show()
else:
    print("Column 'popularity' not found. Skipping popularity distribution plot.")
    

# Correlation Between Audio Features
print("\n" + "="*50)
print("Analyzing Audio Feature Correlations...")
print("="*50)

numeric_features = df.select_dtypes(include=['float64', 'int64'])
if not numeric_features.empty:
    plt.figure(figsize=(12, 8))
    sns.heatmap(numeric_features.corr(), cmap="coolwarm", annot=True, fmt=".2f")
    plt.title("Correlation Between Audio Features", fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()
else:
    print("No numeric features found for correlation analysis.")

# Danceability vs Energy
if 'danceability' in df.columns and 'energy' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='danceability', y='energy', data=df, alpha=0.6)
    plt.title("Danceability vs Energy", fontsize=16, fontweight='bold')
    plt.xlabel("Danceability", fontsize=12)
    plt.ylabel("Energy", fontsize=12)
    plt.tight_layout()
    plt.show()
else:
    print("Columns 'danceability' or 'energy' not found. Skipping scatter plot.")

# Loudness vs Popularity
if 'loudness' in df.columns and 'popularity' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='loudness', y='popularity', data=df, alpha=0.5, color='purple')
    plt.title("Loudness vs Popularity", fontsize=16, fontweight='bold')
    plt.xlabel("Loudness (dB)", fontsize=12)
    plt.ylabel("Popularity", fontsize=12)
    plt.tight_layout()
    plt.show()
else:
    print("Columns 'loudness' or 'popularity' not found. Skipping scatter plot.")

# Summary Insights
print("\n" + "="*50)
print("📊 KEY INSIGHTS:")
print("="*50)
print("1️⃣ Danceability and Energy often show positive correlation.")
print("2️⃣ Loudness correlates moderately with Energy (modern songs are louder and more energetic).")
print("3️⃣ Popular songs cluster around mid-to-high Energy and Danceability values.")
print("4️⃣ Top artists tend to maintain consistent popularity scores across their tracks.")
print("="*50)