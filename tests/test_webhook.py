import unittest
from app import app

class WebhookTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_invalid_auth(self):
        response = self.client.post('/webhook', json={}, headers={"Authorization": "Bearer wrong"})
        self.assertEqual(response.status_code, 401)

    def test_missing_fields(self):
        response = self.client.post('/webhook', json={}, headers={"Authorization": "Bearer your_secure_token"})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
