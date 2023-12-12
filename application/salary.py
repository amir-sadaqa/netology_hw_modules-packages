from application.db.db_creation import conn

def calculate_salary(id):
    with conn.cursor() as cur:
        cur.execute(f'''
            SELECT salary FROM salary WHERE employee_id = {id}
        ''')
        salary = cur.fetchone()[0]
        cur.execute(f'''
            SELECT bonus FROM bonus WHERE employee_id = {id}
        ''')
        bonus = cur.fetchone()[0]
        total = salary + bonus

    return total


