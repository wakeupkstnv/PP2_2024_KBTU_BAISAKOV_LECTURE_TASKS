import psycopg2

def delete_data(count):
    for _ in range(count):
        name, number = input(), input()        
        command = """
        CALL dlt(%s, %s)
            """
        try:
            with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345") as conn:
                with conn.cursor() as cur:
                    cur.execute(command, (name, number))
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
            