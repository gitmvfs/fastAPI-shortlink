from hashids import Hashids
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

base62_inverted = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
secret_word = os.getenv('secret_word')

def link_shortener(id:int) -> str:
    
    encoder = Hashids(secret_word, 4, base62_inverted)
    enconded = encoder.encode(id)
    
    return enconded    
