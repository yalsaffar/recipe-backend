from api import app
import pytest

def test_create_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN a POST request is made to the '/recipe' URL with the recipe data
    THEN check the response contains the id of the created recipe
    """
    response = testing_client.post('/recipe', json={
        'name': 'Pumpkin Pie',
        'ingredients': 'pumpkin, sugar, salt, butter, pie crust',
        'instructions': 'Preheat oven to 425 degrees F (220 degrees C). Mix pumpkin, sugar, salt, and butter together in a bowl. Pour into pie crust. Bake in preheated oven until a knife inserted near the center comes out clean, about 1 hour.'
    })
    assert response.status_code == 200

def test_get_recipes(testing_client):
    """
    GIVEN a Flask application
    WHEN a GET request is made to the '/recipe/' URL with an id of an existing recipe
    THEN check the response contains the details of the recipe
    """
    response = testing_client.get('/recipe')
    assert response.status_code == 200
   
def test_get_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN a GET request is made to the '/recipe/<id>' URL with an id of an existing recipe
    THEN check the response contains the details of the recipe
    """
    response = testing_client.get('/recipe/1')
    assert response.status_code == 200
    assert response.json == {
        'id' : 1,
        'name': 'Pumpkin Pie',
        'ingredients': 'pumpkin, sugar, salt, butter, pie crust',
        'instructions': 'Preheat oven to 425 degrees F (220 degrees C). Mix pumpkin, sugar, salt, and butter together in a bowl. Pour into pie crust. Bake in preheated oven until a knife inserted near the center comes out clean, about 1 hour.'
    }

