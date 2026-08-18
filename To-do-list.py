import json
import sys

class To_do_list():
    def __init__(self):
        self.tasks = {}

    def add_task(self,task):
        if task not in self.tasks:
            self.tasks[task] = False
        else:
            print('Task already in to-do list')
            
    def add_task(self, task):
        if task not in self.tasks:
            self.task[task] = 'False'
        else:
            print('Task already in to-do list')

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
        else:
            print('Task not found')
            
        
            
        

