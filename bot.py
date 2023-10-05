import csv

def layout_data(info: list) -> None:
    departments: Sets = set(row['Департамент'] for row in info)
    for department in departments:
        print(f"Департамент: {department}")
        teams:  Sets = set(row['Отдел'] for row in info if row['Департамент'] == department)
        for team in teams:
            print(f"\t Отдел: {team}")


# Открытие файла в кодировке, чтение, указан разделитель, преобразуем информацию  в словарь
def condition1():
    filename: Str = 'Corp_Summary.csv'
    with open(filename, 'r', encoding='utf-8') as csv_doc:
        reader = csv.DictReader(csv_doc, delimiter = ';')
        info = [row for row in reader]
    layout_data(info)


# Функция ещё не реализована , затрачено много времени , на выходных обязательно доделаю (вывод сводного отчёта)
def condition2():
    print(
       "Функция ещё не реализована, но обязательно будет сделана :("
    )


# Функция ещё не реализована , затрачено много времени , на выходных обязательно доделаю (вывод в файл)
def condition3():
    print("Функция ещё не реализована, но так же будет сделана на выходных :(")


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
        return condition1()
    elif option == 2:
        return condition2()
    elif option == 3:
        return condition3()


if __name__ == '__main__':
    main_menu()



