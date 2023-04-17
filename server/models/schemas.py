from typing import Optional as O
from pydantic import BaseModel, Field


class Record(BaseModel):
    domain:str
    ttl:int
    type_:str
    value:str

class Geo(BaseModel):
    ip: str
    anycast: O[bool] = Field(default=False)
    city: str
    region: str
    country: str
    loc: str
    org: str
    postal: int
    timezone: str

