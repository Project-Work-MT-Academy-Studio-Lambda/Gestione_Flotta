from dataclasses import dataclass
from uuid import UUID

@dataclass
class User:
    id: UUID
    name: str
    email: str
    hashed_password: str

    def __post_init__(self):
        if not self.name:
            raise ValueError("Name cannot be empty")
        if not self.email:
            raise ValueError("Email cannot be empty")
        if not self.hashed_password:
            raise ValueError("Hashed password cannot be empty")