FastAPI To-Do API
Esta é uma API simples de gerenciamento de tarefas (To-Do List) desenvolvida com FastAPI. A API permite criar, ler, atualizar e excluir tarefas, utilizando um armazenamento temporário em memória. O ID das tarefas é gerado automaticamente (auto incrementado).

Recursos
Listar tarefas: Retorna todas as tarefas cadastradas.
Criar tarefa: Cria uma nova tarefa (ID auto incrementado).
Buscar tarefa por ID: Retorna os dados de uma tarefa específica.
Atualizar tarefa: Atualiza os dados de uma tarefa existente.
Excluir tarefa: Remove uma tarefa pelo seu ID.
Tecnologias Utilizadas
FastAPI – Framework moderno e de alta performance para construir APIs.
Pydantic – Para validação e definição de modelos de dados.
Uvicorn – Servidor ASGI para rodar a aplicação.
Requisitos
Python 3.7+
FastAPI
Uvicorn
Instalação
Clone este repositório ou copie o código para um diretório local.

Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
Copy
Edit
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
Instale as dependências:

bash
Copy
Edit
pip install fastapi uvicorn
Como Executar
Para iniciar a aplicação, execute o comando abaixo na raiz do projeto:

bash
Copy
Edit
uvicorn main:app --reload
O parâmetro --reload ativa o modo de recarga automática, útil para desenvolvimento.
A API estará disponível em http://127.0.0.1:8000.
Documentação Interativa
FastAPI gera automaticamente uma interface interativa para a API. Acesse:

Swagger UI
Redoc
Endpoints
GET /tasks
Retorna a lista de todas as tarefas.

Exemplo de resposta:

json
Copy
Edit
[
  {
    "id": 1,
    "title": "Comprar leite",
    "description": "Ir ao supermercado para comprar leite",
    "completed": false
  }
]
POST /tasks
Cria uma nova tarefa. O id é gerado automaticamente.

Exemplo de corpo da requisição:

json
Copy
Edit
{
  "title": "Estudar FastAPI",
  "description": "Ler a documentação e praticar os exemplos",
  "completed": false
}
Exemplo de resposta:

json
Copy
Edit
{
  "id": 1,
  "title": "Estudar FastAPI",
  "description": "Ler a documentação e praticar os exemplos",
  "completed": false
}
GET /tasks/{task_id}
Retorna os detalhes da tarefa com o ID informado.

PUT /tasks/{task_id}
Atualiza a tarefa existente com o ID informado.

Observação: No exemplo atual, o endpoint espera um objeto completo do modelo Task.

DELETE /tasks/{task_id}
Exclui a tarefa com o ID informado.