from fastapi import FastAPI 
from pydantic import BaseModel 
from utils.ocr import extract_text_from_base64 
import openai, os 
 
openai.api_key = os.getenv("OPENAI_API_KEY") 
 
class QuestionRequest(BaseModel): 
    question: str 
    image: str = None 
 
app = FastAPI() 
 
@app.post("/api/") 
async def answer_question(data: QuestionRequest): 
    query = data.question 
    if data.image: 
        query += "\nImage OCR: " + extract_text_from_base64(data.image) 
    completion = openai.ChatCompletion.create( 
        model="gpt-3.5-turbo-0125", 
        messages=[{"role": "system", "content": "You are a helpful TDS TA"}, {"role": "user", "content": query}] 
    ) 
    answer = completion.choices[0].message.content.strip() 
    return { 
        "answer": answer, 
        "links": [ 
            {"url": "https://discourse.onlinedegree.iitm.ac.in/t/example/123", "text": "Example link"} 
        ] 
    } 
