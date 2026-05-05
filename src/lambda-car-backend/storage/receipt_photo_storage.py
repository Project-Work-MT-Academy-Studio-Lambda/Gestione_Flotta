from typing import Protocol
from uuid import UUID

class ReceiptPhotoStorage(Protocol):

    def save_receipt_photo(
            self,
            refueling_id: UUID,
            filename: str,
            content: bytes,
            content_type: str
        ) -> str:
            ...