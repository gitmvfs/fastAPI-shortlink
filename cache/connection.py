import redis
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

host = os.getenv('redis_host')
port = int(os.getenv('redis_port'))

pool = redis.ConnectionPool(
    host=host, 
    port=port, 
    decode_responses=True, 
    max_connections=100
)

redis_connection = redis.Redis(connection_pool=pool)
print('Redis connected to sucessfully!')

def generate_id():
    return redis_connection.incr('link_id')
         
