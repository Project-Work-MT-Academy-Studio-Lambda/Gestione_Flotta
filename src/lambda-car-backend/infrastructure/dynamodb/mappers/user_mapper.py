from ....domain.user import User
from ....domain.enum.role import Role
from uuid import UUID
from ....logger import get_logger

logger = get_logger(__name__)

def user_to_item(user: User) -> dict:
    return {
        'id': str(user.id),
        'name': user.name,
        'email': user.email,
        'hashed_password': user.hashed_password,
        'role': user.role.value
    }

def item_to_user(item: dict) -> User:
    logger.debug(f"Mapping DynamoDB item to User: {item}")
    return User(
        id=UUID(item['id']),
        name=item['name'],
        email=item['email'],
        hashed_password=item['hashed_password'],
        role=Role(item['role'])
    )