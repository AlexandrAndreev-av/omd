import unittest
from one_hot_encoder import fit_transform

class TestFitTransform(unittest.TestCase):

    def test_fit_transform_basic(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        expected_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, expected_transformed_cities)

    def test_fit_transform_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_fit_transform_single_argument(self):
        single_category = 'Single'
        expected_transformed_category = [(single_category, [0])]
        transformed_category = fit_transform(single_category)
        self.assertEqual(transformed_category, expected_transformed_category)

    def test_fit_transform_multiple_arguments(self):
        categories = ['A', 'B', 'C']
        expected_transformed_categories = [
            ('A', [0, 0, 1]),
            ('B', [0, 1, 0]),
            ('C', [1, 0, 0]),
        ]
        transformed_categories = fit_transform(*categories)
        self.assertEqual(transformed_categories, expected_transformed_categories)

    def test_fit_transform_exception(self):
        with self.assertRaises(TypeError):
            fit_transform(123, 'abc')

if __name__ == '__main__':
    unittest.main()



# В этом примере:

# test_fit_transform_basic тестирует основной функционал.
# test_fit_transform_empty проверяет, что функция вызывает исключение TypeError при отсутствии аргументов.
# test_fit_transform_single_argument проверяет обработку одного аргумента.
# test_fit_transform_multiple_arguments тестирует случай с несколькими аргументами.
# test_fit_transform_exception проверяет, что функция вызывает исключение при передаче аргументов неверного типа.
# Чтобы выполнить тесты, выполните следующую команду:

# bash
# Copy code
# python -m unittest test_fit_transform.py
# Убедитесь, что замените 'your_module_name' на фактическое имя вашего модуля.
