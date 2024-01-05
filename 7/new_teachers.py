import psycopg2

db_params = {
  "host": "localhost",
  "database": "ict",
  "user": "ictuser",
  "password": "qwerty90"
}

# Список с данными о преподавателях
teachers_data = [
  {
    "first_name": "Иван",
    "last_name": "Петров",
    "department": "Математика"
  },
  {
    "first_name": "Ольга",
    "last_name": "Смирнова",
    "department": "История"
  },
  {
    "first_name": "Александр",
    "last_name": "Иванов",
    "department": "Физика"
  },
  {
    "first_name": "Екатерина",
    "last_name": "Козлова",
    "department": "Литература"
  },
  {
    "first_name": "Михаил",
    "last_name": "Соколов",
    "department": "Биология"
  },
  {
    "first_name": "Анна",
    "last_name": "Королева",
    "department": "Информатика"
  },
  {
    "first_name": "Сергей",
    "last_name": "Мельников",
    "department": "Химия"
  },
  {
    "first_name": "Ирина",
    "last_name": "Андреева",
    "department": "Иностранные языки"
  },
  {
    "first_name": "Владимир",
    "last_name": "Лебедев",
    "department": "Искусство"
  },
  {
    "first_name": "Надежда",
    "last_name": "Григорьева",
    "department": "Экономика"
  }
]

try:
  # Установка соединения с базой данных
  conn = psycopg2.connect(**db_params)
  cursor = conn.cursor()

  # SQL-запрос для вставки данных о преподавателях
  insert_query = """
  INSERT INTO Teachers (first_name, last_name, department)
  VALUES (%(first_name)s, %(last_name)s, %(department)s);
  """

  # Вставка данных о преподавателях
  for teacher in teachers_data:
    cursor.execute(insert_query, teacher)

  # Фиксация изменений
  conn.commit()
  
  print("Данные о преподавателях успешно вставлены в таблицу Teachers.")
  
except (Exception, psycopg2.DatabaseError) as error:
  print("Ошибка при вставке данных:", error)

finally:
  # Закрытие соединения
  if conn:
      conn.close()
