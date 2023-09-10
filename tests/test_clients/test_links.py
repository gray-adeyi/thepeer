from unittest import TestCase, IsolatedAsyncioTestCase


class LinkClientTestCase(TestCase):
    def test_can_get_user_links(self):
        ...

    def test_can_get_linked_account(self):
        ...

    def test_can_charge(self):
        ...


class AsyncLinkClientTestCase(IsolatedAsyncioTestCase):
    async def test_can_get_user_links(self):
        ...

    async def test_can_get_linked_account(self):
        ...

    async def test_can_charge(self):
        ...
