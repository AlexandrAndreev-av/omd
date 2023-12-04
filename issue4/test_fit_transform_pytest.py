import pytest
from one_hot_encoder import fit_transform

def test_fit_transform_basic():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    expected_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(*cities)
    assert transformed_cities == expected_transformed_cities

def test_fit_transform_empty():
    with pytest.raises(TypeError, match='expected at least 1 arguments, got 0'):
        fit_transform()

def test_fit_transform_single_argument():
    single_category = 'Single'
    expected_transformed_category = [(single_category, [0])]
    transformed_category = fit_transform(single_category)
    assert transformed_category == expected_transformed_category

def test_fit_transform_multiple_arguments():
    categories = ['A', 'B', 'C']
    expected_transformed_categories = [
        ('A', [0, 0, 1]),
        ('B', [0, 1, 0]),
        ('C', [1, 0, 0]),
    ]
    transformed_categories = fit_transform(*categories)
    assert transformed_categories == expected_transformed_categories

def test_fit_transform_exception():
    with pytest.raises(TypeError, match='expected at least 1 arguments, got 0'):
        fit_transform(123, 'abc')
