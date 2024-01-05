import tkinter as tk
import psycopg2

def execute_query(input_text, output_listbox):
    dbname = 'ict'
    user = 'ictuser'
    password = 'qwerty90'
    host = 'localhost'

    connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = connection.cursor()

    query = f"SELECT course_name FROM public.courses ORDER BY id ASC" # Надо заменить
    cursor.execute(query)

    results = cursor.fetchall()
    print(results)
    output_listbox.delete(0, tk.END)
    for result in results:
        output_listbox.insert(tk.END, result[0])

    cursor.close()
    connection.close()

def on_submit(entry, listbox):
    input_text = entry.get()
    execute_query(input_text, listbox)

def on_item_select(event):
    global selected_index 
    selected_index = result_listbox.curselection()
    if selected_index:
        selected_item = result_listbox.get(selected_index)
        print(f"Selected item: {selected_item+1}")
        
def on_next_page_button_click(item_id):
    if item_id == -1:
        return 
    print(item_id)
    
    dbname = 'ict'
    user = 'ictuser'
    password = 'qwerty90'
    host = 'localhost'

    connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = connection.cursor()

    query = f"SELECT * FROM public.courses where id={item_id[0]}" # Надо заменить
    cursor.execute(query)

    result = cursor.fetchone()
    print(result)
    
    
       

# Создание графического интерфейса
root = tk.Tk()
root.title("Пример с PostgreSQL")

# Поле для ввода текста
entry_label = tk.Label(root, text="Введите текст:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

# Кнопка для отправки запроса
submit_button = tk.Button(root, text="Отправить запрос", command=lambda: on_submit(entry, result_listbox))
submit_button.pack()

# Список для отображения результатов
result_listbox = tk.Listbox(root)
result_listbox.pack()

# Привязка функции on_item_select к событию выделения элемента в списке
selected_index = -1
result_listbox.bind('<<ListboxSelect>>', on_item_select)

# Кнопка для перехода на другую страницу
next_page_button = tk.Button(root, text="Следующая страница", command=lambda: on_next_page_button_click(selected_index))
next_page_button.pack()

root.mainloop()