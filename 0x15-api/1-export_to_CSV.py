#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID """
import csv
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

        with open("{}.csv".format(uid), 'w', newline='') as csvfile:
            # Use csv.QUOTE_ALL to wrap every field in quotes
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

            for todo in todos:
                writer.writerow([
                    uid,
                    user['username'],
                    str(todo['completed']),
                    todo['title']
                ])

    except urllib.error.URLError as e:
        print(f"Error fetching the URL: {e.reason}")
