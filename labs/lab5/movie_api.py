import asyncio
import aiohttp

BASE_URL = 'http://api.themoviedb.org/3/trending'
API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZDVhNDU4YzljZmMxODdjZThlMDdhM2ZiYTU1MjE0YyIsInN1YiI6IjY1NzRkNzA2ZTkzZTk1MDExZDRlMmM2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.MsO7CO9573rr8rTEczZJ4PW6dnVX9xuU2OUNOcaHEts'

async def fetch_movie(time_window: str) -> list:
    url = f"{BASE_URL}/movie/{time_window}"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("results", [])
            raise Exception(f"API request failed with status {response.status}")

async def fetch_tv(time_window: str) -> list:
    url = f"{BASE_URL}/tv/{time_window}"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("results", [])
            raise Exception(f"API request failed with status {response.status}")

async def fetch_all(time_window: str) -> list:
    movie_task = fetch_movie(time_window)
    tv_task = fetch_tv(time_window)
    movies, tv_shows = await asyncio.gather(movie_task, tv_task)
    return [*movies, *tv_shows]