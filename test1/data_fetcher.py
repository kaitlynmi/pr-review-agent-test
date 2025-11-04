import requests
import time

class DataFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.example.com"
        self.cache = {}
    
    def fetch_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}?api_key={self.api_key}"
        response = requests.get(url)
        return response.json()
    
    def fetch_multiple_users(self, user_ids):
        users = []
        for user_id in user_ids:
            user = self.fetch_user(user_id)
            users.append(user)
            time.sleep(1)
        return users
    
    def get_cached_data(self, key):
        if key in self.cache:
            return self.cache[key]
        return None
    
    def update_cache(self, key, value):
        self.cache[key] = value