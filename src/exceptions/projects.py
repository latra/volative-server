from fastapi import HTTPException, status

project_name_in_use = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This project is already assigned to other project",
        )

project_not_found = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )
