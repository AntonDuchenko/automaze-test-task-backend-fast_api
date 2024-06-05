## Server Part of the Automaze Application

This part of the application is responsible for handling requests from the client side and interacting with the database.

### Used Technologies

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a full suite of well-known enterprise-level persistence patterns.
- **PostgreSQL**: An object-relational database for storing information.

### Endpoints

#### Todos

- **GET /todos**: Get a list of all todos.
- **POST /todos**: Create a new todo.
- **PATCH /todos/:id**: Partially update an existing todo by its identifier.
- **DELETE /todos/:id**: Delete a todo by its identifier.

### Running the Server

1. Open the terminal.
2. Navigate to the directory where the server-side code is located.
3. Run the command `pip install -r requirements.txt` to install all necessary dependencies.
4. Open another terminal and run the command `uvicorn main:app --reload` to start the server.
5. After a successful startup, the server will be available at [http://localhost:8000/](http://localhost:8000/).

### Files and Directories

- **models.py**: Defines SQLAlchemy models for database tables.
- **routes.py**: Defines FastAPI routes.
- **main.py**: Entrypoint for the FastAPI application.
- **requirements.txt**: Lists all Python dependencies required by the application.
