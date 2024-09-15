from fastapi import HTTPException, status

email_exists = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This email is already registered",
        )

username_exists = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This username is already registered",
        )

user_not_found = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

user_not_found_at_project = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found at this project",
        )
user_exists_at_project = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This user is already registered on this project",
        )