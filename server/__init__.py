from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.router import api
from server.models import collections
import inspect

async def provision_models():
    for name, model in inspect.getmembers(collections):
        if inspect.isclass(model) and issubclass(model, collections.AioModel) and model.__class__ != collections.AioModel:
            await model.provision()

def create_app():
    app = FastAPI()
    app.include_router(api)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    #@app.on_event("startup")
    async def startup():
        await provision_models()
    
    return app