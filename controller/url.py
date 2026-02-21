from controller.link_shortener import link_shortener
from cache.increase_id import generate_id
from database.connection import get_database_session
from database.schema.link import Link

db_session = get_database_session()
link = Link(db_session)

def new_url(url):
    
    try:
        id = generate_id()
        hash = link_shortener(id)
        link.post_link(hash, url)
        
        return hash
    
    except Exception as e:
        print('Error to create new URL:', e)
        return None

def strip_protocol(original_url:str):
    
    try:
        url = original_url.split('https://')[1]
        
        return url
    
    except Exception as e:
        print('Error to remove protocol from URL:', e)
        return None
        
def get_original_link(hash):
    if not hash: 
        raise Exception('Hash null')
    try:  
        original_url = link.get_link(hash)
        
        return f'https://{original_url}'
    
    except Exception as e:
        print('Error to get all URL data:', e)
        return None