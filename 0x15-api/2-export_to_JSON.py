#!/usr/bin/python3

import json
import requests
from sys import argv

if __name__ == "__main__":
    userID = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(userID)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                        format(userID)).json()
    taskList = []
    for task in todo:
        taskDic = {}
        taskDic['task'] = task.get('title')
        taskDic['completed'] = task.get('completed')
        taskDic['username'] = user.get('username')
        taskList.append(taskDic)
    jsonObject = {}
    jsonObject[userID] = taskList
    with open('{}.json'.format(userID), 'w') as jfile:
        json.dump(jsonObject, jfile)
