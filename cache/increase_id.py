from connection import connect_database

def generate_id():
    rc = connect_database() 

    try:
        new_id = rc.incr('link_id')
        print(f"ID Gerado: {new_id}")
        return new_id
    finally:
        rc.close() 
