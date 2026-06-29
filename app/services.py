import google.generativeai as genai
from app.config import settings

class GeminiService:
    def __init__(self):
        if not settings.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set in environment variables")
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(settings.GEMINI_MODEL)

    def summarize(self, text: str) -> str:
        prompt = f"Summarize the following text into 2-3 sentences:\n\n{text}"
        response = self.model.generate_content(prompt)
        return response.text.strip()

    def translate(self, text: str) -> str:
        prompt = f"Translate the following text into Spanish. Return only the translated text, with no extra explanation or conversational filler:\n\n{text}"
        response = self.model.generate_content(prompt)
        return response.text.strip()

    def generate_email(self, text: str) -> str:
        prompt = f"Generate a professional email based on the following notes. Return only the email body, with no extra explanation or conversational filler:\n\n{text}"
        response = self.model.generate_content(prompt)
        return response.text.strip()
