# Project Monitoring API
## A hackathon project
### This is a Django REST API for a project monitoring application that allows for easy monitoring of ongoing projects. The API uses Django Rest Framework for serialization and validation and CORS headers for cross-origin resource sharing.

## Installation
```Clone the repository:
git clone https://github.com/Isquare007/project_delivery_app_api.git
```

```Install the dependencies:
pip install -r requirements.txt
```

```Create the database:
python manage.py migrate
```

```(Optional) Load sample data:
python manage.py loaddata sample_data.json
```

## Usage
```To run the API locally, use the following command:
python manage.py runserver
```

# The API endpoints can be accessed at http://localhost:8000/

Endpoints
/projects
GET /project
Retrieves a list of all projects.

POST /project
Creates a new project.

GET /projects{project_id}
Retrieves the details of a specific project.

PUT /project/{project_id}
Updates the details of a specific project.

DELETE /project/{project_id}
Deletes a specific project.

/users
GET /users
Retrieves a list of all users.

POST /projects{project_id}/user
Creates a new user on a project.

GET /users/{user_id}
Retrieves the details of a specific user.
GET /projects{project_id}/user
Retrieves the details of users a specific project.

PUT /projects{project_id}/user/{user_id}
Updates the details of a specific user.

DELETE /projects{project_id}/user/{user_id}
Deletes a specific user.

/tasks
GET /projects{project_id}/task
Retrieves a list of all tasks.

POST /projects{project_id}/task
Creates a new task.

GET /projects{project_id}/task/{task_id}/<br>
Retrieves the details of a specific task.

PUT /projects{project_id}/task/{task_id}/
Updates the details of a specific task.

DELETE /projects{project_id}/task/{task_id}/
Deletes a specific task.

/teams: CRUD operations for teams
/milestones: CRUD operations for milestones
/transactions: CRUD operations for transactions

You can use a tool like Postman to test the API endpoints, or create a django admin user with
```
python manage.py createsuperuser
```