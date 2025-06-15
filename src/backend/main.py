from fastapi import FastAPI
from pydantic import BaseModel
import json
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



with open('./todos.json', 'r') as file:
    todos = json.load(file)

todos = sorted(
    todos,
    key=lambda task: datetime.strptime(task["Date"], "%d-%m-%y"),
    reverse=True  # ← DESCENDING order
)


# Return the latest 3 pending and 3 completed todos
@app.get('/home_todos')
def get_home_todos():
    home_todos = []
    pending_todos = []
    completed_todos = []
    for todo in todos:
        if todo["Status"] == "Incomplete":
            pending_todos.append(todo)
        if len(pending_todos) >= 3:
            break
    
    for todo in todos:
        if todo["Status"] == "Complete":
            completed_todos.append(todo)
        if len(completed_todos) >= 3:
            break

    home_todos = [*pending_todos, *completed_todos]
    return home_todos
    
# Return all the todos
@app.get('/all_todos')
def get_all_todos():
    return todos

@app.get('/pending_todos')
def get_pending_todos():
    return [todo for todo in todos if todo["Status"] == "Incomplete"]

@app.get('/completed_todos')
def get_completed_todos():
    return [todo for todo in todos if todo["Status"] == "Complete"]

class TodoItem(BaseModel):
    id: int
    Description: str
    Status: str
    Date: str

@app.post('/add_todo')
def add_new_todo(todoitem: TodoItem):

    next_id = max(todos["id"] for todo in todos)
    new_todo_item = {
        "id": next_id,
        "Description": todoitem.Description,
        "Status": todoitem.Status,
        "Date": todoitem.Date
    }

    todos.append(new_todo_item)

    with open('todos.json', 'w') as file:
        json.dump(todos, file, indent=2)

    return todoitem

@app.put('/update_todo/{id}')
def update_todo(id: int, todoItem):
    for index, todo in enumerate(todos):
        if todo["id"] ==  id:
            if todoItem["Description"]:
                todo["Description"] = todoItem["Description"]
            if todoItem["Status"]:
                todo["Status"] = todoItem["Status"]

    return todos[index]