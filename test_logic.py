import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_unknown_flow():
    print("Testing ZeroG Unknown Food Flow...")
    
    # 1. Test "lechon" (should be unknown initially)
    print("1. Logging '2 lechon'...")
    log_data = {'text': "2 lechon"}
    response = requests.post(f"{BASE_URL}/api/log", json=log_data)
    try:
        data = response.json()
    except json.JSONDecodeError:
        print(f"FAIL: JSON Decode Error. Status: {response.status_code}")
        print(f"Response Text: {response.text}")
        return

    if data.get('status') == 'unknown':
        print("PASS: Correctly identified unknown food.")
    else:
        print(f"FAIL: Expected 'unknown', got {data.get('status')}")
        # If it was already added (from previous run), this test might fail. 
        # But we are in-memory SQLite usually? No, it's file based 'zerog.db'.
        # We might need to cleanup DB.
        
    # 2. Add "lechon"
    print("2. Adding 'lechon' to DB...")
    food_data = {
        'name': 'lechon',
        'carbs': 5,
        'fats': 30,
        'protein': 25,
        'calories': 400
    }
    response = requests.post(f"{BASE_URL}/api/add_food", json=food_data)
    if response.status_code == 200:
        print("PASS: Food added.")
    else:
        print(f"FAIL: Add food failed {response.status_code}")

    # 3. Test "2 lechon" again (should succeed)
    print("3. Logging '2 lechon' again...")
    response = requests.post(f"{BASE_URL}/api/log", json=log_data)
    data = response.json()
    
    if data.get('status') == 'success':
        logged = data['logged']
        # 2 lechon = 2 * (5 carbs, 30 fats, 25 protein)
        # Expect 10 carbs, 60 fats, 50 protein
        print(f"PASS: Logged successfully. Stats: {logged}")
        if logged['carbs'] == 10 and logged['protein'] == 50:
             print("PASS: Macros calculated correctly.")
        else:
             print(f"FAIL: Macros incorrect. Got {logged}")
    else:
        print(f"FAIL: Expected 'success', got {data.get('status')}")

if __name__ == "__main__":
    test_unknown_flow()
