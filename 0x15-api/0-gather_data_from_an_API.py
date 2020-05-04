#!/usr/bin/python3

import requests
from sys import argv

if __name__ == "__main__":
    userID = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(userID)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                        format(userID)).json()
    taskDone = []
    for task in todo:
        if task.get('completed') is True:
            taskDone.append(task.get('title'))
    print('Employee {} is done with tasks({}/{}):'.
          format(user.get('name'), len(taskDone), len(todo)))
    print('\n'.join('\t {}'.format(task) for task in taskDone))
