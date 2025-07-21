# 🎓 Course Syllabus Generator

An AI-powered tool to generate detailed and structured course syllabi in minutes. Built using **Streamlit**, **OpenRouter**, and **LLMs**, this app helps educators automate the creation of subject-specific syllabi based on course inputs.

🌐 [Click here to try the app](https://course-syllabus-generator-4zy84q3degmpah6dwiqrgv.streamlit.app/#step-by-step-guide)

---

## 🚀 Features

- 🔍 Generate structured syllabi based on subject input
- 🧠 Powered by OpenRouter (LLMs like GPT-4, Claude, etc.)
- 💡 Clear, organized UI using `streamlit-extras`
- 📤 Deployable in 1 click via Streamlit Cloud

---

## 📦 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI Models**: OpenRouter (supports GPT, Claude, Mixtral, etc.)
- **UI Enhancements**: `streamlit-extras`

---

## 🛠️ Local Setup


1. Clone the Repo
git clone https://github.com/your-username/course-syllabus-generator.git
cd course-syllabus-generator


2. Create & Activate Virtual Environment:

   python -m venv venv

   venv\Scripts\activate

4. Install Dependencies
pip install -r requirements.txt

5. Add Your .env File
OPENROUTER_API_KEY=sk-or-your_openrouter_key_here

6. Run the app
streamlit run app.py
