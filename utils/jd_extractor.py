import base64
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()



client= OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def encode_image(image_file):

   """
    Convert uploaded image into Base64 string.
   """

   return base64.b64encode(image_file.read()).decode("utf-8")


def extract_job_description(image_file):
   
    """
    Extract job description from uploaded image using GPT-4o Vision.
    """

    base64_image= encode_image(image_file)


    response= client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role" :"user",
                "content": [
                    {
                         "type": "input_text",
                    "text": """
Extract only the complete job description from this image.

Rules:
- Return only the job description.
- Do not add explanations.
- Preserve formatting as much as possible.
- If the image does not contain a job description, return:
"No job description found."
"""
                    },

                    {
                        "type": "input_image",
                    "image_url": f"data:image/png;base64,{base64_image}",
                    },
                ],
            }
        ],
    )

    return response.output_text