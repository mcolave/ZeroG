try:
    from food_database import search_food_db
    print(f"Loaded function: {search_food_db}")
    
    res1 = search_food_db("brocolli")
    print(f"brocolli -> {res1}")
    
    res2 = search_food_db("broccoli")
    print(f"broccoli -> {res2}")
    
    import difflib
    print(f"Direct difflib test: {difflib.get_close_matches('brocolli', ['broccoli', 'apple'], n=1, cutoff=0.6)}")
    
except ImportError as e:
    print(f"Import Error: {e}")
except Exception as e:
    print(f"Error: {e}")
