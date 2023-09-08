from typing import Optional

from thepeer.base import BaseClient, BaseAsyncClient
from thepeer.utils import HTTPMethod, Currency


class LinkClient(BaseClient):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    def get_user_links(self, user_reference: str):
        return self.api_call(
            endpoint_path=f"/users/{user_reference}/links", method=HTTPMethod.GET
        )

    def get_linked_account(self, link_id: str):
        return self.api_call(endpoint_path=f"/link/{link_id}", method=HTTPMethod.GET)

    def charge(
        self, link_id: str, amount: int, remark: str, currency: Currency = Currency.NGN
    ):
        data = {"amount": amount, "remark": remark, "currency": currency}
        return self.api_call(
            endpoint_path=f"/link/{link_id}/charge", method=HTTPMethod.POST, data=data
        )


class AsyncLinkClient(BaseAsyncClient):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    async def get_user_links(self, user_reference: str):
        return await self.api_call(
            endpoint_path=f"/users/{user_reference}/links", method=HTTPMethod.GET
        )

    async def get_linked_account(self, link_id: str):
        return await self.api_call(
            endpoint_path=f"/link/{link_id}", method=HTTPMethod.GET
        )

    async def charge(
        self, link_id: str, amount: int, remark: str, currency: Currency = Currency.NGN
    ):
        data = {"amount": amount, "remark": remark, "currency": currency}
        return await self.api_call(
            endpoint_path=f"/link/{link_id}/charge", method=HTTPMethod.POST, data=data
        )
