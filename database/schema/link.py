from cassandra.cluster import Session
import datetime
import asyncio

class Link():
    
    def __init__(self, session:Session):
        self.session = session 
        self.create_table()
        self._prepare_statements()
        
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS short_link (
            id text,
            link text,
            created_at timestamp,
            PRIMARY KEY(id)
            )"""
        self.session.execute(query)
    
    def _prepare_statements(self):
        self.post_link_query = self.session.prepare("INSERT INTO short_link (id,link,created_at) VALUES (?, ?, ?) USING TTL 315360000")
        self.get_link_query = self.session.prepare("SELECT link FROM short_link WHERE id = ?")
    
    async def post_link(self,id_hash:str,url:str):
        datetime_now = datetime.datetime.now(datetime.timezone.utc)
        future = self.session.execute_async(self.post_link_query, (id_hash, url, datetime_now))
        
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, future.result)
        
    def get_link(self, hash):
        data = self.session.execute(self.get_link_query,[hash])
        data = data.one()
        return data['link']