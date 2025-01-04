from fastapi import HTTPException, Response
import os

BASE_DIR = "webdav_storage"

def get_file(path: str):
    full_path = os.path.join(BASE_DIR, path)
    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(full_path, "rb") as file:
        return Response(content=file.read(), media_type="application/octet-stream")