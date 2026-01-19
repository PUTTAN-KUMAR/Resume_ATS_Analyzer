# Resume ATS Score Analyzer (Upload Only)

A professional Streamlit web application that analyzes uploaded resumes (PDF/DOCX) against a **pre-defined job description** and calculates an **ATS (Applicant Tracking System) compatibility score** automatically.

---

## Features
- Upload Resume (PDF or DOCX) only — no need to paste Job Description.
- Automatic ATS score calculation based on a default job description.
- Detects **matched skills** and **missing skills** from the resume.
- Displays **keyword similarity score**.
- Visual **bar chart** showing skill match overview.
- Provides **suggestions for missing skills** to improve resume.

---

## Tech Stack
- Python
- Streamlit (Web UI)
- NLP (CountVectorizer)
- Regex
- PyPDF2 (PDF parsing)
- python-docx (DOCX parsing)
- Matplotlib (Charts)

---

##  How It Works
1. Upload your resume in PDF or DOCX format.
2. The system extracts text from the uploaded file.
3. Pre-defined job description (default JD) is used for comparison.
4. Skills are extracted from both resume and JD using regex.
5. ATS score is calculated based on the number of matched skills.
6. Missing skills and suggestions are displayed visually.

---

## Sample Workflow

1. Upload resume `autoCV.pdf`  
2. ATS Score calculated: **75%**  
3. Matched skills: `['python', 'sql', 'data analysis']`  
4. Missing skills: `['excel', 'power bi', 'machine learning']`  
5. Suggestions displayed to improve resume.

---

## Live Demo
*(Replace with your deployed Streamlit Cloud link)*  
[Resume ATS Analyzer Live](http://localhost:8501)

---

## How to Run Locally

1. Clone the repo:
```bash
git clone https:https://github.com/PUTTAN-KUMAR/Resume_ATS_Analyzer



## Create virtual environment

python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Mac/Linux

## Install dependencies
pip install -r requirements.txt


## Run Streamlit App:
streamlit run app.py

## Developer 
#Puttan kumar
B.Tech IT | Python Developer | Resume & ATS Automation Enthusiast

## Interview Questions from this Project
1️ Project Overview & Motivation

##Q1: Can you explain your project?

“I developed a Resume ATS Analyzer using Streamlit. The app allows users to upload their resume (PDF/DOCX) and automatically compares it against a default job description. It calculates ATS score, identifies matched and missing skills, provides keyword similarity, and suggests improvements.”

##Q2: Why did you choose this project?

“Many resumes are filtered out automatically by ATS in companies. This tool helps candidates understand their resume’s compatibility with ATS and improve it accordingly.”

# Technical Questions

##Q3: Which programming language and libraries did you use?

Python, with libraries: Streamlit, PyPDF2, python-docx, scikit-learn CountVectorizer, regex, Matplotlib.

##Q4: How do you extract skills from a resume?

“I maintain a predefined skill list and use regex to match keywords from the resume text to identify matched and missing skills.”

##Q5: How is ATS score calculated?

“ATS score = (Number of matched skills / Total skills in default JD) * 100.”

##Q6: How do you handle PDF/DOCX parsing?

“For PDFs, PyPDF2’s PdfReader is used; for DOCX, python-docx reads all paragraphs and combines them into text.”

##Q7: How do you calculate keyword similarity?

“I use scikit-learn’s CountVectorizer to vectorize text and calculate similarity using dot product.”

 #Streamlit & Web App

##Q8: Why did you choose Streamlit?

“Streamlit allows fast deployment of Python-based web apps without front-end coding, supports file upload, charts, and interactive UI.”

##Q9: How do you deploy this project?

“Deployed on Streamlit Cloud by connecting GitHub repo and selecting app.py. It provides a live URL shareable anywhere.”

##Q10: How does the progress bar work for ATS score?

“Streamlit’s st.progress takes 0-100 integer. ATS score is passed to show visual progress.”

##4️.Advanced / Conceptual Questions

##Q11: Can your app handle multiple resumes at once?

“Currently one at a time, but can be extended for batch-processing multiple resumes.”

##Q12: Can this app be enhanced for ML-based ATS prediction?

“Yes, using resume and JD datasets, we can train ML models to predict ATS score automatically.”

##Q13: How would you improve the project in the future?

Multiple resume upload & batch analysis

Weightage-based scoring for critical skills

Downloadable PDF report with ATS score summary

ML-based skill matching & ranking

User authentication for dashboard
