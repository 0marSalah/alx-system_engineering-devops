#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID """
import sys
import urllib.request
import urllib.error
import json

id = sys.argv[1]

users_url = 'https://jsonplaceholder.typicode.com/users/' + id
todo_url = 'https://jsonplaceholder.typicode.com/todos/'

try:
    with urllib.request.urlopen(users_url) as res:
        data = res.read().decode('utf-8')
        user = json.loads(data)

    with urllib.request.urlopen(todo_url) as res:
        data = json.loads(res.read().decode('utf-8'))
        todos = []
        done_tasks = 0
        completed_tasks = []
        for todo in data:
            if todo['userId'] == int(id):
                todos.append(todo)
                if todo['completed'] is True:
                    done_tasks += 1
                    completed_tasks.append(todo['title'])

        name = user['name']
        total_tasks = len(todos)
        print(
            f"Employee {name} is done with tasks({done_tasks}/{total_tasks}):"
        )
        for task in completed_tasks:
            print('\t' + task)

except urllib.error.URLError as e:
    print(f"Error fetching the URL: {e.reason}")
