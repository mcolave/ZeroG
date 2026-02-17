import threading
import requests
import time
import random

# Configuration
BASE_URL = "http://127.0.0.1:5000"
NUM_THREADS = 10
REQUESTS_PER_THREAD = 5

def log_food(thread_id):
    foods = ["apple", "banana", "2 eggs", "rice", "chicken", "100g oats", "milk"]
    for i in range(REQUESTS_PER_THREAD):
        food = random.choice(foods)
        try:
            # print(f"Thread {thread_id} sending request {i+1} for {food}")
            response = requests.post(f"{BASE_URL}/api/log", json={"text": food}, timeout=10)
            if response.status_code == 200:
                pass # print(f"Thread {thread_id} success: {food}")
            else:
                print(f"Thread {thread_id} FAILED: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Thread {thread_id} EXCEPTION: {e}")

def run_stress_test():
    print(f"Starting stress test with {NUM_THREADS} threads, {REQUESTS_PER_THREAD} requests each.")
    threads = []
    start_time = time.time()
    
    for i in range(NUM_THREADS):
        t = threading.Thread(target=log_food, args=(i,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    duration = time.time() - start_time
    print(f"Stress test completed in {duration:.2f} seconds.")

if __name__ == "__main__":
    # Ensure app is running on port 5000 before running this!
    try:
        requests.get(f"{BASE_URL}/")
        run_stress_test()
    except requests.exceptions.ConnectionError:
        print("Error: ZeroG app is not running at http://127.0.0.1:5000. Please start it first.")
