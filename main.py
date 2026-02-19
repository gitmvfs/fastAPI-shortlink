from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from database.schema.link import Link
from database.connection import get_database_session
from routes.routes import url_router

app = FastAPI()

#set CORS config for deploy

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"], 
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#Config database
db_session = get_database_session()
Link(db_session)

app.include_router(url_router)

@app.get("/")
def callback_check():
    return {"Status": "Online", "Version": "1.0.0","Current_Time": datetime.today()}