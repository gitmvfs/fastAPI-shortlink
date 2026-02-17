from redis import Redis
from dotenv import load_dotenv, find_dotenv
import os

def connect_database():
    load_dotenv(find_dotenv())

    host = os.getenv('redis_host')
    port = int(os.getenv('redis_port'))

    rc = Redis(host, port, decode_responses= True)
    return rc