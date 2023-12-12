import psycopg2

conn = psycopg2.connect(
    database="employee_salary",
    user="postgres",
    password=input("Enter your password: ")
)

def drop_db():
    with conn.cursor() as cur:
        cur.execute('''
            DROP TABLE IF EXISTS employee CASCADE;
            DROP TABLE IF EXISTS salary;
            DROP TABLE IF EXISTS bonus;
        ''')
        conn.commit()

def create_db():
    with conn.cursor() as cur:
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS employee(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(40) NOT NULL,
                        surname VARCHAR(40) NOT NULL
                    );
        ''')
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS salary(
                        id SERIAL PRIMARY KEY,
                        salary INTEGER NOT NULL,
                        employee_id INTEGER UNIQUE NOT NULL REFERENCES employee(id) ON DELETE CASCADE
                    );
        ''')
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS bonus(
                        id SERIAL PRIMARY KEY,
                        bonus INTEGER NOT NULL,
                        employee_id INTEGER UNIQUE REFERENCES employee(id) ON DELETE CASCADE
                    );
        ''')
        conn.commit()

def add_employee(name, surname):
    with conn.cursor() as cur:
        cur.execute(f'''
            INSERT INTO employee(name, surname) VALUES('{name}', '{surname}');
        ''')
        conn.commit()

def add_salary(employee_id, salary):
    with conn.cursor() as cur:
        cur.execute(f'''
            INSERT INTO salary(employee_id, salary) VALUES({employee_id}, {salary});
        ''')
        conn.commit()

def add_bonus(employee_id, bonus):
    with conn.cursor() as cur:
        cur.execute(f'''
            INSERT INTO bonus(employee_id, bonus) VALUES({employee_id}, {bonus});
        ''')
        conn.commit()

if __name__ == '__main__':
    drop_db()
    create_db()
    add_employee('Иван', 'Иванов')
    add_employee('Петр', 'Петров')
    add_salary(1, 100000)
    add_salary(2, 80000)
    add_bonus(1, 50000)
    add_bonus(2, 30000)


