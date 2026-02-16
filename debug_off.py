import requests
import json

def test_off(query):
    print(f"Testing OpenFoodFacts for: '{query}'")
    try:
        url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={query}&search_simple=1&action=process&json=1"
        print(f"URL: {url}")
        r = requests.get(url, timeout=5)
        print(f"Status: {r.status_code}")
        if r.status_code == 200:
            data = r.json()
            count = data.get('count', 0)
            print(f"Count: {count}")
            if count > 0:
                print("First result:", data['products'][0]['product_name'])
            else:
                print("No products found.")
    except Exception as e:
        print(f"Error: {e}")

test_off("pearl barley")
