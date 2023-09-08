from typing import Optional

from thepeer.base import BaseClient, BaseAsyncClient
from thepeer.utils import HTTPMethod


class UserClient(BaseClient):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    def create(self, name: str, identifier: str, email: str):
        data = {"name": name, "identifier": identifier, "email": email}
        return self.api_call(endpoint_path="/users", method=HTTPMethod.POST, data=data)

    def all(self, page: int = 1, per_page: int = 10):
        return self.api_call(
            endpoint_path=f"/users?page={page}&perPage={per_page}",
            method=HTTPMethod.GET,
        )

    def update(self, user_reference: str, identifier: str):
        return self.api_call(
            endpoint_path=f"/users/{user_reference}",
            method=HTTPMethod.PUT,
            data={"identifier": identifier},
        )

    def delete(self, user_reference: str):
        return self.api_call(
            endpoint_path=f"/users/{user_reference}", method=HTTPMethod.DELETE
        )


class AsyncUserClient(BaseAsyncClient):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    async def create(self, name: str, identifier: str, email: str):
        data = {"name": name, "identifier": identifier, "email": email}
        return await self.api_call(
            endpoint_path="/users", method=HTTPMethod.POST, data=data
        )

    async def all(self, page: int = 1, per_page: int = 10):
        return await self.api_call(
            endpoint_path=f"/users?page={page}&perPage={per_page}",
            method=HTTPMethod.GET,
        )

    async def update(self, user_reference: str, identifier: str):
        return await self.api_call(
            endpoint_path=f"/users/{user_reference}",
            method=HTTPMethod.PUT,
            data={"identifier": identifier},
        )

    async def delete(self, user_reference: str):
        return await self.api_call(
            endpoint_path=f"/users/{user_reference}", method=HTTPMethod.DELETE
        )
