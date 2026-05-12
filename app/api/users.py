from fastapi import APIRouter

from app.schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def register_user(user_in: UserCreate):
    # Logic: Hash password, save to DB
    return {"id": 1, "email": user_in.email, "full_name": user_in.full_name}


@router.get("/me", response_model=UserResponse)
async def get_my_profile():
    # Logic: Get current logged-in user
    return {"id": 1, "email": "user@example.com", "full_name": "John Doe"}
