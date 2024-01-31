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

# Пример SQL-запроса для анализа данных
sql_analysis_query = "SELECT education_level, AVG(salary) FROM salary_dataset GROUP BY education_level;"

# Выполнение запроса
cursor.execute(sql_analysis_query)

# Получение результатов
results = cursor.fetchall()

# Вывод результатов анализа
print("Средняя зарплата по уровню образования:")
for row in results:
    print(f"{row[0]}: {row[1]}")

# Закрытие соединения
connection.close()