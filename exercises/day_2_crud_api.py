"""DAY 2 — Serializer, routes, and CRUD

Today you expose the Task records from your Day 1 project as JSON over HTTP. A
serializer turns model records into JSON and validates incoming JSON before save.

Learning outcomes:
- Explain what a serializer does.
- Route collection and detail requests through a viewset and router.
- Implement all six CRUD operations and expected response codes.
- Keep owner and generated values out of client control.

Steps:
1. Create TaskSerializer in tasks/serializers.py with every required Task field.
   Mark id, owner, created_at, and updated_at read-only.
2. Create a ModelViewSet in tasks/views.py. For this temporary Day 2 checkpoint,
   the queryset can include all tasks. Require an authenticated session and set
   owner from request.user when saving; do not let clients choose the owner.
3. Create tasks/urls.py with a DRF DefaultRouter and register the viewset as
   "tasks". In config/urls.py, include tasks.urls beneath "api/" and include
   rest_framework.urls beneath "api-auth/" for temporary local session login.
4. Use the browsable API login or a local session in your API client. Session
   login is a Day 2 development bridge only; Day 3 replaces it with token auth.
5. Verify GET and POST /api/tasks/, and GET, PUT, PATCH, DELETE
   /api/tasks/{id}/. Try a create body like:
   {"title": "Read API notes", "description": "Chapter 1", "status": "TODO"}
   A create returns 201; list/retrieve/updates return 200; delete returns 204
   with an empty body; an unknown id returns 404. PUT replaces all editable
   fields; PATCH changes only the fields included in its request body.
6. Submit an owner field in a request body and confirm it cannot override the
   signed-in user's ownership. Inspect the database after each write.

Expected result:
All six CRUD operations work locally with valid JSON. A task created in a
session is owned by that signed-in user. Owner remains read-only in the API.

Exit checklist:
[ ] Serializer exposes the required fields; owner/generated values are read-only.
[ ] Router creates collection and detail routes beneath /api/.
[ ] GET/POST collection and GET/PUT/PATCH/DELETE detail requests work.
[ ] Create is 201; read/update is 200; delete is 204; unknown id is 404.
[ ] The server assigns owner; client input cannot choose another owner.
[ ] Temporary session login is clearly limited to local Day 2 use.
[ ] I checked the database and pushed a Day 2 checkpoint.
"""
# TODO 1 — Build the serializer in tasks/serializers.py.
# Hint: ModelSerializer declares its model, fields, and read_only_fields.
# TODO 2 — Build the ModelViewSet in tasks/views.py.
# Hint: ModelViewSet supplies CRUD actions; use perform_create for owner.
# TODO 3 — Register the viewset with DefaultRouter in tasks/urls.py.
# Hint: The parent config/urls.py supplies the /api/ prefix.
if __name__ == "__main__":
    print(__doc__)
