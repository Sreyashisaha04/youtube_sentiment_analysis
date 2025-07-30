import pandas as pd
import matplotlib.pyplot as plt

# Load analyzed sentiment data
df = pd.read_csv("youtube_comments.csv")
print("Columns in CSV file:", df.columns.tolist())  # 👈 Add this line

# Count sentiment labels
sentiment_counts = df['Sentiment'].value_counts()

# Bar Chart
plt.figure(figsize=(6,4))
sentiment_counts.plot(kind='bar', color=['green', 'gray', 'red'])
plt.title("YouTube Comment Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Comments")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/sentiment_bar_chart.png")
plt.show()

