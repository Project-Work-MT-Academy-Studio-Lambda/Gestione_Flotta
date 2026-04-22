from infrastructure.dynamodb.tables import DynamoDbTables
from infrastructure.dynamodb.repositories.dynamodb_user_repository import DynamoDbUserRepository
from infrastructure.dynamodb.repositories.dynamodb_car_repository import DynamoDbCarRepository
from infrastructure.dynamodb.repositories.dynamodb_trip_repository import DynamoDbTripRepository
from infrastructure.dynamodb.repositories.dynamodb_refueling_repository import DynamoDbRefuelingRepository
from infrastructure.dynamodb.repositories.dynamodb_commit_repository import DynamoDbCommitRepository

from services.user_service import UserService
from services.trip_service import TripService
from services.car_service import CarService
from services.refueling_service import RefuelingService
from services.commit_service import CommitService
from security.password_hasher import ArgonPasswordHasher


_tables = DynamoDbTables()
_password_hasher = ArgonPasswordHasher()


def get_user_service() -> UserService:
    return UserService(
        user_repository=DynamoDbUserRepository(_tables.user_table),
        password_hasher=_password_hasher,
    )


def get_car_service() -> CarService:
    return CarService(
        car_repository=DynamoDbCarRepository(_tables.car_table),
    )


def get_trip_service() -> TripService:
    return TripService(
        trip_repository=DynamoDbTripRepository(_tables.trip_table),
        car_repository=DynamoDbCarRepository(_tables.car_table),
        user_repository=DynamoDbUserRepository(_tables.user_table),
        commit_repository=DynamoDbCommitRepository(_tables.commit_table),
        refueling_repository=DynamoDbRefuelingRepository(_tables.refueling_table),
    )


def get_refueling_service() -> RefuelingService:
    return RefuelingService(
        refueling_repository=DynamoDbRefuelingRepository(_tables.refueling_table),
        trip_repository=DynamoDbTripRepository(_tables.trip_table),
    )


def get_commit_service() -> CommitService:
    return CommitService(
        commit_repository=DynamoDbCommitRepository(_tables.commit_table),
        trip_repository=DynamoDbTripRepository(_tables.trip_table),
    )