"""DAY 5 — Deploy, verify, and demonstrate

Today you deploy your tested task-management-api and verify its behavior against
the live HTTPS service using persistent Neon PostgreSQL storage.

Learning outcomes:
- Apply production settings and migrations.
- Read build/runtime logs and diagnose deployment errors.
- Verify token auth, CRUD, validation, isolation, and persistence.
- Present clear technical evidence in five minutes.

Steps:
1. Confirm the instructor has rechecked current Render and Neon availability.
2. Create/use the approved Neon PostgreSQL database. In Render, set DATABASE_URL,
   SECRET_KEY, DEBUG=False, and ALLOWED_HOSTS (the assigned Render hostname) as
   service environment variables. Never put real values in source files or Git.
3. Connect your own GitHub task-management-api repository to a Render Python web
   service. Use the project guide's commands:
   Build: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
   Start: gunicorn config.wsgi:application
4. Open the public HTTPS URL. Check build and runtime logs; fix any startup or
   database errors. A free service may sleep between requests, so allow time for
   its first request to wake.
5. Use two accounts to verify POST /api/auth/token/, authenticated CRUD, the
   401 anonymous response, field validation errors, and cross-user isolation.
6. Create a task, restart or redeploy the service, and confirm the task remains.
   This verifies that production uses Neon rather than Render's ephemeral disk.
7. Gather the submission evidence and rehearse the five-minute demonstration.

Expected result:
The live HTTPS API passes the required checks, uses persistent PostgreSQL, and
is supported by a reviewer-accessible GitHub repository and evidence.

Final demonstration and submission checklist:
[ ] Obtain a token and make an authenticated request.
[ ] Create/list a personal task, update it, and show a validation error.
[ ] Use a second user to demonstrate task isolation.
[ ] Delete an owned task and verify the success response.
[ ] Show a task persists after restart or redeploy.
[ ] Submit the GitHub URL and public HTTPS URL.
[ ] Submit passing test output, live smoke-test evidence, and persistence evidence.
[ ] Review repository history and current files for exposed secrets.
[ ] Deliver a concise five-minute demonstration.

Completion check:
The public HTTPS API passes the required contract, data persists in Neon, and
the complete evidence package is accessible to the reviewer.
"""
# TODO 1 — Set production secrets through Render's environment dashboard.
# Hint: Never commit DATABASE_URL or SECRET_KEY; confirm DEBUG is false.
# TODO 2 — Exercise live endpoints with two accounts and verify persistence.
# Hint: Check the deployed hostname, auth header, trailing slashes, and logs.
if __name__ == "__main__":
    print(__doc__)
