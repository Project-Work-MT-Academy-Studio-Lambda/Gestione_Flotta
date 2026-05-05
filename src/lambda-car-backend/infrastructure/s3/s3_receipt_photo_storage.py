from pathlib import Path
from uuid import UUID

from .client import create_s3_client
from .config import load_s3_config
from ...storage.receipt_photo_storage import ReceiptPhotoStorage


class S3ReceiptPhotoStorage(ReceiptPhotoStorage):
    def __init__(self):
        self.config = load_s3_config()
        self.client = create_s3_client()

    def save_receipt_photo(
        self,
        refueling_id: UUID,
        filename: str,
        content: bytes,
        content_type: str,
    ) -> str:
        extension = Path(filename).suffix.lower()
        key = f"{self.config.receipts_prefix}/{refueling_id}{extension}"

        self.client.put_object(
            Bucket=self.config.bucket_name,
            Key=key,
            Body=content,
            ContentType=content_type,
        )

        return key