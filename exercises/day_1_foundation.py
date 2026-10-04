r"""DAY 1 — Foundation and Task model

Today each participant creates a NEW Django project from an empty folder. The
separate django-readiness-check folder was only for checking your laptop; do not
reuse it, copy files from it, or make it your workshop project.

Learning outcomes:
- Recognize an HTTP method, URL, JSON body, and response status.
- Create a Python virtual environment, Django project, and tasks app.
- Explain how a model and migration become database tables.
- Save user-owned tasks and verify that SQLite data persists.

HTTP idea: POST /api/tasks/ with JSON such as
{"title": "Read API notes", "status": "TODO"} asks the server to create a
resource. A successful create normally returns HTTP 201. This endpoint is an
example for understanding HTTP; you will build it on Day 2.

Create your empty project folder:

Windows PowerShell:
    mkdir task-management-api
    cd task-management-api
    py -3.13 -m venv .venv
    .venv\Scripts\Activate.ps1

macOS Terminal:
    mkdir task-management-api
    cd task-management-api
    python3 -m venv .venv
    source .venv/bin/activate

Then, on either system, continue in the new empty folder:
    python -m pip install --upgrade pip
    python -m pip install "Django>=5.2,<5.3" "djangorestframework>=3.16,<3.17"
    django-admin startproject config .
    python manage.py startapp tasks
    python -m pip freeze > requirements.txt

Steps:
1. Create an empty GitHub repository named task-management-api. Do not add a
   README, license, or .gitignore on GitHub. Make sure the local folder above is
   new and separate from django-readiness-check.
2. In config/settings.py, enable rest_framework and tasks in INSTALLED_APPS.
   Create a local .gitignore with the entries listed below. Run python manage.py
   migrate, then python manage.py runserver once to check the initial project.
3. Add Task in tasks/models.py with id, title, description, status, due_date,
   owner, created_at, and updated_at. Django supplies the id automatically.
   Use exactly these status values: TODO, IN_PROGRESS, DONE. Connect owner to
   Django's user model. Description and due_date may be blank or empty.
4. Make and apply the tasks migration. Register Task in tasks/admin.py.
5. Run python manage.py createsuperuser; use Django admin to create two regular
   users and several tasks split between them. Restart the server and check that
   records remain. Use DB Browser to inspect db.sqlite3 after stopping Django.
6. Check the repository before staging. If Git asks for an identity, set your
   name and GitHub email. Initialize Git, commit, and push your project to your
   own empty GitHub repository.

Local .gitignore entries:
    .venv/
    __pycache__/
    *.py[cod]
    .env
    db.sqlite3
    staticfiles/
    .DS_Store

GitHub checkpoint commands after the project files are ready:
    git init
    git add .
    git status --short
    git commit -m "Initialize Django project"
    git branch -M main
    git remote add origin https://github.com/YOUR-USERNAME/task-management-api.git
    git push -u origin main

Expected result:
You built a separate Django project and tasks app from scratch. Its migrations
are current, admin shows tasks for both users, and the data remains after server
restart. Your own GitHub repository contains the Day 1 checkpoint with no
virtual environment, database file, or secret staged.

Exit checklist:
[ ] My actual task-management-api folder is new and separate from the readiness check.
[ ] My virtual environment activates and Django/DRF are installed and recorded.
[ ] I created config, tasks, enabled both apps, and the server starts locally.
[ ] All Task fields and the three exact status choices are in the model.
[ ] Migrations are current; Task is registered in admin.
[ ] Two users own sample tasks that remain after a restart.
[ ] My own GitHub repository is pushed without .venv, db.sqlite3, or secrets.
"""
# TODO 1 — In tasks/models.py, define the listed fields and status choices.
# Hint: Django creates id automatically; use settings.AUTH_USER_MODEL for owner.
# TODO 2 — Make and apply a migration after changing the model.
# Hint: python manage.py makemigrations tasks, then python manage.py migrate.
# TODO 3 — Register Task in tasks/admin.py.
# Hint: Import Task and register it with admin.site.register or @admin.register.
if __name__ == "__main__":
    print(__doc__)
