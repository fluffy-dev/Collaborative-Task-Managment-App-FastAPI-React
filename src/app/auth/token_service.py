from datetime import datetime, timedelta

from jwt import encode, decode, get_unverified_header, PyJWTError, ExpiredSignatureError, InvalidSignatureError

from src.app.auth.dto import TokenDTO


class TokenService:

    def __init__(self) -> None:
        self.access_token_lifetime = 3600
        self.secret_key = ""
        self.algorithm = "HS256"

    async def get_token(self, dto):
        access_token = await self.generate_token(dto)
        token_type = "access"
        return TokenDTO(access_token=access_token, token_type=token_type)

    async def generate_token(self, dto):
        expire = datetime.now() + timedelta(seconds=self.access_token_lifetime)
        payload = {
            "token_type": "access",
            "user": {"email": str(dto.email)},
            # "exp": str(expire),
            # "iat": datetime.now(),
        }
        return await self.encode_token(payload=payload)

    async def encode_token(self, payload: dict) -> str:
        return encode(payload, self.secret_key, self.algorithm)

    async def decode_token(self, token: str):
        info = decode(token, self.secret_key, self.algorithm)
        return info

    def _validate(self, token: str):
        token_info = get_unverified_header(token)
        if token_info["alg"] != self.algorithm:
            raise InvalidSignatureError("key error")
        return token

    async def _decode_token(self, token: str):
        try:
            self._validate(token)
            return decode(token, self.secret_key, self.algorithm)
        except ExpiredSignatureError:
            raise ExpiredSignatureError("Token lifetime is expired")
        except PyJWTError:
            raise Exception("Token is invalid")
