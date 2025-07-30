import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px

# 🎯 Page Configuration
st.set_page_config(page_title="🎥 YouTube Sentiment Analyzer", layout="wide")
st.title("🎥 YouTube Sentiment Analyzer")
st.markdown("Analyze public sentiments from YouTube comments using Natural Language Processing (NLP).")

# 📁 Upload CSV File
uploaded_file = st.file_uploader("📁 Upload your preprocessed CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # ✅ Validate CSV Structure
    required_cols = {"Comment", "Polarity", "Sentiment"}
    if not required_cols.issubset(df.columns):
        st.error(f"⚠️ The CSV file must contain the columns: {required_cols}")
    else:
        # 🔍 Sidebar Filters
        st.sidebar.header("🔍 Filter Comments by Sentiment")
        sentiment_filter = st.sidebar.radio(
            "Choose a sentiment to display:",
            options=["All", "Positive", "Negative", "Neutral"],
            index=0
        )

        if sentiment_filter != "All":
            df = df[df["Sentiment"] == sentiment_filter]

        # 🔎 Keyword Search Filter
        st.sidebar.header("🔎 Search in Comments")
        keyword = st.sidebar.text_input("Enter a keyword (case-insensitive):")
        if keyword:
            df = df[df["Comment"].str.contains(keyword, case=False, na=False)]

        # ✅ If data remains after filtering
        if not df.empty:
            # 📊 Pie Chart
            st.subheader("📊 Sentiment Distribution (Pie Chart)")
            sentiment_counts = df['Sentiment'].value_counts()
            pie_fig = px.pie(
                names=sentiment_counts.index,
                values=sentiment_counts.values,
                title="Sentiment Breakdown",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            st.plotly_chart(pie_fig, use_container_width=True)

            # 📝 Display Filtered Comments
            st.subheader("📝 Filtered Comments")
            st.dataframe(df, use_container_width=True)

            # 📥 Download Filtered Comments
            csv_download = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Filtered Comments as CSV",
                data=csv_download,
                file_name="filtered_comments.csv",
                mime="text/csv"
            )

            # 📊 Bar Chart of Sentiment Counts
            st.subheader("📊 Sentiment Distribution (Bar Chart)")
            fig1, ax1 = plt.subplots()
            sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="pastel", ax=ax1)
            ax1.set_xlabel("Sentiment")
            ax1.set_ylabel("Number of Comments")
            ax1.set_title("Sentiment Distribution")
            st.pyplot(fig1)

            # 📈 Average Polarity Chart
            st.subheader("📈 Average Polarity by Sentiment")
            polarity_avg = df.groupby("Sentiment")["Polarity"].mean().reset_index()
            fig2, ax2 = plt.subplots()
            sns.barplot(data=polarity_avg, x="Sentiment", y="Polarity", palette="Set2", ax=ax2)
            ax2.set_ylabel("Average Polarity Score")
            ax2.set_title("Sentiment Strength Comparison")
            st.pyplot(fig2)

            # ☁️ Word Cloud Generator
            def generate_wordcloud(sentiment):
                text = " ".join(df[df["Sentiment"] == sentiment]["Comment"].astype(str))
                if text.strip():
                    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
                    st.image(wordcloud.to_array(), caption=f"{sentiment} Word Cloud", use_container_width=True)
                else:
                    st.warning(f"⚠️ No comments available for {sentiment} sentiment.")

            # ☁️ Display Word Clouds
            st.subheader("☁️ Word Clouds by Sentiment")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("**😊 Positive Word Cloud**")
                generate_wordcloud("Positive")
            with col2:
                st.markdown("**😐 Neutral Word Cloud**")
                generate_wordcloud("Neutral")
            with col3:
                st.markdown("**😠 Negative Word Cloud**")
                generate_wordcloud("Negative")

        else:
            st.warning("⚠️ No comments match the current filter or keyword search.")

else:
    st.info("👆 Upload a `.csv` file to begin analyzing YouTube sentiments.")
