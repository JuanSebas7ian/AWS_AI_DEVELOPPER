from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

class TaskManager:
    def __init__(self):
        self.file = "tasks.json"
        self.tasks = self.load()

    def load(self):
        if os.path.exists(self.file):
            with open(self.file) as f:
                return json.load(f)
        return []

    def save(self):
        with open(self.file, 'w') as f:
            json.dump(self.tasks, f)

    def add(self, name, priority):
        self.tasks.append({"name": name, "priority": priority})
        self.tasks.sort(key=lambda x: x["priority"])
        self.save()

    def remove(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save()

manager = TaskManager()

@app.route('/')
def index():
    return render_template('index.html', tasks=manager.tasks)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name', '').strip()
    priority = request.form.get('priority', '').strip()
    if name and priority:
        manager.add(name, priority)
    return redirect('/')

@app.route('/remove/<int:index>')
def remove(index):
    manager.remove(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)