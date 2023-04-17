from fastapi import APIRouter
from server.router import dns, auth

class API(APIRouter):
    def use(self, router):
        self.include_router(router, prefix="/api")
        return self
    
    
api = API().use(dns.app).use(auth.app)
