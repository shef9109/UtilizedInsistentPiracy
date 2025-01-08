from fastapi import FastAPI, Request, Response
from methods.propfind import propfind
from methods.get import get_file
from methods.put import put_file
from methods.delete import delete_file
from methods.mkcol import mkcol
import os
import uvicorn
from importlib import import_module

# Создаем объект приложения
app = FastAPI()

# Регистрация маршрутов
@app.route("/{path:path}", methods=["PROPFIND"])
async def handle_propfind(path: str, request: Request):
    return await propfind(path, request)

@app.get("/{path:path}")
async def handle_get(path: str):
    return await get_file(path)

@app.put("/{path:path}")
async def handle_put(path: str, request: Request):
    return await put_file(path, request)

@app.delete("/{path:path}")
async def handle_delete(path: str):
    return await delete_file(path)

@app.route("/{path:path}", methods=["MKCOL"])
async def handle_mkcol(path: str):
    return await mkcol(path)

    # Корневой маршрут для проверки работоспособности
@app.get("/")
async def read_root():
    return {"message": "WebDAV Server is running"}

    # Функция Bootstrap
def bootstrap():
    modul = os.path(os.getenv())
    for path in modul.iterdir('/env'):  # Проход по всем возможным путям
        if path.is_file() and path.suffix == '.py':
            modul_get = import_module(path.stem())
            for r in modul_get:  # Регистрация роутеров
                app.include_router(r)
    for mod in os.path(os.getenv()).iterdir():
        mod_get = import_module(mod.stem + '.py')
        for method in mod_get.__dict__.keys():
            if method ==:
                app.add_api_route

    # Запуск сервера через uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, reload=True)