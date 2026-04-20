from dataclasses import dataclass
from uuid import UUID
from datetime import (
    datetime,
    timedelta
)

@dataclass
class User:
    id: UUID
    name: str
    email: str
    hashed_password: str

@dataclass
class Trip:
    id: UUID
    user: User
    car:  'Car'
    commit: 'Commit'
    refueling: 'Refueling' | None
    start_position: str | None
    end_position: str | None
    start_date: datetime | None
    end_date: datetime | None
    start_km: int | None
    end_km: int | None

    @property
    def start_position(self) -> str:
        return self.start_position
    
    @property.setter
    def start_position(self, value: str):
        if not value:
            raise ValueError("Start position cannot be empty")
        self.start_position = value
    
    @property
    def end_position(self) -> str:
        return self.end_position
    
    @property.setter
    def end_position(self, value: str):
        if not value:
            raise ValueError("End position cannot be empty")
        self.end_position = value
    
    @property
    def start_date(self) -> datetime:
        return self.start_date
    
    @property.setter
    def start_date(self, value: datetime):
        if abs(datetime.now() - value) <= timedelta(minutes=5):
            raise ValueError("Start date cannot be in the future")  
        self.start_date = value

    @property
    def end_date(self) -> datetime:
        return self.end_date
    
    @property.setter
    def end_date(self, value: datetime):
        if abs(datetime.now() - value) <= timedelta(minutes=5):
            raise ValueError("End date cannot be in the future")  
        self.end_date = value
    
    @property
    def start_km(self) -> int:
        return self.start_km
    
    @property.setter
    def start_km(self, value: int): 
        if value < 0:
            raise ValueError("Start km cannot be negative")
        self.start_km = value

    @property
    def distance(self) -> int:
        return self.end_km - self.start_km
    
    @property
    def duration(self) -> int:
        return int((self.end_date - self.start_date).total_seconds() / 60)
    
@dataclass
class Refueling:
    id: UUID
    cart_number: str
    liter_price: float
    liters: int
    receipt_photo: str

    @property
    def cart_number(self) -> str:
        return self.cart_number
    
    @property.setter
    def cart_number(self, value: str):
        if not value:
            raise ValueError("Cart number cannot be empty")
        self.cart_number = value
    
    @property
    def liter_price(self) -> float:
        return self.liter_price
    
    @property.setter
    def liter_price(self, value: float):
        if value < 0:
            raise ValueError("Liter price cannot be negative")
        self.liter_price = value

    @property
    def liters(self) -> int:
        return self.liters
    
    @property.setter
    def liters(self, value: int):
        if value < 0:
            raise ValueError("Liters cannot be negative")
        self.liters = value

    @property
    def receipt_photo(self) -> str:
        return self.receipt_photo
    
    @property.setter
    def receipt_photo(self, value: str):
        if not value:
            raise ValueError("Receipt photo cannot be empty")
        self.receipt_photo = value

@dataclass
class Car:
    plate: str
    km: int
    fuel_level: int

    @property
    def plate(self) -> str:
        return self.plate
    
    @property.setter
    def plate(self, value: str):
        if not value:
            raise ValueError("Plate cannot be empty")
        self.plate = value
    
    @property
    def km(self) -> int:
        return self.km
    
    @property.setter
    def km(self, value: int):
        if value < 0:
            raise ValueError("Km cannot be negative")
        self.km = value
    
    @property
    def fuel_level(self) -> int:
        return self.fuel_level
    
    @property.setter
    def fuel_level(self, value: int):
        if value < 0:
            raise ValueError("Fuel level cannot be negative")
        self.fuel_level = value

@dataclass
class Commit:
    
    id: UUID
    code: str
    description: str

    @property
    def code(self) -> str:
        return self.code
    
    @property.setter
    def code(self, value: str):
        if not value:
            raise ValueError("Code cannot be empty")
        self.code = value

    @property
    def description(self) -> str:
        return self.description
    
    @property.setter
    def description(self, value: str):
        if not value:
            raise ValueError("Description cannot be empty")
        self.description = value