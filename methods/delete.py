from fastapi import HTTPException, Response
import os
import shutil

BASE_DIR = "webdav_storage"

def delete_file(path: str):
    full_path = os.path.join(BASE_DIR, path)
    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="Resource not found")
    if os.path.isdir(full_path):
        shutil.rmtree(full_path)
    else:
        os.remove(full_path)
    return Response(content="Resource deleted", status_code=200)