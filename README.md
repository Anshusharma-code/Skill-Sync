# SkillSync

SkillSync is an AI-powered web application that analyzes job descriptions and generates a personalized learning path based on the required skills. It helps users identify key skills from job postings and suggests curated resources and projects to bridge skill gaps.

---

## Features

-  Extracts technical skills from job descriptions using **Google Gemini AI**
-  Generates a structured learning roadmap
-  Matches skills with a predefined learning database
-  Estimates learning hours for each skill
-  Suggests resources and mini-projects for practice
- Simple and interactive Flask-based web interface

---

##  Tech Stack

- **Frontend:** HTML, CSS (Jinja Templates)
- **Backend:** Flask (Python)
- **AI Model:** Google Generative AI (Gemini)
- **Data Handling:** JSON (skills database)
- **Environment Management:** python-dotenv

---

##  Project Structure
SkillSync/
│── app.py
│── skills_db.json
│── templates/
│ ├── index.html
│ └── results.html
│── .env
│── requirements.txt

---

##  Installation & Setup

### 1. Clone the repository

git clone https://github.com/your-username/skillsync.git
cd skillsync

Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
Install dependencies
pip install -r requirements.txt
Add API Key
Create a .env file and add your Gemini API key:
GEMINI_API_KEY=your_api_key_here

Run the Project
python app.py

 Author
Anshu
B.Tech Student | AI/ML Enthusiast | Python Developer
