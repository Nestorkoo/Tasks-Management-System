# Tasks Management System

This project implements a task management system with deadline tracking and notification sending via Celery.

---

## 📋 Features

- Create, update, and delete tasks.
- Send notifications when deadlines are approaching or overdue.
- Integration with **Celery** for automated tasks.
- API to manage tasks efficiently.

---

## 🛠️ Technologies

- **Python** – Core programming language.
- **Django** – Web framework for backend development.
- **Django REST Framework (DRF)** – To create API endpoints.
- **Celery** – For task scheduling and background processing.
- **Redis** – Message broker for Celery.
- **PostgreSQL** – Database for storing tasks and notifications.

---
## 🚀 Installation

### 2. Create a virtual environment
Create and activate a virtual environment:

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

```
**On Windows**
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set up Redis (for Celery)
```bash
redis-server
```
If redis isn't installed - download it!!!

### 5. Configure Celery in Django settings
Add the following to your settings.py:
```bash
# settings.py
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
```
### 6. Run database migrations
``` bash
python manage.py makemigrations
python manage.py migrate
```
### 7. Start the Django development server
``` bash
python manage.py runserver
```
---
## 📚 API Endpoints
| Method |        Endpoint        | Description       |
|--------|:----------------------:|-------------------|
| GET    | /api/list/             | List all tasks    |
| POST   | /api/create/           | Create a new task |
| PUT    | /api/task/{id}/update/ | Edit a task       |
| DELETE | /api/task/{id}/delete/ | Delete a task     |

---

## 🛠️ Common Issues

-   **Redis is not running:**  
    Ensure Redis is installed and running on the default port (6379).
    
-   **Task not registered:**  
    Make sure the task is properly imported and your Celery worker is started with the correct app.
    
-   **Permission issues (Windows):**  
    If you encounter a WinError related to file access, close any processes using the Celery executable and try again.
