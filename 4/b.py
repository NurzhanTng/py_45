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

# Пример SQL-запроса для чтения данных
sql_select_query = "SELECT * FROM ваша_таблица;"

# Выполнение запроса
cursor.execute(sql_select_query)

# Получение результатов
results = cursor.fetchall()

# Вывод результатов
for row in results:
    print(row)

# Закрытие соединения
connection.close()
