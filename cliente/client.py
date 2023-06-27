import requests 
import json

class GithubClient():
    
    API_BASE_URL = "https://api.github.com"
    
    @classmethod    
    def get_repository_by_user(self, user):
        response = requests.get(f'{self.API_BASE_URL}/users/{user}/repos')
        if response.status_code == 200:
            # return [json.loads(repo) for repo in response.text]
            return {"status_code": 200, "body": response.json()}
        else:
            return {"status_code": response.status_code, "body":"Error while getting repos"}