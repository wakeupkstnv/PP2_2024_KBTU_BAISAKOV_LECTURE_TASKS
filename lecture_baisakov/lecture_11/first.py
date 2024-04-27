import psycopg2

def part_of_name(insert):
    """Вставка данных в таблицу."""
    
    command = """
        SELECT * FROM part_of_name(%s);
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as conn:
            with conn.cursor() as cur:
                cur.execute(command, (insert, ))
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def delete_data(name, number):
    
    command = """
    CALL dlt(%s, %s)
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as conn:
            with conn.cursor() as cur:
                cur.execute(command, (name, number))
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)



