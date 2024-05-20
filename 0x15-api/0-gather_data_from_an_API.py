#!/usr/bin/python3
'''A Python Module'''
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user_endpoint = "{}/users/{}".format(url, user_id)
    name = requests.get(user_endpoint).json().get("name")
    tasks_endpoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = [task for task in tasks if task.get('userId') == user_id]
    completed_tasks = [task for task in user_tasks if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(completed_tasks), len(user_tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
