from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
load_dotenv()  
app = Flask(__name__)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY=your_actual_key_here")
genai.configure(api_key=GEMINI_API_KEY)
with open('skills_db.json', 'r') as f:
    SKILLS_DB = json.load(f)
def extract_skills(job_description):
    """Use Gemini AI to extract skills from job description"""
    prompt = f"""
    Analyze this job description and extract ONLY the technical skills mentioned.
    Return them as a comma-separated list of keywords.
    Focus on: programming languages, frameworks, tools, platforms.
    Example format: python, react, sql, aws
    
    Job Description:
    {job_description}
    
    Extracted Skills:
    """
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        skills_text = response.text.strip().lower()
        skills_list = [skill.strip() for skill in skills_text.split(',')]
        return skills_list[:5]
    except Exception as e:
        print(f"AI extraction error: {e}")
        return ["python", "javascripyt"]
def create_learning_path(skills_list):
    """Match extracted skills with database to create learning path"""
    learning_path = []
    total_hours = 0
    for skill in skills_list:
        for db_skill, details in SKILLS_DB.items():
            if db_skill in skill or skill in db_skill:
                learning_path.append({
                    "skill": db_skill.capitalize(),
                    "resource": details["resource"],
                    "url": details["url"],
                    "project": details["project"],
                    "hours": details["hours"]
                })
                total_hours += details["hours"]
                break
    
    return learning_path, total_hours

@app.route('/')
def index():
    """Render the input form page"""
    return render_template('index.html')
@app.route('/analyze', methods=['POST'])
def analyze():
    """Process the job description and return results"""
    job_description = request.form.get('job_description', '')
    
    if not job_description.strip():
        return render_template('index.html', error="Please enter a job description")
    
    
    extracted_skills = extract_skills(job_description)
    

    learning_path, total_hours = create_learning_path(extracted_skills)
    
    
    return render_template('results.html', 
                         skills=extracted_skills,
                         learning_path=learning_path,
                         total_hours=total_hours,
                         job_description=job_description[:100] + "..." if len(job_description) > 100 else job_description)

if __name__ == '__main__':
    app.run(debug=True)