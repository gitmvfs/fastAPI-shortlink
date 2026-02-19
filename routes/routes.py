from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from controller.url import *
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

domain = os.getenv('domain_host')
port = os.getenv('domain_port')
domain_string = f'http://{domain}:{port}/' #Switch for Https if have SSL

router = APIRouter(prefix='/shortlink',tags=['shortlink'])

@router.post("/",status_code= 201)
def short_link(original_url:str=Form(...,description="Url to shortner")):
    try:
        normalize_url = strip_protocol(original_url)
        hash = new_url(normalize_url)
        return JSONResponse({'Message':'Success','data':{'original_url':original_url, 'short_url':f'{domain_string}/{hash}'}},status_code=201)
        
    except Exception as e:
        print(f'ERROR LOG: {e}')
        return JSONResponse({'message': 'Internal Server Error, contact an admin or check console log'}, status_code=500)
    

    
url_router = router