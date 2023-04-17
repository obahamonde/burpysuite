from json import loads
from fastapi import APIRouter, HTTPException
from server.enumerator import Enumerator
from server.models.collections import Enumerated        
from server.models.schemas import Geo, Record

app = APIRouter(prefix="/dns", tags=["dns"])

@app.get("/{domain}")
async def enumerate_(domain: str, ref:int):
    """Gets all subdomains, headers, and records for a domain"""
    enumerator = Enumerator(domain)
    try:
        item = {
            "userRef": ref,
            "domain": domain,
            "headers": loads(await enumerator.headers()),
            "records": [Record(**record) for record in loads(enumerator.records)],
            "geo": Geo(**loads(enumerator.geo)),
            "subdomains": loads(enumerator.subdomains),
    
        }
        return await Enumerated(**item).create()
    except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))
  
