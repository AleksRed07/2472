import requests

class PetFriends:
    BASE_URL = "https://petfriends.skillfactory.ru/"

    def __init__(self, api_key):
        self.headers = {"auth_key": api_key}

    def get_pet_by_id(self, pet_id):
        """Получение информации о питомце по его ID"""
        response = requests.get(f"{self.BASE_URL}api/pets/{pet_id}", headers=self.headers)
        return response

    def delete_pet(self, pet_id):
        """Удаление питомца по его ID"""
        response = requests.delete(f"{self.BASE_URL}api/pets/{pet_id}", headers=self.headers)
        return response



