import json
from datetime import datetime

def lambda_handler(event, context):
    agent = event['agent']
    action_group = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])
    
    params = {param['name']: param['value'] for param in parameters}
    
    if function == 'addTask':
        return add_task(params)
    elif function == 'getTasks':
        return get_tasks()
    elif function == 'removeTask':
        return remove_task(params)
    
    return create_response(action_group, function, f"Unknown function: {function}")

def add_task(params):
    task_name = params.get('taskName', '')
    priority = int(params.get('priority', 3))
    
    return create_response('TaskManager', 'addTask', 
        f"Task '{task_name}' added with priority {priority}")

def get_tasks():
    tasks = [
        {'name': 'Complete project', 'priority': 1},
        {'name': 'Review code', 'priority': 2}
    ]
    
    task_list = "\n".join([f"- {task['name']} (Priority: {task['priority']})" for task in tasks])
    
    return create_response('TaskManager', 'getTasks', f"Current tasks:\n{task_list}")

def remove_task(params):
    task_id = params.get('taskId', '')
    return create_response('TaskManager', 'removeTask', f"Task {task_id} removed")

def create_response(action_group, function, message):
    return {
        'response': {
            'actionGroup': action_group,
            'function': function,
            'functionResponse': {
                'responseBody': {
                    'TEXT': {
                        'body': message
                    }
                }
            }
        }
    }