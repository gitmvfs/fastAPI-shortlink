from cache.connection import connect_database
rc = connect_database() 

def generate_id():

    try:
        new_id = rc.incr('link_id')
        return new_id
    finally:
        rc.close() 
