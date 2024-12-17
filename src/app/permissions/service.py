from typing import Annotated, List
from fastapi import Depends, HTTPException, Security, status
from src.app.user.dto import UserDTO
from fastapi.security import OAuth2PasswordBearer
from src.app.user.dependens.service import IUserService

# OAuth2 Scheme with Scopes (if using scopes)
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/token",
    scopes={
        "admin": "Full administrative access.",
        "task:read": "Read tasks.",
        "task:create": "Create tasks.",
        "task:update": "Update tasks.",
        "task:delete": "Delete tasks.",
    }
)

# Custom dependency to require specific roles
def require_roles(required_roles: List[str]):
    def role_checker(
        current_user: Annotated[UserDTO, Depends(IUserService.get_me)]
    ) -> UserDTO:
        if current_user.role not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        return current_user
    return role_checker

