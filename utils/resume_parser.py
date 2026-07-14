import pdfplumber


def extract_resume_text(pdf_file):
   
   """
   Extract text from uploaded resume PDF.
   """

   text= ""

   with pdfplumber.open(pdf_file) as pdf:
      
      for page in pdf.pages:
         page_text= page.extract_text()

         if page_text:
    
            text += page_text + "\n"
   
   
   return text