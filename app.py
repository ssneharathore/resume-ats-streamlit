from dotenv import load_dotenv
load_dotenv()

import base64
import streamlit as st
import os
import io
from PIL import Image
import fitz  # PyMuPDF
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate Gemini response
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# Function to convert PDF first page to image using PyMuPDF
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = []
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        page = pdf_document.load_page(0)  # first page
        pix = page.get_pixmap()
        img_bytes = pix.tobytes("png")

        pdf_parts = [
            {
                "mime_type": "image/png",
                "data": base64.b64encode(img_bytes).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App UI
st.set_page_config(page_title="ATS Resume Expert")
st.header("📄 ATS Resume Evaluation System")

input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.success("✅ PDF Uploaded Successfully")

# Buttons
submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("How Can I Improvise my Skills")
submit3 = st.button("Percentage Match")
submit4 = st.button("Q&A Chat for Resume")

# Prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager with tech experience in the field of any one job role from Web development, Data Science, Data Analyst, Full Stack Developer, Senior Java Developer, Big Data Engineering, or DEVOPS. Your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an experienced Technical Human Resource Manager with tech experience in the field of any one job role from Web development, Data Science, Data Analyst, Full Stack Developer, Senior Java Developer, Big Data Engineering, or DEVOPS. Your task is to review the provided resume against the job description.
Please share your professional evaluation on improvising the skills for a better fit and how deep to be developed. How can I improve my skills?
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. Your task is to evaluate the resume against the provided job description. 
Give me the percentage of match if the resume matches the job description. 
First, the output should come as percentage, then keywords missing, and finally final thoughts.
"""

input_prompt4 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. Your task is to evaluate the resume against the provided job description and do Chat-based Q&A for resumes.
"""

# Button Logic
if submit1:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("🧾 Resume Evaluation:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload the resume")

elif submit2:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("🎯 Skill Improvement Suggestions:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload the resume")

elif submit3:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("📊 ATS Match Percentage:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload the resume")

elif submit4:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4, pdf_content, input_text)
        st.subheader("💬 Resume Q&A:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload the resume")
