import streamlit as st
import re
from skills import SKILLS
from PyPDF2 import PdfReader
from docx import Document
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Resume ATS Analyzer",
    page_icon="",
    layout="centered"
)

st.title("Resume ATS Score Analyzer")
st.caption("Upload your Resume (PDF/DOCX) to check ATS compatibility automatically")

# ---------------- FUNCTIONS ----------------
def read_pdf(file):
    reader = PdfReader(file)
    return " ".join(page.extract_text() or "" for page in reader.pages).lower()

def read_docx(file):
    doc = Document(file)
    return " ".join(p.text for p in doc.paragraphs).lower()

def extract_skills(text):
    found = []
    for skill in SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found.append(skill)
    return found

# ---------------- DEFAULT JOB DESCRIPTION ----------------
DEFAULT_JD = """
We are looking for a candidate with strong Python, SQL, Excel, Power BI, 
Tableau, Data Analysis, Machine Learning, Pandas, Numpy, and communication skills.
"""

# ---------------- INPUT ----------------
st.markdown("Upload Resume (PDF / DOCX)")
uploaded_resume = st.file_uploader("", ["pdf", "docx"])

# ---------------- ANALYSIS ----------------
if st.button("Analyze Resume"):
    if uploaded_resume is not None:
        # Read resume
        if uploaded_resume.name.endswith(".pdf"):
            resume_text = read_pdf(uploaded_resume)
        else:
            resume_text = read_docx(uploaded_resume)

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(DEFAULT_JD.lower())

        matched = list(set(resume_skills) & set(jd_skills))
        missing = list(set(jd_skills) - set(resume_skills))

        ats_score = round((len(matched)/len(jd_skills))*100,2) if jd_skills else 0

        # Keyword similarity
        vectorizer = CountVectorizer()
        vectors = vectorizer.fit_transform([resume_text, DEFAULT_JD])
        similarity = (vectors * vectors.T).toarray()[0][1]

        # ---------------- RESULTS ----------------
        st.subheader("ATS Analysis Result")
        st.metric("ATS Score", f"{ats_score}%")
        st.progress(min(int(ats_score), 100))
        st.metric("Keyword Similarity", similarity)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Matched Skills")
            st.write(matched if matched else "No matched skills")

        with col2:
            st.subheader("Missing Skills")
            st.write(missing if missing else "No missing skills")

        # Skill match chart
        fig, ax = plt.subplots()
        ax.bar(["Matched", "Missing"], [len(matched), len(missing)], color=["green","red"])
        st.subheader("Skill Match Overview")
        st.pyplot(fig)

        # Suggestions
        if missing:
            st.warning("Suggested Skills to Add:")
            st.write(", ".join(missing))
    else:
        st.error("Please upload your resume")
