import asyncio

import movie_api
import formatter

def parse(media_type, time_window, output_format):
    if media_type == 'movie':
        data = asyncio.run(movie_api.fetch_movie(time_window))
    elif media_type == 'tv':
        data = asyncio.run(movie_api.fetch_tv(time_window))
    elif media_type == 'all':
        data = asyncio.run(movie_api.fetch_all(time_window))
    else:
        return

    if output_format == 'json':
        formatter.print_json(data)
    elif output_format == 'csv':
        formatter.print_csv(data)
