import psycopg2

db_params = {
  "host": "localhost",
  "database": "ict",
  "user": "ictuser",
  "password": " "
}

# Список с данными о курсах
courses_data = [
    {
        "course_name": "Математика",
        "teacher_id": 1  
    },
    {
        "course_name": "История Мира",
        "teacher_id": 2  
    },
    {
        "course_name": "Физика для начинающих",
        "teacher_id": 3   
    },
    {
        "course_name": "Литературное искусство",
        "teacher_id": 4   
    },
    {
        "course_name": "Биология в действии",
        "teacher_id": 5   
    },
    {
        "course_name": "Основы программирования",
        "teacher_id": 6   
    },
    {
        "course_name": "Химические реакции",
        "teacher_id": 7   
    },
    {
        "course_name": "Иностранные языки",
        "teacher_id": 8   
    },
    {
        "course_name": "Искусство и культура",
        "teacher_id": 9   
    },
    {
        "course_name": "Основы экономики",
        "teacher_id": 10   
    }
]

try:
    # Установка соединения с базой данных
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # SQL-запрос для вставки данных о курсах
    insert_query = """
    INSERT INTO Courses (course_name, teacher_id)
    VALUES (%(course_name)s, %(teacher_id)s);
    """

    # Вставка данных о курсах
    for course in courses_data:
        cursor.execute(insert_query, course)
    
    # Фиксация изменений
    conn.commit()
    
    print("Данные о курсах успешно вставлены в таблицу Courses.")
    
except (Exception, psycopg2.DatabaseError) as error:
    print("Ошибка при вставке данных:", error)

finally:
    # Закрытие соединения
    if conn:
        conn.close()
