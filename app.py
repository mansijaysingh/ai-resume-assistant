import streamlit as st
from utils.resume_parser import extract_resume_text
from utils.jd_extractor import extract_job_description


st.set_page_config(page_title="AI Resume & Job Match Assistant")

st.title("📄 AI Resume & Job Match Assistant")
st.write("Upload your resume to get started.")


if "resume_text" not in st.session_state:
    st.session_state.resume_text=""

if "job_description" not in st.session_state:
   st.session_state.job_description= ""

uploaded_resume=st.file_uploader(
  "Upload Resume (PDF)",
  type=["pdf"]
)



if uploaded_resume:
  resume_text= extract_resume_text(uploaded_resume)
  st.session_state.resume_text=resume_text


  with st.expander("📄 View Extracted Resume Text"):
     st.text(st.session_state.resume_text)



st.subheader("💼 Job Description")

input_method= st.radio(
   "Choose Job Description Input Method",
   ["Text Input", "Screenshot Upload"],
   horizontal=True
)



if input_method == "Text Input":
  st.session_state.job_description  = st.text_area(
   "Paste Job Description Here",
   height=250,
   placeholder="Paste the complete job description..."
)


if not st.session_state.resume_text:
    st.warning("⚠️ Please upload your resume.")

elif not st.session_state.job_description:
    st.warning("⚠️ Please paste the job description.")

else: 
    
    uploaded_image = st.file_uploader(
       "Upload Job Description Screenshot",
        type=["png", "jpg", "jpeg"]
    )


    if uploaded_image:
       
       with st.spinner("Extracting Job Description..."):
          extracted_text= extract_job_description(uploaded_image)

       st.session_state.job_description = extracted_text