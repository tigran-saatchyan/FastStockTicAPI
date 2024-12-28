import re

from fastapi import HTTPException
from starlette import status


class PasswordValidator:
    """Validator for checking the validity of passwords.

    Args:
        password (str): The password to validate.
        confirm_password (str): The confirmation password.

    Raises:
        HTTPException: If the password is not valid or passwords do not match.
    """

    def __call__(self, password: str, confirm_password: str):
        if not re.search(r"^(?=.*[A-Z])(?=.*[$%&!]).{8,}$", password):

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The password is not valid",
            )
        if password != confirm_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Passwords do not match",
            )
        return True
