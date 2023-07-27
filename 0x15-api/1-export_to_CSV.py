#!/usr/bin/python3
""" Export data in the CSV format """
import requests
import csv


def employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data["name"]

    # Get employee's TODO list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Export data to CSV
    file_name = f"{employee_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME",
                        "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            writer.writerow([employee_id, employee_name,
                             task["completed"], task["title"]])


if __name__ == "__main__":
    import sys

    employee_todo_progress(int(sys.argv[1]))
