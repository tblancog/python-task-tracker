#!/usr/bin/python3

import sys
import json
import os

tasks = []
tasks_file = "tasks.json"

def load_tasks():
  if os.path.exists(tasks_file):
    with open(tasks_file, "r") as f:
      return json.load(f)
  return []

def save_tasks():
  with open(tasks_file, "w") as f:
    json.dump(tasks, f, indent=2)

def find_by_id(target_id):
  for task in tasks:
    if task["id"] == target_id:
      return task
  return None

def filter_by_status(status = None):
  filtered_tasks = [task for task in tasks if task.get("status") == status]
  return filtered_tasks

def pretty_print_tasks(items):
    if not items:
        print("No tasks found.")
        return
    
    print("ID | Status      | Description")
    print("-" * 40)
    for task in items:
        print(f"{task['id']:2d} | {task['status']:<11} | {task['task']}")

def main():

  global tasks
  if len(sys.argv) < 2:
    print(f"""Should enter:
             to add task:    "add" <task name>
             to update task: "update" <task name> <ID>
             to delete task: "delete" <ID>
             to mark done:   "mark-done" <ID>
             to list: "list"
          """)
    return
  


  operation = sys.argv[1]
  if not operation in ['add', 'update', 'delete', 'list', 'mark-done', 'mark-in-progress']:
    print('Invalid operation')
    return
  
  tasks = load_tasks()

  if operation == 'list':
    status_arg = None
    if len(sys.argv) > 2:
      status_arg = sys.argv[2]
    result = []
    if status_arg in ['todo', 'in-progress', 'done']:
      result = filter_by_status(status_arg)
      pretty_print_tasks(result)
      return
    else:
      print("Status unknown listing all.\n")
    result = tasks
    pretty_print_tasks(result)

  elif operation == 'add':
    task_data = sys.argv[2]
    status = 'todo'
    task_id = len(tasks) + 1
    tasks.append({ "id": task_id, "task": task_data, "status": status})
    print(f"Task Added: {task_data}")
  
  elif operation == 'update':
    task_data = sys.argv[2]
    if len(sys.argv) < 4:
      print(f"No ID provided to update")
      return
    
    task_id = sys.argv[3]
    task = find_by_id(int(task_id))
    if not task:
      print(f"No task found")
      return
    
    task["task"] = task_data
    print(f"Task updated: ID: {task_id} -> {task_data}.")

  elif operation == 'delete':
    task_id = sys.argv[2]
    task = find_by_id(int(task_id))
    if not task:
      print(f"No task found")
      return
    tasks.remove(task)

  elif operation == 'mark-done':
    task_id = sys.argv[2]
    task = find_by_id(int(task_id))
    if not task:
      print(f"No task found")
      return
    task["status"] = "done"

  elif operation == 'mark-in-progress':
    task_id = sys.argv[2]
    task = find_by_id(int(task_id))
    if not task:
      print(f"No task found")
      return
    task["status"] = "in-progress"


  
    

  save_tasks()

if __name__ == '__main__':
  main()