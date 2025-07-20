
# 📝 ATS Tracking System

An AI-powered Resume Analyzer built using **Streamlit** and **Google Gemini API**. This tool helps job seekers evaluate their resumes against specific job descriptions.

##APP LINK###
https://resume-ats-app-snehaaaa.streamlit.app/

## 🌟 Features

✅ Upload resume (PDF)  
✅ Paste job description text  
✅ AI-generated insights on:  
- Resume summary  
- Skill improvisation  
- Percentage match with the job description  

## 📸 Demo Screenshot

![App Screenshot](ats_screenshot.png<img width="778" height="598" alt="ats_screenshot" src="https://github.com/user-attachments/assets/4241d1b7-4216-4158-b651-b1ed299c13b4" />)

## 🛠 Tech Stack

- Python 🐍  
- Streamlit 🎈  
- Google Gemini API (via `google.generativeai`)  
- `pdf2image`, `PyMuPDF`, `Pillow` for PDF parsing

## 🚀 How to Run Locally

```bash
git clone https://github.com/ssneharathore/resume-ats-streamlit.git
cd resume-ats-streamlit
pip install -r requirements.txt
streamlit run app.py
```

## 📂 File Structure

```
resume-ats-streamlit/
├── app.py                   # Main Streamlit app
├── requirements.txt         # Python dependencies
├── README.md                # Project overview
├── assets/
│   └── demo.png             # App UI screenshot
├── resume_samples/
│   └── SnehaRathoreResume.pdf  # Sample resume (optional)
```

> Made with ❤️ by Sneha Rathore | [LinkedIn](https://linkedin.com/in/sneha-rathore)
