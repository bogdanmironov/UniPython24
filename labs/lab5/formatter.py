import json

def print_json(media: list) -> None:
    filtered = filter_data(media)
    sorted_media = sorted(filtered, key=lambda x: x['rating'], reverse=True)
    print(json.dumps(sorted_media))

def print_csv(media: list) -> None:
    filtered = filter_data(media)
    sorted_media = sorted(filtered, key=lambda x: x['rating'], reverse=True)
    print("title, rating")
    for item in sorted_media:
        print(f"{item['title']},{item['rating']}")

def filter_data(media: list[dict]) -> list[dict]:
    filtered = []
    for item in media:
        title = item.get('title') or item.get('name', 'unknown')
        rating = item.get('vote_average', 0.0)
        filtered.append({'title': title, 'rating': rating})
    return filtered