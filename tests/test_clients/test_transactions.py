from unittest import TestCase, IsolatedAsyncioTestCase

from dotenv import load_dotenv

from thepeer.clients import TransactionClient


class TransactionClientTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = TransactionClient()

    def test_can_get(self):
        ...

    def test_can_refund(self):
        ...


class AsyncTransactionClientTestCase(IsolatedAsyncioTestCase):
    async def test_can_get(self):
        ...

    async def test_can_refund(self):
        ...
