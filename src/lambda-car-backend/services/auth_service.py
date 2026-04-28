from repositories.user_repository import UserRepository
from security.password_hasher import PasswordHasher
from security.token_service import TokenService
from commands.auth_commands import LoginCommand
from constants import Constants

class AuthService:
    def __init__(
        self,
        user_repository: UserRepository,
        password_hasher: PasswordHasher,
        token_service: TokenService,
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
        self.token_service = token_service

    def login(self, cmd: LoginCommand) -> str:
        user = self.user_repository.get_by_email(cmd.email)
        if user is None:
            raise ValueError(Constants.INVALID_CREDENTIALS)

        if not self.password_hasher.verify(user.hashed_password, cmd.password):
            raise ValueError(Constants.INVALID_CREDENTIALS)

        return self.token_service.create_token(user.id, user.role)
    