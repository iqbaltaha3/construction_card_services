import streamlit as st
import requests

# Set page configuration
st.set_page_config(
    page_title="Construction Card Services",
    page_icon="🏗️",
    layout="centered"
)

# Initialize chat history in the session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Minimalist custom CSS styling
st.markdown("""
    <style>
        /* Overall page styling with a clean white background and simple font */
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #ffffff;
            color: #111;
            font-family: Arial, sans-serif;
        }
        /* Title styling */
        .title {
            text-align: center;
            font-size: 24px;
            font-weight: 600;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        /* Container for chat messages */
        .chat-container {
            max-width: 600px;
            margin: 0 auto;
        }
        /* Styling for user messages (appearing on the right) */
        .user-message {
            background-color: #e1ffc7;
            padding: 10px 14px;
            border-radius: 12px;
            margin: 8px 0;
            text-align: right;
        }
        /* Styling for assistant messages (appearing on the left) */
        .assistant-message {
            background-color: #f0f0f0;
            padding: 10px 14px;
            border-radius: 12px;
            margin: 8px 0;
            text-align: left;
        }
        /* Input box styling to make it simple and centered */
        .input-box {
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown('<div class="title">🏗️ Construction Card Services</div>', unsafe_allow_html=True)

# Container for chat messages
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-message"><strong>You:</strong> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="assistant-message"><strong>Consultant:</strong> {msg["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Create a form for input with clear_on_submit enabled
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "", 
        placeholder="Type your message here...", 
        label_visibility="collapsed"
    )
    submit_button = st.form_submit_button("Send")

# Process form submission only when text is provided
if submit_button and user_input.strip() != "":
    # Append user's message to the chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Show a spinner while waiting for the API response
    with st.spinner('Consultant is thinking...'):
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
                    'context': 'Assume the role of an expert',
                    'imp': 'Always provide relevant links from the document',
                    'content': user_input
                }
            ]
        }
        
        try:
            response = requests.post(chat_url, headers=headers, json=chat_payload)
            if response.status_code == 200:
                reply = response.json().get('content', 'No content found.')
                st.session_state.messages.append({"role": "assistant", "content": reply})
            else:
                st.error(f"Request failed: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")


