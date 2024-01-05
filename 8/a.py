import psycopg2

dbname = 'example1'
user = 'example1'
password = 'pass123'
host = 'localhost'

connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cursor = connection.cursor()

query = f"delete FROM analytics.amazon where product_id='B07JW9H4J1'" # Надо заменить
cursor.execute(query)

results = cursor.fetchall()
print(results[:5])