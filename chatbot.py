import streamlit as st
import requests
import re

# Set page configuration
st.set_page_config(
    page_title="Construction Card Services",
    page_icon="🏗️",
    layout="centered"
)

# Helper function to convert URLs in the text into clickable links.
def linkify(text):
    url_pattern = r"(https?://[^\s]+)"
    # Replace URL with an HTML <a> tag that opens the link in a new tab.
    return re.sub(url_pattern, r'<a href="\1" target="_blank">\1</a>', text)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Minimalist custom CSS styling for a traditional chat look
st.markdown("""
    <style>
        /* Overall page styling */
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
        /* Chat container */
        .chat-container {
            max-width: 600px;
            margin: 0 auto;
        }
        /* User message styling (right aligned) */
        .user-message {
            background-color: #e1ffc7;
            padding: 10px 14px;
            border-radius: 12px;
            margin: 8px 0;
            text-align: right;
        }
        /* Assistant message styling (left aligned) */
        .assistant-message {
            background-color: #f0f0f0;
            padding: 10px 14px;
            border-radius: 12px;
            margin: 8px 0;
            text-align: left;
        }
        /* Styling for the text input */
        [data-testid="stTextInput"] label p {
            color: #555 !important;
        }
        [data-testid="stTextInput"] > label > div > input {
            background-color: #fff !important;
            color: #111 !important;
            border: 1px solid #ccc !important;
            border-radius: 4px !important;
            font-size: 14px !important;
            padding: 8px !important;
        }
        /* Send button styling */
        .stButton button {
            background-color: #4CAF50 !important;
            color: #fff !important;
            border: none !important;
            border-radius: 4px !important;
            padding: 8px 16px !important;
            font-size: 14px !important;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #45a049 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown('<div class="title">🏗️ Construction Card Services</div>', unsafe_allow_html=True)

# Create a form for input with clear_on_submit enabled
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "", 
        placeholder="Type your message here...", 
        label_visibility="collapsed"
    )
    submit_button = st.form_submit_button("Send")

# Process form submission if triggered and input is not empty
if submit_button and user_input.strip() != "":
    # Append user's message immediately to the chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Call the API to get the answer and add the assistant's message
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
                    'most imp': 'when asked about health,safety and awareness course or NVQ qualifications or things not in pdf, then always ask the user to contact support team (phone no - +443030030136 and email - support@constructioncardservices.com)'
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

# Display chat history (processing the assistant text to make links clickable)
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f'<div class="user-message"><strong>You:</strong> {msg["content"]}</div>',
            unsafe_allow_html=True
        )
    else:
        # Process the assistant message text to wrap URLs with clickable <a> tags.
        processed_text = linkify(msg["content"])
        st.markdown(
            f'<div class="assistant-message"><strong>Consultant:</strong> {processed_text}</div>',
            unsafe_allow_html=True
        )
st.markdown('</div>', unsafe_allow_html=True)





