#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID """
import json
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    uid = sys.argv[1]

    users_url = 'https://jsonplaceholder.typicode.com/users/' + uid
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'

    try:
        with urllib.request.urlopen(users_url) as res:
            data = res.read().decode('utf-8')
            user = json.loads(data)

        with urllib.request.urlopen(todo_url) as res:
            data = json.loads(res.read().decode('utf-8'))
            todos = []
            for todo in data:
                if todo['userId'] == int(uid):
                    todos.append(todo)

        # TODO Export to JSON
        with open("{}.json".format(uid), 'w', newline='') as json_file:
            data = {
                uid: [
                    {
                        "task": todo['title'],
                        "completed": todo['completed'],
                        "username": user['username']
                    } for todo in todos
                ]
            }
            json.dump(data, json_file)

    except urllib.error.URLError as e:
        print(f"Error fetching the URL: {e.reason}")
