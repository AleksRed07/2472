from zadanie2472 import PetFriends


def test_get_pet_by_valid_id(api_key):
    pet_id = "existing_pet_id"
    response = PetFriends(api_key).get_pet_by_id(pet_id)
    assert response.status_code == 200
    assert "id" in response.json()

def test_delete_pet_by_valid_id(api_key):
    pet_id = "existing_pet_id"
    response = PetFriends(api_key).delete_pet(pet_id)
    assert response.status_code == 200

def test_get_pet_by_invalid_id(api_key):
    response = PetFriends(api_key).get_pet_by_id("non_existing_id")
    assert response.status_code == 404

def test_delete_pet_by_invalid_id(api_key):
    response = PetFriends(api_key).delete_pet("non_existing_id")
    assert response.status_code == 404

def test_get_pet_no_auth():
    response = PetFriends(None).get_pet_by_id("existing_pet_id")
    assert response.status_code == 401


def test_delete_pet_no_auth():
    response = PetFriends(None).delete_pet("existing_pet_id")
    assert response.status_code == 401

def test_delete_pet_with_empty_id(api_key):
    response = PetFriends(api_key).delete_pet("")
    assert response.status_code == 400

def test_get_pet_with_wrong_type_id(api_key):
    response = PetFriends(api_key).get_pet_by_id(12345)  # Передача числа вместо строки
    assert response.status_code == 400

def test_delete_pet_with_invalid_auth():
    response = PetFriends("invalid_key").delete_pet("existing_pet_id")
    assert response.status_code == 401

def test_get_pet_with_empty_auth():
    response = PetFriends("").get_pet_by_id("existing_pet_id")
    assert response.status_code == 401
