from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware  # Add this line

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Adjust this to allow specific HTTP methods
    allow_headers=["*"],  # Adjust this to allow specific headers
)

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "FastAPI Template Example"})

@app.get("/api/hello")
async def get_hello_api():
    return {"message": "Hello, API!"}
