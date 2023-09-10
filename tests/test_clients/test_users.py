from unittest import TestCase, IsolatedAsyncioTestCase


class UserClientTestCase(TestCase):
    def test_can_create(self):
        ...

    def test_can_all(self):
        ...

    def test_can_update(self):
        ...

    def test_can_delete(self):
        ...


class AsyncUserClientTestCase(IsolatedAsyncioTestCase):
    async def test_can_create(self):
        ...

    async def test_can_all(self):
        ...

    async def test_can_update(self):
        ...

    async def test_can_delete(self):
        ...
