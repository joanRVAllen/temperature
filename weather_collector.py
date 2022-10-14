import asyncio
from statistics import mean
from geopy.geocoders import Nominatim
import aiohttp
geolocator = Nominatim(user_agent="geoapiExercises")

class WeatherCollector:

    async def fetch(self, apis: list):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            tasks = [self.collect_data(session, api) for api in apis]
            await asyncio.gather(*tasks)

    async def collect_data(self, session, url: str):
        response = await session.get(url)

        if response.ok:
            response_data = await response.json()
            avg_temp = self.get_temperature(response_data)
            location = self.get_location(response_data)
            print(f"{location}{avg_temp}")

        else:
            print('Invalid url')
             
    
    def get_temperature(self, data: dict):
        temps = []

        if data == None or 'properties' not in data.keys(): 
            return 'No properties available '

        else:
            if data['properties'] == None or 'periods' not in data['properties'].keys():
                return 'No periods available '
            elif data['properties']['periods'] == None:
                return 'No periods available '
            else:
                for i in data['properties']['periods']:
                    if i is not None and 'isDaytime' in i.keys():
                        if i['isDaytime'] == True:
                            if 'temperature' in i.keys():
                                temps.append(i['temperature'])

                return round(mean(temps), 2)
            

    def get_location(self, data: dict):
        if data == None or 'geometry' not in data.keys():
            return 'No geometry available ' 
        else:
            if data['geometry'] == None or 'coordinates' not in data['geometry'].keys():
                return 'No coordinates available '
            else:
                long, lat = data['geometry']['coordinates'][0][0]
                self.location = geolocator.reverse(f'{lat},{long}')
                return f"{self.location.raw['address']['city']} {self.location.raw['address']['state']} Average Temp: "