# 📊 Project Report: YouTube Sentiment Analyzer

## 📝 Introduction

With the increasing influence of YouTube on public opinion, analyzing user comments helps understand sentiment trends about topics, events, or influencers. This project aims to build an **interactive web application** that performs **sentiment analysis** on YouTube comments using NLP and visualizes insights effectively.

---

## 🎯 Objectives

- Analyze sentiment (Positive, Negative, Neutral) from YouTube comments.
- Visualize data using charts and word clouds.
- Allow users to filter comments by sentiment and keywords.
- Enable downloading of filtered comment data.

---

## 🧰 Tools & Technologies Used

| Tool/Library       | Purpose                          |
|--------------------|----------------------------------|
| Python             | Core programming language        |
| Streamlit          | Web application framework        |
| Pandas             | Data handling and manipulation   |
| Matplotlib & Seaborn | Static plotting                 |
| Plotly             | Interactive visualizations       |
| WordCloud          | Generate sentiment-based clouds  |

---

## 📂 Dataset Description

The app uses a **CSV file** containing preprocessed YouTube comments with the following columns:

- `Comment`: The actual user comment.
- `Polarity`: Sentiment polarity score (range: -1 to +1).
- `Sentiment`: Categorical label — Positive, Negative, or Neutral.

---

## 🚀 Features Implemented

### ✅ File Upload
- Upload a preprocessed `.csv` file with comment data.

### ✅ Sentiment Filtering
- Use a sidebar to filter by sentiment: **All / Positive / Negative / Neutral**.

### ✅ Keyword Search
- Case-insensitive keyword search to find relevant comments.

### ✅ Visualizations
- 📊 **Pie Chart** of sentiment distribution.
- 📊 **Bar Chart** of sentiment counts.
- 📈 **Polarity comparison** across sentiments.
- ☁️ **Word clouds** for each sentiment category.

### ✅ Data Display & Download
- Shows filtered comments in a scrollable table.
- Allows download of filtered results as a `.csv`.

---

## 📸 Screenshots

> (Add screenshots of your app here if needed. Example titles below.)
- Home Page with Upload Panel
- Pie Chart Sentiment Distribution
- Word Cloud for Positive Sentiment

---

## 📁 File Structure

youtube-sentiment-analyzer/
│
├── app.py # Main Streamlit application
├── youtube_comments.csv # Sample dataset (optional)
├── README.md # Project overview
└── report.md # This report

yaml
Copy
Edit

---

## 💡 Future Improvements

- Integrate live YouTube Data API to fetch comments directly from videos.
- Support for multilingual sentiment analysis.
- Add emoji-based sentiment scoring.
- Allow comment length filtering or time-based filtering.

---

## 🙋‍♀️ Author

**Sreyashi Saha**  
*B.Tech IT Student | Beginner in Data Science & Web App Development*

---

