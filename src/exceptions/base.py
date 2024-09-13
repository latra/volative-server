from fastapi import HTTPException, status
credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

permission_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Not enought permissions to perform this action"
    )


missing_query_parameters = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="You need to specify at least one query parameter"
    )

incopatible_query_parameters = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Incompatible query parameters"
    )