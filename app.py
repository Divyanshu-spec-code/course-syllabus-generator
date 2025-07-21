import os
import streamlit as st
import requests
from dotenv import load_dotenv

def main():
    OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

    if not OPENROUTER_API_KEY:
        st.error("API Key not found. Please set OPENROUTER_API_KEY in Streamlit secrets.")
        return
# Import UI enhancement functions
from ui_enhancer import (
    apply_global_styles,
    show_title,
    info_card,
    create_input_container,
    success_card,
    create_syllabus_container,
    create_feature_cards,
    loading_animation,
    error_card,
    warning_card,
    footer
)

# Load API key from .env
load_dotenv()
api_key = st.secrets["OPENROUTER_API_KEY"]

def generate_syllabus(subject, duration):
    """
    Generate syllabus using OpenRouter API
    
    Args:
        subject (str): The subject for the syllabus
        duration (str): The duration of the course
    
    Returns:
        tuple: (success: bool, content: str, error_message: str)
    """
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:8501",
                "X-Title": "Course Syllabus Generator"
            },
            json={
                "model": "openai/gpt-3.5-turbo",

                "messages": [
                    {
                        "role": "system", 
                        "content": "You are an experienced university professor who designs comprehensive, structured course syllabi. Create detailed week-by-week breakdowns with clear learning objectives, topics, and outcomes."
                    },
                    {
                        "role": "user", 
                        "content": f"""Generate a detailed {duration} syllabus for the subject '{subject}'. 

Please format the response EXACTLY as follows:

# {subject} - {duration} Course Syllabus

## Course Overview
[Brief description of the course and what students will learn]

## Course Objectives
- [Objective 1]
- [Objective 2]
- [Objective 3]

## Learning Outcomes
By the end of this course, students will be able to:
- [Outcome 1]
- [Outcome 2]
- [Outcome 3]

## Weekly Breakdown

### Week 1: [Topic Name]
**Learning Objectives:**
- [Objective 1]
- [Objective 2]

**Topics Covered:**
- [Topic 1]
- [Topic 2]
- [Topic 3]

**Activities:**
- [Activity 1]
- [Activity 2]

**Assessment:** [Brief description]

---

[Continue this format for each week]

## Assessment Methods
- **Assignments:** [Percentage]% - [Description]
- **Midterm Exam:** [Percentage]% - [Description]  
- **Final Project:** [Percentage]% - [Description]
- **Participation:** [Percentage]% - [Description]

## Required Materials
- [Material 1]
- [Material 2]
- [Material 3]

## Recommended Resources
- [Resource 1]
- [Resource 2]
- [Resource 3]

## Course Policies
- **Attendance:** [Policy]
- **Late Submissions:** [Policy]
- **Academic Integrity:** [Policy]

Make sure to use this exact formatting with proper markdown headers, bullet points, and clear section divisions."""
                    }
                ],
                "max_tokens": 2000,
                "temperature": 0.7
            }
        )
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            
            if "choices" in data and len(data["choices"]) > 0:
                syllabus = data["choices"][0]["message"]["content"]
                return True, syllabus, ""
            else:
                return False, "", "No syllabus content received from the API"
        else:
            return False, "", f"API request failed with status code: {response.status_code}"
            
    except requests.exceptions.RequestException as e:
        return False, "", f"Network error: {str(e)}"
    except KeyError as e:
        return False, "", f"Unexpected API response format: {str(e)}"
    except Exception as e:
        return False, "", f"Unexpected error: {str(e)}"

def get_subject_options():
    """Return list of available subject options"""
    return [
        "Select a subject...",
        "Data Structures and Algorithms", 
        "Artificial Intelligence",
        "Machine Learning",
        "Python Programming",
        "Web Development",
        "Database Management Systems",
        "Computer Networks",
        "Operating Systems",
        "Software Engineering",
        "Project Management",
        "Mathematics",
        "Statistics",
        "Physics",
        "Chemistry",
        "Business Administration",
        "Marketing",
        "Finance",
        "Custom (enter below)"
    ]

def initialize_session_state():
    """Initialize session state variables"""
    if 'generated_syllabus' not in st.session_state:
        st.session_state.generated_syllabus = ""
    if 'last_subject' not in st.session_state:
        st.session_state.last_subject = ""
    if 'last_duration' not in st.session_state:
        st.session_state.last_duration = ""

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # Apply global styles
    apply_global_styles()
    
    # Streamlit UI setup
    st.set_page_config(
        page_title="Course Syllabus Generator",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Show enhanced title
    show_title()
    
    # Input validation for API key
    if not OPENROUTER_API_KEY:
        error_card("Please set your OPENROUTER_API_KEY in the .env file")
        st.stop()
    
    # Show info card
    info_card()
    
    # Create feature cards
    create_feature_cards()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Create columns for better layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Input fields with enhanced styling
        with create_input_container():
            st.markdown("### 📚 Course Details")
            
            subject_options = get_subject_options()
            
            subject_dropdown = st.selectbox(
                "Choose a subject:",
                subject_options,
                help="Select from predefined subjects or choose 'Custom' to enter your own"
            )
            
            # Custom subject input (only show if "Custom" is selected)
            if subject_dropdown == "Custom (enter below)":
                subject = st.text_input(
                    "Enter your custom subject name:",
                    placeholder="e.g., Advanced Quantum Computing",
                    help="Enter a specific subject name for your course"
                )
            else:
                subject = subject_dropdown if subject_dropdown != "Select a subject..." else ""
            
            duration = st.selectbox(
                "Course Duration",
                ["4 Weeks", "6 Weeks", "8 Weeks", "12 Weeks","14 Weeks"],
                help="Select the total duration of your course"
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Center the generate button
            col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
            with col_btn2:
                generate_clicked = st.button(
                    "🚀 Generate Syllabus", 
                    use_container_width=True,
                    help="Click to generate your customized syllabus"
                )
    
    # Generation logic
    if generate_clicked and subject:
        # Show custom loading animation
        loading_placeholder = st.empty()
        with loading_placeholder:
            loading_animation()
        
        # Generate syllabus
        success, syllabus_content, error_message = generate_syllabus(subject, duration)
        
        # Clear loading animation
        loading_placeholder.empty()
        
        if success:
            # Store in session state
            st.session_state.generated_syllabus = syllabus_content
            st.session_state.last_subject = subject
            st.session_state.last_duration = duration
            
            # Show success message
            success_card(subject, duration)
            
            # Display the syllabus in a styled container
            with create_syllabus_container():
                st.markdown("### 📚 Your Generated Syllabus")
                st.markdown(syllabus_content)
            
            # Add download option
            col_dl1, col_dl2, col_dl3 = st.columns([1, 1, 1])
            with col_dl2:
                st.download_button(
                    label="📥 Download Syllabus",
                    data=syllabus_content,
                    file_name=f"{subject.replace(' ', '_').replace('/', '_')}_syllabus.txt",
                    mime="text/plain",
                    use_container_width=True,
                    help="Download your syllabus as a text file"
                )
        else:
            error_card(error_message)
            
    elif generate_clicked and not subject:
        warning_card("Please select or enter a subject before generating the syllabus.")
    
    # Display previously generated syllabus if exists
    elif st.session_state.generated_syllabus and not generate_clicked:
        st.markdown("### 📚 Previously Generated Syllabus")
        
        # Show info about the previous generation
        st.info(f"📖 Last generated: **{st.session_state.last_subject}** ({st.session_state.last_duration})")
        
        with create_syllabus_container():
            st.markdown(st.session_state.generated_syllabus)
        
        # Add download option for previous syllabus
        col_dl1, col_dl2, col_dl3 = st.columns([1, 1, 1])
        with col_dl2:
            st.download_button(
                label="📥 Download Previous Syllabus",
                data=st.session_state.generated_syllabus,
                file_name=f"{st.session_state.last_subject.replace(' ', '_').replace('/', '_')}_syllabus.txt",
                mime="text/plain",
                use_container_width=True
            )

    # Add helpful information
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    with st.expander("ℹ️ How to Use This Tool", expanded=False):
        st.markdown("""
        ### Step-by-Step Guide:
        
        1. **📚 Select Subject**: Choose from our predefined subjects or select "Custom" to enter your own
        
        2. **⏰ Choose Duration**: Pick how many weeks your course should run (4, 6, 8, or 12 weeks)
        
        3. **🚀 Generate**: Click the "Generate Syllabus" button to create your customized syllabus
        
        4. **📥 Download**: Once generated, use the download button to save your syllabus as a text file
        
        ### ✨ Features:
        - **AI-Powered Generation**: Advanced AI creates detailed, structured syllabi
        - **Week-by-Week Breakdown**: Complete course structure with learning objectives
        - **Comprehensive Content**: Includes assessments, resources, and policies
        - **Multiple Formats**: Downloadable text format for easy sharing
        - **Session Memory**: Your last generated syllabus is saved during the session
        
        ### 📋 What's Included:
        - Course overview and objectives
        - Detailed weekly topics and learning objectives
        - Assessment methods and grading breakdown
        - Required materials and recommended resources
        - Course policies and guidelines
        
        ### 💡 Tips:
        - Be specific with custom subject names for better results
        - Choose appropriate duration based on content complexity
        - Review and customize the generated syllabus as needed
        """)
    
    # Additional resources
    with st.expander("📖 Additional Resources", expanded=False):
        st.markdown("""
        ### Useful Links for Educators:
        - [Bloom's Taxonomy for Learning Objectives](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/)
        - [Course Design Best Practices](https://www.edutopia.org/topic/course-design)
        - [Assessment Strategies](https://www.edutopia.org/topic/assessment)
        - [Syllabus Templates](https://www.google.com/search?q=university+syllabus+templates)
        
        ### 🎯 Subject-Specific Resources:
        - **STEM Subjects**: Include lab work, problem sets, and practical applications
        - **Liberal Arts**: Focus on critical thinking, writing, and discussion
        - **Business**: Incorporate case studies and real-world applications
        - **Technical**: Add hands-on projects and industry connections
        """)

    # Footer
    footer()

if __name__ == "__main__":
    main()
