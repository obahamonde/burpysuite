from pydantic import BaseSettings, BaseConfig, Field


class Env(BaseSettings):

    class Config(BaseConfig):

        env_file = ".env"

        env_file_encoding = "utf-8"


    AUTH0_DOMAIN: str = Field(..., env="AUTH0_DOMAIN")

    FAUNA_SECRET: str = Field(..., env="FAUNA_SECRET")

    browser_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

    record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'PTR', 'SOA', 'SRV', 'TXT']


    def __init__(self, **data):

        super().__init__(**data)

env = Env()

