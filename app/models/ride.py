import enum

from sqlalchemy import DateTime, Enum, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.db.base_class import Base


class RideStatus(enum.Enum):
    REQUESTED = "requested"
    ACCEPTED = "accepted"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Ride(Base):
    __tablename__ = "rides"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    passenger_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    driver_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)

    # Locations
    pickup_lat: Mapped[float] = mapped_column(Float, nullable=False)
    pickup_long: Mapped[float] = mapped_column(Float, nullable=False)
    dropoff_lat: Mapped[float] = mapped_column(Float, nullable=False)
    dropoff_long: Mapped[float] = mapped_column(Float, nullable=False)

    status: Mapped[RideStatus] = mapped_column(
        Enum(RideStatus), default=RideStatus.REQUESTED
    )
    price: Mapped[float] = mapped_column(Float, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
