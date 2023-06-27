from cliente.client import GithubClient
from repo.parser import RepoParser

if __name__=='__main__':
    username="VictorAlexandre"
    response = GithubClient.get_repository_by_user(username)
    
    if response['status_code'] == 200:
        RepoParser.parse(response['body'])
    else:
        print(response['body'])