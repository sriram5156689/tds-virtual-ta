from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import openai
import os

# Use Groq setup instead of OpenAI
client = openai.OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

app = FastAPI()

# Optional: Static & Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "result": ""})

@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, question: str = Form(...)):
    chat_completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",  # or your chosen Groq model
        messages=[
            {"role": "system", "content": "You are a helpful teaching assistant."},
            {"role": "user", "content": question}
        ]
    )
    result = chat_completion.choices[0].message.content
    return templates.TemplateResponse("form.html", {"request": request, "result": result, "question": question})
