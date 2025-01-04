from fastapi import Request, Response
import os

BASE_DIR = "webdav_storage"

def put_file(path: str, request: Request):
    full_path = os.path.join(BASE_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    body = request.body()  # Синхронное чтение тела запроса
    with open(full_path, "wb") as file:
        file.write(body)
    return Response(content="File created/updated", status_code=201)