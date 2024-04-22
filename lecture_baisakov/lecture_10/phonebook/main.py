import psycopg2
import csv

def create_tables():
    """Создание таблиц в базе данных PostgreSQL."""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(32) NOT NULL,
            last_name VARCHAR(32) NOT NULL,
            phone_number VARCHAR(11) NOT NULL
        )
        """,
    )
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_data():
    """Вставка данных в таблицу."""
    data = (input("Введите имя: "), input("Введите фамилию: "), input("Введите номер телефона: "))
    command = """
        INSERT INTO phonebook(name, last_name, phone_number) 
        VALUES(%s, %s, %s)
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as conn:
            with conn.cursor() as cur:
                cur.execute(command, data)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def from_csv():
    command = """
        INSERT INTO phonebook(name, last_name, phone_number) 
        VALUES(%s, %s, %s)
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as conn:
            with conn.cursor() as cur:
                with open('numbers.csv', 'r', newline='') as file:
                    rows = csv.reader(file)
                    
                    for data in rows:
                        with conn.cursor() as cur:
                            cur.execute(command, (data[0], data[1], data[2]))

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
def delete_data():
    """Удаление данных из таблицы на основе имени."""
    name = input("Введите имя: ")
    
    command = """
        DELETE FROM phonebook 
        WHERE name = %s;
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as conn:
            with conn.cursor() as cur:
                cur.execute(command, (name,))
                print(f"Удалено записей: {cur.rowcount}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def check_data(id: bool):
    """Удаление данных из таблицы на основе имени."""
    if id:
        command = """
            SELECT id, name, last_name, phone_number FROM phonebook ORDER BY id;
        """
    else:
        command = """
            SELECT id, name, last_name, phone_number FROM phonebook ORDER BY name;
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                print("-----------------------------------------------------")
                for data in cur.fetchall():
                    print(f"| {data[0]} | {data[1]} | {data[2]} | {data[3]} |")
                
                print(f"Удалено записей: {cur.rowcount}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    create_tables()
    insert_data()
    from_csv()
    delete_data()
    check_data(True)
    
    
