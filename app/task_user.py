import math
import json
from typing import Dict, List, Tuple
import random
from random import randint, choice

class TaskData:
    def __init__(self, data):
        self.data: Dict[str, Dict[str, List, Dict[str, str]]] = data

    @classmethod
    def load_json(cls, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)[0]
            return cls(data)

    @staticmethod
    def task_code(txt_task) -> Tuple[str, float]:
        lcls = dict(rad = math.radians,
                    grad = lambda x: 180 * x / math.pi)
        glbl = {
            'pi': math.pi,
            'cos': math.cos,
            'sin': math.sin,
            'tan': math.tan,
            'arctan': math.atan,
            'randint': randint,
            'choice': choice,
            'random': random
        }
        exec(txt_task, glbl, lcls)
        return lcls['text'], lcls['result']

    @staticmethod
    def derivative(f,a,method='central', h=0.01):
        if method == 'central':
            return (f(a + h) - f(a - h))/(2*h)
        elif method == 'forward':
            return (f(a + h) - f(a))/h
        elif method == 'backward':
            return (f(a) - f(a - h))/h
        else:
            print("Method must be 'central', 'forward' or 'backward'.")

    def get_list_tasks(self, group: str, level: str) -> List[Dict[str, str]]:
        return self.data[group][level]

    def get_task(self, number: int = 0, level: str = 3):
        tasks = self.get_list_tasks("STATICS", level)
        return self.run_task(tasks[number])

    def get_all_tasks(self, level: str = "3") -> List[dict]:
        tasks = []
        for task in self.get_list_tasks("STATICS", level):
            text, number = self.run_task(task)
            tasks.append({"text": text, "image": task['image'], "answer": number, "max_error": 0.05})
        return tasks

    def run_task(self, task: Dict[str, str]):
        text, number = self.task_code(task["code"])
        return text.replace('\n', '').strip(), number

task = TaskData.load_json("/root/stepik/theorethical_mechanics/app/DYNRAND.json")
print(*task.get_all_tasks(), sep='\n')