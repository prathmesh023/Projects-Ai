import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname='agrosmart',
        user='postgres',
        password='your_actual_password',  # Replace with your PostgreSQL password
        host='localhost',
        port='5432'
    )
