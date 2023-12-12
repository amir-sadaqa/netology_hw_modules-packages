from application.db.db_creation import conn

def get_employees():
    with conn.cursor() as cur:
        cur.execute('''
            SELECT * FROM employee
        ''')
        list_of_employees = cur.fetchall()

    return list_of_employees