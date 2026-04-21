from dataclasses import dataclass
from uuid import UUID
import re

@dataclass
class Car:
    id: UUID
    trip_id: UUID
    plate: str
    km: int
    fuel_level: int

    def __post_init__(self):
        if not self.plate:
            raise ValueError("Plate cannot be empty")
        plate_clean = self.plate.replace(" ", "").upper()

        if len(plate_clean) != 7:
            raise ValueError(f"Plate must be 7 characters (got {len(plate_clean)})")
        
        pattern = r"^[A-Z]{2}[0-9]{3}[A-Z]{2}$"
        if not re.match(pattern, plate_clean):
            raise ValueError(f"Invalid plate format: {self.plate}")
        if self.km < 0:
            raise ValueError("Km cannot be negative")
        if self.fuel_level < 0:
            raise ValueError("Fuel level cannot be negative")