# Simulated "Online" Database
# Nutritional values per 100g (approximate)

FOOD_DB = {
    # Fruits & Vegetables
    'apple': {'carbs': 14, 'fats': 0.2, 'protein': 0.3, 'calories': 52, 'potassium': 107, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 36},
    'banana': {'carbs': 23, 'fats': 0.3, 'protein': 1.1, 'calories': 89, 'potassium': 358, 'sodium': 1, 'saturated_fat': 0.1, 'trans_fat': 0, 'gi': 51},
    'eggplant': {'carbs': 6, 'fats': 0.2, 'protein': 1, 'calories': 25, 'potassium': 229, 'sodium': 2, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'spinach': {'carbs': 3.6, 'fats': 0.4, 'protein': 2.9, 'calories': 23, 'potassium': 558, 'sodium': 79, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'broccoli': {'carbs': 7, 'fats': 0.4, 'protein': 2.8, 'calories': 34, 'potassium': 316, 'sodium': 33, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'carrot': {'carbs': 10, 'fats': 0.2, 'protein': 0.9, 'calories': 41, 'potassium': 320, 'sodium': 69, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 39},
    'radish': {'carbs': 3.4, 'fats': 0.1, 'protein': 0.7, 'calories': 16, 'potassium': 233, 'sodium': 39, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'white radish': {'carbs': 4.1, 'fats': 0.1, 'protein': 0.6, 'calories': 18, 'potassium': 227, 'sodium': 21, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'white raddish': {'carbs': 4.1, 'fats': 0.1, 'protein': 0.6, 'calories': 18, 'potassium': 227, 'sodium': 21, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15}, # Typo handling
    'daikon': {'carbs': 4.1, 'fats': 0.1, 'protein': 0.6, 'calories': 18, 'potassium': 227},
    'lettuce': {'carbs': 2.9, 'fats': 0.2, 'protein': 1.4, 'calories': 15, 'potassium': 194},
    'cucumber': {'carbs': 3.6, 'fats': 0.1, 'protein': 0.7, 'calories': 15, 'potassium': 147},
    'tomato': {'carbs': 3.9, 'fats': 0.2, 'protein': 0.9, 'calories': 18, 'potassium': 237},
    'potato': {'carbs': 17, 'fats': 0.1, 'protein': 2, 'calories': 77, 'potassium': 421},
    'garlic': {'carbs': 33, 'fats': 0.5, 'protein': 6.4, 'calories': 149, 'potassium': 401},
    'onion': {'carbs': 9, 'fats': 0.1, 'protein': 1.1, 'calories': 40, 'potassium': 146},
    
    'rice': {'carbs': 28, 'fats': 0.3, 'protein': 2.7, 'calories': 130, 'potassium': 35},
    'white rice': {'carbs': 28, 'fats': 0.3, 'protein': 2.7, 'calories': 130, 'potassium': 35},
    'brown rice': {'carbs': 23, 'fats': 0.9, 'protein': 2.6, 'calories': 111, 'potassium': 43},
    'pearl barley': {'carbs': 28, 'fats': 0.4, 'protein': 2.3, 'calories': 123, 'potassium': 93},
    'barley': {'carbs': 28, 'fats': 0.4, 'protein': 2.3, 'calories': 123, 'potassium': 93},
    'quinoa': {'carbs': 21, 'fats': 1.9, 'protein': 4.4, 'calories': 120, 'potassium': 172},
    'oats': {'carbs': 12, 'fats': 1.4, 'protein': 2.4, 'calories': 68, 'potassium': 80}, # Porridge/cooked
    
    # Proteins
    'egg': {'carbs': 1.1, 'fats': 11, 'protein': 13, 'calories': 155, 'potassium': 126},
    'boiled egg': {'carbs': 1.1, 'fats': 11, 'protein': 13, 'calories': 155, 'potassium': 126},
    'fried egg': {'carbs': 0.8, 'fats': 15, 'protein': 14, 'calories': 196, 'potassium': 132},
    'chicken': {'carbs': 0, 'fats': 3.6, 'protein': 31, 'calories': 165, 'potassium': 256},
    'chicken breast': {'carbs': 0, 'fats': 3.6, 'protein': 31, 'calories': 165, 'potassium': 256},
    'pork': {'carbs': 0, 'fats': 14, 'protein': 27, 'calories': 242, 'potassium': 423},
    'beef': {'carbs': 0, 'fats': 15, 'protein': 26, 'calories': 250, 'potassium': 318},
    'fish': {'carbs': 0, 'fats': 12, 'protein': 20, 'calories': 206, 'potassium': 384},
    'salmon': {'carbs': 0, 'fats': 13, 'protein': 20, 'calories': 208, 'potassium': 363},
    
    # Filipino / Asian Common
    'lechon': {'carbs': 0, 'fats': 25, 'protein': 27, 'calories': 350, 'potassium': 300, 'sodium': 510, 'saturated_fat': 11, 'trans_fat': 0, 'gi': 0},
    'lechon belly': {'carbs': 0, 'fats': 28, 'protein': 25, 'calories': 380, 'potassium': 280, 'sodium': 540, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 0},
    'adobo': {'carbs': 2, 'fats': 18, 'protein': 25, 'calories': 280, 'potassium': 250, 'sodium': 850, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 0},
    'sinigang': {'carbs': 5, 'fats': 8, 'protein': 15, 'calories': 150, 'potassium': 200, 'sodium': 600, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 0},
    'sisig': {'carbs': 2, 'fats': 30, 'protein': 20, 'calories': 380, 'potassium': 280, 'sodium': 550, 'saturated_fat': 9, 'trans_fat': 0.5, 'gi': 0},
    'pancit': {'carbs': 35, 'fats': 8, 'protein': 10, 'calories': 250, 'potassium': 100, 'sodium': 700, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 45},
    
    # Common Snacks/Others
    'bread': {'carbs': 49, 'fats': 3.2, 'protein': 9, 'calories': 265, 'potassium': 115},
    'white bread': {'carbs': 49, 'fats': 3.2, 'protein': 9, 'calories': 265, 'potassium': 115},
    'whole wheat bread': {'carbs': 41, 'fats': 3.5, 'protein': 13, 'calories': 247, 'potassium': 250},
    'low gi bread': {'carbs': 40, 'fats': 4, 'protein': 12, 'calories': 240, 'potassium': 200},
    'multigrain bread': {'carbs': 43, 'fats': 4.2, 'protein': 13, 'calories': 265, 'potassium': 220},
    
    'milk': {'carbs': 5, 'fats': 3.2, 'protein': 3.4, 'calories': 60, 'potassium': 150, 'sodium': 44, 'saturated_fat': 1.9, 'trans_fat': 0.1, 'gi': 31},
    'coffee': {'carbs': 0, 'fats': 0, 'protein': 0.1, 'calories': 1, 'potassium': 49, 'sodium': 2, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    
    # Condiments / Cooking
    'salt': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 8, 'sodium': 38758, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'sugar': {'carbs': 100, 'fats': 0, 'protein': 0, 'calories': 387, 'potassium': 2, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'oil': {'carbs': 0, 'fats': 100, 'protein': 0, 'calories': 884, 'potassium': 0, 'sodium': 0, 'saturated_fat': 13, 'trans_fat': 0, 'gi': 0}, # Generic vegetable oil
    'olive oil': {'carbs': 0, 'fats': 100, 'protein': 0, 'calories': 884, 'potassium': 0, 'sodium': 0, 'saturated_fat': 14, 'trans_fat': 0, 'gi': 0},
    'soy sauce': {'carbs': 5, 'fats': 0.1, 'protein': 8, 'calories': 53, 'potassium': 200, 'sodium': 5493, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    
    # Fast Food / Western
    'burger': {'carbs': 30, 'fats': 14, 'protein': 16, 'calories': 295, 'potassium': 250, 'sodium': 450, 'saturated_fat': 5, 'trans_fat': 0.5, 'gi': 66},
    'cheeseburger': {'carbs': 30, 'fats': 16, 'protein': 18, 'calories': 320, 'potassium': 280, 'sodium': 550, 'saturated_fat': 7, 'trans_fat': 0.5, 'gi': 66},
    'fries': {'carbs': 41, 'fats': 15, 'protein': 3.4, 'calories': 312, 'potassium': 579, 'sodium': 210, 'saturated_fat': 2.3, 'trans_fat': 0.1, 'gi': 75},
    'french fries': {'carbs': 41, 'fats': 15, 'protein': 3.4, 'calories': 312, 'potassium': 579, 'sodium': 210, 'saturated_fat': 2.3, 'trans_fat': 0.1, 'gi': 75},
    'pizza': {'carbs': 33, 'fats': 10, 'protein': 11, 'calories': 266, 'potassium': 170, 'sodium': 600, 'saturated_fat': 4.5, 'trans_fat': 0.2, 'gi': 60}, # per slice (approx 100g)
    'hotdog': {'carbs': 2, 'fats': 25, 'protein': 10, 'calories': 290, 'potassium': 150, 'sodium': 1000, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},
    'fried chicken': {'carbs': 10, 'fats': 15, 'protein': 25, 'calories': 280, 'potassium': 220, 'sodium': 600, 'saturated_fat': 4, 'trans_fat': 0.2, 'gi': 0},
    
    # Breakfast
    'bacon': {'carbs': 1.4, 'fats': 42, 'protein': 37, 'calories': 541, 'potassium': 565, 'sodium': 1717, 'saturated_fat': 14, 'trans_fat': 0, 'gi': 0},
    'sausage': {'carbs': 2, 'fats': 27, 'protein': 14, 'calories': 300, 'potassium': 200, 'sodium': 800, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},
    'toast': {'carbs': 50, 'fats': 4, 'protein': 9, 'calories': 270, 'potassium': 120, 'sodium': 450, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 70},
    'butter': {'carbs': 0.1, 'fats': 81, 'protein': 0.9, 'calories': 717, 'potassium': 24, 'sodium': 11, 'saturated_fat': 51, 'trans_fat': 3, 'gi': 0},
    'cheese': {'carbs': 1.3, 'fats': 33, 'protein': 25, 'calories': 402, 'potassium': 98, 'sodium': 621, 'saturated_fat': 21, 'trans_fat': 1, 'gi': 0}, # Cheddar-ish
    'yogurt': {'carbs': 4.7, 'fats': 3.3, 'protein': 3.5, 'calories': 61, 'potassium': 155, 'sodium': 46, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 35},
    
    # Extended Filipino
    'tapa': {'carbs': 5, 'fats': 12, 'protein': 25, 'calories': 230, 'potassium': 300, 'sodium': 800, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 0},
    'longganisa': {'carbs': 10, 'fats': 25, 'protein': 12, 'calories': 320, 'potassium': 200, 'sodium': 900, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 50},
    'tocino': {'carbs': 15, 'fats': 20, 'protein': 10, 'calories': 280, 'potassium': 150, 'sodium': 600, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 60},
    'pandesal': {'carbs': 55, 'fats': 5, 'protein': 10, 'calories': 300, 'potassium': 100, 'sodium': 400, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 70},
    'kare-kare': {'carbs': 8, 'fats': 15, 'protein': 18, 'calories': 240, 'potassium': 300, 'sodium': 500, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 0},
    'lumpia': {'carbs': 20, 'fats': 15, 'protein': 8, 'calories': 250, 'potassium': 150, 'sodium': 400, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 60}, # Fried spring roll
    'champorado': {'carbs': 40, 'fats': 2, 'protein': 4, 'calories': 200, 'potassium': 150, 'sodium': 20, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 70},
    
    # More Fruits
    'orange': {'carbs': 12, 'fats': 0.1, 'protein': 0.9, 'calories': 47, 'potassium': 181, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 40},
    'mango': {'carbs': 15, 'fats': 0.4, 'protein': 0.8, 'calories': 60, 'potassium': 168, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 51},
    'pineapple': {'carbs': 13, 'fats': 0.1, 'protein': 0.5, 'calories': 50, 'potassium': 109, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 59},
    'watermelon': {'carbs': 8, 'fats': 0.2, 'protein': 0.6, 'calories': 30, 'potassium': 112, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 72},
    'grapes': {'carbs': 18, 'fats': 0.2, 'protein': 0.7, 'calories': 69, 'potassium': 191, 'sodium': 2, 'saturated_fat': 0.1, 'trans_fat': 0, 'gi': 59},
    
    # Drinks
    'coke': {'carbs': 10.6, 'fats': 0, 'protein': 0, 'calories': 42, 'potassium': 0, 'sodium': 4, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 60},
    'soda': {'carbs': 10.6, 'fats': 0, 'protein': 0, 'calories': 42, 'potassium': 0, 'sodium': 4, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 60},
    'sprite': {'carbs': 10, 'fats': 0, 'protein': 0, 'calories': 40, 'potassium': 0, 'sodium': 9, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 60},
    'orange juice': {'carbs': 10, 'fats': 0.2, 'protein': 0.7, 'calories': 45, 'potassium': 200, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 50},
    'iced tea': {'carbs': 8, 'fats': 0, 'protein': 0, 'calories': 32, 'potassium': 10, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 40},

    # Italian
    'pasta': {'carbs': 25, 'fats': 1.1, 'protein': 5, 'calories': 131, 'potassium': 24, 'sodium': 6, 'saturated_fat': 0.2, 'trans_fat': 0, 'gi': 50},
    'spaghetti': {'carbs': 30, 'fats': 1, 'protein': 5, 'calories': 158, 'potassium': 44, 'sodium': 1, 'saturated_fat': 0.2, 'trans_fat': 0, 'gi': 45},
    'carbonara': {'carbs': 25, 'fats': 15, 'protein': 10, 'calories': 290, 'potassium': 150, 'sodium': 400, 'saturated_fat': 7, 'trans_fat': 0.2, 'gi': 55},
    'bolognese': {'carbs': 18, 'fats': 6, 'protein': 8, 'calories': 160, 'potassium': 300, 'sodium': 350, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 50},
    'lasagna': {'carbs': 15, 'fats': 5, 'protein': 7, 'calories': 135, 'potassium': 200, 'sodium': 300, 'saturated_fat': 2.5, 'trans_fat': 0.1, 'gi': 50},
    'risotto': {'carbs': 50, 'fats': 12, 'protein': 8, 'calories': 340, 'potassium': 100, 'sodium': 400, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 70},
    'tiramisu': {'carbs': 40, 'fats': 20, 'protein': 6, 'calories': 380, 'potassium': 100, 'sodium': 150, 'saturated_fat': 10, 'trans_fat': 0.5, 'gi': 60},

    # Japanese
    'sushi': {'carbs': 30, 'fats': 0.5, 'protein': 5, 'calories': 150, 'potassium': 100, 'sodium': 400, 'saturated_fat': 0.1, 'trans_fat': 0, 'gi': 55},
    'sashimi': {'carbs': 0, 'fats': 5, 'protein': 25, 'calories': 150, 'potassium': 400, 'sodium': 50, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 0},
    'ramen': {'carbs': 55, 'fats': 18, 'protein': 10, 'calories': 436, 'potassium': 300, 'sodium': 1500, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 50},
    'tempura': {'carbs': 20, 'fats': 15, 'protein': 8, 'calories': 250, 'potassium': 150, 'sodium': 300, 'saturated_fat': 2, 'trans_fat': 0.1, 'gi': 60},
    'gyoza': {'carbs': 20, 'fats': 8, 'protein': 6, 'calories': 180, 'potassium': 120, 'sodium': 350, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 55},
    'miso soup': {'carbs': 5, 'fats': 1, 'protein': 3, 'calories': 40, 'potassium': 150, 'sodium': 600, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 30},
    'teriyaki': {'carbs': 15, 'fats': 8, 'protein': 20, 'calories': 220, 'potassium': 350, 'sodium': 700, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 50},
    'matcha': {'carbs': 0, 'fats': 0, 'protein': 0.5, 'calories': 3, 'potassium': 20, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},

    # Chinese
    'fried rice': {'carbs': 30, 'fats': 6, 'protein': 5, 'calories': 190, 'potassium': 100, 'sodium': 350, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 65},
    'chow mein': {'carbs': 25, 'fats': 10, 'protein': 8, 'calories': 220, 'potassium': 150, 'sodium': 500, 'saturated_fat': 2, 'trans_fat': 0.1, 'gi': 55},
    'siomai': {'carbs': 10, 'fats': 12, 'protein': 10, 'calories': 200, 'potassium': 150, 'sodium': 400, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 45},
    'dumpling': {'carbs': 20, 'fats': 5, 'protein': 6, 'calories': 150, 'potassium': 100, 'sodium': 300, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 45},
    'sweet and sour pork': {'carbs': 25, 'fats': 15, 'protein': 10, 'calories': 275, 'potassium': 250, 'sodium': 350, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 60},
    'mapo tofu': {'carbs': 8, 'fats': 12, 'protein': 10, 'calories': 180, 'potassium': 200, 'sodium': 500, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 30},
    'spring roll': {'carbs': 20, 'fats': 10, 'protein': 4, 'calories': 190, 'potassium': 120, 'sodium': 300, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 55},

    # FairPrice / SG / Local Snacks
    'milo': {'carbs': 60, 'fats': 10, 'protein': 12, 'calories': 400, 'potassium': 300, 'sodium': 150, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 55}, # Power/Dinosaur typically high sugar
    'maggi': {'carbs': 60, 'fats': 15, 'protein': 8, 'calories': 400, 'potassium': 100, 'sodium': 1800, 'saturated_fat': 7, 'trans_fat': 0.2, 'gi': 60}, # Instant Noodles
    'indomie': {'carbs': 60, 'fats': 20, 'protein': 8, 'calories': 450, 'potassium': 100, 'sodium': 1600, 'saturated_fat': 9, 'trans_fat': 0.5, 'gi': 60},
    'prawn crackers': {'carbs': 65, 'fats': 25, 'protein': 3, 'calories': 500, 'potassium': 50, 'sodium': 900, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 75}, # Keropok
    'dried mango': {'carbs': 80, 'fats': 0.5, 'protein': 2, 'calories': 320, 'potassium': 200, 'sodium': 50, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'kaya': {'carbs': 55, 'fats': 15, 'protein': 2, 'calories': 350, 'potassium': 100, 'sodium': 20, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 70}, # Coconut jam
    'cream crackers': {'carbs': 70, 'fats': 15, 'protein': 8, 'calories': 450, 'potassium': 100, 'sodium': 400, 'saturated_fat': 7, 'trans_fat': 0.5, 'gi': 70},
    'curry puff': {'carbs': 35, 'fats': 20, 'protein': 8, 'calories': 350, 'potassium': 150, 'sodium': 400, 'saturated_fat': 8, 'trans_fat': 0.1, 'gi': 65},
    'fish ball': {'carbs': 8, 'fats': 2, 'protein': 12, 'calories': 100, 'potassium': 100, 'sodium': 600, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 40},
    'otah': {'carbs': 10, 'fats': 15, 'protein': 15, 'calories': 230, 'potassium': 200, 'sodium': 500, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 60},
    'siew mai': {'carbs': 10, 'fats': 12, 'protein': 10, 'calories': 200, 'potassium': 150, 'sodium': 400, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 45},
    'har gow': {'carbs': 15, 'fats': 4, 'protein': 6, 'calories': 120, 'potassium': 80, 'sodium': 300, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 45},

    # More Drinks (Hot, Local, Alcohol)
    'green tea': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 0, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'black tea': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 0, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'latte': {'carbs': 10, 'fats': 5, 'protein': 8, 'calories': 120, 'potassium': 200, 'sodium': 100, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 30},
    'cappuccino': {'carbs': 8, 'fats': 4, 'protein': 6, 'calories': 100, 'potassium': 180, 'sodium': 80, 'saturated_fat': 2.5, 'trans_fat': 0, 'gi': 30},
    'bubble tea': {'carbs': 60, 'fats': 10, 'protein': 2, 'calories': 350, 'potassium': 50, 'sodium': 50, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 65}, # Milk tea with pearls
    'milk tea': {'carbs': 25, 'fats': 8, 'protein': 3, 'calories': 180, 'potassium': 100, 'sodium': 80, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 55},
    'teh tarik': {'carbs': 28, 'fats': 6, 'protein': 3, 'calories': 180, 'potassium': 150, 'sodium': 60, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 60},
    'soya bean milk': {'carbs': 15, 'fats': 4, 'protein': 7, 'calories': 130, 'potassium': 300, 'sodium': 40, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 40},
    'bandung': {'carbs': 35, 'fats': 6, 'protein': 4, 'calories': 210, 'potassium': 150, 'sodium': 50, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65}, # Rose syrup + milk
    'barley water': {'carbs': 25, 'fats': 0, 'protein': 1, 'calories': 110, 'potassium': 50, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 40},
    'coconut water': {'carbs': 9, 'fats': 0, 'protein': 0.7, 'calories': 40, 'potassium': 250, 'sodium': 105, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 55},
    'beer': {'carbs': 13, 'fats': 0, 'protein': 1.6, 'calories': 150, 'potassium': 96, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 100},
    'wine': {'carbs': 3.8, 'fats': 0, 'protein': 0.1, 'calories': 125, 'potassium': 100, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'diet coke': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'coke zero': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'water': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 0, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},

    # Canned / Preserved
    'corned beef': {'carbs': 0, 'fats': 15, 'protein': 25, 'calories': 250, 'potassium': 150, 'sodium': 1000, 'saturated_fat': 7, 'trans_fat': 0.5, 'gi': 0},
    'luncheon meat': {'carbs': 2, 'fats': 30, 'protein': 12, 'calories': 330, 'potassium': 100, 'sodium': 1200, 'saturated_fat': 11, 'trans_fat': 0, 'gi': 0},
    'spam': {'carbs': 2, 'fats': 30, 'protein': 12, 'calories': 330, 'potassium': 100, 'sodium': 1200, 'saturated_fat': 11, 'trans_fat': 0, 'gi': 0},
    'tuna': {'carbs': 0, 'fats': 1, 'protein': 25, 'calories': 110, 'potassium': 250, 'sodium': 300, 'saturated_fat': 0.2, 'trans_fat': 0, 'gi': 0}, # Canned in water
    'tuna in oil': {'carbs': 0, 'fats': 8, 'protein': 25, 'calories': 180, 'potassium': 250, 'sodium': 350, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 0},
    'sardines': {'carbs': 0, 'fats': 10, 'protein': 20, 'calories': 190, 'potassium': 300, 'sodium': 400, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 0}, # In oil/water generic
    'sardines tomato': {'carbs': 4, 'fats': 8, 'protein': 18, 'calories': 170, 'potassium': 350, 'sodium': 600, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 45}, # In tomato sauce
    'mackerel': {'carbs': 0, 'fats': 12, 'protein': 18, 'calories': 200, 'potassium': 300, 'sodium': 450, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 0},
    'vienna sausage': {'carbs': 2, 'fats': 20, 'protein': 10, 'calories': 230, 'potassium': 100, 'sodium': 900, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 0},
    'corned tuna': {'carbs': 5, 'fats': 5, 'protein': 15, 'calories': 130, 'potassium': 150, 'sodium': 550, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 0}, # Chili tuna etc

    # Instant / Processed
    'instant noodles': {'carbs': 60, 'fats': 15, 'protein': 8, 'calories': 400, 'potassium': 100, 'sodium': 1800, 'saturated_fat': 7, 'trans_fat': 0.2, 'gi': 60},
    'cup noodles': {'carbs': 45, 'fats': 12, 'protein': 7, 'calories': 300, 'potassium': 90, 'sodium': 1200, 'saturated_fat': 6, 'trans_fat': 0.2, 'gi': 60},
    'ramen packet': {'carbs': 65, 'fats': 20, 'protein': 9, 'calories': 480, 'potassium': 150, 'sodium': 1900, 'saturated_fat': 9, 'trans_fat': 0.5, 'gi': 60}, # High sodium warning
    'yakisoba': {'carbs': 70, 'fats': 20, 'protein': 10, 'calories': 500, 'potassium': 150, 'sodium': 1400, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 65},
    'mac and cheese': {'carbs': 50, 'fats': 15, 'protein': 12, 'calories': 400, 'potassium': 200, 'sodium': 800, 'saturated_fat': 6, 'trans_fat': 0.5, 'gi': 65}, # Instant box
    'frozen pizza': {'carbs': 30, 'fats': 12, 'protein': 12, 'calories': 280, 'potassium': 150, 'sodium': 600, 'saturated_fat': 5, 'trans_fat': 0.3, 'gi': 60}, # Per slice
    'fish finger': {'carbs': 20, 'fats': 12, 'protein': 12, 'calories': 240, 'potassium': 200, 'sodium': 400, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 60},
    'nuggets': {'carbs': 20, 'fats': 18, 'protein': 16, 'calories': 300, 'potassium': 250, 'sodium': 500, 'saturated_fat': 4, 'trans_fat': 0.1, 'gi': 60},
}

import difflib

def search_food_db(query):
    query = query.lower().strip()
    
    # 1. Direct match
    if query in FOOD_DB:
        return FOOD_DB[query]
        
    # 2. Singularize (simple)
    if query.endswith('s') and query[:-1] in FOOD_DB:
        return FOOD_DB[query[:-1]]
    
    # 3. Fuzzy match (catch typos like 'brocolli')
    matches = difflib.get_close_matches(query, FOOD_DB.keys(), n=1, cutoff=0.7)
    if matches:
        return FOOD_DB[matches[0]]
        
    # 4. Substring / Phrase Match (e.g. "lechon belly" -> "lechon")
    # We look for known food keys inside the query string (as whole words).
    # We prioritize the LONGEST key found (e.g. "fried chicken" over "chicken").
    import re
    best_match = None
    best_match_len = 0
    
    for key in FOOD_DB.keys():
        # Check if key exists in query as a whole word
        # escape key to handle special chars, though keys are usually simple
        if re.search(r'\b' + re.escape(key) + r'\b', query):
            if len(key) > best_match_len:
                best_match = key
                best_match_len = len(key)
                
    if best_match:
        return FOOD_DB[best_match]
        
    return None
