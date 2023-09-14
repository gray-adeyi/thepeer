from unittest import TestCase, IsolatedAsyncioTestCase

from dotenv import load_dotenv

from thepeer.clients import LinkClient


class LinkClientTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = LinkClient()

    def test_can_get_user_links(self):
        response = self.client.get_user_links("59e86b01-1a0d-4bd3-955c-746686792e04")
        print(response)

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
