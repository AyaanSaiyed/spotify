# 🎵 Spotify Music Data Analysis (Exploratory Data Analysis)

## 📌 Project Description

This project performs an **Exploratory Data Analysis (EDA)** on Spotify music data to understand how audio features relate to song popularity and to identify trends among popular artists.

It was completed as part of my **First Year B.Sc. Data Science** program using Python-based data analysis and visualization techniques.

---

## 🎯 Objectives

- Analyze the distribution of song popularity on Spotify
- Identify the **Top 10 most popular artists** based on average popularity
- Explore relationships between key audio features such as:
  - Danceability
  - Energy
  - Loudness
- Visualize correlations among numerical features

---

## 🛠️ Tools & Libraries Used

- **Python**
- **Pandas** – data loading and manipulation
- **NumPy** – numerical computations
- **Matplotlib** – basic visualizations
- **Seaborn** – statistical and advanced plots

---

## 📊 Dataset Information

- **Dataset Name:** Spotify Tracks Dataset  
- **Source:** Spotify Tracks Dataset by Maharshi Pandya  
- **Platform:** Kaggle  

**Description:**  
The dataset contains Spotify tracks across **125 different genres**, with each track having multiple audio features such as popularity, danceability, energy, loudness, tempo, and more.

---

## 🔍 Analysis Workflow

### 1️⃣ Data Loading & Inspection
- Loaded the dataset using `pandas.read_csv()`
- Inspected:
  - First few rows of the dataset
  - Column names
  - Data types and missing values using `.info()`

---

### 2️⃣ Top 10 Most Popular Artists
- Grouped data by artist
- Calculated average popularity per artist
- Visualized the top 10 artists using a **horizontal bar chart**

📊 *Visualization:* Bar Plot (Seaborn)

---

### 3️⃣ Distribution of Song Popularity
- Analyzed how popularity scores are distributed across all tracks
- Used a **histogram with KDE** to observe skewness and clustering

📊 *Visualization:* Histogram with KDE

---

### 4️⃣ Correlation Analysis of Audio Features
- Selected numerical features automatically
- Computed the correlation matrix
- Visualized correlations using a **heatmap with annotations**

📊 *Visualization:* Correlation Heatmap

---

### 5️⃣ Feature Relationship Analysis

- **Danceability vs Energy**
  - Scatter plot to observe correlation between how danceable and energetic songs are

- **Loudness vs Popularity**
  - Scatter plot to understand whether louder songs tend to be more popular

📊 *Visualization:* Scatter Plots

---

## 📈 Key Insights

- 🎶 **Danceability and Energy** often show a positive relationship
- 🔊 **Loudness** correlates moderately with Energy, reflecting modern music production trends
- ⭐ Popular songs tend to cluster around **mid to high energy and danceability** values
- 🎤 Top artists generally maintain consistent popularity across their tracks
## 🚀 Conclusion

This project demonstrates the application of **Exploratory Data Analysis (EDA)** techniques to real-world music data. It strengthened my understanding of:

- Data inspection and cleaning  
- Statistical analysis  
- Data visualization using Python  

This analysis forms a strong foundation for future projects involving **machine learning**, **recommendation systems**, and **predictive modeling**.
