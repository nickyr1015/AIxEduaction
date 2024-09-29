from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from model.database_connection import DatabaseConnection


app = FastAPI()
db = DatabaseConnection()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define the API endpoint
@app.get("/courses", response_model=List[dict])
def get_data():
    print(db.base_dir)
    data = db.get_course_all()
    print(f"data: {data}")
    course = [course.to_dict() for course in data]
    print("Get All Course Information")
    print(f"course: {course}")
    return course
