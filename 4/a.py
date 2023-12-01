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

# Пример SQL-запроса для создания записи
# sql_insert_query = "INSERT INTO salary_dataset (id, ...) VALUES (%s, %s, %s);"
# record_to_insert = ('значение1', 'значение2', 'значение3')

sql = f'''
insert into salary_dataset (id, ...)
values ({1}, {23}, {'fasdfae'})
'''

# Выполнение запроса
# cursor.execute(sql_insert_query, record_to_insert)
cursor.execute(sql)

# Подтверждение изменений
connection.commit()

# Закрытие соединения
connection.close()
