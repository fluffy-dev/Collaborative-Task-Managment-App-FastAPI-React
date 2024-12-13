from pydantic import BaseModel, constr, EmailStr


class UserDTO(BaseModel):
    id:int = None
    password : constr(min_length=8)
    email: EmailStr


class RegistrationDTO(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
