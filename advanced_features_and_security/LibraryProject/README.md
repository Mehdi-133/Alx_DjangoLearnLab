"# frist_project_task" 

# Permissions and Groups Setup

This project uses Django's permission system to manage access control.

## Custom Permissions

The following custom permissions are defined for the `Book` model:
- `can_view`: Permission to view books.
- `can_create`: Permission to create books.
- `can_edit`: Permission to edit books.
- `can_delete`: Permission to delete books.

## Groups and Permissions

- **Admins**: Can view, create, edit, and delete books. (Assigned all permissions: `can_view`, `can_create`, `can_edit`, `can_delete`)
- **Editors**: Can create and edit books. (Assigned `can_create`, `can_edit`)
- **Viewers**: Can view books only. (Assigned `can_view`)

## How to Assign Permissions in Admin:

1. Go to the Django admin at `http://127.0.0.1:8000/admin/`.
2. Under the **Groups** section, create the groups and assign the appropriate permissions.
3. Assign users to these groups as needed.

## Testing Permissions:

1. Create users and assign them to `Admins`, `Editors`, and `Viewers`.
2. Log in as users from each group and test their access to the views:
   - **Admins**: Can perform all actions.
   - **Editors**: Can create and edit books.
   - **Viewers**: Can only view books.

