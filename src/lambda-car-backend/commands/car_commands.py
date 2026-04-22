from dataclasses import dataclass
from uuid import UUID

@dataclass
class CreateCarCommand:
    trip_id: UUID
    plate: str
    km: int
    fuel_level: int

@dataclass
class UpdateCarCommand:
    car_id: UUID
    trip_id: UUID
    plate: str
    km: int
    fuel_level: int