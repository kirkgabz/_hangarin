# Hangarin – Task & To-Do Manager

Hangarin is a **Django-based web application** that helps users organize daily tasks, manage priorities, add notes, and break large goals into smaller subtasks.

This project was built as part of a system design exercise involving task management, database modeling, and Django admin configuration.

---

# Features

### Task Management
- Create and manage tasks
- Assign priorities to tasks
- Set deadlines
- Track task status
- Organize tasks using categories

### Subtasks
Break large tasks into smaller manageable subtasks.

### Notes
Attach notes to tasks for additional context or reminders.

### Task Status Tracking
Tasks support the following statuses:

- Pending
- In Progress
- Completed

### Django Admin Management
The admin panel allows administrators to:

- View and manage tasks
- Filter tasks by status, priority, and category
- Search tasks by title and description
- Manage priorities and categories
- Manage notes and subtasks

---

# System Architecture

The system includes the following main models:

- Priority
- Category
- Task
- SubTask
- Note

Relationships:

- A **Task**
  - belongs to a **Category**
  - has a **Priority**
  - can contain multiple **SubTasks**
  - can contain multiple **Notes**

---

# Tech Stack

Backend
- Python
- Django

Database
- SQLite (default Django database)

Libraries
- Faker (for generating test data)

Version Control
- Git
- GitHub

Deployment
- PythonAnywhere

---

# Installation

## 1 Clone the Repository

```bash
git clone https://github.com/kirkgabz/_hangarin.git
cd _hangarin
```

---

## 2 Create Virtual Environment

```bash
python -m venv venv
```

Activate it.

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

---

## 3 Install Dependencies

```bash
pip install django faker
```

Or if a requirements file exists:

```bash
pip install -r requirements.txt
```

---

## 4 Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5 Create Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

---

## 6 Run the Development Server

```bash
python manage.py runserver
```

Open your browser and go to:

```
http://127.0.0.1:8000
```

Admin panel:

```
http://127.0.0.1:8000/admin
```

---

# Admin Features

## TaskAdmin
Displays:

- Title
- Status
- Deadline
- Priority
- Category

Features:

- Filter by status
- Filter by priority
- Filter by category
- Search by title
- Search by description

---

## SubTaskAdmin

Displays:

- Title
- Status
- Parent task name

Features:

- Filter by status
- Search by title

---

## CategoryAdmin & PriorityAdmin

Displays:

- Name field

Features:

- Search functionality

---

## NoteAdmin

Displays:

- Task
- Content
- Created date

Features:

- Filter by created date
- Search by content

---

# Sample Data Generation

This project uses the **Faker** library to generate sample data.

Example:

Generate task title

```python
fake.sentence(nb_words=5)
```

Generate description

```python
fake.paragraph(nb_sentences=3)
```

Generate random status

```python
fake.random_element(elements=["Pending","In Progress","Completed"])
```

Generate random deadline

```python
from django.utils import timezone
deadline = timezone.make_aware(fake.date_time_this_month())
```

---

# Project Structure

```
hangarin/
│
├── manage.py
├── requirements.txt
│
├── hangarin/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
```

---

# Deployment

The project can be deployed using **PythonAnywhere**.

Basic deployment steps:

1. Push project to GitHub
2. Clone repository in PythonAnywhere
3. Configure the WSGI file
4. Run migrations
5. Collect static files
6. Reload the web application

---

# Contributors
- Kirk John Gabo  

---

# License

This project is created for **educational purposes**.