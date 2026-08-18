import json
import sys

class To_do_list():
    def __init__(self):
        self.tasks = {}

    def add_task(self,task):
        if task not in self.tasks:
            self.tasks[task.lower()] = False
        else:
            print('Task already in to-do list')
            
    def add_task(self, task):
        if task.lower() not in self.tasks:
            self.task[task.lower()] = 'Not Done'
        else:
            print('Task already in to-do list')

    def remove_task(self, task):
        if task.lower() in self.tasks:
            del self.tasks[task.lower()]
        else:
            print('Task not found')

    def complete(self, task):
        if task.lower() in self.tasks:
            self.tasks[task.lower()] = 'Done'
        else:
            print('Could not mark as done since task does not exist')

        
            
        

