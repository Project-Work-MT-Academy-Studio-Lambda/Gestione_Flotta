from ....domain.user import User
from uuid import UUID

def user_to_item(user: User) -> dict:
    return {
        'id': str(user.id),
        'name': user.name,
        'email': user.email,
        'hashed_password': user.hashed_password,
        'role': user.role.value
    }

def item_to_user(item: dict) -> User:
    return User(
        id=UUID(item['id']),
        name=item['name'],
        email=item['email'],
        hashed_password=item['hashed_password'],
        role=item['role']
    )