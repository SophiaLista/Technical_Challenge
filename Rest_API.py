import requests

def bestInGenre(genre):
    base_url = "https://jsonmock.hackerrank.com/api/tvseries"
    page = 1
    max_rating = -1
    best_show = ""
    
    while True:
        url = f"{base_url}?page={page}"
        
        try:
            response = requests.get(url)
            data = response.json()
            
            if page > data['total_pages']:
                break
            
            for show in data['data']:
                if genre.lower() in show['genre'].lower():
                    if (show['imdb_rating'] > max_rating or (show['imdb_rating'] == max_rating and (best_show == "" or show['name'] < best_show))):
                        max_rating = show['imdb_rating']
                        best_show = show['name']
            
            page += 1
        
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    
    return best_show


print(bestInGenre("Action"))
