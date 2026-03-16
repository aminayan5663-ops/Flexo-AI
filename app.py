import streamlit as st
import google.generativeai as genai

# সরাসরি API Key সেট করা (বস্, আপনার নিউ কী এখানে বসানো হলো)
API_KEY = "AIzaSyDd1yGqZX49oxSZPONDJwPk559a0GMxG8s"
genai.configure(api_key=API_KEY)

# UI ডিজাইন
st.set_page_config(page_title="Flexo_AI", page_icon="🤖")
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stTextInput { border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Flexo_AI")
st.caption("A Professional AI Assistant by Nayan")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("আপনি কী জানতে চান?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error: {e}")
        
