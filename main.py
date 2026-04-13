print("Starting...")
import os
from gmail_service import get_gmail_service, get_emails
from ai_responder import setup_gemini, categorize_email, is_suspicious, summarize_email, generate_reply
from config import MAX_EMAILS_TO_FETCH

def main():
    # Setup
    print("🚀 AI Email Responder Starting...")
    
    # Get Gemini API Key
    api_key = input("Enter your Gemini API Key: ")
    
    # Initialize AI
    print("🤖 Setting up AI...")
    model = setup_gemini(api_key)
    
    # Connect to Gmail
    print("📧 Connecting to Gmail...")
    service = get_gmail_service()
    
    # Fetch emails
    print(f"📬 Fetching last {MAX_EMAILS_TO_FETCH} unread emails...")
    emails = get_emails(service, MAX_EMAILS_TO_FETCH)
    
    if not emails:
        print("✅ No unread emails found!")
        return
    
    print(f"\n📨 Found {len(emails)} unread emails\n")
    print("=" * 60)
    
    for i, email in enumerate(emails, 1):
        print(f"\n📧 Email {i}:")
        print(f"From: {email['sender']}")
        print(f"Subject: {email['subject']}")
        
        # Check if suspicious
        suspicious = is_suspicious(model, email['subject'], 
                                   email['sender'], email['body'])
        if suspicious:
            print("⚠️  STATUS: SUSPICIOUS EMAIL - Be careful!")
        
        # Categorize
        category = categorize_email(model, email['subject'],
                                    email['sender'], email['body'])
        print(f"📁 Category: {category}")
        
        # Summarize
        summary = summarize_email(model, email['subject'], email['body'])
        print(f"📝 Summary: {summary}")
        
        # Generate reply
        reply = generate_reply(model, email['subject'],
                               email['sender'], email['body'], category)
        print(f"\n💬 Suggested Reply:\n{reply}")
        print("=" * 60)
        time.sleep(15)

if __name__ == "__main__":
    main()