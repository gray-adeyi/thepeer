from unittest import TestCase, IsolatedAsyncioTestCase
from uuid import uuid4
from httpx import codes
from dotenv import load_dotenv

from thepeer.clients import UserClient, AsyncUserClient


class UserClientTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = UserClient()

    def test_can_create(self):
        name = "John Doe"
        email = f"johndoe{uuid4()}@example.com"
        response = self.client.create(
            name=name,
            identifier=email,
            email=email,
        )
        self.assertEqual(response.status_code, codes.CREATED)
        self.assertEqual(response.data["indexed_user"]["name"], name)
        self.assertEqual(response.data["indexed_user"]["identifier"], email)

    def test_can_all(self):
        response = self.client.all()
        self.assertEqual(response.status_code, codes.OK)
        self.assertIsInstance(response.data["indexed_users"]["data"], list)

    def test_can_update(self):
        new_identifier = "johndoe@example.com"
        response = self.client.update(
            user_reference="59e86b01-1a0d-4bd3-955c-746686792e04",
            identifier=new_identifier,
        )
        self.assertEqual(response.status_code, codes.OK)
        self.assertEqual(response.data["indexed_user"]["identifier"], new_identifier)

    def test_can_delete(self):
        user_reference = self.client.all().data["indexed_users"]["data"][-1][
            "reference"
        ]
        response = self.client.delete(user_reference)
        self.assertEqual(response.status_code, codes.OK)
        self.assertDictEqual(response.data, {"message": "user deleted"})


class AsyncUserClientTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncUserClient()

    async def test_can_create(self):
        name = "John Doe"
        email = f"johndoe{uuid4()}@example.com"
        response = await self.client.create(
            name=name,
            identifier=email,
            email=email,
        )
        self.assertEqual(response.status_code, codes.CREATED)
        self.assertEqual(response.data["indexed_user"]["name"], name)
        self.assertEqual(response.data["indexed_user"]["identifier"], email)

    async def test_can_all(self):
        response = await self.client.all()
        self.assertEqual(response.status_code, codes.OK)
        self.assertIsInstance(response.data["indexed_users"]["data"], list)

    async def test_can_update(self):
        new_identifier = "johndoe@example.com"
        response = await self.client.update(
            user_reference="59e86b01-1a0d-4bd3-955c-746686792e04",
            identifier=new_identifier,
        )
        self.assertEqual(response.status_code, codes.OK)
        self.assertEqual(response.data["indexed_user"]["identifier"], new_identifier)

    async def test_can_delete(self):
        user_reference = (await self.client.all()).data["indexed_users"]["data"][-1][
            "reference"
        ]
        response = await self.client.delete(user_reference)
        self.assertEqual(response.status_code, codes.OK)
        self.assertDictEqual(response.data, {"message": "user deleted"})
