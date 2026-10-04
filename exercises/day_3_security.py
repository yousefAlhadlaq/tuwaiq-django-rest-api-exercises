"""DAY 3 — Token authentication, ownership, and validation

Authentication identifies the caller; authorization limits which Task records
that person may access. Today you add both to the API created in your own project.

Learning outcomes:
- Exchange credentials for a DRF token.
- Require authentication on every task endpoint.
- Filter every task query to its owner.
- Return useful field-level validation errors.

Steps:
1. Add rest_framework.authtoken to INSTALLED_APPS and apply its migration.
2. Replace the temporary session authentication with TokenAuthentication and
   keep IsAuthenticated on task routes. Do not allow anonymous access to tasks.
3. Add POST /api/auth/token/ using DRF's obtain_auth_token view. Leave only
   credential exchange unauthenticated.
4. Set owner from request.user and filter TaskViewSet.get_queryset() to that
   user. A different user's retrieve, update, or delete should return 404.
5. Validate a required nonblank title, an allowed status, and a due_date not
   earlier than today on creation. Invalid input returns a useful field-level
   400 response. Do not reject a past due date when updating an existing task;
   the contract applies that date rule to creation.
6. In Postman, send username and password as JSON to /api/auth/token/. Send
   Authorization: Token <token> on task requests. Use two accounts to compare
   their lists and attempt cross-user retrieve/update/delete. Confirm failed
   requests change no data.

Expected result:
Anonymous task requests receive 401. Each user can access only their own tasks;
other-user detail actions return 404. Invalid fields return 400 with clear errors.

Exit checklist:
[ ] Valid credentials return a token from POST /api/auth/token/.
[ ] Anonymous task requests return 401.
[ ] Server-assigned owner cannot be overridden by a request body.
[ ] Each user's list contains only that user's records.
[ ] Cross-user retrieve, update, and delete return 404 without changing data.
[ ] Blank title, invalid status, and past due date on create return field errors.
[ ] Two-user verification is recorded and the Day 3 checkpoint is pushed.
"""
# TODO 1 — Enable the token app and configure DRF TokenAuthentication.
# Hint: Add rest_framework.authtoken, then run migrate and update REST_FRAMEWORK.
# TODO 2 — Expose obtain_auth_token at /api/auth/token/.
# Hint: Add it to tasks/urls.py; credentials are the only public API call.
# TODO 3 — Filter access, assign owner, and validate input.
# Hint: Filter by request.user; compare a create date with timezone.localdate().
if __name__ == "__main__":
    print(__doc__)
