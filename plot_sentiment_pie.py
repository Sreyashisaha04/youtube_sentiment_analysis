import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV with sentiments
df = pd.read_csv("youtube_comments.csv")

# Count sentiment categories
sentiment_counts = df['Sentiment'].value_counts()

# Pie chart
plt.figure(figsize=(6, 6))
colors = ['lightgreen', 'lightcoral', 'lightgray']
sentiment_counts.plot.pie(autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('YouTube Sentiment Breakdown')
plt.ylabel('')  # Remove y-label
plt.tight_layout()
plt.savefig('output/sentiment_pie_chart.png')
plt.show()
