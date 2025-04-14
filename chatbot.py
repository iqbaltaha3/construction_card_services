import streamlit as st
import requests

# Set page config
st.set_page_config(
    page_title="CSCS Card Services",
    page_icon="🏗️",
    layout="centered"
)

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Minimalist CSS for a clean look
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            background-color: #ffffff;
            color: #000000;
            padding: 0;
            margin: 0;
        }
        .title {
            font-size: 2.5em;
            font-weight: 600;
            color: #a83279; /* reddish purple */
            text-align: center;
            margin-bottom: 30px;
            padding-top: 30px;
        }
        .stTextInput>div>div>input {
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #a83279;
            color: white;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 15px;
            transition: background 0.3s;
            border: none;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #8f2f6f;
        }
        .chat-box {
            max-height: 400px;
            overflow-y: auto;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            background-color: #f8f8f8;
            border: 1px solid #ddd;
        }
        .message-box {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .user-msg, .assistant-msg {
            padding: 15px;
            border-radius: 10px;
            max-width: 70%;
            word-wrap: break-word;
            font-size: 16px;
        }
        .user-msg {
            background-color: #d1e7ff;
            align-self: flex-start;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .assistant-msg {
            background-color: #e0e0e0;
            align-self: flex-end;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .message-box p {
            margin: 0;
        }
        footer {
            text-align: center;
            margin-top: 40px;
            font-size: 0.9rem;
            color: #666;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🏗️ CSCS Card Services</div>', unsafe_allow_html=True)

# Chat history section
with st.container():
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)
    if st.session_state.chat_history:
        for chat in st.session_state.chat_history:
            if chat["role"] == "user":
                st.markdown(f'<div class="message-box"><div class="user-msg"><p>{chat["content"]}</p></div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="message-box"><div class="assistant-msg"><p>{chat["content"]}</p></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Input box
user_input = st.text_input("Ask a question about CSCS cards:", placeholder="e.g. Do labourers need a CSCS card?")

# Submit button to send question
if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Store user's question in history
        st.session_state.chat_history.append({"role": "user", "content": user_input})

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

# Footer
st.markdown("""
    <footer>
        Official Partner of UK Construction Industry ∙ v2.1.2024
    </footer>
""", unsafe_allow_html=True)

# Scroll to the latest message
st.markdown("""
    <script>
        const chatBox = document.querySelector('.chat-box');
        chatBox.scrollTop = chatBox.scrollHeight;
    </script>
""", unsafe_allow_html=True)

