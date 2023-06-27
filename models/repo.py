class Repo():
    
    def __init__(self, id, name, stars):
        self._id = id 
        self._name = name 
        self._stars = stars
        
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    def stars(self):
        return self._stars
    
    def __str__(self) -> str:
        return f'Id: {self.id} Name: {self.name} Stars{self.stars}'