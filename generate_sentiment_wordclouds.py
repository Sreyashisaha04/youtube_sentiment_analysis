import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

df = pd.read_csv("youtube_comments.csv")

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

for sentiment in ['Positive', 'Negative', 'Neutral']:
    text = " ".join(df[df['Sentiment'] == sentiment]['Comment'].astype(str))
    if text.strip():  # Check if text is not empty
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(8, 4))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'{sentiment} Comments Word Cloud')
        plt.tight_layout()
        plt.savefig(f"output/{sentiment.lower()}_wordcloud.png")
        plt.close()
