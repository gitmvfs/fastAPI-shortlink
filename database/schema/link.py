from cassandra.cluster import Session

class Link():
    
    def __init__(self,session:Session):
        self.session = session 
        self.create_table()
        
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS short_link (
            id text,
            link text,
            created_at timestamp,
            PRIMARY KEY(id)
            )"""
        self.session.execute(query)
        
    def insert_link(self,id_hash:str,url:str):
        query = "INSERT INTO short_link (id,link,created_at) VALUES (%s, %s, toTimestamp(now()))"
        self.session.execute(query, (id_hash, url))