from .models import Task

"""
Arquivo responsável pelas regras de negócio da aplicação.

Aqui ficam as funções que manipulam os dados.
As rotas apenas chamam essas funções.
"""

# Simulação de banco de dados em memória
tasks = list()
next_id = 1

def get_all_tasks():
    return [task.to_dict() for task in tasks]

def create_task(title):
    global next_id
    task = Task(next_id, title)
    tasks.append(task)
    next_id += 1
    return task.to_dict()

def update_task(task_id, data):
    for task in tasks:
        if task.id == task_id:
            task.title = data.get("title", task.title)
            task.completed = data.get("completed", task.completed)
            return task.to_dict()
    return None

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]