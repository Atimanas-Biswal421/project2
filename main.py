import json
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Load student data from JSON file
with open("q-vercel-python.json", "r") as file:
    students = json.load(file)
    student_dict = {s["name"]: s["marks"] for s in students}

@app.get("/api")
def get_marks(name: List[str]):
    marks = [student_dict.get(n, None) for n in name]
    return {"marks": marks}

# Vercel entry point
def handler(request, *args, **kwargs):
    return app(request, *args, **kwargs)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
