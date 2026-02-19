from controller.link_shortener import link_shortener
from cache.increase_id import generate_id
from database.connection import get_database_session
from database.schema.link import Link

db_session = get_database_session()
link = Link(db_session)

def new_url(original_url):
    
    try:
        id = generate_id()
        hash = link_shortener(id)
        link.insert_link(hash, original_url)
        
        return hash
    
    except Exception as e:
        print('Error to create new URL:', e)

