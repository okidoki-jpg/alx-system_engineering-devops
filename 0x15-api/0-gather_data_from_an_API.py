#!/usr/bin/python3
"""Return information about user TODO list progress"""
import requests


def employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data["name"]

    # Get employee's TODO list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Calculate progress
    total = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    # Display progress
    print(f"Employee {employee_name} is done with\
 tasks({completed_tasks}/{total}):")

    # Display completed task titles
    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    import sys

    employee_todo_progress(int(sys.argv[1]))
