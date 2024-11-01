
# Task Manager CLI

A simple task manager built in Python, allowing users to add, update, delete, list, and modify task statuses in a command-line environment. Tasks are stored in a JSON file (`tasks.json`).

## Features
- Add, update, and delete tasks
- List tasks by status
- Mark tasks as "done" or "in-progress"
- Save tasks to `tasks.json`

## Prerequisites
- Python 3.x

## Project URL
[Roadmap.sh Task tracker](https://roadmap.sh/projects/task-tracker)

## Setup
Clone the repository and navigate to the project directory.

## Usage
Run the script using the following command:

```bash
python3 task_manager.py <operation> [arguments]
```

### Operations

| Operation           | Arguments                | Description                                         |
|---------------------|--------------------------|-----------------------------------------------------|
| `add`               | `<task name>`            | Adds a new task with status `todo`.                 |
| `update`            | `<task name> <ID>`       | Updates the description of an existing task by ID.  |
| `delete`            | `<ID>`                   | Deletes a task by ID.                               |
| `mark-done`         | `<ID>`                   | Marks a task as `done`.                             |
| `mark-in-progress`  | `<ID>`                   | Marks a task as `in-progress`.                      |
| `list`              | `[status]`               | Lists all tasks, or tasks filtered by `todo`, `in-progress`, or `done` status. |

### Examples

#### Add a Task
```bash
python3 task_manager.py add "Finish documentation"
```

#### Update a Task
```bash
python3 task_manager.py update "Review pull requests" 2
```

#### Delete a Task
```bash
python3 task_manager.py delete 3
```

#### Mark a Task as Done
```bash
python3 task_manager.py mark-done 4
```

#### List All Tasks
```bash
python3 task_manager.py list
```

#### List Tasks by Status
```bash
python3 task_manager.py list done
```

## File Structure
- `tasks.json`: Stores all tasks in JSON format.

## License
This project is licensed under the MIT License.

---

Happy task managing!
