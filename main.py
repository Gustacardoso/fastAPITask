from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modelo de dados para a tarefa
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    
# Modelo para criação de tarefa (sem ID)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False    

# Armazenamento temporário de tarefas (em memória)
tasks: List[Task] = []
next_id= 1 # Variável global para gerar IDs automaticamente

# Endpoint para listar todas as tarefas
@app.get("/tasks", response_model=List[Task])
def read_tasks():
    return tasks

# Endpoint para criar uma nova tarefa com ID auto incrementado
@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    global next_id
    new_task = Task(id=next_id, **task.dict())
    next_id += 1
    tasks.append(new_task)
    return new_task

# Endpoint para buscar uma tarefa específica pelo ID
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Endpoint para atualizar uma tarefa existente
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# Endpoint para deletar uma tarefa pelo ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[index]
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")