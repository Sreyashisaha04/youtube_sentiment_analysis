# 🎥 YouTube Sentiment Analyzer

This project is an interactive web app to analyze public sentiment from YouTube comments using Natural Language Processing (NLP). Built with **Python** and **Streamlit**, it visualizes sentiment trends, polarity scores, and keyword patterns using your own CSV file or the default one provided.

---

## 📌 Features

✅ Upload your own YouTube comments CSV file  
✅ Filter by sentiment (Positive, Negative, Neutral)  
✅ Search keywords within comments  
✅ View sentiment distribution charts (pie & bar)  
✅ Generate Word Clouds per sentiment  
✅ Export filtered results as CSV  
✅ Live deployment on Streamlit Cloud

---

## 📁 Dataset Format

Make sure your CSV file includes these columns:

- `Comment`: The actual comment text
- `Polarity`: A float between -1 (negative) and 1 (positive)
- `Sentiment`: One of `Positive`, `Negative`, or `Neutral`

A sample file (`youtube_comments.csv`) is already included in this project.

---

## 🚀 Launch the App

### ▶️ Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sreyashisaha04/youtube_sentiment_analysis.git
   cd youtube_sentiment_analysis
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run app.py
🌐 Try the Live App
🔗 Open Deployed App
(No setup needed. A sample file is already preloaded.)

📦 Dependencies
Install all required libraries using:

bash
Copy
Edit
pip install -r requirements.txt
requirements.txt includes:

nginx
Copy
Edit
streamlit
pandas
matplotlib
seaborn
plotly
wordcloud
🧠 Future Scope
Integrate YouTube Data API for real-time comment fetching

Add VADER sentiment scoring and BERT-based classification

Include visual trends by upload date or likes

Add comment length filtering and top-comment analysis

👩‍💻 Author
Sreyashi Saha
Beginner Data Analyst | Python Developer
📫 LinkedIn (Optional)

📄 License
This project is licensed under the MIT License – use freely for learning and improvement.

yaml
Copy
Edit

---

✅ Let me know if you want:
- A Markdown preview version
- A `requirements.txt` file generated
- Help pushing this to GitHub with `README.md` and dataset included
