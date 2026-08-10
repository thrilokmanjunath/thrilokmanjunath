import os
import requests

class GitHubClient:
    def __init__(self):
        self.token = os.environ.get("GITHUB_TOKEN")
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if self.token:
            self.headers["Authorization"] = f"token {self.token}"
        self.base_url = "https://api.github.com"
        
    def get_user_data(self, username):
        resp = requests.get(f"{self.base_url}/users/{username}", headers=self.headers)
        if resp.status_code != 200:
            print(f"Failed to fetch user data: {resp.text}")
            return {}
        return resp.json()
        
    def get_repos(self, username):
        repos = []
        page = 1
        while True:
            resp = requests.get(f"{self.base_url}/users/{username}/repos?per_page=100&page={page}&sort=updated", headers=self.headers)
            if resp.status_code != 200:
                print(f"Failed to fetch repos: {resp.text}")
                break
            data = resp.json()
            if not data:
                break
            repos.extend(data)
            page += 1
        return repos

    def get_events(self, username):
        resp = requests.get(f"{self.base_url}/users/{username}/events/public?per_page=15", headers=self.headers)
        if resp.status_code != 200:
            return []
        return resp.json()
