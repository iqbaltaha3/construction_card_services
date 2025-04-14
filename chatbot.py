import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="Construction Card Services",
    page_icon="🏗️",
    layout="centered"
)

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Modern minimalist CSS
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            background-color: #ffffff;
            color: #000000;
        }
        .title {
            font-size: 2.5em;
            font-weight: 600;
            color: #a83279;
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
            background-color: #f9f9f9;
            color: #000000;
            padding: 15px;
            border-left: 4px solid #a83279;
            border-radius: 8px;
            margin-top: 10px;
        }
        .user-msg {
            font-weight: 600;
            margin-top: 20px;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🏗️ Construction Card Services</div>', unsafe_allow_html=True)

# User input
user_input = st.text_input("Ask a question about CSCS cards:", placeholder="e.g. Do labourers need a CSCS card?")

# Submit button
if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Store user's question in history
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # API Call
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
                    'content': f"{user_input} [Provide relevant links and official sources if possible]"
                }
            ]
        }

        try:
            response = requests.post(chat_url, headers=headers, json=chat_payload)
            if response.status_code == 200:
                reply = response.json().get('content', 'No content found.')
                # Store assistant's reply in history
                st.session_state.chat_history.append({"role": "assistant", "content": reply})
            else:
                error_msg = f"Request failed: {response.text}"
                st.session_state.chat_history.append({"role": "assistant", "content": error_msg})
        except Exception as e:
            st.session_state.chat_history.append({"role": "assistant", "content": f"An error occurred: {e}"})


# Display chat history
for i, chat in enumerate(st.session_state.chat_history):
    if chat["role"] == "user":
        st.markdown(f'<div class="user-msg">🧑‍💼 You:</div><div class="response-box">{chat["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="user-msg">🤖 CSCS Bot:</div><div class="response-box">{chat["content"]}</div>', unsafe_allow_html=True)


