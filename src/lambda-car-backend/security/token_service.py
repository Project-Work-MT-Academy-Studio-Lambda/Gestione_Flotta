import jwt
from datetime import (
    datetime,
    timedelta,
    timezone
)


class TokenService:
    def __init__(self, secret: str):
        self.secret = secret

    def create_token(self, user_id: str, role: str) -> str:
        payload = {
            "sub": user_id,
            "exp": datetime.now(timezone.utc) + timedelta(hours=2),
            "role": role
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def verify_token(self, token: str) -> str:
        payload = jwt.decode(token, self.secret, algorithms=["HS256"])
        return payload["sub"]