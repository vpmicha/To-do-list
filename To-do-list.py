import json

class To_do_list():
    def __init__(self):
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
            list = json.load(file)
            return str(list)

    

        
            
        

