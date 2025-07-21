
# ui_enhancer.py
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.card import card

def create_input_container():
    return stylable_container(
        key="input-container",
        css_styles="""
            {
                background: white;
                border-radius: 20px;
                padding: 25px;
                box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
                margin-bottom: 2rem;
            }
        """
    )

def success_card(subject, duration):
    with stylable_container(
        key="success-card",
        css_styles="""
            {
                background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
                border-radius: 15px;
                padding: 20px;
                margin: 1rem 0;
                border-left: 5px solid #28a745;
            }
        """
    ):
        st.markdown(f"""
        <div style="display: flex; align-items: center;">
            <span style="font-size: 2rem; margin-right: 1rem;">✅</span>
            <div>
                <h4 style="color: #155724; margin: 0;">Syllabus Generated Successfully!</h4>
                <p style="color: #155724; margin: 0.5rem 0 0 0;">
                    Your {duration} syllabus for <strong>{subject}</strong> is ready below.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

def create_syllabus_container():
    return stylable_container(
        key="syllabus-container",
        css_styles="""
            {
                background: white;
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
                margin: 2rem 0;
                border-left: 4px solid #4CAF50;
            }
        """
    )

def create_feature_cards():
    col1, col2, col3 = st.columns(3)

    with col1:
        with stylable_container("feature-1", css_styles="""
            {
                background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
                border-radius: 15px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 4px 15px rgba(255, 154, 158, 0.3);
            }
        """):
            st.markdown("""
            <h3 style="margin: 0; color: white;">🤖 AI-Powered</h3>
            <p style="margin: 0.5rem 0 0 0; color: white; font-size: 0.9rem;">
                Advanced AI creates detailed, structured syllabi
            </p>
            """, unsafe_allow_html=True)

    with col2:
        with stylable_container("feature-2", css_styles="""
            {
                background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
                border-radius: 15px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 4px 15px rgba(168, 237, 234, 0.3);
            }
        """):
            st.markdown("""
            <h3 style="margin: 0; color: #2c3e50;">⚡ Fast Generation</h3>
            <p style="margin: 0.5rem 0 0 0; color: #2c3e50; font-size: 0.9rem;">
                Complete syllabus ready in seconds
            </p>
            """, unsafe_allow_html=True)

    with col3:
        with stylable_container("feature-3", css_styles="""
            {
                background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
                border-radius: 15px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 4px 15px rgba(255, 236, 210, 0.3);
            }
        """):
            st.markdown("""
            <h3 style="margin: 0; color: #2c3e50;">📚 Comprehensive</h3>
            <p style="margin: 0.5rem 0 0 0; color: #2c3e50; font-size: 0.9rem;">
                Includes objectives, assessments, and resources
            </p>
            """, unsafe_allow_html=True)

def loading_animation():
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div style="
            display: inline-block;
            width: 40px;
            height: 40px;
            border: 4px solid #f3f3f3;
            border-top: 4px solid #4CAF50;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        "></div>
        <p style="margin-top: 1rem; color: #4CAF50; font-weight: 600;">
            🎯 Crafting your perfect syllabus...
        </p>
    </div>
    <style>
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>
    """, unsafe_allow_html=True)

def error_card(message):
    with stylable_container("error-card", css_styles="""
        {
            background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
            border-radius: 15px;
            padding: 20px;
            margin: 1rem 0;
            border-left: 5px solid #dc3545;
        }
    """):
        st.markdown(f"""
        <div style="display: flex; align-items: center;">
            <span style="font-size: 2rem; margin-right: 1rem;">❌</span>
            <div>
                <h4 style="color: #721c24; margin: 0;">Oops! Something went wrong</h4>
                <p style="color: #721c24; margin: 0.5rem 0 0 0;">{message}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

def warning_card(message):
    with stylable_container("warning-card", css_styles="""
        {
            background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
            border-radius: 15px;
            padding: 20px;
            margin: 1rem 0;
            border-left: 5px solid #ffc107;
        }
    """):
        st.markdown(f"""
        <div style="display: flex; align-items: center;">
            <span style="font-size: 2rem; margin-right: 1rem;">⚠️</span>
            <div>
                <h4 style="color: #856404; margin: 0;">Please Note</h4>
                <p style="color: #856404; margin: 0.5rem 0 0 0;">{message}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

def apply_global_styles():
    """Apply safe global CSS styles to the Streamlit app"""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3 {
        color: #2c3e50;
        font-weight: 600;
    }

    .stSelectbox select,
    .stTextInput input {
        border-radius: 15px;
        padding: 12px 15px;
        border: 2px solid #e1e8ed;
        background: white;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }

    .stButton > button {
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
    }

    .stDownloadButton > button {
        background: linear-gradient(45deg, #2196F3, #1976D2);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 25px;
        font-weight: 500;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        transform: translateY(-2px);
    }

    </style>
    """, unsafe_allow_html=True)

def show_title():
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="
            font-size: 3rem;
            background: linear-gradient(45deg, #2c3e50, #4CAF50);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        ">
            🎓 Course Syllabus Generator
        </h1>
        <p style="color: #7f8c8d; font-size: 1.2rem;">
            Create comprehensive course syllabi in minutes
        </p>
    </div>
    """, unsafe_allow_html=True)

def info_card():
    with stylable_container("info-card", css_styles="""
        {
            background: white;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        }
    """):
        st.markdown("""
        <h3 style="color: #4CAF50;">👋 Welcome!</h3>
        <p style="color: #333;">
            Select a subject and duration to automatically generate a detailed, structured course syllabus.
        </p>
        """, unsafe_allow_html=True)

def generate_card():
    clicked = card(
        title="✨ Generate Syllabus",
        text="Click to begin the syllabus generation process.",
        image="https://img.icons8.com/color/96/000000/book.png",
        styles={
            "card": {
                "width": "100%",
                "height": "200px",
                "border-radius": "20px",
                "box-shadow": "0 4px 15px rgba(0, 0, 0, 0.1)",
                "background": "linear-gradient(135deg, #4CAF50 0%, #45a049 100%)",
                "color": "white"
            }
        }
    )
    return clicked

def footer():
    st.markdown("""
    <hr>
    <div style="text-align: center; padding: 1rem; font-size: 0.9rem; color: #888;">
        Built by <b style="color: #4CAF50;">Divyanshu Pant</b> • Powered by Streamlit & LLMs
    </div>
    """, unsafe_allow_html=True)
