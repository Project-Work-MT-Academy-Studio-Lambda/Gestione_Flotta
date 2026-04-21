from uuid import UUID, uuid4
from datetime import datetime

from domain.refueling import Refueling
from repositories.refueling_repository import RefuelingRepository
from repositories.trip_repository import TripRepository
from constants import Constants


class RefuelingService:
    def __init__(
        self,
        refueling_repository: RefuelingRepository,
        trip_repository: TripRepository,
    ):
        self.refueling_repository = refueling_repository
        self.trip_repository = trip_repository

    def create_refueling(
        self,
        trip_id: UUID,
        liters: float,
        price: float,
        date: datetime,
    ) -> Refueling:
        trip = self.trip_repository.get_by_id(trip_id)
        if not trip:
            raise ValueError(Constants.TRIP_NOT_FOUND)

        refueling = Refueling(
            id=uuid4(),
            trip_id=trip_id,
            liters=liters,
            price=price,
            date=date,
        )

        self.refueling_repository.save(refueling)
        return refueling

    def get_refueling(self, refueling_id: UUID) -> Refueling:
        refueling = self.refueling_repository.get_by_id(refueling_id)
        if not refueling:
            raise ValueError(Constants.REFUELING_NOT_FOUND)
        return refueling

    def get_refuelings_for_trip(self, trip_id: UUID) -> list[Refueling]:
        trip = self.trip_repository.get_by_id(trip_id)
        if not trip:
            raise ValueError(Constants.TRIP_NOT_FOUND)

        return self.refueling_repository.list_by_trip_id(trip_id)

    def update_refueling(
        self,
        refueling_id: UUID,
        trip_id: UUID,
        liters: float,
        price: float,
        date: datetime,
    ) -> Refueling:
        refueling = self.get_refueling(refueling_id)

        trip = self.trip_repository.get_by_id(trip_id)
        if not trip:
            raise ValueError(Constants.TRIP_NOT_FOUND)

        refueling.trip_id = trip_id
        refueling.liters = liters
        refueling.price = price
        refueling.date = date

        self.refueling_repository.save(refueling)
        return refueling

    def delete_refueling(self, refueling_id: UUID) -> None:
        refueling = self.get_refueling(refueling_id)
        if not refueling:
            raise ValueError(Constants.REFUELING_NOT_FOUND)
        self.refueling_repository.delete(refueling_id)