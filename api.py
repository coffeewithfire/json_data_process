import httpx


url = "https://base.media108.ru/training/sample/"

def get_data(url: str = url) -> dict:
    
    response = httpx.get(url=url)
    response.raise_for_status()
    
    return response.json()