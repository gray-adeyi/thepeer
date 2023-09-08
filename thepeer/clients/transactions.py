from typing import Optional

from thepeer.base import BaseClient, BaseAsyncClient
from thepeer.utils import HTTPMethod


class TransactionClient(BaseClient):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    def get(self, transaction_id: str):
        return self.api_call(
            endpoint_path=f"/transactions/{transaction_id}", method=HTTPMethod.GET
        )

    def refund(self, transaction_id: str, reason: str):
        return self.api_call(
            endpoint_path=f"/transactions/{transaction_id}/refund",
            method=HTTPMethod.POST,
            data={"reason": reason},
        )


class AsyncTransactionClient(BaseAsyncClient):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    async def get(self, transaction_id: str):
        return await self.api_call(
            endpoint_path=f"/transactions/{transaction_id}", method=HTTPMethod.GET
        )

    async def refund(self, transaction_id: str, reason: str):
        return await self.api_call(
            endpoint_path=f"/transactions/{transaction_id}/refund",
            method=HTTPMethod.POST,
            data={"reason": reason},
        )
