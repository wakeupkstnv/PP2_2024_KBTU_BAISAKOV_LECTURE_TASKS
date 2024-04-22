import psycopg2

def insert_data(nickname):
    """Вставка данных в таблицу."""
    data = (nickname, 0)
    command = """
        INSERT INTO scores(user_name, score) 
        VALUES(%s, %s)
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as conn:
            with conn.cursor() as cur:
                cur.execute(command, data)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
