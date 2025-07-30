import pandas as pd
import matplotlib.pyplot as plt

# Load the updated CSV (must include 'Sentiment' column)
df = pd.read_csv("youtube_comments.csv")  # ✅ No longer 'data/youtube_comments.csv'

# Confirm the required column exists
print("Columns in CSV:", df.columns.tolist())

# Count sentiment occurrences
sentiment_counts = df['Sentiment'].value_counts()

# Plot the sentiment distribution
sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
plt.title('YouTube Comment Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Comments')
plt.tight_layout()

# Save and show the plot
plt.savefig('sentiment_distribution.png')
print("✅ Sentiment bar chart saved as sentiment_distribution.png")
plt.show()
