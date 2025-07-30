import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# Load comments from CSV
df = pd.read_csv("data/youtube_comments.csv")

# Join all comments into one large string
text = " ".join(str(comment) for comment in df['Comment'])

# Create WordCloud object
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    stopwords=set(['https', 'www', 'com', 'the', 'and', 'this', 'that']),
    colormap='viridis'
).generate(text)

# Create output folder if not exists
os.makedirs("output", exist_ok=True)

# Save the wordcloud image
wordcloud.to_file("output/wordcloud.png")
print("✅ Word Cloud saved to output/wordcloud.png")

# Show the WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Most Common Words in YouTube Comments")
plt.tight_layout()
plt.show()
