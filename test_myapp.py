import unittest
from myapp import app

class MyAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to my Flask app!', response.data)

    def test_hello(self):
        name = 'Alice'
        response = self.app.get(f'/hello/{name}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(f'Hello, {name}!'.encode(), response.data)

if __name__ == '__main__':
    unittest.main()
