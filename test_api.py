import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_app():
    print("Testing ZeroG API...")
    
    # 1. Test Homepage
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            print("OK - Homepage loaded")
        else:
            print(f"FAIL - Homepage returned {response.status_code}")
    except Exception as e:
        print(f"FAIL - Could not connect to {BASE_URL}: {e}")
        return

    # 2. Test Logging
    log_data = {'text': "2 apples"}
    response = requests.post(f"{BASE_URL}/api/log", json=log_data)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            print("OK - Log entry successful")
            # Verify parsed data (mock logic: apple -> carbs=25)
            # wait, mock logic adds 25 for "apple" (singular/plural check might be simple string match)
            # Code says: if 'apple' in text.lower():
            #   carbs = 25
        else:
            print(f"FAIL - Log entry status: {data.get('status')}")
    else:
        print(f"FAIL - Log endpoint returned {response.status_code}")

    # 3. Test Retrieve Data
    response = requests.get(f"{BASE_URL}/api/data")
    if response.status_code == 200:
        data = response.json()
        if 'totals' in data and 'targets' in data:
            print("OK - Data retrieval successful")
            print(f"   Current Carbs: {data['totals']['carbs']}")
        else:
            print(f"FAIL - Data structure invalid: {data.keys()}")
    else:
        print(f"FAIL - Data endpoint returned {response.status_code}")

    # 4. Test Settings Update
    settings_data = {'diabetes_mode': 1, 'ckd_mode': 0}
    response = requests.post(f"{BASE_URL}/api/settings", json=settings_data)
    if response.status_code == 200:
        print("OK - Settings update successful")
    else:
        print(f"FAIL - Settings endpoint returned {response.status_code}")

if __name__ == "__main__":
    test_app()
