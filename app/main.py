import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai

app = FastAPI()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class QuestionRequest(BaseModel):
    question: str
    image: str = None  # optional base64 image

@app.post("/api/")
async def answer_question(request: QuestionRequest):
    query = request.question

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful TDS TA"},
            {"role": "user", "content": query}
        ]
    )

    response_text = chat_completion.choices[0].message.content

    return {
        "answer": response_text,
        "links": []  # optional: fill if you add retrieval later
    }

