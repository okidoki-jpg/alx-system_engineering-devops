#!/usr/bin/python3
""" Export data in the JSON format """
import requests
import json


def employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data["name"]

    # Get employee's TODO list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Export data to JSON file
    data_to_export = {
        str(employee_id): [
            {"task": task["title"], "completed": task["completed"],
             "username": employee_name}
            for task in todo_data
        ]
    }
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(data_to_export, json_file, indent=2)


if __name__ == "__main__":
    import sys

    employee_todo_progress(int(sys.argv[1]))
