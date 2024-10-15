from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import sys
import os
from fastapi.responses import Response, FileResponse
from textSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/templates", StaticFiles(directory="templates"), name="templates")

text: str = "What is Text Summarization?"

@app.get("/docs", tags=["api documentation"])
async def custom_docs(request: Request):
    return templates.TemplateResponse("api_docs.html", {"request": request})

@app.get("/", tags=["authentication"])
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)