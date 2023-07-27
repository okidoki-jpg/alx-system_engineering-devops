#!/usr/bin/python3
""" Export all data in the JSON format """
import requests
import json


def export_todo_all_employees():
    base_url = "https://jsonplaceholder.typicode.com"

    # Get all users
    users_response = requests.get(f"{base_url}/users")
    users_data = users_response.json()

    # Create a dictionary to store tasks of all employees
    all_tasks = {}

    for user in users_data:
        user_id = user["id"]
        username = user["username"]

        # Get TODO list for the current user
        todo_response = requests.get(f"{base_url}/todos?userId={user_id}")
        todo_data = todo_response.json()

        # Store the tasks of the current user
        user_tasks = []
        for task in todo_data:
            task_entry = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            user_tasks.append(task_entry)

        # Add the user's tasks to the dictionary
        all_tasks[user_id] = user_tasks

    # Create the final data format with user IDs as keys
    final_data = json.dumps(all_tasks, indent=2)

    # Write the data to the JSON file
    with open("todo_all_employees.json", "w") as file:
        file.write(final_data)


if __name__ == "__main__":
    export_todo_all_employees()
