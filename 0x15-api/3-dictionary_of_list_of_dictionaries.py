#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID """
import json
import urllib.error
import urllib.request

if __name__ == "__main__":
    users_url = 'https://jsonplaceholder.typicode.com/users/'
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'

    try:
        with urllib.request.urlopen(users_url) as res:
            users = res.read().decode('utf-8')

        with urllib.request.urlopen(todo_url) as res:
            todos = json.loads(res.read().decode('utf-8'))

        # TODO Export all record to JSON
        with open("todo_all_employees.json", 'w', newline='') as json_file:
            data = {
                user['id']: [
                    {
                        "username": user['username'],
                        "task": todo['title'],
                        "completed": todo['completed']
                    } for todo in todos if todo['userId'] == user['id']
                ] for user in json.loads(users)
            }
            json.dump(data, json_file)

    except urllib.error.URLError as e:
        print(f"Error fetching the URL: {e.reason}")
