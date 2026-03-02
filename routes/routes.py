from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
import controller.url as url
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

domain = os.getenv('domain_host')
port = os.getenv('domain_port')
domain_string = f'http://{domain}:{port}/' #Switch for Https if have SSL

router = APIRouter(prefix='/url',tags=['url'])

@router.post("/",status_code= 201)
async def short_link(original_url:str=Form(...,description="Url to shortner")):
    try:
        normalize_url = url.strip_protocol(original_url)
        hash = await url.new_url(normalize_url)
        return JSONResponse({'message':'success','data':{'original_url':original_url, 'short_url':f'{domain_string}{hash}'}},status_code=201)
        
    except Exception as e:
        print(f'ERROR LOG: {e}')
        return JSONResponse({'message':'error','message_error':e},status_code=500)

    
@router.get("/{hash}",status_code = 302)
async def redirect(hash:str):
    try:
        link = await url.get_original_link(hash)
        return RedirectResponse(link, status_code=302)
    except Exception as e:
        print(f'Error to get all links: {e}')
        return JSONResponse({'message': 'Internal Server Error, contact an admin or check console log'}, status_code=500)
        
    
url_router = router