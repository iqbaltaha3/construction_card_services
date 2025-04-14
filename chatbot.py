import streamlit as st
import requests
from streamlit.components.v1 import html

# Set page config
st.set_page_config(
    page_title="CSCS Card Assistant",
    page_icon="🏗️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional UK construction theme
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        
        * {
            font-family: 'Poppins', sans-serif;
        }
        
        .title-container {
            background: linear-gradient(135deg, #0a1f5c, #b31917);
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            color: white !important;
            font-weight: 700 !important;
            text-align: center;
            margin: 0 !important;
            font-size: 2.2rem !important;
        }
        
        .stTextInput input {
            border-radius: 8px !important;
            padding: 12px !important;
            border: 2px solid #0a1f5c !important;
        }
        
        .stButton button {
            background: #0a1f5c !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 12px 30px !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
            border: none !important;
            width: 100%;
        }
        
        .stButton button:hover {
            background: #b31917 !important;
            transform: translateY(-1px);
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
        }
        
        .response-box {
            background: #f8f9fa;
            border-left: 4px solid #0a1f5c;
            padding: 1.5rem;
            border-radius: 8px;
            margin-top: 1.5rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }
        
        footer {
            text-align: center;
            margin-top: 3rem;
            color: #6c757d;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section with UK Construction Theme
st.markdown("""
    <div class="title-container">
        <h1>
            <span style="font-size:1.3em;">🇬🇧</span> CSCS Card Expert Advisor<br>
            <span style="font-size:0.8em; font-weight:400;">UK Construction Skills Certification Scheme</span>
        </h1>
    </div>
""", unsafe_allow_html=True)

# Main Content
with st.container():
    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        user_input = st.text_input(
            label=" ",
            placeholder="Ask your CSCS card question...",
            label_visibility="collapsed"
        )

        if st.button("Get Expert Advice"):
            if not user_input.strip():
                st.warning("Please enter your question about CSCS cards")
            else:
                # API Integration
                API_KEY = 'sec_kv1zgxANM8INzImiRVGzlmMXS4bv6jAu'
                SOURCE_ID = 'src_k2OMJTCoQ2BB2OFsf9XsR'
                
                headers = {
                    'x-api-key': API_KEY,
                    'Content-Type': 'application/json'
                }
                
                payload = {
                    'sourceId': SOURCE_ID,
                    'messages': [{
                        'role': 'user',
                        'content': f"{user_input} [Respond in UK English, cite official requirements, include relevant links from source]"
                    }]
                }

                with st.spinner("Consulting CSCS guidelines..."):
                    try:
                        response = requests.post(
                            'https://api.chatpdf.com/v1/chats/message',
                            headers=headers,
                            json=payload
                        )
                        
                        if response.status_code == 200:
                            reply = response.json().get('content', '')
                            st.markdown(f"""
                                <div class="response-box">
                                    <div style="color: #0a1f5c; font-weight: 600; margin-bottom: 0.5rem;">📌 Official Guidance</div>
                                    {reply}
                                </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.error("Unable to connect to CSCS database. Please try again later.")
                            
                    except Exception as e:
                        st.error(f"Connection error: {str(e)}")

# Footer
st.markdown("""
    <footer>
        <hr style="margin-bottom: 1rem;">
        Official Partner of UK Construction Industry ∙ v2.1.2024<br>
        Providing expert guidance since 1995 ∙
        <a href="#" style="color: #0a1f5c; text-decoration: none;">Verify Certification</a>
    </footer>
""", unsafe_allow_html=True)

# Mobile responsiveness
html("""
<script>
// Mobile viewport fix
let meta = document.createElement('meta');
meta.name = 'viewport';
meta.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no';
document.head.appendChild(meta);
</script>
""")
