# Gmail API Configuration
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.modify'
]

# Gemini AI Configuration
GEMINI_MODEL = "gemini-2.5-flash"

# Email Settings
MAX_EMAILS_TO_FETCH = 10
AUTO_REPLY_LABEL = "AI-Replied"

# Categories
EMAIL_CATEGORIES = [
    "Important",
    "Spam",
    "Newsletter", 
    "Work",
    "Personal",
    "Urgent"
]