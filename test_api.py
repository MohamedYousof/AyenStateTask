import requests

server_ip = "http://127.0.0.1:8000/api/v1"


def add_task(title, description):
    url = f'{server_ip}/tasks/'
    data = {'title': title, 'description': description}
    resp = requests.post(url, data=data)
    print(resp.json())


def get_tasks():
    url = f'{server_ip}/tasks/'
    resp = requests.get(url)
    print(resp.json())


def get_task_by_id(pk):
    url = f'{server_ip}/tasks/{pk}'
    resp = requests.get(url)
    print(resp.json())


def edit_task(pk, linked_id):
    url = f'{server_ip}/tasks/{pk}/'
    data = {'linked_task': linked_id}
    resp = requests.put(url, data=data)
    print(resp.json())


# add_task('task2', 'this is a new task 2!')

edit_task(1, 3)

# get_tasks()

# get_task_by_id(1)
