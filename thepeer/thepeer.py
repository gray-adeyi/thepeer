from typing import Optional

from thepeer.base import BaseClient, BaseAsyncClient
from thepeer.clients.links import LinkClient, AsyncLinkClient
from thepeer.clients.transactions import TransactionClient, AsyncTransactionClient
from thepeer.clients.users import UserClient, AsyncUserClient
from thepeer.utils import ChargeEvent, HTTPMethod, Response, Currency


class ThePeerClient(BaseClient):
    def __init__(self, secret_key: str):
        super().__init__(secret_key)
        self.users = UserClient(self.secret_key)
        self.transactions = TransactionClient(self.secret_key)
        self.links = LinkClient(self.secret_key)

    def charge(self, reference: str, event: ChargeEvent) -> Response:
        return self.api_call(
            endpoint_path=f"/authorization/{reference}",
            method=HTTPMethod.POST,
            data={"event": event},
        )

    def checkout(
        self,
        amount: int,
        email: str,
        redirect_url: Optional[str] = None,
        meta: Optional[dict] = None,
        currency: Currency = Currency.NGN,
    ):
        data = {
            "currency": currency,
            "amount": amount,
            "email": email,
            "redirect_url": redirect_url,
            "meta": meta,
        }
        return self.api_call(
            endpoint_path="/checkout", method=HTTPMethod.POST, data=data
        )


class AsyncThePeerClient(BaseAsyncClient):
    def __init__(self, secret_key: str):
        super().__init__(secret_key)
        self.users = AsyncUserClient(self.secret_key)
        self.transactions = AsyncTransactionClient(self.secret_key)
        self.links = AsyncLinkClient(self.secret_key)

    async def charge(self, reference: str, event: ChargeEvent) -> Response:
        return await self.api_call(
            endpoint_path=f"/authorization/{reference}",
            method=HTTPMethod.POST,
            data={"event": event},
        )

    async def checkout(
        self,
        amount: int,
        email: str,
        redirect_url: Optional[str] = None,
        meta: Optional[dict] = None,
        currency: Currency = Currency.NGN,
    ):
        data = {
            "currency": currency,
            "amount": amount,
            "email": email,
            "redirect_url": redirect_url,
            "meta": meta,
        }
        return await self.api_call(
            endpoint_path="/checkout", method=HTTPMethod.POST, data=data
        )
