import cmd
import os
import json
from datetime import datetime
import os



class FileManagerCLI(cmd.Cmd):
    """CLI commands goes here"""
    # Create prompt text
    prompt = "task-cli>> "
    # Intro message
    intro = "Welcome to the Task CLI!"
    
    

    def __init__(self):
        super().__init__()
        self.current_directory = os.getcwd()
        self.filepath = 'file.json'
        __objects = {}

    def do_add(self, line):
        """
        add a new task
        """
        json_objects = {}
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            # if file not found create a new list
            data = []

        if data:
            next_id = data[-1]['id'] + 1
        else:
            next_id = 1

        json_objects['id'] = next_id
        json_objects['description'] = line
        json_objects['status'] = 'todo'
        json_objects['createdAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        json_objects['updatedAt'] = json_objects['createdAt']

        data.append(json_objects)

        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)
            print(f"Task added successfully (ID: {json_objects['id']})")

    def do_update(self, args):
        """
        update a task description
        """
        try:
            parts = args.split(" ", 1)

            id = int(parts[0])
            new_description = parts[1]

            with open(self.filepath, 'r') as f:
                data = json.load(f)

            for task in data:
                if task['id'] == id:
                    task['description'] = new_description
                    task['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    break

            with open(self.filepath, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Task updated successfully (ID: {id})")
        except IndexError:
            print("Please provide an ID and a new description.")
        except ValueError:
            print("ID must be a number")
        except FileNotFoundError:
            print("Task file not found")
    

    def do_delete(self, args):
        """
        delete a task
        """
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)

                found = False
                for task in data:
                    if task['id'] == int(args):
                        data.remove(task)
                        found = True
                        print("Task removed successfully")
                        break
                if not found:
                    print(f"Task with ID: {args} not found")

                with open(self.filepath, 'w') as f:
                    json.dump(data, f, indent=4)

        except FileNotFoundError:
            print("Task file not found")
        except json.JSONDecodeError:
            print("Error reading task file")

    
    def do_mark_in_progress(self, args):
        """
        change a task status to in-progress
        """
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)

                found = False
                for task in data:
                    if task['id'] == int(args):
                        found = True
                        task['status'] = 'in-progress'
                        task['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        break
                if not found:
                    print("File not found")

                with open(self.filepath, 'w') as f:
                    json.dump(data, f, indent=4)

        except FileNotFoundError:
            print("Task file not found")
        except json.JSONDecodeError:
            print("Error reading task file")

    def do_mark_done(self, args):
        """
        change a task status to done
        """
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)

                found = False
                for task in data:
                    if task['id'] == int(args):
                        found = True
                        task['status'] = 'done'
                        task['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        break
                if not found:
                    print("File not found")

                with open(self.filepath, 'w') as f:
                    json.dump(data, f, indent=4)

        except FileNotFoundError:
            print("Task file not found")
        except json.JSONDecodeError:
            print("Error reading task file")

    def do_list(self, line=None):
        """
        list all tasks, if status specified, list task with the
        specified status.
        """
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)

                found = False
                if not line:
                    for task in data:
                        print(task)
                    found = True
                else:
                        for task in data:
                            if task['status'] == line:
                                print(task)
                        found = True
                if not found:
                    print("Task not found")

        except FileNotFoundError:
            print("Task file not found")
        except json.JSONDecodeError:
            print("Error reading task file")

    def do_clear(self, args):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_exit(self, line):
        """Exit CLI"""
        return True
