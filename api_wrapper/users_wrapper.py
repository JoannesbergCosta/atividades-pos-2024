import requests

class Users:
    def __init__(self):
        self.api_url = "https://jsonplaceholder.typicode.com"

    def list(self):
        return requests.get(self.api_url+"/users/").json()

    def read(self,user_id):
        response = requests.get(self.api_url+"/users/"+user_id)
        if response.status_code == 200:
            return response.json()
        else:
            return False
        
    def delete(self,user_id):
        response = requests.delete(self.api_url+"/users/"+user_id)
        if response.status_code == 200:
            return True
        else:
            return False
        
    def create(self,user_data):
        response = requests.post(self.api_url+"/users/"+user_data)
        return response.json()
        
    def update(self,user_id,user_data):
        response = requests.patch(f"{self.api_url}/{user_id}", json=user_data)
        return response.status_code
    
