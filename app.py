import streamlit as st
from groq import Groq

# 1. Configuration
st.set_page_config(page_title="AI Applied Analyzer", page_icon="🤖", layout="centered")

# 2. Initialize Groq Client
# Replace "YOUR_GROQ_API_KEY" with your actual key
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# 3. UI Design (English Only)
st.title("🤖 AI Smart Document Analyzer")
st.markdown("""
This application uses **Llama 3.1** to analyze, summarize, and extract insights from your text. 
Perfect for quick document reviews and task extraction.
""")

st.divider()

# 4. Input Area
text_input = st.text_area("Paste your English text here:", height=250, placeholder="Enter or paste the article content...")

# 5. Action Buttons
col1, col2, col3 = st.columns(3)

with col1:
    summarize_btn = st.button("📝 Summarize")
with col2:
    tasks_btn = st.button("✅ Extract Tasks")
with col3:
    keywords_btn = st.button("🔍 Keywords")

# 6. Logic and API Calls
if text_input:
    try:
        if summarize_btn:
            with st.spinner("Summarizing..."):
                res = client.chat.completions.create(
                    messages=[{"role": "user", "content": f"Provide a concise summary of this text: {text_input}"}],
                    model="llama-3.1-8b-instant",
                )
                st.subheader("Summary:")
                st.write(res.choices[0].message.content)

        if tasks_btn:
            with st.spinner("Extracting tasks..."):
                res = client.chat.completions.create(
                    messages=[{"role": "user", "content": f"Extract all actionable tasks or to-do items from this text: {text_input}"}],
                    model="llama-3.1-8b-instant",
                )
                st.subheader("Action Items:")
                st.write(res.choices[0].message.content)

        if keywords_btn:
            with st.spinner("Extracting keywords..."):
                res = client.chat.completions.create(
                    messages=[{"role": "user", "content": f"List the top 5-10 keywords from this text: {text_input}"}],
                    model="llama-3.1-8b-instant",
                )
                st.subheader("Main Keywords:")
                st.write(res.choices[0].message.content)

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    if summarize_btn or tasks_btn or keywords_btn:
        st.warning("Please paste some text first!")

# 7. Footer
st.divider()
st.caption("Developed by Asadbek | Applied AI Engineer Portfolio Project")
