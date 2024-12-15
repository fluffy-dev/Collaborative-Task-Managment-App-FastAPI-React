from pydantic import BaseModel, constr, EmailStr, model_validator
import re


class UserDTO(BaseModel):
    id:int = None
    password : constr(min_length=8)
    email: EmailStr


class RegistrationDTO(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    password2: constr(min_length=8)

    @model_validator(mode="after")
    def code_validate(self):
        if self.password != self.password2:
            raise ValueError("password missmatch")
        return self


class LoginDTO(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class FindUserDTO(BaseModel):
    email: EmailStr