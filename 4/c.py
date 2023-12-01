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

# Пример SQL-запроса для обновления данных
# sql_update_query = "UPDATE ваша_таблица SET column1 = %s WHERE условие;"
# new_value = 'новое_значение'

sql = f"""
update salary_dataset 
set job_title = ''
where id = 1
"""

# Выполнение запроса
# cursor.execute(sql_update_query, (new_value,))
cursor.execute(sql)

# Подтверждение изменений
connection.commit()

# Закрытие соединения
connection.close()
