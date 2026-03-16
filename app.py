import streamlit as st
import google.generativeai as genai

# সরাসরি API Key (বস্, আপনার কি এখানে বসিয়ে দিলাম)
API_KEY = "AIzaSyDd1yGqZX49oxSZPONDJwPk559a0GMxG8s"
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Flexo_AI", page_icon="🚀")
st.title("🚀 Flexo_AI")
st.caption("A Professional AI by Nayan")

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
        # এখানে gemini-pro ব্যবহার করছি, যা বর্তমানে সবথেকে বেশি স্ট্যাবল
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error: {e}")
