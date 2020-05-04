#!/usr/bin/python3

import csv
import requests
from sys import argv

if __name__ == "__main__":
    userID = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(userID)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                        format(userID)).json()
    with open('{}.csv'.format(userID), 'w', newline='') as cfile:
        writer = csv.writer(cfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([int(userID),
                             user.get('username'),
                             task.get('completed'),
                             task.get('title')])
