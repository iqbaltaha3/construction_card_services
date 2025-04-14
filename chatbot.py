import streamlit as st
import requests

# Set page config
st.set_page_config(
    page_title="Construction Card Services",
    page_icon="🏗️",
    layout="centered"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Custom CSS
st.markdown("""
    <style>
        /* Overall page background and text color */
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #f7f7f7 !important;
            color: #333 !important;
        }

        .title {
            text-align: center;
            font-size: 2em;
            margin-top: 10px;
            color: #333;
        }

        .user-message {
            background-color: #eceff1; /* Light gray */
            color: #000;              /* Dark text */
            padding: 12px;
            border-radius: 15px;
            margin: 8px 0;
            max-width: 80%;
            float: right;
            clear: both;
        }

        .assistant-message {
            background-color: #a83279; 
            color: #fff;
            padding: 12px;
            border-radius: 15px;
            margin: 8px 0;
            max-width: 80%;
            float: left;
            clear: both;
        }

        /* Optional: remove default gray from Streamlit containers */
        .css-18e3th9 {
            background-color: transparent !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🏗️ Construction Card Services</div>', unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-message">You: {message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="assistant-message">Consultant: {message["content"]}</div>', unsafe_allow_html=True)

# Create a form for input with clear_on_submit enabled
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "Ask a question about CSCS cards:",
        placeholder="e.g. Do labourers need a CSCS card?",
        label_visibility="collapsed"
    )
    submit_button = st.form_submit_button("Ask")

# Process the form only when submit button is clicked and input is not empty
if submit_button and user_input.strip() != "":
    # Add user question to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Show thinking indicator while waiting for API response
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
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": reply})
            else:
                st.error(f"Request failed: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

