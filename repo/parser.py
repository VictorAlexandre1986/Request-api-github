from models.repo import Repo

class RepoParser():
    
    @classmethod
    def parse(cls, response):
        for i in range(len(response)):
            result = response[i]
            #Instancia do módulo repo
            repo = Repo(result["id"], result["name"], result["stargazers_count"])
            print (repo)