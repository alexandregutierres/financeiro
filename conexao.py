import requests

class Conexao:
   
    def __init__(self, classe: str, ordem: str):
        self.classe = classe
        
        self.ordem = ordem
        if self.ordem == '':
            self.api_url = 'https://parseapi.back4app.com/classes/' + self.classe
        else:
            self.api_url = 'https://parseapi.back4app.com/classes/' + self.classe + '?order=' + self.ordem
            
        self.headers = {"accept": "application/json",
                        "X-Parse-Application-Id" : "5qYGdcl6opRF8nltPYjOOIFCatF40inhOyXYLpdo",
                        "X-Parse-REST-API-Key" : "oE6cpdY1BEuP8m0UED9fsMoSkGDfy3ATWbrOU9sR"}
        
        
    def Get(self):
        api_url = self.api_url
        headers = self.headers
        response = requests.get(api_url, headers=headers)
        dados = response.json()['results']
        
        return dados
    
    