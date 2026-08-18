import json

class To_do_list():
    def __init__(self):
        try:
            with open('To do list', 'r') as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = {}
            
    def add_task(self,task):
        if task.lower() not in self.tasks:
            self.tasks[task.lower()] = 'Not Done'
            with open('To do list', 'w') as file:
                json.dump(self.tasks, file)
        else:
            print('Task already in to-do list')
            
    def remove_task(self, task):
        if task.lower() in self.tasks:
            del self.tasks[task.lower()]
            with open('To do list', 'w') as file:
                json.dump(self.tasks, file)
        else:
            print('Task not found')

    def complete(self, task):
        if task.lower() in self.tasks:
            self.tasks[task.lower()] = 'Done'
            with open('To do list', 'w') as file:
                json.dump(self.tasks, file)
        else:
            print('Could not mark as done since task does not exist')
    
    def __str__(self):
        with open('To do list', 'r') as file:
            return str(json.load(file))
           

todo = To_do_list()
todo.add_task('Learn Git and GitHub')
todo.add_task('Learn Machine learning')
todo.add_task('Learn Python')
todo.add_task('Learn Linear Algebra')

print(todo)

todo.remove_task('Learn Linear Algebra')
todo.complete('Learn Git and GitHub')
todo.complete('Learn Python')

print(todo)
        
            
        

