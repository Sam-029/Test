'''
first priority to deadline so sorted that and than 
Then loop through the sorted list and keep allocating time
to tasks as long as total time does not exceed the deadline of the current task.
then just added completed task.
'''

def max_tasks(tasks):
    tasks.sort(key=lambda x: x['deadline'])

    total_time = 0
    selected_tasks = []

    for task in tasks:
        if total_time + task['duration'] <= task['deadline']:
            total_time += task['duration']
            selected_tasks.append(task['name'])

    return selected_tasks

tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 5, 'duration': 3},
]

result = max_tasks(tasks)
print("Maximum tasks that can be completed:", result)