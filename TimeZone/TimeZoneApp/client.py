import requests
from .settings import OPENWEATHERMAP_API_KEY

class ClimaClient:

    def get_clima_info(self,city:str):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}'
        response = requests.get(url)

        if response.status_code == 400:
            return None
        
        if response.status_code == 200:
            data = response.json()
            return data
        

        