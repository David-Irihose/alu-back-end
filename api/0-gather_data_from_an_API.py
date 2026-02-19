#!/usr/bin/python3
#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
Fetches an employee's TODO list progress from a REST API.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys


def fetch_employee_todos(employee_id):
    """Fetch employee name and their TODO list from the API."""
    # Get employee info
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    employee_resp = requests.get(employee_url)
    todos_resp = requests.get(todos_url)

    if employee_resp.status_code != 200 or todos_resp.status_code != 200:
        print("Failed to retrieve data from API")
        return

    employee_name = employee_resp.json().get("name")
    todos_list = todos_resp.json()

    # Count total and done tasks
    total_tasks = len(todos_list)
    done_tasks = len([t for t in todos_list if t.get("completed")])

    # Print first line
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")

    # Print completed tasks
    for task in todos_list:
        if task.get("completed"):
            print("\t", task.get("title"))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_todos(employee_id)
        except ValueError:
            print("Employee ID must be an integer")

