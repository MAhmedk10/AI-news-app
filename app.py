import streamlit as st  
import feedparser  

def fetch_ai_research():
    url = "http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending"
    feed = feedparser.parse(url)  
    return feed.entries  

st.title("🤖 AI Research News in just one click!")  
st.write("Get the latest AI research papers on models like ChatGPT, DeepSeek, Gemini, and more!")

if st.button("Get Latest AI Research"):  
    News = fetch_ai_research()  

    if not News:
        st.write("⚠ No AI research found. Try again later!")
    else:
        for news in News[:5]:  
            st.subheader(news["title"])  
            st.write(f"*Published on:* {news['published'][:10]}")  
            st.write(f"[Read Paper]({news['link']})")  
            st.write("---")