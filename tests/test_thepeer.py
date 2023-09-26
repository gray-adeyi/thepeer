from unittest import TestCase, IsolatedAsyncioTestCase

from thepeer import ThePeerClient, AsyncThePeerClient, PaymentChannel
from thepeer.clients import (
    UserClient,
    TransactionClient,
    LinkClient,
    AsyncUserClient,
    AsyncLinkClient,
    AsyncTransactionClient,
)
from dotenv import load_dotenv
from httpx import codes


class ThePeerClientTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = ThePeerClient()

    def test_has_attr_users(self):
        self.assertIsInstance(getattr(self.client, "users"), UserClient)

    def test_has_attr_transactions(self):
        self.assertIsInstance(getattr(self.client, "transactions"), TransactionClient)

    def test_has_attr_links(self):
        self.assertIsInstance(getattr(self.client, "links"), LinkClient)

    def test_can_authorize_charge(self):
        ...

    def test_can_generate_checkout(self):
        response = self.client.generate_checkout(10_000, "johndoe@example.com")
        self.assertEqual(response.status_code, codes.OK)
        self.assertEqual(response.data["checkout"]["amount"], 10_000)
        self.assertEqual(response.data["checkout"]["email"], "johndoe@example.com")

    def test_can_get_businesses(self):
        response = self.client.get_businesses(channel=PaymentChannel.SEND)
        self.assertEqual(response.status_code, codes.NOT_ACCEPTABLE)
        expected_data = {"message": "only available on live mode"}
        self.assertDictEqual(response.data, expected_data)


class AsyncThePeerClientTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncThePeerClient()

    def test_has_attr_users(self):
        self.assertIsInstance(getattr(self.client, "users"), AsyncUserClient)

    def test_has_attr_transactions(self):
        self.assertIsInstance(
            getattr(self.client, "transactions"), AsyncTransactionClient
        )

    def test_has_attr_links(self):
        self.assertIsInstance(getattr(self.client, "links"), AsyncLinkClient)

    async def test_can_authorize_charge(self):
        ...

    async def test_can_generate_checkout(self):
        response = await self.client.generate_checkout(10_000, "johndoe@example.com")
        self.assertEqual(response.status_code, codes.OK)
        self.assertEqual(response.data["checkout"]["amount"], 10_000)
        self.assertEqual(response.data["checkout"]["email"], "johndoe@example.com")

    async def test_can_get_businesses(self):
        response = await self.client.get_businesses(channel=PaymentChannel.SEND)
        self.assertEqual(response.status_code, codes.NOT_ACCEPTABLE)
        expected_data = {"message": "only available on live mode"}
        self.assertDictEqual(response.data, expected_data)
