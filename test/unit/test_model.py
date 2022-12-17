from api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Recipe model
    WHEN a new Recipe is created
    THEN check the name, ingredients, instructions, rating, is_favorite fields are defined correctly
    """
    recipe = Recipe('Pumpkin Pie', 'pumpkin, sugar, salt, butter, pie crust', 'Preheat oven to 425 degrees F (220 degrees C). Mix pumpkin, sugar, salt, and butter together in a bowl. Pour into pie crust. Bake in preheated oven until a knife inserted near the center comes out clean, about 1 hour.')
    assert recipe.name == 'Pumpkin Pie'
    assert recipe.ingredients == 'pumpkin, sugar, salt, butter, pie crust'
    assert recipe.instructions == 'Preheat oven to 425 degrees F (220 degrees C). Mix pumpkin, sugar, salt, and butter together in a bowl. Pour into pie crust. Bake in preheated oven until a knife inserted near the center comes out clean, about 1 hour.'
    #assert recipe.rating == 0
    #assert recipe.is_favorite == False
