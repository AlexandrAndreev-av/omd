
Установите необходимые зависимости
pip install pytest coverage
pytest -v --cov=what_is_year_now --cov-report=html

Запуск теста
pytest -v --cov=what_is_year_now --cov-report=html

Теперь, когда вы запустите тесты с помощью `pytest` и проверите покрытие с использованием `coverage`, вы сможете видеть отчет в формате HTML
