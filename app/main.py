from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import uvicorn
from .model import GarbageClassifier
from .utils import validate_image
import time

app = FastAPI(title="Garbage Classification API")

# Setup static files and templates
# Mount the static directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize model
model = None

@app.on_event("startup")
async def startup_event():
    global model
    model = GarbageClassifier()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Validate file
    file_ext = os.path.splitext(file.filename)[1]
    contents = await file.read()
    
    # Validate the image size and format
    validate_image(len(contents), file_ext)
    
    # Make prediction
    try:
        result = model.predict(contents)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": time.time()}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)