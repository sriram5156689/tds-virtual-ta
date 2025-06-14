import os
import openai
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Groq client
client = openai.OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",  # 👈 Groq's base URL
)

@app.post("/api/")
async def answer_question(request: Request):
    data = await request.json()
    query = data.get("query", "")

    chat_completion = client.chat.completions.create(
        model="llama3-70b-8192",  # ✅ Groq supports llama3, mixtral, gemma
        messages=[
            {"role": "system", "content": "You are a helpful TDS TA."},
            {"role": "user", "content": query}
        ]
    )

    response_text = chat_completion.choices[0].message.content
    return {"response": response_text}
