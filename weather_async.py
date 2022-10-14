import sys
import asyncio

sys.path.append('/Users/christian/Desktop/joan_proj/coding_test/')
from weather_collector import WeatherCollector

with open('list.txt', 'r') as urls:
    apis = urls.read().split('\n')

async def main():
    weather = WeatherCollector()
    await weather.fetch(apis)

asyncio.run(main())