import requests
import pandas as pd
import os

# Load API key
with open("api_key.txt", "r") as f:
    API_KEY = f.read().strip()

# 🔹 Function to fetch comments
def fetch_comments(video_id, max_results=100):
    comments = []
    url = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
        "part": "snippet",
        "videoId": video_id,
        "key": API_KEY,
        "textFormat": "plainText",
        "maxResults": 100
    }

    while len(comments) < max_results:
        response = requests.get(url, params=params)
        data = response.json()

        for item in data.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        if "nextPageToken" in data:
            params["pageToken"] = data["nextPageToken"]
        else:
            break

    return comments[:max_results]

# 🔹 MAIN
if __name__ == "__main__":
    video_id = input("Enter YouTube Video ID: ")
    max_comments = int(input("How many comments to fetch? (e.g. 100): "))

    print("Fetching comments...")

    fetched_comments = fetch_comments(video_id, max_results=max_comments)

    df = pd.DataFrame(fetched_comments, columns=["Comment"])
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/youtube_comments.csv", index=False)

    print(f"✅ {len(fetched_comments)} comments saved to data/youtube_comments.csv")
