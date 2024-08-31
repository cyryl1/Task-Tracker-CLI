import argparse
from filemanagercli import FileManagerCLI

# Create CLI instance
cli = FileManagerCLI()

parser = argparse.ArgumentParser(description="Task CLI")
subparsers = parser.add_subparsers(dest="command", help="Commands")

# Define the commands
# add command
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("description", type=str, help="Task description")

#update command
update_parser = subparsers.add_parser("update", help="Update a task")
update_parser.add_argument("id", type=int, help="Task ID")
update_parser.add_argument("description", type=str, help="New task description")

# Update status
inProgress_status_parser = subparsers.add_parser("mark_in_progress", help="change status to in progress")
inProgress_status_parser.add_argument("id", type=int, help="Task ID")
doneProgress_status_parser = subparsers.add_parser("mark_done", help="change status to done")
doneProgress_status_parser.add_argument("id", type=int, help="Task ID")

# List objects
list_parser = subparsers.add_parser("list", help="List all tasks")
list_parser.add_argument("status", type=str, nargs='?', default=None, help="List all tasks with the specifies status")


args = parser.parse_args()

if args.command == "add":
    description = args.description
    cli.add(description)

if args.command == "update":
    id = args.id
    description = args.description
    cli.do_update(id, description)

if args.command == "delete":
    id = args.id
    cli.delete(id)

if args.command == "mark-in-progress":
    id = args.id
    cli.mark_in_progress(id)

if args.command == "mark-done":
    id = args.id
    cli.mark_done(id)

if args.command == "list":
    status = args.status
    cli.list(status)

if __name__ == '__main__':
    cli.cmdloop()
