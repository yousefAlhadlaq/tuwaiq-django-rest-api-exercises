# Tuwaiq Club at KFUPM — Building REST APIs with Django

Welcome! This repository contains the five daily exercise handouts for Tuwaiq Club at KFUPM’s five-day Django REST API program.

You will build a Personal Task Management API using Django and Django REST Framework. **This repository contains exercise instructions, not a ready-made Django project.** You will create your own project from scratch on Day 1 and keep building it throughout the program.

## Before the program

Complete the environment setup guide before Day 1. You will need Python 3.13, VS Code, Git, Postman Desktop, and DB Browser for SQLite. You will also need GitHub, Neon, and Render accounts for the later sessions.

You should be comfortable with basic Python, including variables, functions, conditions, loops, lists, dictionaries, and simple classes. You do not need previous Django, REST API, database, or deployment experience.

## How to use this repository

Open the matching Python exercise file in VS Code at the start of each day. The instructions, steps, hints, and completion checklist are inside the file.

| Day | Exercise | What you will build |
|---|---|---|
| 1 | `exercises/day_1_foundation.py` | A new Django project, the Task model, migrations, and Django admin |
| 2 | `exercises/day_2_crud_api.py` | A serializer, routes, and create, read, update, and delete operations |
| 3 | `exercises/day_3_security.py` | Token login, ownership protection, and input validation |
| 4 | `exercises/day_4_tests.py` | At least eight API tests and deployment preparation |
| 5 | `exercises/day_5_deploy.py` | A deployed API, live checks, and your final demonstration |

The `django-readiness-check` folder from the setup guide is only for checking your computer. Do not use it as your workshop project. On Day 1, create a separate, new project folder named `task-management-api`.

## Your final project

Your API will let authenticated users manage their own tasks. It will use token authentication, validate task data, prevent users from accessing other people’s tasks, pass at least eight automated tests, and run over HTTPS with persistent PostgreSQL storage.

Write and understand the code you submit yourself. AI coding tools are not required for the program; follow your instructor’s guidance on their use.

## Your project on GitHub

The exercise repository is separate from your project repository. On Day 1, create your own empty GitHub repository for `task-management-api`, then follow the exercise instructions to commit and push your project. Save and push a checkpoint at the end of each day.

Never commit passwords, tokens, secret keys, database URLs, `.env` files, your virtual environment, or your local database.

## Completion checklist

By the end of Day 5, your project should have:

- The required Task fields and status choices.
- Token authentication and all required CRUD operations.
- Server-assigned task ownership and per-user access restrictions.
- Clear validation errors and at least eight passing automated tests.
- Setup, API, testing, and deployment instructions in your project’s README.
- A public HTTPS deployment with persistent PostgreSQL data.
- A completed live demonstration and submission evidence.

Your final submission includes your project’s GitHub URL, deployment URL, passing test evidence, and production smoke-test and persistence checks.
