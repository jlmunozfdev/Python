import PyPDF2 #pip install pypdf2
from gtts import gTTS # pip install gtts  
import os

def pdf_to_audio(pdf_path, audio_path, language='en', speed=1.0):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Initialize an empty string to store the text
            text = ''

            # Extract text from each page
            for page in pdf_reader.pages:
                text += page.extract_text()

            # Create a gTTS object with specified language and speed
            tts = gTTS(text, lang=language, slow=False)
            tts.speed = speed

            # Save the audio to a file
            tts.save(audio_path)

        print("PDF converted to audio successfully!")
    except Exception as e:
        print("Error: ", e)

# Example usage
pdf_path = 'example.pdf'
audio_path = 'output.mp3'
language = 'es'  # Language code (e.g., 'es' for Spanish, 'en' for English)
speed = 1.0  # Speech speed (1.0 is normal speed)
pdf_to_audio(pdf_path, audio_path, language, speed)