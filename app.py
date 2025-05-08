import streamlit as st
from resume_parser import parse_resume
from analyzer import analyze_resume
from utils import get_job_keywords, suggest_improvements

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("📄 AI Resume Analyzer & Improvement Tool")

uploaded_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])

job_role = st.selectbox("Select Job Role", ["Software Engineer", "Machine Learning Engineer", "Mechanical Engineer", "Web Developer"])

if uploaded_file is not None:
    with st.spinner("Parsing resume..."):
        resume_text = parse_resume(uploaded_file)
        st.subheader("Extracted Resume Text:")
        st.write(resume_text[:1500] + "..." if len(resume_text) > 1500 else resume_text)

        st.subheader("Analysis Results")
        keywords = get_job_keywords(job_role)
        score, found_keywords = analyze_resume(resume_text, keywords)

        st.success(f"Match Score for {job_role}: {score}%")
        st.write(f"Keywords Found: {', '.join(found_keywords)}")

        improvements = suggest_improvements(resume_text, keywords, found_keywords)
        if improvements:
            st.warning("Suggested Improvements:")
            for tip in improvements:
                st.write(f"- {tip}")
        else:
            st.success("Your resume looks great for this role!")
