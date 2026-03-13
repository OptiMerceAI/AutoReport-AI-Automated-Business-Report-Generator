from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from app.routes import router

app = FastAPI(title="AutoReport AI")

# Mount static directories
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/reports", StaticFiles(directory="reports"), name="reports")

templates = Jinja2Templates(directory="templates")

# Include routes
app.include_router(router)

# Home page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})