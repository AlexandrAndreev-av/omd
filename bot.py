import csv
from typing import Dict, List, Tuple


def layout_data(info: list) -> None:
    departments: Sets = set(row['Департамент'] for row in info)
    for department in departments:
        print(f"Департамент: {department}")
        teams:  Sets = set(row['Отдел'] for row in info if row['Департамент'] == department)
        for team in teams:
            print(f"\t Отдел: {team}")


# Чтение данных из CSV-файла и возвращение списка словарей
def read_csv(file_path: str) -> List[Dict[str, str]]:
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data


# Генерация сводного отчёта по департаментам
def generate_report(data: List[Dict[str, str]]) -> Dict[str, Tuple[int, str, str, float]]:
    report = {}
    for row in data:
        department = row['Департамент']
        salary = int(row['Оклад'])
        if department not in report:
            report[department] = {
                'численность': 1,
                'вилка зарплат': (salary, salary),
                'средняя зарплата': salary
            }
        else:
            report[department]['численность'] += 1
            min_salary, max_salary = report[department]['вилка зарплат']
            report[department]['вилка зарплат'] = (min(min_salary, salary), max(max_salary, salary))
            report[department]['средняя зарплата'] += salary
    for department in report:
        report[department]['средняя зарплата'] /= report[department]['численность']
    return report


# Сохранение сводного отчёта в виде CSV-файла
def save_report(report: Dict[str, Tuple[int, str, str, float]], file_path: str):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Департамент', 'Численность', 'Вилка зарплат', 'Средняя зарплата'])
        for department, data in report.items():
            writer.writerow([
                department,
                data['численность'],
                f"{data['вилка зарплат'][0]} - {data['вилка зарплат'][1]}",
                data['средняя зарплата']
            ])


data = read_csv('Corp_Summary.csv')
report = generate_report(data)


def condition2():
    for department, data in report.items():
        print(f"Департамент: {department}")
        print(f"Численность: {data['численность']}")
        print(f"Вилка зарплат: {data['вилка зарплат'][0]} - {data['вилка зарплат'][1]}")
        print(f"Средняя зарплата: {data['средняя зарплата']}")
        print()


# Функция вывода меню + выбор пункта
def main_menu():
    print('1. Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него')
    print('2. Вывести сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату')
    print('3. Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. При этом необязательно вызывать сначала команду из п.2')

    option = int(input())
    while option not in range(1, 4):
        print("Выберите число от 1 до 3")
        option = int(input())
    if option == 1:
        return layout_data(data)
    elif option == 2:
        return condition2()
    elif option == 3:
        return save_report(report, 'report.csv')


if __name__ == '__main__':
    main_menu()


