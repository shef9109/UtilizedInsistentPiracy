from fastapi import HTTPException, Response
import os

BASE_DIR = "webdav_storage"

def mkcol(path: str):
    full_path = os.path.join(BASE_DIR, path)
    if os.path.exists(full_path):
        raise HTTPException(status_code=405, detail="Resource already exists")
    os.makedirs(full_path)
    return Response(content="Directory created", status_code=201)