from unittest import TestCase, IsolatedAsyncioTestCase

from thepeer._base import BaseClient, __version__


class BaseClientTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.secret_key = "qwerty"
        cls.client = BaseClient(cls.secret_key)

    def test_base_url(self):
        self.assertEqual(
            self.client.BASE_URL, "https://api.thepeer.co", "BASE_URL has changed"
        )

    def test_headers(self):
        expected_headers = {
            "x-api-key": self.secret_key,
            "Accept": "Application/json",
            "User-Agent": f"thepeer {__version__}",
        }
        self.assertDictEqual(
            self.client.headers, expected_headers, "expected headers not provided"
        )

    def test_api_call(self):
        ...


class BaseAsyncClient(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.secret_key = "qwerty"
        cls.client = BaseClient(cls.secret_key)

    def test_base_url(self):
        self.assertEqual(
            self.client.BASE_URL, "https://api.thepeer.co", "BASE_URL has changed"
        )

    def test_headers(self):
        expected_headers = {
            "x-api-key": self.secret_key,
            "Accept": "Application/json",
            "User-Agent": f"thepeer {__version__}",
        }
        self.assertDictEqual(
            self.client.headers, expected_headers, "expected headers not provided"
        )

    async def test_api_call(self):
        ...
