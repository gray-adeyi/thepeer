from typing import Optional

from thepeer.base import BaseClient, BaseAsyncClient
from thepeer.clients.links import LinkClient, AsyncLinkClient
from thepeer.clients.transactions import TransactionClient, AsyncTransactionClient
from thepeer.clients.users import UserClient, AsyncUserClient
from thepeer.utils import ChargeEvent, HTTPMethod, Response, Currency


class ThePeerClient(BaseClient):
    """ThePeerClient provides methods and attributes that serves as a
    convenience for interacting with thepeer"""

    def __init__(self, secret_key: str):
        """
        Args:
             secret_key: your thepeer secret_key. if not provide.
                the client tries to access your thepeer secret key
                from your environmental variables via.
                THEPEER_SECRET_KEY=<secret_key>. if the secret
                key is provided on instantiation, it overrides
                the secret key in the environmental variables.
        """
        super().__init__(secret_key)
        self.users = UserClient(self.secret_key)
        self.transactions = TransactionClient(self.secret_key)
        self.links = LinkClient(self.secret_key)

    def charge(self, charge_reference: str, event: ChargeEvent) -> Response:
        """Process a charge authorization request.

        Arg:
            charge_reference: The reference of the charge in the authorization payload
            event: The event is a required string that could be one of four supported
                values that describes the status of the charge

        Returns:
            Response: A dataclass containing the HTTP status code and
                data returned by thepeer servers
        """
        return self.api_call(
            endpoint_path=f"/authorization/{charge_reference}",
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
    ) -> Response:
        """Generate a checkout.

        Args:
            amount: The amount you are debiting the customer.
                This should be in kobo. The minimum value is 10000
            email: The customer’s email address
            redirect_url: The url we should redirect to after the
                customer completes payment.
            meta: An dict containing additional attributes you
                would like to have in your transaction response.
            currency: The currency the transaction should be
                carried out in. The supported value is `Currency.NGN`

        Returns:
            Response: A dataclass containing the HTTP status code and
                data returned by thepeer servers
        """
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
    """AsyncThePeerClient is an async equivalent of ThePeerClient that provides
    methods and attributes that serves as a convenience for interacting with thepeer."""

    def __init__(self, secret_key: str):
        """
        Args:
             secret_key: your thepeer secret_key. if not provide.
                the client tries to access your thepeer secret key
                from your environmental variables via.
                THEPEER_SECRET_KEY=<secret_key>. if the secret
                key is provided on instantiation, it overrides
                the secret key in the environmental variables.
        """
        super().__init__(secret_key)
        self.users = AsyncUserClient(self.secret_key)
        self.transactions = AsyncTransactionClient(self.secret_key)
        self.links = AsyncLinkClient(self.secret_key)

    async def charge(self, reference: str, event: ChargeEvent) -> Response:
        """Process a charge authorization request.

        Arg:
            charge_reference: The reference of the charge in the authorization payload
            event: The event is a required string that could be one of four supported
                values that describes the status of the charge

        Returns:
            Response: A dataclass containing the HTTP status code and
                data returned by thepeer servers
        """
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
    ) -> Response:
        """Generate a checkout.

        Args:
            amount: The amount you are debiting the customer.
                This should be in kobo. The minimum value is 10000
            email: The customer’s email address
            redirect_url: The url we should redirect to after the
                customer completes payment.
            meta: An dict containing additional attributes you
                would like to have in your transaction response.
            currency: The currency the transaction should be
                carried out in. The supported value is `Currency.NGN`

        Returns:
            Response: A dataclass containing the HTTP status code and
                data returned by thepeer servers
        """
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
