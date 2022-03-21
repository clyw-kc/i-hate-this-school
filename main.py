from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from base64 import b64decode
import binascii

app = FastAPI()

@app.get("/{url}")
async def read_root(url):
    try:
        url = b64decode(url)
    except binascii.Error:
        raise HTTPException(400, "Bad base64")
    
    return url