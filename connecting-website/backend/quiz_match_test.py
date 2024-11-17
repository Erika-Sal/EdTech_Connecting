import unittest
from app import app  # Import your Flask app here

class FlaskTestCase(unittest.TestCase):
    def test_knn_match(self):
        tester = app.test_client()
        response = tester.post(
            '/api/match',
            json={"answers": [1, 2, 0, 1]},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Music Club', response.data)

if __name__ == '__main__':
    unittest.main()
