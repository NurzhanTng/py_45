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

# Пример SQL-запроса для удаления данных
sql_delete_query = "DELETE FROM salary_dataset WHERE id = 0;"

# Выполнение запроса
cursor.execute(sql_delete_query)

# Подтверждение изменений
connection.commit()

# Закрытие соединения
connection.close()
