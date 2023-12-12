from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime

if __name__ == '__main__':
    print(get_employees(), datetime.now())
    print(calculate_salary(1), datetime.now())
    print(calculate_salary(2), datetime.now())

