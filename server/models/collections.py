from aiofauna import AioModel, Optional as O, List as L, Dict as D
from pydantic import Field
from server.models.schemas import Geo, Record

class User(AioModel):

    email: str = Field(default=None, index=True)

    email_verified: bool = Field(default=False)

    family_name: O[str] = Field(default=None)

    give_name: O[str] = Field(default=None)

    locale: O[str] = Field(default=None)

    name: str = Field(..., index=True)

    nickname: O[str] = Field(default=None)

    picture: O[str] = Field(default=None)

    sub: str = Field(..., unique=True)

    updated_at: O[str] = Field(default=None)

class Enumerated(AioModel):
    userRef:int = Field(..., index=True)
    domain:str = Field(..., index=True)
    geo:Geo = Field(..., unique=True)
    headers:O[dict] = Field(default=None)
    records:O[L[Record]] = Field(default_factory=list)
    subdomains:O[L[str]] = Field(default_factory=list)
