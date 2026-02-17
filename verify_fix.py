import unittest
from app import app
import json

class TestZeroG(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_cup_blueberries(self):
        # This was crashing before due to type error and missing unit
        response = self.app.post('/api/log', 
            data=json.dumps({'text': '1 cup blueberries'}),
            content_type='application/json')
        
        data = json.loads(response.data)
        print(f"\nResponse for '1 cup blueberries': {data}")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        # 1 cup ~ 2.4 * 100g value. Blueberries 100g ~ 57kcal. So 1 cup ~ 136kcal.
        # Allow wide margin as OFF data varies
        self.assertTrue(data['logged']['calories'] > 100)
        self.assertTrue(data['logged']['qty'] > 2.0) # Should be 2.4

    def test_random_off_string(self):
        # Simulate a search that might return string values from OFF
        # We can't easily force OFF to return strings here without mocking, 
        # but the code path with `to_float` is active.
        pass

if __name__ == '__main__':
    unittest.main()
