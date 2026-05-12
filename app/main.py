from fastapi import FastAPI

from app.api import drivers, health, rides, users

app = FastAPI(title="Shared Ride Matching API")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(rides.router, prefix="/rides", tags=["Rides"])
app.include_router(drivers.router, prefix="/drivers", tags=["Drivers"])
app.include_router(health.router, prefix="/health", tags=["Health"])
