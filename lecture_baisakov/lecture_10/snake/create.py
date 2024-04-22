import psycopg2

def create_tables():
    
    commands = (
        """
        CREATE TABLE IF NOT EXISTS scores (
            id SERIAL PRIMARY KEY,
            user_name VARCHAR(32) NOT NULL,
            score INT NOT NULL
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


