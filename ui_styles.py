import streamlit as st

def load_ui_styles():
    st.markdown("""
        <style>
            /* Main Background and App Container */
            body {
                background: linear-gradient(135deg, #ffe4ec 0%, #e0c3fc 100%);
                font-family: 'Inter', sans-serif;
            }
            .stApp {
                background: linear-gradient(135deg, #ffe4ec 0%, #e0c3fc 100%);
            }
            
            /* Card Styles */
            .css-1d391kg, .css-12oz5g7 {
                background-color: rgba(255, 255, 255, 0.85);
                padding: 2rem;
                border-radius: 20px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.12);
                backdrop-filter: blur(4px);
                -webkit-backdrop-filter: blur(4px);
                border: 1px solid rgba(255, 255, 255, 0.18);
                margin-bottom: 1rem;
            }
            
            /* Text Area Styling */
            .stTextArea textarea {
                border-radius: 15px;
                border: 2px solid #e0c3fc;
                background: rgba(255, 255, 255, 0.9);
                padding: 1rem;
                font-size: 1rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
                transition: all 0.3s ease;
            }
            .stTextArea textarea:focus {
                border-color: #7e22ce;
                box-shadow: 0 4px 20px rgba(126, 34, 206, 0.15);
            }
            
            /* Button Styling */
            .stButton > button {
                width: 100%;
                background: linear-gradient(135deg, #7e22ce 0%, #9333ea 100%);
                color: white;
                padding: 0.75rem 2rem;
                border-radius: 9999px;
                font-weight: 600;
                border: none;
                box-shadow: 0 4px 15px rgba(126, 34, 206, 0.2);
                transition: all 0.3s ease;
            }
            .stButton > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 20px rgba(126, 34, 206, 0.3);
                background: linear-gradient(135deg, #9333ea 0%, #7e22ce 100%);
            }
            .stButton > button:active {
                transform: translateY(0px);
            }
            
            /* Spinner/Loading Animation */
            div.stSpinner > div {
                border-top-color: #7e22ce !important;
                border-width: 3px;
            }
            
            /* File Uploader */
            .uploadedFile {
                background: rgba(255, 255, 255, 0.9);
                border-radius: 15px;
                padding: 1rem;
                margin: 0.5rem 0;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            }
            
            /* Headers and Text */
            h1, h2, h3 {
                color: #7e22ce;
                font-weight: 700;
                margin-bottom: 1rem;
            }
            .subtitle {
                color: #555;
                font-size: 1.1rem;
                margin-bottom: 2rem;
            }
            
            /* Image Container */
            .image-container {
                background: white;
                border-radius: 15px;
                padding: 1rem;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
                margin-bottom: 1rem;
            }
            
            /* Custom Divider */
            .custom-divider {
                height: 2px;
                background: linear-gradient(90deg, #ffe4ec 0%, #e0c3fc 100%);
                margin: 2rem 0;
                border-radius: 2px;
            }
            
            /* Responsive Adjustments */
            @media (max-width: 768px) {
                .stButton > button {
                    padding: 0.5rem 1rem;
                }
            }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    st.markdown("""
        <div style='text-align: center; padding: 2rem 0;'>
            <h1 style='color: #7e22ce; font-size: 2.5rem; margin-bottom: 0.5rem;'>AI Stylist Assistant 👗</h1>
            <p class='subtitle'>Upload your outfit images and get personalized style recommendations</p>
        </div>
    """, unsafe_allow_html=True)

def render_welcome_message():
    st.markdown("""
        <div style='text-align: center; padding: 3rem; background: rgba(255, 255, 255, 0.9); 
             border-radius: 20px; box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.12);'>
            <h3 style='color: #7e22ce; margin-bottom: 1rem;'>👗 Ready to get started?</h3>
            <p style='color: #666; font-size: 1.1rem;'>Upload your outfit images and I'll help you create amazing combinations!</p>
        </div>
    """, unsafe_allow_html=True)

def render_section_header(text, emoji):
    st.markdown(f"""
        <h3 style='color: #7e22ce; display: flex; align-items: center; gap: 0.5rem; margin: 1.5rem 0 1rem 0;'>
            {emoji} {text}
        </h3>
    """, unsafe_allow_html=True)

def render_analysis_section(title, content):
    st.markdown(f"""
        <div style='background: rgba(255, 255, 255, 0.9); border-radius: 20px; 
             padding: 1.5rem; margin: 1rem 0; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);'>
            <h3 style='color: #7e22ce; margin-bottom: 1rem;'>{title}</h3>
            <div style='color: #333; font-size: 1.1rem;'>{content}</div>
        </div>
    """, unsafe_allow_html=True)
