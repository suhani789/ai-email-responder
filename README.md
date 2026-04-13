# 🤖 AI Email Responder

> *"I was missing placement drive emails in my email inbox. So I built an AI to make sure that never happens again."*

An intelligent email assistant that connects to your Gmail, reads unread emails, and uses **Google Gemini AI** to automatically categorize, analyze, detect suspicious emails, and generate smart replies — all in one run.

---

## 😤 The Problem

As a college student, I kept missing important **placement drive emails** buried under newsletters, LinkedIn notifications, and spam. Notifications were inconsistent, and by the time I saw the email — it was too late.

So I built this.

---

## ✨ Features

| Feature | What it does |
|---|---|
| 📧 **Auto Email Fetch** | Reads your unread Gmail emails automatically |
| 📁 **Smart Categorization** | Labels emails as Work, Personal, Spam, Urgent, **Placement Drive** etc. |
| ⚠️ **Suspicious Detection** | Catches phishing & scam emails before you open them |
| 📝 **AI Summarization** | Converts long emails into 2-3 line summaries |
| 💬 **Auto Reply Generation** | Generates professional replies instantly |

---

## 🛠️ Tech Stack

- **Python 3.12**
- **Gmail API** + OAuth 2.0
- **Google Gemini AI** (gemini-2.5-flash)
- **Google Cloud Console**

---

## 🚀 Run It Yourself

```bash
# Clone the repo
git clone https://github.com/suhani789/ai-email-responder.git
cd ai-email-responder

# Install dependencies
pip install -r requirements.txt

# Add your credentials.json from Google Cloud Console
# (See setup instructions below)

# Run!
python main.py
```

### Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Enable Gmail API
3. Create OAuth credentials → Download as `credentials.json`
4. Get Gemini API key from [Google AI Studio](https://aistudio.google.com)
5. Run `python main.py` and enter your API key

---

## 🔮 Future Scope

- 🔔 Desktop notifications for Placement Drive emails
- 📱 WhatsApp/SMS alerts for urgent emails
- 📅 Auto Google Calendar entries for interview schedules
- 🌐 Web dashboard to view email analysis

---

## 🔐 Security

- API keys are never hardcoded in code
- Gmail credentials stored locally only
- Sensitive files excluded via `.gitignore`

---

## 👩‍💻 About Me

Hi! I'm **Suhani Saxena**, a developer who loves building practical AI tools that solve real problems.

🔗 [GitHub](https://github.com/suhani789) | [LinkedIn](https://www.linkedin.com/in/suhani-saxena-a04045319)
