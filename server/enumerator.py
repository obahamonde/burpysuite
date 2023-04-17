from json import loads, dumps
from socket import gethostbyname
from aiohttp import ClientSession
from geocoder import ip as geo
from dns.resolver import resolve
from server.models.config import env
from server.models.schemas import Record, Geo
class Enumerator(object):

    domain:str

    def __init__(self, domain:str):
        self.domain = domain

    @property
    def records(self):

        records = []
        for record_type in env.record_types:
            try:
                records.extend(str(resolve(self.domain, record_type).rrset).split('\\n'))
            except Exception:
                continue
        responses = []
        for record in records:
            if record not in responses:
                record = record.split(' ')
                record.pop(2)
                record.pop(0)
                responses.append(record)
            if record[1] == 'MX':
                record.pop(2)
        return dumps([Record(domain=self.domain, ttl=int(record[0]), type_=record[1], value=record[2]).dict() for record in responses])
 
    @property
    def geo(self):
        """Get's geo information for a domain"""
        return dumps(geo(gethostbyname(self.domain)).json['raw'])

    @property
    def subdomains(self):
        """Get's all subdomains for a domain"""
        response = []
        with open('./subdomains.txt', 'r', encoding='utf-8') as file:
            subdomains = file.read().split('\\n')
            for subdomain in subdomains:
                try:
                    res = resolve(f"{subdomain}.{self.domain}", 'A').rrset
                    if res:
                        for ipval in res:
                            response.append({"ip":str(ipval),"domain": f"{subdomain}.{self.domain}"})
                except Exception:
                    continue
        return dumps(response)
    
    async def headers(self):
        """Get's all headers for a domain"""
        async with ClientSession(headers=env.browser_headers) as session:
            async with session.head(f"https://{self.domain}") as response:
                return dumps(dict(response.headers))
            
