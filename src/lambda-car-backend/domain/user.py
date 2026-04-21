from dataclasses import dataclass
from uuid import UUID
from constants import Constants

@dataclass
class User:
    id: UUID
    name: str
    email: str
    password: str

    def __post_init__(self):
        if not self.name:
            raise ValueError(Constants.NAME_CANNOT_BE_EMPTY)
        if not self.email:
            raise ValueError(Constants.EMAIL_CANNOT_BE_EMPTY)
        if not self.password:
            raise ValueError(Constants.PASSWORD_CANNOT_BE_EMPTY)