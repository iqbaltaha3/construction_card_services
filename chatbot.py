import streamlit as st
import requests

# Set page configuration
st.set_page_config(
    page_title="Construction Card Services",
    page_icon="🏗️",
    layout="centered",
    initial_sidebar_state="auto"
)

# Custom CSS for violet-purple theme
st.markdown("""
    <style>
    .main {
        background-color: #f5f0ff;
    }
    .stButton>button {
        background-color: #6a0dad;
        color: white;
        border-radius: 8px;
        padding: 8px 20px;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        border: 1px solid #6a0dad;
        border-radius: 6px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🦺 Construction Card Services")

# Input from user
user_input = st.text_input("Ask something about CSCS cards...", placeholder="e.g. cscs card for labours?")

# Button to submit
if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        # API details
        API_KEY = 'sec_kv1zgxANM8INzImiRVGzlmMXS4bv6jAu'
        SOURCE_ID = 'src_k2OMJTCoQ2BB2OFsf9XsR'
        chat_url = 'https://api.chatpdf.com/v1/chats/message'
        headers = {
            'x-api-key': API_KEY,
            'Content-Type': 'application/json'
        }
        chat_payload = {
            'sourceId': SOURCE_ID,
            'messages': [
                {
                    'role': 'user',
                    'imp': 'Always provide relevant links from the document',
                    'content': user_input
                }
            ]
        }

        # API call
        try:
            response = requests.post(chat_url, headers=headers, json=chat_payload)
            if response.status_code == 200:
                reply = response.json().get('content', 'No content found.')
                st.success("Response:")
                st.write(reply)
            else:
                st.error(f"Request failed: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
