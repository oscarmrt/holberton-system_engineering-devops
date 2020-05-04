#!/usr/bin/python3

import json
import requests

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    userDic = {}
    usernameDic = {}
    for u in user:
        userID = u.get('id')
        userDic[userID] = []
        usernameDic[userID] = u.get('username')

    for task in todo:
        taskDic = {}
        userID = task.get('userId')
        taskDic['task'] = task.get('title')
        taskDic['completed'] = task.get('completed')
        taskDic['username'] = usernameDic.get(userID)
        userDic.get(userID).append(taskDic)
    with open('todo_all_employees.json', 'w') as jfile:
        json.dump(userDic, jfile)
