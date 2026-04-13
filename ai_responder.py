import time
from google import genai
from config import GEMINI_MODEL, EMAIL_CATEGORIES

def setup_gemini(api_key):
    client = genai.Client(api_key=api_key)
    return client

def call_gemini(client, prompt, retries=3):
    for i in range(retries):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            if i < retries - 1:
                print(f"⏳ Retrying... ({i+1}/{retries})")
                time.sleep(5)
            else:
                raise e

def categorize_email(client, subject, sender, body):
    prompt = f"""
    Analyze this email and categorize it:
    From: {sender}
    Subject: {subject}
    Body: {body}
    Categories: {', '.join(EMAIL_CATEGORIES)}
    Reply with ONLY the category name, nothing else.
    """
    category = call_gemini(client, prompt)
    if category not in EMAIL_CATEGORIES:
        category = "Important"
    return category

def is_suspicious(client, subject, sender, body):
    prompt = f"""
    Analyze this email for suspicious/spam/phishing indicators:
    From: {sender}
    Subject: {subject}
    Body: {body}
    Reply with ONLY 'YES' if suspicious or 'NO' if legitimate.
    """
    return call_gemini(client, prompt).upper() == 'YES'

def summarize_email(client, subject, body):
    prompt = f"""
    Summarize this email in 2-3 sentences:
    Subject: {subject}
    Body: {body}
    """
    return call_gemini(client, prompt)

def generate_reply(client, subject, sender, body, category):
    prompt = f"""
    Write a professional email reply for this {category} email:
    From: {sender}
    Subject: {subject}
    Body: {body}
    Write a concise, helpful and professional reply.
    Do not include subject line, just the body of the reply.
    """
    return call_gemini(client, prompt)