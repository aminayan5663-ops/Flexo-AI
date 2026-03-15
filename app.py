import streamlit as st
import google.generativeai as genai

# API Key Config (নিরাপত্তার জন্য পরে এটি সেটিংস থেকে সেট করব)
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

# UI ডিজাইন (প্রফেশনাল লুকের জন্য)
st.set_page_config(page_title="Flexo_AI", page_icon="🤖")
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stTextInput { border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Flexo_AI")
st.caption("A Professional AI Assistant by Nayan")

# চ্যাট হিস্ট্রি স্টোর করা
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ইউজার ইনপুট
if prompt := st.chat_input("আপনি কী জানতে চান?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI রেসপন্স জেনারেট করা
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
  
