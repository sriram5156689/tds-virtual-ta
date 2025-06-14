# 🤖 TDS Virtual TA - IIT Madras Online Degree Project

This is a Virtual Teaching Assistant (TA) developed as part of the **Tools in Data Science (TDS)** course for the **IIT Madras BSc/MSc Data Science Online Degree**. The TA is capable of answering student questions based on:

- **TDS Course content (Jan 2025 batch as of 15 Apr 2025)**
- **TDS Discourse forum posts (from 1 Jan 2025 to 14 Apr 2025)**

The app exposes an API endpoint that takes student questions (and optional image attachments) and responds with an intelligent answer and relevant links.

---

## 🚀 Features

- Accepts plain text questions and optional base64-encoded screenshots
- Extracts text from images using OCR
- Searches relevant course content and Discourse posts
- Uses OpenAI GPT (or other LLMs) for question answering
- Returns an answer and helpful Discourse post links
- Response within 30 seconds
- Publicly deployed API endpoint

---

## 📦 API Endpoint

**POST** `/api/`  
Example: `https://your-deployed-url/api/`

### Request Format

```json
{
  "question": "Should I use gpt-4o-mini or gpt-3.5-turbo?",
  "image": "BASE64_ENCODED_IMAGE_STRING (optional)"
}
