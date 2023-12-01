import psycopg2

# Параметры подключения (замените их на свои)
dbname = 'ict'
user = 'ictuser'
password = 'qwerty90'
host = 'localhost'

# Подключение к базе данных
connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# Создание курсора
cursor = connection.cursor()

# Пример SQL-запроса для получения данных
sql_query = "SELECT * FROM salary_dataset;"

# Выполнение запроса
cursor.execute(sql_query)

# Получение результатов
results = cursor.fetchall()

# Закрытие соединения
connection.close()

# Обработка результатов в Python
education_salary_mapping = {}

for row in results:
    education_level = row[3]  # Предположим, что education_level находится в четвёртом столбце
    salary = row[6]  # Предположим, что salary находится в седьмом столбце

    if education_level not in education_salary_mapping:
        education_salary_mapping[education_level] = []

    education_salary_mapping[education_level].append(salary)

# Вывод результатов анализа
print("Средняя зарплата по уровню образования:")
for education_level, salaries in education_salary_mapping.items():
    # print(education_level, salaries)
    try:
        average_salary = sum(salaries) / len(salaries) if salaries else 0
        print(f"{education_level}: {average_salary}")
    except Exception as e:
        ...
