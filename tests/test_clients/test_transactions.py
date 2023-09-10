from unittest import TestCase, IsolatedAsyncioTestCase


class TransactionClientTestCase(TestCase):
    def test_can_get(self):
        ...

    def test_can_refund(self):
        ...


class AsyncTransactionClientTestCase(IsolatedAsyncioTestCase):
    async def test_can_get(self):
        ...

    async def test_can_refund(self):
        ...
