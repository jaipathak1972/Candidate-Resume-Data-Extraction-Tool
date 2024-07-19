from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
import pdf2image
import google.generativeai as genai
import requests

# Load environment variables
load_dotenv()

# Configure the Google Generative AI
api_key = os.getenv("API_KEY")
if not api_key:
    st.error("API key is missing. Please check your .env file.")
    print("API key not found")
else:
    genai.configure(api_key=api_key)
    print("API key loaded")

def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    
    try:
        response = model.generate_content([input_text, pdf_content[0], prompt])
        return response.text
    except Exception as e:
        st.error(f"Error during API request: {e}")
        print(f"Error during API request: {e}")
        return "Error"

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        try:
            images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=r"C:\Users\Dell\OneDrive\Desktop\poppler-24.02.0\Library\bin")
        except Exception as e:
            st.error(f"Error converting PDF to images: {e}")
            return None

        # Get the first page
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        st.error("No file uploaded")
        return None

# Streamlit App
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit4 = st.button("Extract Name")
submit5 = st.button("Extract Location")
submit6 = st.button("Extract Experience")

input_prompt1 = """You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. Your task is to extract all TECHNICAL SKILLS from the provided resume. 
List the top 10 to 30 skills mentioned in the resume. Only technical skills remember that and try to give minimum 
"""

input_prompt4 = """You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of 
data science and ATS functionality. Extract NAME of the candidate from the resume.
"""
input_prompt5 = """You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of
data science and ATS functionality. Extract Address of the candidate from the resume.
"""
input_prompt6 = """Extract EXPERIENCE of the candidate from the resume total time period candidate worked in numarical value like 3 month 6 month 1 year and so on.
"""

Resume_Data = {}

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content is not None:
            response = get_gemini_response(input_text, pdf_content, input_prompt1)
            st.subheader("The Response is")
            st.write(response)
            Resume_Data["Skills"] = response
    else:
        st.write("Please upload the resume")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content is not None:
            response = get_gemini_response(input_text, pdf_content, input_prompt4)
            st.subheader("The Response is")
            st.write(response)
            Resume_Data["Name"] = response
    else:
        st.write("Please upload the resume")

elif submit5:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content is not None:
            response = get_gemini_response(input_text, pdf_content, input_prompt5)
            st.subheader("The Response is")
            st.write(response)
            Resume_Data["Location"] = response
    else:
        st.write("Please upload the resume")

elif submit6:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content is not None:
            response = get_gemini_response(input_text, pdf_content, input_prompt6)
            st.subheader("The Response is")
            st.write(response)
            Resume_Data["Experience"] = response
    else:
        st.write("Please upload the resume")
