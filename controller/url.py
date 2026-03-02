from controller.link_shortener import link_shortener
from cache.connection import generate_id
from database.connection import session
from database.schema.link import Link

link = Link(session)

async def new_url(url): 
    try:
        id = generate_id()
        hash = link_shortener(id)
        await link.post_link(hash, url) 
        return hash
    except Exception as e:
        print('Error to create new URL:', e)
        return None

def strip_protocol(original_url:str):
    
    try:
        if 'https://' in original_url:
            url = original_url.split('https://')[1]
            return url
        
        return original_url
        
    except Exception as e:
        print('Error to remove protocol from URL:', e)
        return None
        
async def get_original_link(hash): 
    if not hash: 
        raise Exception('Hash null')
    try:  
        original_url = await link.get_link(hash) 
        if original_url:
            return f'https://{original_url}'
        return None
    except Exception as e:
        print('Error to get all URL data:', e)
        return None