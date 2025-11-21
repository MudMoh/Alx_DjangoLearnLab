# Permissions and Groups Setup

## Custom Permissions

The Book model in `relationship_app/models.py` has the following custom permissions defined in the Meta class:

- `can_view_book`: Allows viewing books
- `can_create_book`: Allows creating new books
- `can_edit_book`: Allows editing existing books
- `can_delete_book`: Allows deleting books

## Groups

Three groups are set up via Django admin:

- **Viewers**: Assigned `can_view_book` permission
- **Editors**: Assigned `can_view_book`, `can_create_book`, `can_edit_book` permissions
- **Admins**: Assigned all permissions (`can_view_book`, `can_create_book`, `can_edit_book`, `can_delete_book`)

## Views with Permission Checks

- `list_books`: Requires `can_view_book`
- `add_book`: Requires `can_create_book`
- `edit_book`: Requires `can_edit_book`
- `delete_book`: Requires `can_delete_book`

## Testing

To test:

1. Create users via admin.
2. Assign users to groups.
3. Log in as different users and check access to views.

## Management

Groups and permissions can be managed through Django admin under Groups and Users sections.
