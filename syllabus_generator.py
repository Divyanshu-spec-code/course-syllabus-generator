import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # To load your Gemini API key from .env file

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini Pro model
model = genai.GenerativeModel('gemini-pro')

def generate_syllabus(course_name, duration, level, custom_goals=None):
    prompt = f"""
You are an expert education planner.

Generate a weekly course syllabus for the following:
- Title: {course_name}
- Duration: {duration} weeks
- Student Level: {level}
{f"- Include these topics or goals: {custom_goals}" if custom_goals else ""}

Include:
1. Weekly topic breakdown (Week 1 to Week {duration})
2. Learning objectives per week
3. One assignment idea per week

Return the output in clear markdown format.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating syllabus: {str(e)}"
