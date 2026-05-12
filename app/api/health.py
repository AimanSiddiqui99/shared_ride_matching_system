import redis.asyncio as redis
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db  # Your DB session dependency

router = APIRouter()


@router.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    health_status = {"api": "healthy", "database": "unhealthy", "redis": "unhealthy"}

    # 1. Check Database
    try:
        await db.execute("SELECT 1")
        health_status["database"] = "healthy"
    except Exception:
        health_status["database"] = "unhealthy"

    # 2. Check Redis (Assuming you have a redis_client setup)
    try:
        # Example using a basic redis connection
        r = redis.from_url("redis://redis:6379")
        await r.ping()
        health_status["redis"] = "healthy"
    except Exception:
        health_status["redis"] = "unhealthy"

    return health_status
