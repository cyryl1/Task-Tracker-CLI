# Task Tracker

Task Tracker is a command-line interface (CLI) application designed to help you track and manage your tasks efficiently. This project allows you to monitor what needs to be done, what you are currently working on, and what you have already completed. It’s a great way to practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

## Features

- Add a Task: Create a new task with a description.
- Update a Task: Modify the description of an existing task.
- Delete a Task: Remove a task from the list.
- Mark a Task as In Progress: Change the status of a task to "in-progress."
- Mark a Task as Done: Change the status of a task to "done."
- List All Tasks: Display all tasks regardless of their status.
- Filter Tasks by Status: Display tasks based on their status (todo, in-progress, or done).

## Requirements

- The application should run from the command line, accept user actions and inputs as arguments, and store tasks in a JSON file.
- The JSON file should be stored in the current directory and created automatically if it does not exist.
- The application should handle errors and edge cases gracefully.
- No external libraries or frameworks should be used; only native modules provided by the programming language.

## Task Properties

Each task in the JSON file should have the following properties:

- id: A unique identifier for the task.
- description: A short description of the task.
- status: The status of the task (`todo`, `in-progress`, or `done`).
- createdAt: The date and time when the task was created.
- updatedAt: The date and time when the task was last updated.

## Example Commands

Below are some example commands and their expected outputs:

### Adding a New Task
task-cli>> add "Buy groceries"
# Output: Task added successfully (ID: 1)

### Updating and Deleting Tasks
task-cli>> update 1 "Buy groceries and cook dinner"
task-cli>> delete 1

### Marking a Task as In Progress or Done
task-cli>> mark_in_progress 1
task-cli>> mark_done 1

### Listing All Tasks
task-cli>> list

### Listing Tasks by Status
task-cli>> list done
task-cli>> list todo
task-cli>> list in_progress

## Constraints

- You can use any programming language to build this project.
- Use positional arguments in the command line to accept user inputs.
- Store tasks in a JSON file using the native file system module of your programming language.


## Project URL
- (https://roadmap.sh/projects/task-tracker)

## How to Run

1. Clone the repository.
2. Navigate to the directory where the project is located.
3. Run the CLI commands as demonstrated in the examples.

