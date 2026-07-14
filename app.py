import streamlit as st
from utils.resume_parser import extract_resume_text


st.set_page_config(page_title="AI Resume & Job Match Assistant")

st.title("📄 AI Resume & Job Match Assistant")
st.write("Upload your resume to get started.")


if "resume_text" not in st.session_state:
    st.session_state.resume_text=""


uploaded_resume=st.file_uploader(
  "Upload Resume (PDF)",
  type=["pdf"]
)



if uploaded_resume:
  resume_text= extract_resume_text(uploaded_resume)
  st.session_state.resume_text=resume_text


  with st.expander("📄 View Extracted Resume Text"):
     st.text(st.session_state.resume_text)