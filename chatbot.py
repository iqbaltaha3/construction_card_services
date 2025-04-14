import streamlit as st
import requests

# Set page config
st.set_page_config(
    page_title="Construction Card Services",
    page_icon="🏗️",
    layout="centered"
)

# Custom CSS for modern minimalist UI
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            background-color: #ffffff;
            color: #000000;
        }
        .title {
            font-size: 2.5em;
            font-weight: 600;
            color: #a83279; /* reddish purple */
            text-align: center;
            margin-bottom: 30px;
        }
        .stTextInput>div>div>input {
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        .stButton>button {
            background-color: #000000;
            color: white;
            border-radius: 6px;
            padding: 10px 24px;
            font-size: 15px;
            transition: background 0.3s;
        }
        .stButton>button:hover {
            background-color: #a83279;
        }
        .response-box {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🏗️ Construction Card Services</div>', unsafe_allow_html=True)

# Input box
user_input = st.text_input("Ask a question about CSCS cards:", placeholder="e.g. Do labourers need a CSCS card?")

# Submit button
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

        try:
            response = requests.post(chat_url, headers=headers, json=chat_payload)
            if response.status_code == 200:
                reply = response.json().get('content', 'No content found.')
                st.markdown(f'<div class="response-box">{reply}</div>', unsafe_allow_html=True)
            else:
                st.error(f"Request failed: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

