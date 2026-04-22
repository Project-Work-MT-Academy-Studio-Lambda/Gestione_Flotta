from uuid import UUID, uuid4

from domain.car import Car
from repositories.car_repository import CarRepository
from constants import Constants

from commands.car_commands import (
    CreateCarCommand,
    UpdateCarCommand
)


class CarService:
    def __init__(self, car_repository: CarRepository):
        self.car_repository = car_repository
    
    def _get_car_or_raise(self, car_id: UUID) -> Car:
        car = self.car_repository.get_by_id(car_id)
        if not car:
            raise ValueError(Constants.CAR_NOT_FOUND)
        return car

    def create_car(
        self,
        cmd: CreateCarCommand
    ) -> Car:
        existing_car = self.car_repository.get_by_plate(cmd.plate)
        if existing_car is not None:
            raise ValueError(Constants.CAR_ALREADY_EXISTS)

        car = Car(
            id=uuid4(),
            trip_id=cmd.trip_id,
            plate=cmd.plate,
            model=cmd.model,
        )

        self.car_repository.save(car)
        return car

    def get_car_by_plate(self, plate: str) -> Car:
        car = self.car_repository.get_by_plate(plate)
        if not car:
            raise ValueError(Constants.CAR_NOT_FOUND)
        return car

    def update_car(
        self,
        cmd: UpdateCarCommand
    ) -> Car:
        car = self._get_car_or_raise(cmd.car_id)
        existing_car = self.car_repository.get_by_plate(cmd.plate)
        if existing_car is not None and existing_car.id != cmd.car_id:
            raise ValueError(Constants.CAR_ALREADY_EXISTS)

        car.plate = cmd.plate
        car.model = cmd.model

        self.car_repository.save(car)
        return car

    def delete_car(self, car_id: UUID):
        car = self._get_car_or_raise(car_id)
        self.car_repository.delete(car_id)