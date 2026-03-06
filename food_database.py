# Simulated "Online" Database
# Nutritional values per 100g (approximate)

FOOD_DB = {
    # Fruits & Vegetables
    'apple': {'carbs': 14, 'fats': 0.2, 'protein': 0.3, 'calories': 52, 'potassium': 107, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 36},
    'banana': {'carbs': 23, 'fats': 0.3, 'protein': 1.1, 'calories': 89, 'potassium': 358, 'sodium': 1, 'saturated_fat': 0.1, 'trans_fat': 0, 'gi': 51},
    'kiwi': {'carbs': 15, 'fats': 0.5, 'protein': 1.1, 'calories': 61, 'potassium': 312, 'sodium': 3, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 50},
    'pomegranate': {'carbs': 19, 'fats': 1.2, 'protein': 1.7, 'calories': 83, 'potassium': 236, 'sodium': 3, 'saturated_fat': 0.1, 'trans_fat': 0, 'gi': 53},
    'grapefruit': {'carbs': 11, 'fats': 0.1, 'protein': 0.8, 'calories': 42, 'potassium': 135, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 25},
    'papaya': {'carbs': 11, 'fats': 0.3, 'protein': 0.5, 'calories': 43, 'potassium': 182, 'sodium': 8, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 60},
    'peach': {'carbs': 10, 'fats': 0.3, 'protein': 0.9, 'calories': 39, 'potassium': 190, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 42},
    'cherry': {'carbs': 12, 'fats': 0.2, 'protein': 1, 'calories': 50, 'potassium': 173, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 22},
    'cherries': {'carbs': 12, 'fats': 0.2, 'protein': 1, 'calories': 50, 'potassium': 173, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 22},
    'strawberry': {'carbs': 8, 'fats': 0.3, 'protein': 0.7, 'calories': 32, 'potassium': 153, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 40},
    'strawberries': {'carbs': 8, 'fats': 0.3, 'protein': 0.7, 'calories': 32, 'potassium': 153, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 40},
    'blueberry': {'carbs': 14, 'fats': 0.3, 'protein': 0.7, 'calories': 57, 'potassium': 77, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 53},
    'blueberries': {'carbs': 14, 'fats': 0.3, 'protein': 0.7, 'calories': 57, 'potassium': 77, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 53},
    'eggplant': {'carbs': 6, 'fats': 0.2, 'protein': 1, 'calories': 25, 'potassium': 229, 'sodium': 2, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'spinach': {'carbs': 3.6, 'fats': 0.4, 'protein': 2.9, 'calories': 23, 'potassium': 558, 'sodium': 79, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'broccoli': {'carbs': 7, 'fats': 0.4, 'protein': 2.8, 'calories': 34, 'potassium': 316, 'sodium': 33, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'carrot': {'carbs': 10, 'fats': 0.2, 'protein': 0.9, 'calories': 41, 'potassium': 320, 'sodium': 69, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 39},
    'radish': {'carbs': 3.4, 'fats': 0.1, 'protein': 0.7, 'calories': 16, 'potassium': 233, 'sodium': 39, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'white radish': {'carbs': 4.1, 'fats': 0.1, 'protein': 0.6, 'calories': 18, 'potassium': 227, 'sodium': 21, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'white radish': {'carbs': 4.1, 'fats': 0.1, 'protein': 0.6, 'calories': 18, 'potassium': 227, 'sodium': 21, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'white raddish': {'carbs': 4.1, 'fats': 0.1, 'protein': 0.6, 'calories': 18, 'potassium': 227, 'sodium': 21, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15}, # Typo handling
    'daikon': {'carbs': 4.1, 'fats': 0.1, 'protein': 0.6, 'calories': 18, 'potassium': 227, 'gi': 15},
    'lettuce': {'carbs': 2.9, 'fats': 0.2, 'protein': 1.4, 'calories': 15, 'potassium': 194, 'gi': 15},
    'cucumber': {'carbs': 3.6, 'fats': 0.1, 'protein': 0.7, 'calories': 15, 'potassium': 147, 'gi': 15},
    'tomato': {'carbs': 3.9, 'fats': 0.2, 'protein': 0.9, 'calories': 18, 'potassium': 237, 'gi': 15},
    'potato': {'carbs': 17, 'fats': 0.1, 'protein': 2, 'calories': 77, 'potassium': 421, 'gi': 78},
    'garlic': {'carbs': 33, 'fats': 0.5, 'protein': 6.4, 'calories': 149, 'potassium': 401, 'gi': 10},
    'onion': {'carbs': 9, 'fats': 0.1, 'protein': 1.1, 'calories': 40, 'potassium': 146, 'gi': 10},
    'bell pepper': {'carbs': 6, 'fats': 0.3, 'protein': 1, 'calories': 25, 'potassium': 211, 'sodium': 4, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'red bell pepper': {'carbs': 6, 'fats': 0.3, 'protein': 1, 'calories': 25, 'potassium': 211, 'sodium': 4, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'green bell pepper': {'carbs': 4.6, 'fats': 0.2, 'protein': 0.9, 'calories': 20, 'potassium': 175, 'sodium': 3, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'yellow bell pepper': {'carbs': 6.3, 'fats': 0.2, 'protein': 1, 'calories': 27, 'potassium': 212, 'sodium': 2, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'zucchini': {'carbs': 3.1, 'fats': 0.3, 'protein': 1.2, 'calories': 17, 'potassium': 261, 'sodium': 8, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'asparagus': {'carbs': 3.9, 'fats': 0.1, 'protein': 2.2, 'calories': 20, 'potassium': 202, 'sodium': 2, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'celery': {'carbs': 3, 'fats': 0.2, 'protein': 0.7, 'calories': 14, 'potassium': 260, 'sodium': 80, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    'mushroom': {'carbs': 3.3, 'fats': 0.3, 'protein': 3.1, 'calories': 22, 'potassium': 318, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15}, # Generic white button
    'mushrooms': {'carbs': 3.3, 'fats': 0.3, 'protein': 3.1, 'calories': 22, 'potassium': 318, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 15},
    
    # Seeds & Legumes
    'chia seeds': {'carbs': 42, 'fats': 31, 'protein': 17, 'calories': 486, 'potassium': 407, 'sodium': 16, 'saturated_fat': 3.3, 'trans_fat': 0, 'gi': 1},
    'flaxseed': {'carbs': 29, 'fats': 42, 'protein': 18, 'calories': 534, 'potassium': 813, 'sodium': 30, 'saturated_fat': 3.7, 'trans_fat': 0, 'gi': 32},
    'pumpkin seeds': {'carbs': 15, 'fats': 49, 'protein': 30, 'calories': 574, 'potassium': 809, 'sodium': 7, 'saturated_fat': 8.5, 'trans_fat': 0, 'gi': 15},
    'sunflower seeds': {'carbs': 20, 'fats': 51, 'protein': 21, 'calories': 584, 'potassium': 645, 'sodium': 9, 'saturated_fat': 4.5, 'trans_fat': 0, 'gi': 20},
    'sesame seeds': {'carbs': 23, 'fats': 50, 'protein': 18, 'calories': 573, 'potassium': 468, 'sodium': 11, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 35},
    'chickpeas': {'carbs': 61, 'fats': 6, 'protein': 19, 'calories': 364, 'potassium': 875, 'sodium': 24, 'saturated_fat': 0.6, 'trans_fat': 0, 'gi': 28},
    'black beans': {'carbs': 62, 'fats': 1.4, 'protein': 21, 'calories': 341, 'potassium': 1483, 'sodium': 5, 'saturated_fat': 0.4, 'trans_fat': 0, 'gi': 30},
    'kidney beans': {'carbs': 60, 'fats': 0.8, 'protein': 24, 'calories': 333, 'potassium': 1406, 'sodium': 24, 'saturated_fat': 0.1, 'trans_fat': 0, 'gi': 29},
    'lentils': {'carbs': 60, 'fats': 1.1, 'protein': 26, 'calories': 353, 'potassium': 955, 'sodium': 6, 'saturated_fat': 0.2, 'trans_fat': 0, 'gi': 32},
    'edamame': {'carbs': 9, 'fats': 5, 'protein': 11, 'calories': 122, 'potassium': 436, 'sodium': 6, 'saturated_fat': 0.6, 'trans_fat': 0, 'gi': 20},

    # Grains & Meats
    'white rice': {'carbs': 28, 'fats': 0.3, 'protein': 2.7, 'calories': 130, 'potassium': 35, 'gi': 73},
    'brown rice': {'carbs': 23, 'fats': 0.9, 'protein': 2.6, 'calories': 111, 'potassium': 43, 'gi': 68},
    'pearl barley': {'carbs': 28, 'fats': 0.4, 'protein': 2.3, 'calories': 123, 'potassium': 93, 'gi': 28},
    'barley': {'carbs': 28, 'fats': 0.4, 'protein': 2.3, 'calories': 123, 'potassium': 93, 'gi': 28},
    'quinoa': {'carbs': 21, 'fats': 1.9, 'protein': 4.4, 'calories': 120, 'potassium': 172, 'gi': 53},
    'couscous': {'carbs': 23, 'fats': 0.2, 'protein': 3.8, 'calories': 112, 'potassium': 58, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'oats': {'carbs': 66, 'fats': 6.9, 'protein': 16.9, 'calories': 389, 'potassium': 429, 'sodium': 2, 'saturated_fat': 1.2, 'trans_fat': 0, 'gi': 55},
    'rolled oats': {'carbs': 68, 'fats': 6.5, 'protein': 13, 'calories': 379, 'potassium': 362, 'sodium': 2, 'saturated_fat': 1.2, 'trans_fat': 0, 'gi': 55},
    'steel cut oats': {'carbs': 68, 'fats': 7, 'protein': 14, 'calories': 375, 'potassium': 362, 'sodium': 2, 'saturated_fat': 1.2, 'trans_fat': 0, 'gi': 42},
    'millet': {'carbs': 73, 'fats': 4.2, 'protein': 11, 'calories': 378, 'potassium': 195, 'sodium': 5, 'saturated_fat': 0.7, 'trans_fat': 0, 'gi': 71},
    'amaranth': {'carbs': 65, 'fats': 7, 'protein': 14, 'calories': 371, 'potassium': 508, 'sodium': 4, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 97},
    'bulgur': {'carbs': 76, 'fats': 1.3, 'protein': 12, 'calories': 342, 'potassium': 410, 'sodium': 17, 'saturated_fat': 0.2, 'trans_fat': 0, 'gi': 46},
    'buckwheat': {'carbs': 71, 'fats': 3.4, 'protein': 13, 'calories': 343, 'potassium': 460, 'sodium': 1, 'saturated_fat': 0.7, 'trans_fat': 0, 'gi': 45},
    'farro': {'carbs': 71, 'fats': 2, 'protein': 15, 'calories': 337, 'potassium': 300, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 45},
    'jasmine rice': {'carbs': 28, 'fats': 0.2, 'protein': 2.7, 'calories': 130, 'potassium': 29, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 89},
    'basmati rice': {'carbs': 25, 'fats': 0.4, 'protein': 3.5, 'calories': 121, 'potassium': 32, 'sodium': 1, 'saturated_fat': 0.1, 'trans_fat': 0, 'gi': 52},
    'black rice': {'carbs': 74, 'fats': 3.3, 'protein': 8.9, 'calories': 356, 'potassium': 245, 'sodium': 0, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 45},
    'wild rice': {'carbs': 21, 'fats': 0.3, 'protein': 4, 'calories': 101, 'potassium': 137, 'sodium': 3, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 35},

    'chicken': {'carbs': 0, 'fats': 3.6, 'protein': 31, 'calories': 165, 'potassium': 256, 'gi': 0},
    'chicken breast': {'carbs': 0, 'fats': 3.6, 'protein': 31, 'calories': 165, 'potassium': 256, 'gi': 0},
    'chicken thigh': {'carbs': 0, 'fats': 10.9, 'protein': 26, 'calories': 209, 'potassium': 239, 'gi': 0},
    'chicken wing': {'carbs': 0, 'fats': 8.1, 'protein': 30, 'calories': 203, 'potassium': 189, 'gi': 0},
    'chicken leg': {'carbs': 0, 'fats': 5.7, 'protein': 28, 'calories': 172, 'potassium': 240, 'gi': 0},
    'drumstick': {'carbs': 0, 'fats': 5.7, 'protein': 28, 'calories': 172, 'potassium': 240, 'gi': 0},
    'pork': {'carbs': 0, 'fats': 14, 'protein': 27, 'calories': 242, 'potassium': 423, 'gi': 0},
    'pork tenderloin': {'carbs': 0, 'fats': 3.5, 'protein': 26, 'calories': 143, 'potassium': 421, 'gi': 0},
    'pork chop': {'carbs': 0, 'fats': 14, 'protein': 24, 'calories': 231, 'potassium': 350, 'gi': 0},
    'ground pork': {'carbs': 0, 'fats': 20, 'protein': 25, 'calories': 297, 'potassium': 286, 'gi': 0},
    'pork belly': {'carbs': 0, 'fats': 53, 'protein': 9, 'calories': 518, 'potassium': 250, 'gi': 0},
    'liempo': {'carbs': 0, 'fats': 53, 'protein': 9, 'calories': 518, 'potassium': 250, 'gi': 0},
    'beef': {'carbs': 0, 'fats': 15, 'protein': 26, 'calories': 250, 'potassium': 318, 'gi': 0},
    'beef sirloin': {'carbs': 0, 'fats': 13, 'protein': 29, 'calories': 244, 'potassium': 346, 'gi': 0},
    'beef steak': {'carbs': 0, 'fats': 13, 'protein': 29, 'calories': 244, 'potassium': 346, 'gi': 0},
    'beef brisket': {'carbs': 0, 'fats': 26, 'protein': 25, 'calories': 342, 'potassium': 313, 'gi': 0},
    'ground beef': {'carbs': 0, 'fats': 20, 'protein': 17, 'calories': 254, 'potassium': 282, 'gi': 0},
    'fish': {'carbs': 0, 'fats': 12, 'protein': 20, 'calories': 206, 'potassium': 384, 'gi': 0},
    'salmon': {'carbs': 0, 'fats': 13, 'protein': 20, 'calories': 208, 'potassium': 363, 'gi': 0},
    
    # Filipino / Asian Common
    'lechon': {'carbs': 0, 'fats': 25, 'protein': 27, 'calories': 350, 'potassium': 300, 'sodium': 510, 'saturated_fat': 11, 'trans_fat': 0, 'gi': 0},
    'lechon belly': {'carbs': 0, 'fats': 28, 'protein': 25, 'calories': 380, 'potassium': 280, 'sodium': 540, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 0},
    'adobo': {'carbs': 2, 'fats': 18, 'protein': 25, 'calories': 280, 'potassium': 250, 'sodium': 850, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 0},
    'sinigang': {'carbs': 5, 'fats': 8, 'protein': 15, 'calories': 150, 'potassium': 200, 'sodium': 600, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 0},
    'sisig': {'carbs': 2, 'fats': 30, 'protein': 20, 'calories': 380, 'potassium': 280, 'sodium': 550, 'saturated_fat': 9, 'trans_fat': 0.5, 'gi': 0},
    'pancit': {'carbs': 35, 'fats': 8, 'protein': 10, 'calories': 250, 'potassium': 100, 'sodium': 700, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 45},
    
    # Common Snacks/Others
    'bread': {'carbs': 49, 'fats': 3.2, 'protein': 9, 'calories': 265, 'potassium': 115, 'gi': 75},
    'white bread': {'carbs': 49, 'fats': 3.2, 'protein': 9, 'calories': 265, 'potassium': 115, 'gi': 75},
    'whole wheat bread': {'carbs': 41, 'fats': 3.5, 'protein': 13, 'calories': 247, 'potassium': 250, 'gi': 74},
    'low gi bread': {'carbs': 40, 'fats': 4, 'protein': 12, 'calories': 240, 'potassium': 200, 'gi': 53},
    'multigrain bread': {'carbs': 43, 'fats': 4.2, 'protein': 13, 'calories': 265, 'potassium': 220, 'gi': 45},
    
    'milk': {'carbs': 5, 'fats': 3.2, 'protein': 3.4, 'calories': 60, 'potassium': 150, 'sodium': 44, 'saturated_fat': 1.9, 'trans_fat': 0.1, 'gi': 31},
    'cheddar cheese': {'carbs': 1.3, 'fats': 33, 'protein': 25, 'calories': 403, 'potassium': 98, 'sodium': 621, 'saturated_fat': 21, 'trans_fat': 1, 'gi': 0},
    'mozzarella': {'carbs': 2.2, 'fats': 22, 'protein': 22, 'calories': 300, 'potassium': 76, 'sodium': 627, 'saturated_fat': 14, 'trans_fat': 1, 'gi': 0},
    'parmesan': {'carbs': 4.1, 'fats': 29, 'protein': 38, 'calories': 431, 'potassium': 125, 'sodium': 1529, 'saturated_fat': 17, 'trans_fat': 1, 'gi': 0},
    'cream cheese': {'carbs': 5.5, 'fats': 34, 'protein': 6, 'calories': 342, 'potassium': 138, 'sodium': 321, 'saturated_fat': 19, 'trans_fat': 1, 'gi': 0},
    'butter': {'carbs': 0.1, 'fats': 81, 'protein': 0.9, 'calories': 717, 'potassium': 24, 'sodium': 643, 'saturated_fat': 51, 'trans_fat': 3, 'gi': 0},
    'coffee': {'carbs': 0, 'fats': 0, 'protein': 0.1, 'calories': 1, 'potassium': 49, 'sodium': 2, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    
    # Condiments / Cooking
    'salt': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 8, 'sodium': 38758, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'sugar': {'carbs': 100, 'fats': 0, 'protein': 0, 'calories': 387, 'potassium': 2, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'oil': {'carbs': 0, 'fats': 100, 'protein': 0, 'calories': 884, 'potassium': 0, 'sodium': 0, 'saturated_fat': 13, 'trans_fat': 0, 'gi': 0}, # Generic vegetable oil
    'olive oil': {'carbs': 0, 'fats': 100, 'protein': 0, 'calories': 884, 'potassium': 0, 'sodium': 0, 'saturated_fat': 14, 'trans_fat': 0, 'gi': 0},
    'soy sauce': {'carbs': 5, 'fats': 0.1, 'protein': 8, 'calories': 53, 'potassium': 200, 'sodium': 5493, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'mayonnaise': {'carbs': 0.6, 'fats': 75, 'protein': 1, 'calories': 680, 'potassium': 20, 'sodium': 635, 'saturated_fat': 12, 'trans_fat': 0.2, 'gi': 0},
    'ketchup': {'carbs': 27, 'fats': 0.2, 'protein': 1.1, 'calories': 112, 'potassium': 315, 'sodium': 907, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 55},
    'mustard': {'carbs': 5, 'fats': 3.3, 'protein': 4.4, 'calories': 60, 'potassium': 138, 'sodium': 1136, 'saturated_fat': 0.2, 'trans_fat': 0, 'gi': 5},
    'ranch dressing': {'carbs': 6, 'fats': 45, 'protein': 1.5, 'calories': 430, 'potassium': 100, 'sodium': 900, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 15},
    
    # Fast Food / Western
    'burger': {'carbs': 30, 'fats': 14, 'protein': 16, 'calories': 295, 'potassium': 250, 'sodium': 450, 'saturated_fat': 5, 'trans_fat': 0.5, 'gi': 66},
    'cheeseburger': {'carbs': 30, 'fats': 16, 'protein': 18, 'calories': 320, 'potassium': 280, 'sodium': 550, 'saturated_fat': 7, 'trans_fat': 0.5, 'gi': 66},
    'fries': {'carbs': 41, 'fats': 15, 'protein': 3.4, 'calories': 312, 'potassium': 579, 'sodium': 210, 'saturated_fat': 2.3, 'trans_fat': 0.1, 'gi': 75},
    'french fries': {'carbs': 41, 'fats': 15, 'protein': 3.4, 'calories': 312, 'potassium': 579, 'sodium': 210, 'saturated_fat': 2.3, 'trans_fat': 0.1, 'gi': 75},
    'pizza': {'carbs': 33, 'fats': 10, 'protein': 11, 'calories': 266, 'potassium': 170, 'sodium': 600, 'saturated_fat': 4.5, 'trans_fat': 0.2, 'gi': 60}, # per slice (approx 100g)
    'hotdog': {'carbs': 2, 'fats': 25, 'protein': 10, 'calories': 290, 'potassium': 150, 'sodium': 1000, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},
    'fried chicken': {'carbs': 10, 'fats': 15, 'protein': 25, 'calories': 280, 'potassium': 220, 'sodium': 600, 'saturated_fat': 4, 'trans_fat': 0.2, 'gi': 0},
    
    # Fast Food / Branded
    'mcdonalds burger': {'carbs': 33, 'fats': 9, 'protein': 12, 'calories': 250, 'potassium': 200, 'sodium': 480, 'saturated_fat': 3.5, 'trans_fat': 0.5, 'gi': 66},
    'mcdonalds cheeseburger': {'carbs': 33, 'fats': 12, 'protein': 15, 'calories': 300, 'potassium': 220, 'sodium': 680, 'saturated_fat': 5, 'trans_fat': 0.5, 'gi': 66},
    'mcdonalds fries': {'carbs': 43, 'fats': 15, 'protein': 4, 'calories': 320, 'potassium': 600, 'sodium': 260, 'saturated_fat': 2.5, 'trans_fat': 0, 'gi': 75},
    'big mac': {'carbs': 45, 'fats': 30, 'protein': 25, 'calories': 550, 'potassium': 400, 'sodium': 1010, 'saturated_fat': 10, 'trans_fat': 1, 'gi': 66},
    'mcchicken': {'carbs': 39, 'fats': 21, 'protein': 14, 'calories': 400, 'potassium': 250, 'sodium': 560, 'saturated_fat': 3.5, 'trans_fat': 0, 'gi': 66},
    'mcnuggets': {'carbs': 16, 'fats': 16, 'protein': 15, 'calories': 280, 'potassium': 300, 'sodium': 500, 'saturated_fat': 2.5, 'trans_fat': 0, 'gi': 60},
    'mcdonalds mcspicy': {'carbs': 45, 'fats': 28, 'protein': 25, 'calories': 530, 'potassium': 350, 'sodium': 1200, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65},
    'mcspicy': {'carbs': 45, 'fats': 28, 'protein': 25, 'calories': 530, 'potassium': 350, 'sodium': 1200, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65},
    'mcdonalds buttermilk crispy chicken': {'carbs': 55, 'fats': 30, 'protein': 28, 'calories': 600, 'potassium': 400, 'sodium': 1300, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 65},
    'mcdonalds double mcspicy': {'carbs': 55, 'fats': 48, 'protein': 45, 'calories': 850, 'potassium': 500, 'sodium': 1900, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 65},
    
    'jollibee yum burger': {'carbs': 35, 'fats': 12, 'protein': 11, 'calories': 280, 'potassium': 150, 'sodium': 500, 'saturated_fat': 5, 'trans_fat': 0.5, 'gi': 66},
    'jollibee chickenjoy': {'carbs': 15, 'fats': 22, 'protein': 25, 'calories': 350, 'potassium': 250, 'sodium': 850, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 0},
    'jollibee spaghetti': {'carbs': 55, 'fats': 10, 'protein': 15, 'calories': 360, 'potassium': 300, 'sodium': 850, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 55},
    'jollibee burger steak': {'carbs': 30, 'fats': 18, 'protein': 14, 'calories': 320, 'potassium': 200, 'sodium': 750, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 65},
    'jollibee fries': {'carbs': 45, 'fats': 16, 'protein': 4, 'calories': 340, 'potassium': 650, 'sodium': 300, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 75},

    'carls jr burger': {'carbs': 42, 'fats': 18, 'protein': 22, 'calories': 420, 'potassium': 300, 'sodium': 850, 'saturated_fat': 7, 'trans_fat': 1, 'gi': 66},
    'famous star': {'carbs': 53, 'fats': 37, 'protein': 28, 'calories': 670, 'potassium': 450, 'sodium': 1210, 'saturated_fat': 13, 'trans_fat': 1.5, 'gi': 66},
    
    'burger king whopper': {'carbs': 49, 'fats': 40, 'protein': 28, 'calories': 660, 'potassium': 400, 'sodium': 980, 'saturated_fat': 12, 'trans_fat': 1, 'gi': 66},
    'burger king burger': {'carbs': 30, 'fats': 14, 'protein': 16, 'calories': 295, 'potassium': 250, 'sodium': 450, 'saturated_fat': 5, 'trans_fat': 0.5, 'gi': 66},
    'burger king chicken sandwich': {'carbs': 40, 'fats': 25, 'protein': 18, 'calories': 430, 'potassium': 300, 'sodium': 1000, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 66},
    'burger king fries': {'carbs': 52, 'fats': 17, 'protein': 5, 'calories': 380, 'potassium': 600, 'sodium': 570, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 75},
    
    'wendys burger': {'carbs': 48, 'fats': 36, 'protein': 30, 'calories': 650, 'potassium': 400, 'sodium': 1350, 'saturated_fat': 14, 'trans_fat': 1.5, 'gi': 66},
    'wendys chicken sandwich': {'carbs': 46, 'fats': 25, 'protein': 22, 'calories': 500, 'potassium': 350, 'sodium': 1140, 'saturated_fat': 4.5, 'trans_fat': 0, 'gi': 66},
    'carls jr chicken sandwich': {'carbs': 45, 'fats': 20, 'protein': 25, 'calories': 470, 'potassium': 350, 'sodium': 1100, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 66},
    
    'kfc original recipe chicken': {'carbs': 11, 'fats': 21, 'protein': 18, 'calories': 320, 'potassium': 250, 'sodium': 970, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 50},
    'kfc chicken': {'carbs': 11, 'fats': 21, 'protein': 18, 'calories': 320, 'potassium': 250, 'sodium': 970, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 50},
    'kfc fries': {'carbs': 39, 'fats': 15, 'protein': 4, 'calories': 300, 'potassium': 550, 'sodium': 600, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 75},
    'kfc zinger': {'carbs': 42, 'fats': 25, 'protein': 25, 'calories': 500, 'potassium': 300, 'sodium': 1050, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65},
    'zinger': {'carbs': 42, 'fats': 25, 'protein': 25, 'calories': 500, 'potassium': 300, 'sodium': 1050, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65},
    'kfc cheese fries': {'carbs': 45, 'fats': 25, 'protein': 8, 'calories': 450, 'potassium': 400, 'sodium': 1200, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 70},

    'subway chicken breast': {'carbs': 40, 'fats': 5, 'protein': 23, 'calories': 300, 'potassium': 350, 'sodium': 650, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 50},
    'subway roasted chicken': {'carbs': 40, 'fats': 5, 'protein': 23, 'calories': 300, 'potassium': 350, 'sodium': 650, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 50},
    'subway chicken teriyaki': {'carbs': 48, 'fats': 4, 'protein': 24, 'calories': 340, 'potassium': 300, 'sodium': 750, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 55},
    'subway meatball marinara': {'carbs': 45, 'fats': 18, 'protein': 21, 'calories': 430, 'potassium': 400, 'sodium': 1000, 'saturated_fat': 7, 'trans_fat': 0.5, 'gi': 55},
    'subway italian bmt': {'carbs': 40, 'fats': 16, 'protein': 20, 'calories': 410, 'potassium': 300, 'sodium': 1200, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 55},
    'subway bmt': {'carbs': 40, 'fats': 16, 'protein': 20, 'calories': 410, 'potassium': 300, 'sodium': 1200, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 55},
    'subway tuna': {'carbs': 38, 'fats': 20, 'protein': 18, 'calories': 410, 'potassium': 200, 'sodium': 600, 'saturated_fat': 3.5, 'trans_fat': 0, 'gi': 50},
    'subway steak and cheese': {'carbs': 40, 'fats': 10, 'protein': 26, 'calories': 340, 'potassium': 350, 'sodium': 1050, 'saturated_fat': 4.5, 'trans_fat': 0, 'gi': 55},
    'subway veggie delite': {'carbs': 39, 'fats': 2.5, 'protein': 9, 'calories': 200, 'potassium': 250, 'sodium': 280, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 45},
    'subway club': {'carbs': 41, 'fats': 8, 'protein': 24, 'calories': 330, 'potassium': 350, 'sodium': 850, 'saturated_fat': 2.5, 'trans_fat': 0, 'gi': 50},

    
    # Singapore Local Fast Food / Chains
    'ya kun kaya toast': {'carbs': 45, 'fats': 15, 'protein': 5, 'calories': 350, 'potassium': 100, 'sodium': 200, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 70},
    'ya kun soft boiled eggs': {'carbs': 1, 'fats': 10, 'protein': 12, 'calories': 140, 'potassium': 120, 'sodium': 180, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 0},
    'toast box kaya toast': {'carbs': 48, 'fats': 18, 'protein': 4, 'calories': 380, 'potassium': 110, 'sodium': 250, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 70},
    'old chang kee curry o': {'carbs': 35, 'fats': 20, 'protein': 8, 'calories': 350, 'potassium': 150, 'sodium': 450, 'saturated_fat': 8, 'trans_fat': 0.1, 'gi': 65},
    'old chang kee sotong head': {'carbs': 15, 'fats': 12, 'protein': 15, 'calories': 230, 'potassium': 200, 'sodium': 600, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 55},
    'old chang kee chicken wing': {'carbs': 10, 'fats': 15, 'protein': 18, 'calories': 250, 'potassium': 180, 'sodium': 550, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 0},
    'mos burger yakiniku rice burger': {'carbs': 45, 'fats': 12, 'protein': 15, 'calories': 350, 'potassium': 250, 'sodium': 750, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 70},
    'mos burger teriyaki chicken burger': {'carbs': 40, 'fats': 15, 'protein': 20, 'calories': 380, 'potassium': 300, 'sodium': 850, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 65},
    'texas chicken regular': {'carbs': 12, 'fats': 22, 'protein': 25, 'calories': 340, 'potassium': 260, 'sodium': 800, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 50},
    'texas chicken honey butter biscuit': {'carbs': 25, 'fats': 12, 'protein': 4, 'calories': 220, 'potassium': 100, 'sodium': 350, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 70},
    'four fingers soy garlic chicken wing': {'carbs': 8, 'fats': 10, 'protein': 12, 'calories': 170, 'potassium': 150, 'sodium': 400, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 55},
    'crave nasi lemak with chicken wing': {'carbs': 75, 'fats': 35, 'protein': 25, 'calories': 720, 'potassium': 450, 'sodium': 1200, 'saturated_fat': 18, 'trans_fat': 0, 'gi': 80},
    'stuffd chicken kebab': {'carbs': 45, 'fats': 15, 'protein': 28, 'calories': 430, 'potassium': 500, 'sodium': 950, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 55},
    'stuffd beef daily bowl': {'carbs': 35, 'fats': 20, 'protein': 30, 'calories': 450, 'potassium': 600, 'sodium': 1100, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 50},
    
    # Singapore Chinese Food / Zi Char / Famous Dishes
    'chicken rice': {'carbs': 65, 'fats': 25, 'protein': 25, 'calories': 600, 'potassium': 200, 'sodium': 800, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 65},
    'hainanese chicken rice': {'carbs': 65, 'fats': 25, 'protein': 25, 'calories': 600, 'potassium': 200, 'sodium': 800, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 65},
    'roasted chicken rice': {'carbs': 65, 'fats': 27, 'protein': 26, 'calories': 620, 'potassium': 210, 'sodium': 850, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 65},
    'char siew rice': {'carbs': 80, 'fats': 25, 'protein': 22, 'calories': 650, 'potassium': 150, 'sodium': 900, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 70},
    'roast pork rice': {'carbs': 70, 'fats': 33, 'protein': 24, 'calories': 680, 'potassium': 180, 'sodium': 950, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 68},
    'siew yoke rice': {'carbs': 70, 'fats': 33, 'protein': 24, 'calories': 680, 'potassium': 180, 'sodium': 950, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 68},
    'duck rice': {'carbs': 65, 'fats': 30, 'protein': 22, 'calories': 640, 'potassium': 190, 'sodium': 880, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 65},
    'wanton mee': {'carbs': 55, 'fats': 14, 'protein': 15, 'calories': 410, 'potassium': 150, 'sodium': 1200, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 55},
    'hokkien mee': {'carbs': 50, 'fats': 25, 'protein': 20, 'calories': 520, 'potassium': 200, 'sodium': 1100, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 60},
    'char kway teow': {'carbs': 75, 'fats': 38, 'protein': 22, 'calories': 740, 'potassium': 250, 'sodium': 1400, 'saturated_fat': 15, 'trans_fat': 0, 'gi': 70},
    'laksa': {'carbs': 60, 'fats': 30, 'protein': 25, 'calories': 600, 'potassium': 300, 'sodium': 1500, 'saturated_fat': 20, 'trans_fat': 0, 'gi': 55},
    'bak chor mee': {'carbs': 55, 'fats': 20, 'protein': 25, 'calories': 500, 'potassium': 180, 'sodium': 1300, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 55},
    'yong tau foo': {'carbs': 20, 'fats': 10, 'protein': 15, 'calories': 250, 'potassium': 300, 'sodium': 800, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 45},
    'sweet and sour pork rice': {'carbs': 80, 'fats': 25, 'protein': 18, 'calories': 650, 'potassium': 250, 'sodium': 800, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65},
    'hor fun': {'carbs': 65, 'fats': 20, 'protein': 25, 'calories': 600, 'potassium': 250, 'sodium': 1200, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 60},
    'beef hor fun': {'carbs': 65, 'fats': 20, 'protein': 25, 'calories': 600, 'potassium': 250, 'sodium': 1200, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 60},
    
    # Din Tai Fung
    'xiao long bao': {'carbs': 20, 'fats': 15, 'protein': 10, 'calories': 250, 'potassium': 150, 'sodium': 450, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 50},
    'dtf xiao long bao': {'carbs': 20, 'fats': 15, 'protein': 10, 'calories': 250, 'potassium': 150, 'sodium': 450, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 50},
    'pork chop fried rice': {'carbs': 75, 'fats': 35, 'protein': 30, 'calories': 750, 'potassium': 300, 'sodium': 1100, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 65},
    'dtf pork chop fried rice': {'carbs': 75, 'fats': 35, 'protein': 30, 'calories': 750, 'potassium': 300, 'sodium': 1100, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 65},

    # Seafood / Shellfish / Zi Char
    'chili crab': {'carbs': 30, 'fats': 15, 'protein': 40, 'calories': 450, 'potassium': 400, 'sodium': 1500, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 55},
    'black pepper crab': {'carbs': 20, 'fats': 15, 'protein': 40, 'calories': 400, 'potassium': 400, 'sodium': 1300, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 45},
    'fried mantou': {'carbs': 20, 'fats': 3, 'protein': 3, 'calories': 120, 'potassium': 50, 'sodium': 100, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 70},
    'cereal prawn': {'carbs': 30, 'fats': 15, 'protein': 25, 'calories': 350, 'potassium': 250, 'sodium': 800, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 60},
    'salted egg yolk chicken': {'carbs': 40, 'fats': 30, 'protein': 30, 'calories': 550, 'potassium': 300, 'sodium': 900, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 55},

    # Filipino Restaurant Chains
    'mang inasal pm1': {'carbs': 85, 'fats': 30, 'protein': 35, 'calories': 750, 'potassium': 300, 'sodium': 1200, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 70},
    'mang inasal pm2': {'carbs': 85, 'fats': 35, 'protein': 40, 'calories': 800, 'potassium': 350, 'sodium': 1300, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 70},
    'mang inasal pork bbq': {'carbs': 80, 'fats': 25, 'protein': 25, 'calories': 650, 'potassium': 250, 'sodium': 1100, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 70},
    'mang inasal unli rice': {'carbs': 45, 'fats': 1, 'protein': 4, 'calories': 220, 'potassium': 30, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 73},
    'mang inasal halo-halo': {'carbs': 80, 'fats': 12, 'protein': 8, 'calories': 450, 'potassium': 250, 'sodium': 150, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 70},
    
    'chowking chao fan': {'carbs': 70, 'fats': 20, 'protein': 15, 'calories': 550, 'potassium': 150, 'sodium': 850, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'chowking beef chao fan': {'carbs': 70, 'fats': 25, 'protein': 20, 'calories': 600, 'potassium': 200, 'sodium': 950, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 65},
    'chowking lauriat': {'carbs': 110, 'fats': 40, 'protein': 35, 'calories': 950, 'potassium': 350, 'sodium': 1800, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 65},
    'chowking siomai mami': {'carbs': 50, 'fats': 15, 'protein': 18, 'calories': 450, 'potassium': 200, 'sodium': 1200, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 60},
    'chowking halo-halo': {'carbs': 85, 'fats': 15, 'protein': 8, 'calories': 500, 'potassium': 250, 'sodium': 160, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 70},

    'maxs fried chicken': {'carbs': 20, 'fats': 55, 'protein': 65, 'calories': 850, 'potassium': 500, 'sodium': 1600, 'saturated_fat': 14, 'trans_fat': 0, 'gi': 0},
    "max's fried chicken": {'carbs': 20, 'fats': 55, 'protein': 65, 'calories': 850, 'potassium': 500, 'sodium': 1600, 'saturated_fat': 14, 'trans_fat': 0, 'gi': 0},
    'maxs regular meal': {'carbs': 65, 'fats': 25, 'protein': 35, 'calories': 650, 'potassium': 400, 'sodium': 1200, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 60},
    'maxs pancit canton': {'carbs': 55, 'fats': 15, 'protein': 12, 'calories': 400, 'potassium': 180, 'sodium': 900, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 55},
    'maxs kare-kare': {'carbs': 20, 'fats': 45, 'protein': 35, 'calories': 600, 'potassium': 450, 'sodium': 850, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 35},

    'gerrys grill sisig': {'carbs': 15, 'fats': 60, 'protein': 35, 'calories': 750, 'potassium': 350, 'sodium': 1400, 'saturated_fat': 20, 'trans_fat': 0.5, 'gi': 0},
    "gerry's grill sisig": {'carbs': 15, 'fats': 60, 'protein': 35, 'calories': 750, 'potassium': 350, 'sodium': 1400, 'saturated_fat': 20, 'trans_fat': 0.5, 'gi': 0},
    'gerrys grill inihaw na pusit': {'carbs': 10, 'fats': 8, 'protein': 55, 'calories': 350, 'potassium': 400, 'sodium': 800, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 0},
    
    'kuya j crispy pata': {'carbs': 5, 'fats': 75, 'protein': 55, 'calories': 900, 'potassium': 400, 'sodium': 1800, 'saturated_fat': 25, 'trans_fat': 0, 'gi': 0},
    'kuya j halo-halo': {'carbs': 75, 'fats': 15, 'protein': 6, 'calories': 450, 'potassium': 250, 'sodium': 150, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 70},

    'greenwich hawaiian overload': {'carbs': 30, 'fats': 12, 'protein': 12, 'calories': 280, 'potassium': 150, 'sodium': 650, 'saturated_fat': 5, 'trans_fat': 0.1, 'gi': 60},
    'greenwich lasagna supreme': {'carbs': 50, 'fats': 20, 'protein': 18, 'calories': 450, 'potassium': 300, 'sodium': 900, 'saturated_fat': 8, 'trans_fat': 0.2, 'gi': 55},

    'goldilocks mamon': {'carbs': 35, 'fats': 10, 'protein': 5, 'calories': 250, 'potassium': 80, 'sodium': 200, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
    'goldilocks ensaymada': {'carbs': 40, 'fats': 15, 'protein': 6, 'calories': 320, 'potassium': 100, 'sodium': 350, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 65},
    'red ribbon empanada': {'carbs': 35, 'fats': 14, 'protein': 10, 'calories': 300, 'potassium': 150, 'sodium': 450, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 55},

    # Japanese Restaurant Chains / Fast Food
    'yoshinoya beef bowl': {'carbs': 65, 'fats': 22, 'protein': 20, 'calories': 550, 'potassium': 450, 'sodium': 1800, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 70},
    'sukiya beef bowl': {'carbs': 65, 'fats': 23, 'protein': 21, 'calories': 560, 'potassium': 460, 'sodium': 1850, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 70},
    
    'tokyo tokyo beef misono': {'carbs': 75, 'fats': 25, 'protein': 25, 'calories': 650, 'potassium': 350, 'sodium': 1400, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 65},
    'tokyo tokyo pork tonkatsu': {'carbs': 70, 'fats': 35, 'protein': 22, 'calories': 750, 'potassium': 300, 'sodium': 1000, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 65},
    'tokyo tokyo chicken teriyaki': {'carbs': 75, 'fats': 18, 'protein': 24, 'calories': 600, 'potassium': 320, 'sodium': 1200, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'tokyo tokyo red iced tea': {'carbs': 38, 'fats': 0, 'protein': 0, 'calories': 150, 'potassium': 10, 'sodium': 20, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'bento box': {'carbs': 80, 'fats': 30, 'protein': 25, 'calories': 700, 'potassium': 300, 'sodium': 1200, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 65},
    
    'marugame udon kake': {'carbs': 60, 'fats': 2, 'protein': 10, 'calories': 300, 'potassium': 150, 'sodium': 1100, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 60},
    'marugame udon niku': {'carbs': 60, 'fats': 15, 'protein': 20, 'calories': 450, 'potassium': 250, 'sodium': 1500, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 60},
    'marugame udon curry': {'carbs': 70, 'fats': 18, 'protein': 15, 'calories': 550, 'potassium': 200, 'sodium': 1800, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65},
    'marugame udon bukkake': {'carbs': 60, 'fats': 3, 'protein': 12, 'calories': 320, 'potassium': 180, 'sodium': 1200, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 60},
    'udon': {'carbs': 60, 'fats': 2, 'protein': 10, 'calories': 300, 'potassium': 150, 'sodium': 1100, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 60},

    'pepper lunch beef pepper rice': {'carbs': 60, 'fats': 28, 'protein': 25, 'calories': 600, 'potassium': 450, 'sodium': 1200, 'saturated_fat': 12, 'trans_fat': 0.5, 'gi': 65},
    'pepper lunch chicken pepper rice': {'carbs': 60, 'fats': 22, 'protein': 25, 'calories': 550, 'potassium': 400, 'sodium': 1100, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65},
    'pepper lunch salmon pepper rice': {'carbs': 60, 'fats': 25, 'protein': 22, 'calories': 580, 'potassium': 420, 'sodium': 1000, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
    
    'genki sushi salmon nigiri': {'carbs': 15, 'fats': 3, 'protein': 4, 'calories': 110, 'potassium': 100, 'sodium': 150, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 55},
    'sushi tei salmon sashimi': {'carbs': 0, 'fats': 8, 'protein': 20, 'calories': 150, 'potassium': 350, 'sodium': 50, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 0},
    'aburi salmon sushi': {'carbs': 15, 'fats': 5, 'protein': 5, 'calories': 130, 'potassium': 120, 'sodium': 200, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 55},
    'spicy tuna roll': {'carbs': 40, 'fats': 9, 'protein': 12, 'calories': 290, 'potassium': 200, 'sodium': 450, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 55},
    'california maki': {'carbs': 38, 'fats': 8, 'protein': 6, 'calories': 250, 'potassium': 150, 'sodium': 400, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 55},
    'ebi tempura': {'carbs': 15, 'fats': 12, 'protein': 8, 'calories': 200, 'potassium': 100, 'sodium': 350, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 60},

    'coco ichibanya pork cutlet curry': {'carbs': 110, 'fats': 45, 'protein': 25, 'calories': 950, 'potassium': 400, 'sodium': 1800, 'saturated_fat': 15, 'trans_fat': 0, 'gi': 70},
    'coco ichibanya beef curry': {'carbs': 90, 'fats': 30, 'protein': 20, 'calories': 750, 'potassium': 350, 'sodium': 1400, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 70},

    # European / Western / Italian Chains
    'saizeriya milano baked rice': {'carbs': 60, 'fats': 25, 'protein': 18, 'calories': 550, 'potassium': 350, 'sodium': 850, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 60},
    'saizeriya carbonara': {'carbs': 65, 'fats': 28, 'protein': 20, 'calories': 600, 'potassium': 280, 'sodium': 1100, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 55},
    'saizeriya aglio olio': {'carbs': 60, 'fats': 15, 'protein': 12, 'calories': 450, 'potassium': 200, 'sodium': 600, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 55},
    
    'pastamania beef bolognese': {'carbs': 70, 'fats': 15, 'protein': 22, 'calories': 520, 'potassium': 450, 'sodium': 950, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 55},
    'pastamania chicken arrabbiata': {'carbs': 65, 'fats': 14, 'protein': 25, 'calories': 500, 'potassium': 400, 'sodium': 1050, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 55},
    
    'poulet roast chicken': {'carbs': 10, 'fats': 25, 'protein': 45, 'calories': 450, 'potassium': 400, 'sodium': 850, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 0},
    'fish and co seafood platter': {'carbs': 65, 'fats': 45, 'protein': 40, 'calories': 850, 'potassium': 600, 'sodium': 1800, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 65},

    # Middle Eastern / Mediterranean / Kebab
    'stuffd chicken burrito': {'carbs': 65, 'fats': 18, 'protein': 30, 'calories': 550, 'potassium': 500, 'sodium': 1200, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 55},
    'stuffd beef burrito': {'carbs': 60, 'fats': 22, 'protein': 35, 'calories': 600, 'potassium': 600, 'sodium': 1300, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 55},
    
    'kazbar chicken shawarma': {'carbs': 45, 'fats': 18, 'protein': 35, 'calories': 500, 'potassium': 450, 'sodium': 1100, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 55},
    'kazbar mixed grill': {'carbs': 20, 'fats': 40, 'protein': 65, 'calories': 700, 'potassium': 800, 'sodium': 1500, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 45},
    
    'beef kebab roll': {'carbs': 50, 'fats': 25, 'protein': 30, 'calories': 550, 'potassium': 400, 'sodium': 900, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 55},
    'chicken kebab roll': {'carbs': 50, 'fats': 18, 'protein': 28, 'calories': 480, 'potassium': 350, 'sodium': 850, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 55},
    'hummus with pita': {'carbs': 45, 'fats': 15, 'protein': 10, 'calories': 350, 'potassium': 250, 'sodium': 400, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 45},

    # Indian / Mamak / Biryani
    'prata wala plain prata': {'carbs': 30, 'fats': 12, 'protein': 5, 'calories': 250, 'potassium': 80, 'sodium': 200, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
    'prata wala egg prata': {'carbs': 32, 'fats': 18, 'protein': 12, 'calories': 350, 'potassium': 120, 'sodium': 400, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 60},
    'prata wala chicken biryani': {'carbs': 90, 'fats': 35, 'protein': 35, 'calories': 850, 'potassium': 450, 'sodium': 1200, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 60},

    'komalas chole bhature': {'carbs': 85, 'fats': 22, 'protein': 15, 'calories': 600, 'potassium': 400, 'sodium': 950, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65},
    'komalas masala dosa': {'carbs': 65, 'fats': 15, 'protein': 10, 'calories': 450, 'potassium': 300, 'sodium': 600, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 55},
    
    'mutton biryani': {'carbs': 90, 'fats': 40, 'protein': 40, 'calories': 900, 'potassium': 500, 'sodium': 1300, 'saturated_fat': 15, 'trans_fat': 0, 'gi': 60},
    'chicken tikka masala': {'carbs': 15, 'fats': 25, 'protein': 35, 'calories': 450, 'potassium': 450, 'sodium': 900, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 40},
    'butter chicken': {'carbs': 15, 'fats': 35, 'protein': 30, 'calories': 500, 'potassium': 400, 'sodium': 850, 'saturated_fat': 15, 'trans_fat': 0, 'gi': 40},
    'garlic naan': {'carbs': 30, 'fats': 4, 'protein': 5, 'calories': 180, 'potassium': 90, 'sodium': 250, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 60},
    'tandoori chicken': {'carbs': 5, 'fats': 12, 'protein': 35, 'calories': 280, 'potassium': 350, 'sodium': 800, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 0},
    'murtabak': {'carbs': 70, 'fats': 40, 'protein': 40, 'calories': 800, 'potassium': 450, 'sodium': 1500, 'saturated_fat': 15, 'trans_fat': 0, 'gi': 65},

    # Cafe Chains / Pastries / Drinks
    'starbucks caramel macchiato': {'carbs': 35, 'fats': 7, 'protein': 10, 'calories': 250, 'potassium': 320, 'sodium': 150, 'saturated_fat': 4.5, 'trans_fat': 0, 'gi': 60},
    'caramel macchiato': {'carbs': 35, 'fats': 7, 'protein': 10, 'calories': 250, 'potassium': 320, 'sodium': 150, 'saturated_fat': 4.5, 'trans_fat': 0, 'gi': 60},
    'starbucks vanilla latte': {'carbs': 37, 'fats': 6, 'protein': 12, 'calories': 250, 'potassium': 380, 'sodium': 150, 'saturated_fat': 3.5, 'trans_fat': 0, 'gi': 60},
    'vanilla latte': {'carbs': 37, 'fats': 6, 'protein': 12, 'calories': 250, 'potassium': 380, 'sodium': 150, 'saturated_fat': 3.5, 'trans_fat': 0, 'gi': 60},
    'starbucks cafe mocha': {'carbs': 44, 'fats': 15, 'protein': 13, 'calories': 360, 'potassium': 400, 'sodium': 140, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 65},
    'cafe mocha': {'carbs': 44, 'fats': 15, 'protein': 13, 'calories': 360, 'potassium': 400, 'sodium': 140, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 65},
    'mocha': {'carbs': 44, 'fats': 15, 'protein': 13, 'calories': 360, 'potassium': 400, 'sodium': 140, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 65},
    'starbucks americano': {'carbs': 3, 'fats': 0, 'protein': 1, 'calories': 15, 'potassium': 200, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'americano': {'carbs': 3, 'fats': 0, 'protein': 1, 'calories': 15, 'potassium': 200, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'cafe americano': {'carbs': 3, 'fats': 0, 'protein': 1, 'calories': 15, 'potassium': 200, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'starbucks cappuccino': {'carbs': 14, 'fats': 5, 'protein': 9, 'calories': 140, 'potassium': 300, 'sodium': 120, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 45},
    'cappuccino': {'carbs': 14, 'fats': 5, 'protein': 9, 'calories': 140, 'potassium': 300, 'sodium': 120, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 45},
    'starbucks flat white': {'carbs': 18, 'fats': 11, 'protein': 12, 'calories': 220, 'potassium': 400, 'sodium': 150, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 45},
    'flat white': {'carbs': 18, 'fats': 11, 'protein': 12, 'calories': 220, 'potassium': 400, 'sodium': 150, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 45},
    'starbucks matcha latte': {'carbs': 34, 'fats': 7, 'protein': 12, 'calories': 240, 'potassium': 300, 'sodium': 160, 'saturated_fat': 4.5, 'trans_fat': 0, 'gi': 65},
    'matcha latte': {'carbs': 34, 'fats': 7, 'protein': 12, 'calories': 240, 'potassium': 300, 'sodium': 160, 'saturated_fat': 4.5, 'trans_fat': 0, 'gi': 65},
    
    'starbucks mocha frappuccino': {'carbs': 60, 'fats': 15, 'protein': 5, 'calories': 370, 'potassium': 300, 'sodium': 240, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 75},
    'mocha frappe': {'carbs': 60, 'fats': 15, 'protein': 5, 'calories': 370, 'potassium': 300, 'sodium': 240, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 75},
    'mocha frappuccino': {'carbs': 60, 'fats': 15, 'protein': 5, 'calories': 370, 'potassium': 300, 'sodium': 240, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 75},
    'starbucks caramel frappuccino': {'carbs': 65, 'fats': 16, 'protein': 4, 'calories': 380, 'potassium': 250, 'sodium': 230, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 75},
    'caramel frappe': {'carbs': 65, 'fats': 16, 'protein': 4, 'calories': 380, 'potassium': 250, 'sodium': 230, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 75},
    'caramel frappuccino': {'carbs': 65, 'fats': 16, 'protein': 4, 'calories': 380, 'potassium': 250, 'sodium': 230, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 75},
    'starbucks java chip frappuccino': {'carbs': 72, 'fats': 18, 'protein': 6, 'calories': 440, 'potassium': 330, 'sodium': 260, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 75},
    'java chip frappe': {'carbs': 72, 'fats': 18, 'protein': 6, 'calories': 440, 'potassium': 330, 'sodium': 260, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 75},
    'starbucks matcha frappuccino': {'carbs': 65, 'fats': 16, 'protein': 6, 'calories': 420, 'potassium': 250, 'sodium': 240, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 75},
    'matcha frappe': {'carbs': 65, 'fats': 16, 'protein': 6, 'calories': 420, 'potassium': 250, 'sodium': 240, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 75},
    'green tea frappe': {'carbs': 65, 'fats': 16, 'protein': 6, 'calories': 420, 'potassium': 250, 'sodium': 240, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 75},
    'frappe': {'carbs': 60, 'fats': 15, 'protein': 5, 'calories': 370, 'potassium': 250, 'sodium': 200, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 75},
    
    'macchiato': {'carbs': 20, 'fats': 5, 'protein': 6, 'calories': 150, 'potassium': 200, 'sodium': 80, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 55},
    'espresso': {'carbs': 1, 'fats': 0, 'protein': 0.1, 'calories': 5, 'potassium': 115, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'double espresso': {'carbs': 2, 'fats': 0, 'protein': 0.2, 'calories': 10, 'potassium': 230, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'cafe latte': {'carbs': 15, 'fats': 7, 'protein': 10, 'calories': 160, 'potassium': 350, 'sodium': 130, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 45},
    'cold brew': {'carbs': 2, 'fats': 0, 'protein': 0, 'calories': 10, 'potassium': 150, 'sodium': 15, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'nitro cold brew': {'carbs': 2, 'fats': 0, 'protein': 0, 'calories': 10, 'potassium': 150, 'sodium': 15, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'iced latte': {'carbs': 12, 'fats': 5, 'protein': 8, 'calories': 130, 'potassium': 250, 'sodium': 100, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 45},
    'iced americano': {'carbs': 2, 'fats': 0, 'protein': 0.5, 'calories': 10, 'potassium': 150, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'iced coffee': {'carbs': 15, 'fats': 1, 'protein': 1, 'calories': 70, 'potassium': 150, 'sodium': 10, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 55}, # With some syrup
    'black coffee': {'carbs': 1, 'fats': 0, 'protein': 0, 'calories': 5, 'potassium': 115, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    
    'chai tea latte': {'carbs': 40, 'fats': 4, 'protein': 8, 'calories': 240, 'potassium': 200, 'sodium': 100, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 65},
    'iced chai latte': {'carbs': 42, 'fats': 5, 'protein': 8, 'calories': 250, 'potassium': 200, 'sodium': 100, 'saturated_fat': 2.5, 'trans_fat': 0, 'gi': 65},
    'earl grey tea': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 2, 'potassium': 30, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'chamomile tea': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 2, 'potassium': 10, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'peppermint tea': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 2, 'potassium': 10, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'lemon tea': {'carbs': 20, 'fats': 0, 'protein': 0, 'calories': 80, 'potassium': 30, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 60},

    'starbucks blueberry muffin': {'carbs': 52, 'fats': 15, 'protein': 5, 'calories': 360, 'potassium': 100, 'sodium': 320, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 70},
    'starbucks chocolate chip cookie': {'carbs': 45, 'fats': 15, 'protein': 3, 'calories': 310, 'potassium': 80, 'sodium': 250, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 70},
    'starbucks butter croissant': {'carbs': 28, 'fats': 14, 'protein': 5, 'calories': 250, 'potassium': 80, 'sodium': 300, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 75},
    'starbucks almond croissant': {'carbs': 36, 'fats': 22, 'protein': 8, 'calories': 380, 'potassium': 150, 'sodium': 350, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 70},
    'starbucks egg white wrap': {'carbs': 33, 'fats': 10, 'protein': 20, 'calories': 290, 'potassium': 250, 'sodium': 850, 'saturated_fat': 3.5, 'trans_fat': 0, 'gi': 55},

    'coffee bean pure vanilla ice blended': {'carbs': 85, 'fats': 10, 'protein': 10, 'calories': 480, 'potassium': 350, 'sodium': 320, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 75},
    'coffee bean mocha ice blended': {'carbs': 75, 'fats': 12, 'protein': 8, 'calories': 450, 'potassium': 400, 'sodium': 300, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 75},
    'coffee bean hazelnut latte': {'carbs': 45, 'fats': 8, 'protein': 10, 'calories': 300, 'potassium': 300, 'sodium': 200, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},

    'kopi': {'carbs': 22, 'fats': 5, 'protein': 2, 'calories': 140, 'potassium': 100, 'sodium': 40, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 60},
    'kopi c': {'carbs': 15, 'fats': 5, 'protein': 2, 'calories': 110, 'potassium': 100, 'sodium': 50, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 60},
    'kopi o': {'carbs': 15, 'fats': 0, 'protein': 0, 'calories': 60, 'potassium': 100, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'kopi o kosong': {'carbs': 1, 'fats': 0, 'protein': 0, 'calories': 5, 'potassium': 100, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'teh': {'carbs': 24, 'fats': 5, 'protein': 2, 'calories': 150, 'potassium': 50, 'sodium': 40, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 60},
    'teh c': {'carbs': 18, 'fats': 5, 'protein': 2, 'calories': 120, 'potassium': 50, 'sodium': 50, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 60},
    'teh o': {'carbs': 16, 'fats': 0, 'protein': 0, 'calories': 65, 'potassium': 50, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'teh o kosong': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 50, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'milo peng': {'carbs': 30, 'fats': 5, 'protein': 4, 'calories': 180, 'potassium': 200, 'sodium': 80, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 65},
    'milo dinosaur': {'carbs': 45, 'fats': 6, 'protein': 6, 'calories': 250, 'potassium': 250, 'sodium': 100, 'saturated_fat': 3.5, 'trans_fat': 0, 'gi': 65},
    'bandung': {'carbs': 32, 'fats': 3, 'protein': 2, 'calories': 150, 'potassium': 50, 'sodium': 60, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 65},
    'teh tarik': {'carbs': 25, 'fats': 6, 'protein': 2, 'calories': 160, 'potassium': 50, 'sodium': 50, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 60},

    # Bakeries & Pastries (BreadTalk, Four Leaves, Bengawan Solo)
    'breadtalk flosss': {'carbs': 35, 'fats': 15, 'protein': 10, 'calories': 320, 'potassium': 120, 'sodium': 450, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 70},
    'breadtalk fire flosss': {'carbs': 35, 'fats': 18, 'protein': 10, 'calories': 350, 'potassium': 120, 'sodium': 550, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 70},
    'breadtalk sausage bun': {'carbs': 30, 'fats': 14, 'protein': 8, 'calories': 280, 'potassium': 150, 'sodium': 400, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 70},
    'breadtalk cheese sausage': {'carbs': 30, 'fats': 18, 'protein': 10, 'calories': 320, 'potassium': 150, 'sodium': 500, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 70},
    'breadtalk red bean bun': {'carbs': 45, 'fats': 5, 'protein': 6, 'calories': 250, 'potassium': 180, 'sodium': 150, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 65},
    'breadtalk matcha bun': {'carbs': 40, 'fats': 8, 'protein': 5, 'calories': 260, 'potassium': 150, 'sodium': 150, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
    'breadtalk earthquake cheese': {'carbs': 38, 'fats': 16, 'protein': 12, 'calories': 350, 'potassium': 200, 'sodium': 450, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 70},
    
    'four leaves strawberry shortcake': {'carbs': 35, 'fats': 15, 'protein': 4, 'calories': 300, 'potassium': 100, 'sodium': 150, 'saturated_fat': 8, 'trans_fat': 0.2, 'gi': 70},
    'four leaves pizza slice': {'carbs': 25, 'fats': 12, 'protein': 8, 'calories': 250, 'potassium': 150, 'sodium': 450, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'tuna bun': {'carbs': 30, 'fats': 10, 'protein': 10, 'calories': 260, 'potassium': 150, 'sodium': 350, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 65},
    'kaya bun': {'carbs': 40, 'fats': 6, 'protein': 5, 'calories': 240, 'potassium': 120, 'sodium': 180, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 75},
    'curry bun': {'carbs': 35, 'fats': 12, 'protein': 6, 'calories': 280, 'potassium': 200, 'sodium': 400, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 70},
    'chicken floss bun': {'carbs': 35, 'fats': 12, 'protein': 10, 'calories': 300, 'potassium': 130, 'sodium': 400, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 70},
    'pork floss bun': {'carbs': 35, 'fats': 15, 'protein': 10, 'calories': 320, 'potassium': 130, 'sodium': 450, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 70},
    'butter sugar bun': {'carbs': 35, 'fats': 14, 'protein': 4, 'calories': 280, 'potassium': 100, 'sodium': 200, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 75},
    'coffee bun': {'carbs': 45, 'fats': 18, 'protein': 5, 'calories': 350, 'potassium': 150, 'sodium': 250, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 70},
    'roti boy': {'carbs': 45, 'fats': 18, 'protein': 5, 'calories': 350, 'potassium': 150, 'sodium': 250, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 70},
    'pineapple bun': {'carbs': 45, 'fats': 12, 'protein': 6, 'calories': 320, 'potassium': 150, 'sodium': 250, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 75},
    'bolo bao': {'carbs': 45, 'fats': 12, 'protein': 6, 'calories': 320, 'potassium': 150, 'sodium': 250, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 75},
    'cheese bun': {'carbs': 30, 'fats': 14, 'protein': 8, 'calories': 280, 'potassium': 150, 'sodium': 350, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 70},

    'bengawan solo pandan chiffon': {'carbs': 18, 'fats': 8, 'protein': 3, 'calories': 150, 'potassium': 80, 'sodium': 100, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
    'pandan chiffon cake': {'carbs': 18, 'fats': 8, 'protein': 3, 'calories': 150, 'potassium': 80, 'sodium': 100, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
    'kueh lapis': {'carbs': 15, 'fats': 12, 'protein': 2, 'calories': 180, 'potassium': 50, 'sodium': 120, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 65},
    'ondeh ondeh': {'carbs': 22, 'fats': 3, 'protein': 1, 'calories': 120, 'potassium': 60, 'sodium': 80, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 70},
    'kueh salat': {'carbs': 28, 'fats': 5, 'protein': 2, 'calories': 160, 'potassium': 80, 'sodium': 90, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
    'seri muka': {'carbs': 28, 'fats': 5, 'protein': 2, 'calories': 160, 'potassium': 80, 'sodium': 90, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
    'kueh dadar': {'carbs': 25, 'fats': 5, 'protein': 1, 'calories': 150, 'potassium': 70, 'sodium': 80, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 60},
    'ang ku kueh': {'carbs': 30, 'fats': 4, 'protein': 2, 'calories': 160, 'potassium': 90, 'sodium': 100, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 65},
    'soon kueh': {'carbs': 22, 'fats': 3, 'protein': 2, 'calories': 120, 'potassium': 100, 'sodium': 250, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 60},

    'toast box kaya toast': {'carbs': 30, 'fats': 12, 'protein': 4, 'calories': 250, 'potassium': 80, 'sodium': 250, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 75},
    'yakun kaya toast': {'carbs': 30, 'fats': 12, 'protein': 4, 'calories': 250, 'potassium': 80, 'sodium': 250, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 75},
    'peanut butter thick toast': {'carbs': 40, 'fats': 18, 'protein': 8, 'calories': 350, 'potassium': 150, 'sodium': 300, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
    'egg tart': {'carbs': 25, 'fats': 12, 'protein': 4, 'calories': 220, 'potassium': 80, 'sodium': 150, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65},

    # Indonesian / Ayam Penyet / Nasi Padang
    'ayam penyet ria ayam penyet': {'carbs': 45, 'fats': 35, 'protein': 35, 'calories': 650, 'potassium': 350, 'sodium': 1100, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 70},
    'ayam penyet': {'carbs': 45, 'fats': 35, 'protein': 35, 'calories': 650, 'potassium': 350, 'sodium': 1100, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 70},
    'ayam bakar': {'carbs': 50, 'fats': 20, 'protein': 35, 'calories': 550, 'potassium': 400, 'sodium': 900, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 70},
    'bebek goreng': {'carbs': 40, 'fats': 55, 'protein': 25, 'calories': 750, 'potassium': 300, 'sodium': 1200, 'saturated_fat': 18, 'trans_fat': 0, 'gi': 70},
    'nasi padang beef rendang': {'carbs': 60, 'fats': 35, 'protein': 30, 'calories': 680, 'potassium': 450, 'sodium': 1400, 'saturated_fat': 15, 'trans_fat': 0, 'gi': 65},
    'beef rendang': {'carbs': 15, 'fats': 28, 'protein': 25, 'calories': 400, 'potassium': 350, 'sodium': 1200, 'saturated_fat': 15, 'trans_fat': 0, 'gi': 45},
    'nasi padang ayam gulai': {'carbs': 60, 'fats': 25, 'protein': 30, 'calories': 600, 'potassium': 400, 'sodium': 1100, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 65},
    'nasi goreng kampung': {'carbs': 65, 'fats': 20, 'protein': 15, 'calories': 500, 'potassium': 250, 'sodium': 1300, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65},
    'gado gado': {'carbs': 30, 'fats': 20, 'protein': 12, 'calories': 350, 'potassium': 350, 'sodium': 800, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 55},
    'sate ayam': {'carbs': 20, 'fats': 15, 'protein': 25, 'calories': 300, 'potassium': 300, 'sodium': 850, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 55},
    'soto ayam': {'carbs': 35, 'fats': 15, 'protein': 20, 'calories': 350, 'potassium': 400, 'sodium': 1200, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 60},

    # Malaysian / PappaRich / Penang / Kopitiam
    'papparich nasi lemak with fried chicken': {'carbs': 80, 'fats': 45, 'protein': 30, 'calories': 850, 'potassium': 400, 'sodium': 1500, 'saturated_fat': 20, 'trans_fat': 0, 'gi': 75},
    'nasi lemak with fried chicken': {'carbs': 80, 'fats': 45, 'protein': 30, 'calories': 850, 'potassium': 400, 'sodium': 1500, 'saturated_fat': 20, 'trans_fat': 0, 'gi': 75},
    'nasi lemak with curry chicken': {'carbs': 80, 'fats': 35, 'protein': 28, 'calories': 750, 'potassium': 450, 'sodium': 1400, 'saturated_fat': 18, 'trans_fat': 0, 'gi': 75},
    'penang assam laksa': {'carbs': 65, 'fats': 10, 'protein': 15, 'calories': 450, 'potassium': 300, 'sodium': 1500, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 60},
    'penang char kway teow': {'carbs': 70, 'fats': 35, 'protein': 20, 'calories': 700, 'potassium': 200, 'sodium': 1300, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 70},
    'papparich curry laksa': {'carbs': 60, 'fats': 35, 'protein': 25, 'calories': 650, 'potassium': 350, 'sodium': 1600, 'saturated_fat': 22, 'trans_fat': 0, 'gi': 65},
    'mee rebus': {'carbs': 75, 'fats': 20, 'protein': 18, 'calories': 550, 'potassium': 400, 'sodium': 1400, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'mee soto': {'carbs': 50, 'fats': 12, 'protein': 20, 'calories': 400, 'potassium': 350, 'sodium': 1500, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
    'roti canai': {'carbs': 35, 'fats': 15, 'protein': 6, 'calories': 300, 'potassium': 100, 'sodium': 350, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 70},
    'maggi goreng': {'carbs': 60, 'fats': 22, 'protein': 12, 'calories': 500, 'potassium': 150, 'sodium': 1800, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 75},
    'kolo mee': {'carbs': 55, 'fats': 18, 'protein': 18, 'calories': 450, 'potassium': 200, 'sodium': 1000, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65},
    'pan mee': {'carbs': 60, 'fats': 15, 'protein': 20, 'calories': 450, 'potassium': 250, 'sodium': 1200, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},

    # Liquor / Beer / Wine / Cocktails (Calories include alcohol)
    'beer': {'carbs': 13, 'fats': 0, 'protein': 1, 'calories': 150, 'potassium': 100, 'sodium': 15, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 100},
    'tiger beer': {'carbs': 11, 'fats': 0, 'protein': 1, 'calories': 140, 'potassium': 90, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 100},
    'heineken': {'carbs': 11, 'fats': 0, 'protein': 1, 'calories': 140, 'potassium': 90, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 100},
    'san miguel pale pilsen': {'carbs': 12, 'fats': 0, 'protein': 1, 'calories': 140, 'potassium': 90, 'sodium': 15, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 100},
    'red horse beer': {'carbs': 14, 'fats': 0, 'protein': 1, 'calories': 190, 'potassium': 100, 'sodium': 15, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 100},
    'somersby apple cider': {'carbs': 28, 'fats': 0, 'protein': 0, 'calories': 200, 'potassium': 120, 'sodium': 20, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'guinness stout': {'carbs': 10, 'fats': 0, 'protein': 1, 'calories': 125, 'potassium': 120, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 100},
    
    'red wine': {'carbs': 4, 'fats': 0, 'protein': 0, 'calories': 125, 'potassium': 180, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'white wine': {'carbs': 4, 'fats': 0, 'protein': 0, 'calories': 120, 'potassium': 100, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'soju': {'carbs': 15, 'fats': 0, 'protein': 0, 'calories': 400, 'potassium': 10, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'flavored soju': {'carbs': 30, 'fats': 0, 'protein': 0, 'calories': 450, 'potassium': 10, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},

    'vodka': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 64, 'potassium': 0, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'whiskey': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 70, 'potassium': 0, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'whisky': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 70, 'potassium': 0, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'gin': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 73, 'potassium': 0, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'rum': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 65, 'potassium': 0, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'gin and tonic': {'carbs': 15, 'fats': 0, 'protein': 0, 'calories': 150, 'potassium': 5, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'vodka soda': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 65, 'potassium': 5, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'rum and coke': {'carbs': 25, 'fats': 0, 'protein': 0, 'calories': 180, 'potassium': 10, 'sodium': 15, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'margarita': {'carbs': 20, 'fats': 0, 'protein': 0, 'calories': 250, 'potassium': 30, 'sodium': 200, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'mojito': {'carbs': 25, 'fats': 0, 'protein': 0, 'calories': 220, 'potassium': 40, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'long island iced tea': {'carbs': 30, 'fats': 0, 'protein': 0, 'calories': 280, 'potassium': 20, 'sodium': 20, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},

    # Convenience Store / 7-Eleven Drinks
    '7-eleven slurpee': {'carbs': 48, 'fats': 0, 'protein': 0, 'calories': 190, 'potassium': 0, 'sodium': 20, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 80},
    'slurpee': {'carbs': 48, 'fats': 0, 'protein': 0, 'calories': 190, 'potassium': 0, 'sodium': 20, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 80},
    '7-eleven big gulp cola': {'carbs': 85, 'fats': 0, 'protein': 0, 'calories': 320, 'potassium': 5, 'sodium': 40, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'big gulp': {'carbs': 85, 'fats': 0, 'protein': 0, 'calories': 320, 'potassium': 5, 'sodium': 40, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'pokka green tea': {'carbs': 25, 'fats': 0, 'protein': 0, 'calories': 100, 'potassium': 50, 'sodium': 30, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'pokka oolong tea': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 30, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    '100 plus': {'carbs': 33, 'fats': 0, 'protein': 0, 'calories': 135, 'potassium': 150, 'sodium': 250, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 75},
    'gatorade': {'carbs': 35, 'fats': 0, 'protein': 0, 'calories': 140, 'potassium': 75, 'sodium': 270, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 75},
    'red bull': {'carbs': 27, 'fats': 0, 'protein': 1, 'calories': 110, 'potassium': 10, 'sodium': 100, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'monster energy': {'carbs': 54, 'fats': 0, 'protein': 0, 'calories': 210, 'potassium': 20, 'sodium': 370, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'yakult': {'carbs': 15, 'fats': 0, 'protein': 1, 'calories': 65, 'potassium': 35, 'sodium': 15, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},

    # Bubble Tea & Toppings (Medium/M, 100% Sugar assumed unless noted)
    'bubble tea': {'carbs': 60, 'fats': 10, 'protein': 2, 'calories': 350, 'potassium': 100, 'sodium': 40, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 75},
    'milk tea': {'carbs': 45, 'fats': 10, 'protein': 2, 'calories': 250, 'potassium': 90, 'sodium': 40, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'brown sugar bubble tea': {'carbs': 80, 'fats': 12, 'protein': 2, 'calories': 450, 'potassium': 110, 'sodium': 50, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 85},

    'koi golden bubble milk tea': {'carbs': 65, 'fats': 14, 'protein': 2, 'calories': 400, 'potassium': 120, 'sodium': 60, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 75},
    'koi milk tea': {'carbs': 45, 'fats': 10, 'protein': 2, 'calories': 260, 'potassium': 90, 'sodium': 40, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'koi hazelnut milk tea': {'carbs': 60, 'fats': 10, 'protein': 2, 'calories': 320, 'potassium': 95, 'sodium': 45, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 70},
    'koi yakult green tea': {'carbs': 50, 'fats': 0, 'protein': 2, 'calories': 220, 'potassium': 80, 'sodium': 25, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 70},
    'koi green tea': {'carbs': 30, 'fats': 0, 'protein': 0, 'calories': 120, 'potassium': 60, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},

    'gong cha milk tea': {'carbs': 44, 'fats': 8, 'protein': 2, 'calories': 250, 'potassium': 90, 'sodium': 40, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
    'gong cha earl grey milk tea': {'carbs': 44, 'fats': 8, 'protein': 2, 'calories': 250, 'potassium': 90, 'sodium': 40, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
    'gong cha alisan tea': {'carbs': 28, 'fats': 0, 'protein': 0, 'calories': 110, 'potassium': 50, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'gong cha passionfruit green tea': {'carbs': 45, 'fats': 0, 'protein': 0, 'calories': 180, 'potassium': 70, 'sodium': 15, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},

    'liho classic milk tea': {'carbs': 40, 'fats': 9, 'protein': 2, 'calories': 240, 'potassium': 80, 'sodium': 35, 'saturated_fat': 4.5, 'trans_fat': 0, 'gi': 65},
    'liho da hong pao milk tea': {'carbs': 40, 'fats': 9, 'protein': 2, 'calories': 240, 'potassium': 80, 'sodium': 35, 'saturated_fat': 4.5, 'trans_fat': 0, 'gi': 65},
    'liho passion aloe': {'carbs': 48, 'fats': 0, 'protein': 0, 'calories': 200, 'potassium': 60, 'sodium': 20, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},

    'chicha san chen bubble milk tea': {'carbs': 55, 'fats': 15, 'protein': 3, 'calories': 380, 'potassium': 100, 'sodium': 50, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 75},
    'chicha san chen dong ding oolong milk tea': {'carbs': 45, 'fats': 12, 'protein': 3, 'calories': 280, 'potassium': 90, 'sodium': 40, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65},
    'chicha san chen green tea with passionfruit': {'carbs': 45, 'fats': 0, 'protein': 1, 'calories': 200, 'potassium': 70, 'sodium': 15, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},

    'tapioca pearls': {'carbs': 35, 'fats': 0, 'protein': 0, 'calories': 150, 'potassium': 10, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 75},
    'boba': {'carbs': 35, 'fats': 0, 'protein': 0, 'calories': 150, 'potassium': 10, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 75},
    'golden pearls': {'carbs': 33, 'fats': 0, 'protein': 0, 'calories': 140, 'potassium': 10, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 75},
    'grass jelly': {'carbs': 10, 'fats': 0, 'protein': 0, 'calories': 40, 'potassium': 40, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 60},
    'aiyu jelly': {'carbs': 11, 'fats': 0, 'protein': 0, 'calories': 45, 'potassium': 35, 'sodium': 5, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 60},
    'coconut jelly': {'carbs': 15, 'fats': 0, 'protein': 0, 'calories': 60, 'potassium': 20, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'nata de coco': {'carbs': 15, 'fats': 0, 'protein': 0, 'calories': 60, 'potassium': 20, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    'pudding': {'carbs': 20, 'fats': 4, 'protein': 2, 'calories': 120, 'potassium': 50, 'sodium': 80, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 65},
    'cheese foam': {'carbs': 8, 'fats': 12, 'protein': 2, 'calories': 150, 'potassium': 30, 'sodium': 120, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 45},
    'macchiato foam': {'carbs': 8, 'fats': 12, 'protein': 2, 'calories': 150, 'potassium': 30, 'sodium': 120, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 45},

    # Breakfast
    'bacon': {'carbs': 1.4, 'fats': 42, 'protein': 37, 'calories': 541, 'potassium': 565, 'sodium': 1717, 'saturated_fat': 14, 'trans_fat': 0, 'gi': 0},
    'sausage': {'carbs': 2, 'fats': 27, 'protein': 14, 'calories': 300, 'potassium': 200, 'sodium': 800, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},
    'toast': {'carbs': 50, 'fats': 4, 'protein': 9, 'calories': 270, 'potassium': 120, 'sodium': 450, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 70},
    'butter': {'carbs': 0.1, 'fats': 81, 'protein': 0.9, 'calories': 717, 'potassium': 24, 'sodium': 11, 'saturated_fat': 51, 'trans_fat': 3, 'gi': 0},
    'cheese': {'carbs': 1.3, 'fats': 33, 'protein': 25, 'calories': 402, 'potassium': 98, 'sodium': 621, 'saturated_fat': 21, 'trans_fat': 1, 'gi': 0}, # Cheddar-ish
    'yogurt': {'carbs': 4.7, 'fats': 3.3, 'protein': 3.5, 'calories': 61, 'potassium': 155, 'sodium': 46, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 35},
    'mozzarella': {'carbs': 2, 'fats': 22, 'protein': 22, 'calories': 280, 'potassium': 95, 'sodium': 486, 'saturated_fat': 13, 'trans_fat': 0.5, 'gi': 0},
    'feta': {'carbs': 4, 'fats': 21, 'protein': 14, 'calories': 264, 'potassium': 62, 'sodium': 917, 'saturated_fat': 15, 'trans_fat': 0, 'gi': 0},
    'parmesan': {'carbs': 4, 'fats': 29, 'protein': 38, 'calories': 431, 'potassium': 125, 'sodium': 1529, 'saturated_fat': 17, 'trans_fat': 0, 'gi': 0},
    'brie': {'carbs': 0.5, 'fats': 28, 'protein': 21, 'calories': 334, 'potassium': 152, 'sodium': 629, 'saturated_fat': 17, 'trans_fat': 0, 'gi': 0},
    'cottage cheese': {'carbs': 3, 'fats': 4, 'protein': 11, 'calories': 98, 'potassium': 104, 'sodium': 364, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 10},
    'cream cheese': {'carbs': 4, 'fats': 34, 'protein': 6, 'calories': 342, 'potassium': 138, 'sodium': 321, 'saturated_fat': 21, 'trans_fat': 1, 'gi': 0},
    
    # Extended Filipino
    'tapa': {'carbs': 5, 'fats': 12, 'protein': 25, 'calories': 230, 'potassium': 300, 'sodium': 800, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 45},
    'longganisa': {'carbs': 10, 'fats': 25, 'protein': 12, 'calories': 320, 'potassium': 200, 'sodium': 900, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 50},
    'tocino': {'carbs': 15, 'fats': 20, 'protein': 10, 'calories': 280, 'potassium': 150, 'sodium': 600, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 60},
    'pandesal': {'carbs': 55, 'fats': 5, 'protein': 10, 'calories': 300, 'potassium': 100, 'sodium': 400, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 70},
    'kare-kare': {'carbs': 8, 'fats': 15, 'protein': 18, 'calories': 240, 'potassium': 300, 'sodium': 500, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 35},
    'lumpia': {'carbs': 20, 'fats': 15, 'protein': 8, 'calories': 250, 'potassium': 150, 'sodium': 400, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 60}, # Fried spring roll
    'champorado': {'carbs': 40, 'fats': 2, 'protein': 4, 'calories': 200, 'potassium': 150, 'sodium': 20, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 70},
    
    # More Fruits
    'orange': {'carbs': 12, 'fats': 0.1, 'protein': 0.9, 'calories': 47, 'potassium': 181, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 40},
    'mango': {'carbs': 15, 'fats': 0.4, 'protein': 0.8, 'calories': 60, 'potassium': 168, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 51},
    'pineapple': {'carbs': 13, 'fats': 0.1, 'protein': 0.5, 'calories': 50, 'potassium': 109, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 59},
    'watermelon': {'carbs': 8, 'fats': 0.2, 'protein': 0.6, 'calories': 30, 'potassium': 112, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 72},
    'grapes': {'carbs': 18, 'fats': 0.2, 'protein': 0.7, 'calories': 69, 'potassium': 191, 'sodium': 2, 'saturated_fat': 0.1, 'trans_fat': 0, 'gi': 59},
    'blueberry': {'carbs': 14, 'fats': 0.3, 'protein': 0.7, 'calories': 57, 'potassium': 77, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 53},
    'blackberry': {'carbs': 10, 'fats': 0.5, 'protein': 1.4, 'calories': 43, 'potassium': 162, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 25},
    'cranberry': {'carbs': 12, 'fats': 0.1, 'protein': 0.4, 'calories': 46, 'potassium': 85, 'sodium': 2, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 45},
    'cherry': {'carbs': 16, 'fats': 0.2, 'protein': 1.1, 'calories': 63, 'potassium': 222, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 20},
    'peach': {'carbs': 10, 'fats': 0.3, 'protein': 0.9, 'calories': 39, 'potassium': 190, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 42},
    'pear': {'carbs': 15, 'fats': 0.1, 'protein': 0.4, 'calories': 57, 'potassium': 116, 'sodium': 1, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 38},
    'plum': {'carbs': 11, 'fats': 0.3, 'protein': 0.7, 'calories': 46, 'potassium': 157, 'sodium': 0, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 40},
    'melon': {'carbs': 8, 'fats': 0.2, 'protein': 0.8, 'calories': 34, 'potassium': 267, 'sodium': 16, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 60}, # Cantaloupe/Honeydew avg
    
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

    # Restaurant Ramen (SG/JP/PH Chains)
    'tonkotsu ramen': {'carbs': 55, 'fats': 20, 'protein': 22, 'calories': 500, 'potassium': 350, 'sodium': 2000, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 65},
    'shoyu ramen': {'carbs': 55, 'fats': 10, 'protein': 18, 'calories': 380, 'potassium': 320, 'sodium': 1800, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 65},
    'miso ramen': {'carbs': 58, 'fats': 15, 'protein': 20, 'calories': 450, 'potassium': 400, 'sodium': 2200, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'shio ramen': {'carbs': 55, 'fats': 8, 'protein': 16, 'calories': 350, 'potassium': 300, 'sodium': 1900, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 65},
    'ichiran tonkotsu ramen': {'carbs': 60, 'fats': 22, 'protein': 23, 'calories': 525, 'potassium': 400, 'sodium': 2100, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 65},
    'ichiran ramen': {'carbs': 60, 'fats': 22, 'protein': 23, 'calories': 525, 'potassium': 400, 'sodium': 2100, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 65},
    'ippudo shiromaru classic': {'carbs': 55, 'fats': 19, 'protein': 21, 'calories': 490, 'potassium': 380, 'sodium': 2050, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 65},
    'ippudo akamaru modern': {'carbs': 56, 'fats': 24, 'protein': 22, 'calories': 540, 'potassium': 410, 'sodium': 2200, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 65},
    'ramen nagi butao king': {'carbs': 58, 'fats': 25, 'protein': 24, 'calories': 550, 'potassium': 450, 'sodium': 2300, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 65},
    'ramen nagi black king': {'carbs': 60, 'fats': 28, 'protein': 26, 'calories': 600, 'potassium': 500, 'sodium': 2400, 'saturated_fat': 11, 'trans_fat': 0, 'gi': 65},
    'ramen nagi red king': {'carbs': 59, 'fats': 26, 'protein': 25, 'calories': 580, 'potassium': 460, 'sodium': 2350, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 65},
    'mendokoro shoyu ramen': {'carbs': 56, 'fats': 14, 'protein': 19, 'calories': 420, 'potassium': 390, 'sodium': 1900, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'mendokoro tonkotsu ramen': {'carbs': 58, 'fats': 25, 'protein': 25, 'calories': 560, 'potassium': 420, 'sodium': 2150, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 65},
    'keisuke tonkotsu king': {'carbs': 55, 'fats': 21, 'protein': 23, 'calories': 510, 'potassium': 400, 'sodium': 2100, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 65},
    'tsuta shoyu soba': {'carbs': 52, 'fats': 12, 'protein': 18, 'calories': 400, 'potassium': 350, 'sodium': 1850, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
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

    # Deli & Processed Meats
    'salami': {'carbs': 1.2, 'fats': 26, 'protein': 22, 'calories': 336, 'potassium': 340, 'sodium': 1740, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 0},
    'pepperoni': {'carbs': 0, 'fats': 44, 'protein': 20, 'calories': 494, 'potassium': 286, 'sodium': 1582, 'saturated_fat': 17, 'trans_fat': 0.5, 'gi': 0},
    'bologna': {'carbs': 2, 'fats': 28, 'protein': 12, 'calories': 311, 'potassium': 180, 'sodium': 980, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 0},
    'pastrami': {'carbs': 0, 'fats': 6, 'protein': 22, 'calories': 147, 'potassium': 350, 'sodium': 1078, 'saturated_fat': 2.5, 'trans_fat': 0, 'gi': 0},
    'prosciutto': {'carbs': 0, 'fats': 19, 'protein': 25, 'calories': 269, 'potassium': 370, 'sodium': 2500, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 0},
    'deli ham': {'carbs': 2, 'fats': 3, 'protein': 16, 'calories': 105, 'potassium': 287, 'sodium': 1200, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 0},
    'sliced ham': {'carbs': 2, 'fats': 3, 'protein': 16, 'calories': 105, 'potassium': 287, 'sodium': 1200, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 0},
    'deli turkey': {'carbs': 1, 'fats': 2, 'protein': 17, 'calories': 104, 'potassium': 250, 'sodium': 1049, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 0},
    'sliced turkey': {'carbs': 1, 'fats': 2, 'protein': 17, 'calories': 104, 'potassium': 250, 'sodium': 1049, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 0},
    'chorizo': {'carbs': 2, 'fats': 38, 'protein': 24, 'calories': 455, 'potassium': 398, 'sodium': 1235, 'saturated_fat': 14, 'trans_fat': 0, 'gi': 0},
    'bratwurst': {'carbs': 2, 'fats': 28, 'protein': 12, 'calories': 333, 'potassium': 250, 'sodium': 848, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 0},
    'italian sausage': {'carbs': 1, 'fats': 28, 'protein': 14, 'calories': 344, 'potassium': 263, 'sodium': 740, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 0},
    'halal pepperoni': {'carbs': 0, 'fats': 43, 'protein': 20, 'calories': 490, 'potassium': 286, 'sodium': 1500, 'saturated_fat': 16, 'trans_fat': 0.5, 'gi': 0},
    'beef bacon': {'carbs': 1.5, 'fats': 32, 'protein': 30, 'calories': 415, 'potassium': 420, 'sodium': 1450, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 0},
    'turkey bacon': {'carbs': 2, 'fats': 27, 'protein': 29, 'calories': 366, 'potassium': 380, 'sodium': 1300, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},
    'halal hotdog': {'carbs': 2, 'fats': 25, 'protein': 10, 'calories': 290, 'potassium': 150, 'sodium': 1000, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},
    'halal sausage': {'carbs': 2, 'fats': 27, 'protein': 14, 'calories': 300, 'potassium': 200, 'sodium': 850, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},
    'chicken sausage': {'carbs': 2, 'fats': 10, 'protein': 19, 'calories': 186, 'potassium': 210, 'sodium': 750, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 0},
    'chicken ham': {'carbs': 2, 'fats': 4, 'protein': 16, 'calories': 112, 'potassium': 250, 'sodium': 1000, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 0},

    # Halal Meats
    'halal chicken': {'carbs': 0, 'fats': 3.6, 'protein': 31, 'calories': 165, 'potassium': 256, 'sodium': 0, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 0},
    'halal beef': {'carbs': 0, 'fats': 15, 'protein': 26, 'calories': 250, 'potassium': 318, 'sodium': 0, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 0},
    'halal goat': {'carbs': 0, 'fats': 3, 'protein': 27, 'calories': 143, 'potassium': 405, 'sodium': 86, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 0},
    'goat meat': {'carbs': 0, 'fats': 3, 'protein': 27, 'calories': 143, 'potassium': 405, 'sodium': 86, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 0},
    'mutton': {'carbs': 0, 'fats': 21, 'protein': 25, 'calories': 294, 'potassium': 310, 'sodium': 72, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},
    'lamb': {'carbs': 0, 'fats': 21, 'protein': 25, 'calories': 294, 'potassium': 310, 'sodium': 72, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},
    'lamb chop': {'carbs': 0, 'fats': 21, 'protein': 25, 'calories': 294, 'potassium': 310, 'sodium': 72, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},

    # FairPrice / SG / Local Snacks
    'milo': {'carbs': 60, 'fats': 10, 'protein': 12, 'calories': 400, 'potassium': 300, 'sodium': 150, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 55}, # Power/Dinosaur typically high sugar
    'maggi': {'carbs': 60, 'fats': 15, 'protein': 8, 'calories': 400, 'potassium': 100, 'sodium': 1800, 'saturated_fat': 7, 'trans_fat': 0.2, 'gi': 60}, # Instant Noodles
    'indomie': {'carbs': 60, 'fats': 20, 'protein': 8, 'calories': 450, 'potassium': 100, 'sodium': 1600, 'saturated_fat': 9, 'trans_fat': 0.5, 'gi': 60},
    'prawn crackers': {'carbs': 65, 'fats': 25, 'protein': 3, 'calories': 500, 'potassium': 50, 'sodium': 900, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 75}, # Keropok
    
    # SG Street Food & Pasar Malam
    'ramly burger': {'carbs': 40, 'fats': 28, 'protein': 22, 'calories': 500, 'potassium': 300, 'sodium': 1200, 'saturated_fat': 12, 'trans_fat': 0.5, 'gi': 65},
    'tutu kueh': {'carbs': 15, 'fats': 1, 'protein': 1, 'calories': 70, 'potassium': 45, 'sodium': 50, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 65},
    'muah chee': {'carbs': 60, 'fats': 10, 'protein': 4, 'calories': 350, 'potassium': 150, 'sodium': 100, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 75},
    'sweet potato balls': {'carbs': 35, 'fats': 6, 'protein': 2, 'calories': 200, 'potassium': 280, 'sodium': 80, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 70},
    'vadai': {'carbs': 18, 'fats': 10, 'protein': 5, 'calories': 180, 'potassium': 150, 'sodium': 250, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 55},
    'prawn vadai': {'carbs': 18, 'fats': 12, 'protein': 8, 'calories': 210, 'potassium': 180, 'sodium': 300, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 55},
    'taiwan sausage': {'carbs': 15, 'fats': 20, 'protein': 10, 'calories': 280, 'potassium': 180, 'sodium': 800, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 0},
    'keropok lekor': {'carbs': 45, 'fats': 10, 'protein': 8, 'calories': 300, 'potassium': 200, 'sodium': 500, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 65},
    'min jiang kueh': {'carbs': 40, 'fats': 8, 'protein': 5, 'calories': 250, 'potassium': 180, 'sodium': 250, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 60},
    'apam balik': {'carbs': 40, 'fats': 8, 'protein': 5, 'calories': 250, 'potassium': 180, 'sodium': 250, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 60},
    'tea leaf egg': {'carbs': 1, 'fats': 5, 'protein': 7, 'calories': 80, 'potassium': 65, 'sodium': 400, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 0},
    'otah': {'carbs': 8, 'fats': 10, 'protein': 8, 'calories': 150, 'potassium': 150, 'sodium': 450, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 45},
    'rojak': {'carbs': 65, 'fats': 18, 'protein': 10, 'calories': 450, 'potassium': 450, 'sodium': 900, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 65},
    'oyster omelette': {'carbs': 35, 'fats': 45, 'protein': 15, 'calories': 600, 'potassium': 400, 'sodium': 1100, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 55},
    'orh luak': {'carbs': 35, 'fats': 45, 'protein': 15, 'calories': 600, 'potassium': 400, 'sodium': 1100, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 55},
    'popiah': {'carbs': 24, 'fats': 7, 'protein': 8, 'calories': 188, 'potassium': 250, 'sodium': 600, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 45},
    'takoyaki': {'carbs': 40, 'fats': 14, 'protein': 10, 'calories': 320, 'potassium': 200, 'sodium': 850, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 65},
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
    'dr pepper': {'carbs': 11, 'fats': 0, 'protein': 0, 'calories': 42, 'potassium': 0, 'sodium': 15, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65}, # per 100ml
    'mountain dew': {'carbs': 12, 'fats': 0, 'protein': 0, 'calories': 48, 'potassium': 0, 'sodium': 15, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65}, # per 100ml
    'fanta orange': {'carbs': 11, 'fats': 0, 'protein': 0, 'calories': 45, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65}, # per 100ml
    'fanta': {'carbs': 11, 'fats': 0, 'protein': 0, 'calories': 45, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65}, # per 100ml
    'diet coke': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'coke zero': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'coke light': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'pepsi zero': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'pepsi max': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'pepsi light': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    'sprite zero': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
    '7up free': {'carbs': 0, 'fats': 0, 'protein': 0, 'calories': 0, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 0},
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
    'purefoods meatloaf': {'carbs': 5, 'fats': 15, 'protein': 12, 'calories': 200, 'potassium': 150, 'sodium': 850, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 0},
    'purefoods corned beef': {'carbs': 0, 'fats': 15, 'protein': 25, 'calories': 250, 'potassium': 150, 'sodium': 1000, 'saturated_fat': 7, 'trans_fat': 0.5, 'gi': 0},
    'purefoods tender juicy hotdog': {'carbs': 3, 'fats': 25, 'protein': 12, 'calories': 280, 'potassium': 160, 'sodium': 950, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},
    'purefoods hotdog': {'carbs': 3, 'fats': 25, 'protein': 12, 'calories': 280, 'potassium': 160, 'sodium': 950, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},
    'argentina corned beef': {'carbs': 2, 'fats': 15, 'protein': 20, 'calories': 240, 'potassium': 140, 'sodium': 900, 'saturated_fat': 6, 'trans_fat': 0.5, 'gi': 0},
    'cdo meatloaf': {'carbs': 5, 'fats': 14, 'protein': 11, 'calories': 190, 'potassium': 130, 'sodium': 800, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 0},
    'century tuna': {'carbs': 0, 'fats': 5, 'protein': 18, 'calories': 120, 'potassium': 200, 'sodium': 400, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 0},
    'century tuna flakes in oil': {'carbs': 0, 'fats': 12, 'protein': 16, 'calories': 180, 'potassium': 200, 'sodium': 450, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 0},
    '555 sardines': {'carbs': 4, 'fats': 8, 'protein': 18, 'calories': 170, 'potassium': 300, 'sodium': 550, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 45},
    'ligo sardines': {'carbs': 4, 'fats': 8, 'protein': 18, 'calories': 170, 'potassium': 300, 'sodium': 550, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 45},
    'maling luncheon meat': {'carbs': 2, 'fats': 28, 'protein': 13, 'calories': 320, 'potassium': 100, 'sodium': 1100, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},
    'maling': {'carbs': 2, 'fats': 28, 'protein': 13, 'calories': 320, 'potassium': 100, 'sodium': 1100, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 0},
    'dace with black beans': {'carbs': 2, 'fats': 20, 'protein': 18, 'calories': 260, 'potassium': 200, 'sodium': 850, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 0},
    'fried dace': {'carbs': 1, 'fats': 21, 'protein': 17, 'calories': 250, 'potassium': 200, 'sodium': 800, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 0},
    'hunts pork and beans': {'carbs': 25, 'fats': 1, 'protein': 7, 'calories': 140, 'potassium': 300, 'sodium': 450, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 45},
    'pork and beans': {'carbs': 23, 'fats': 1, 'protein': 7, 'calories': 130, 'potassium': 280, 'sodium': 400, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 45},
    'campbells chicken noodle soup': {'carbs': 8, 'fats': 2, 'protein': 3, 'calories': 60, 'potassium': 100, 'sodium': 890, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 45},
    'campbells tomato soup': {'carbs': 17, 'fats': 2, 'protein': 2, 'calories': 90, 'potassium': 350, 'sodium': 480, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 45},
    'chef boyardee beef ravioli': {'carbs': 34, 'fats': 7, 'protein': 7, 'calories': 220, 'potassium': 250, 'sodium': 750, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 55},
    'bushs baked beans': {'carbs': 30, 'fats': 1, 'protein': 6, 'calories': 160, 'potassium': 500, 'sodium': 550, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 45},
    'hormel chili': {'carbs': 17, 'fats': 14, 'protein': 16, 'calories': 260, 'potassium': 450, 'sodium': 990, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 45},
    'hormel chili with beans': {'carbs': 22, 'fats': 15, 'protein': 16, 'calories': 290, 'potassium': 500, 'sodium': 950, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 45},
    'libbys vienna sausage': {'carbs': 2, 'fats': 18, 'protein': 9, 'calories': 200, 'potassium': 100, 'sodium': 850, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 0},
    'meatloaf': {'carbs': 5, 'fats': 15, 'protein': 12, 'calories': 200, 'potassium': 150, 'sodium': 850, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 0},

    # Instant / Processed
    'instant noodles': {'carbs': 60, 'fats': 15, 'protein': 8, 'calories': 400, 'potassium': 100, 'sodium': 1800, 'saturated_fat': 7, 'trans_fat': 0.2, 'gi': 60},
    'cup noodles': {'carbs': 45, 'fats': 12, 'protein': 7, 'calories': 300, 'potassium': 90, 'sodium': 1200, 'saturated_fat': 6, 'trans_fat': 0.2, 'gi': 60},
    'ramen packet': {'carbs': 65, 'fats': 20, 'protein': 9, 'calories': 480, 'potassium': 150, 'sodium': 1900, 'saturated_fat': 9, 'trans_fat': 0.5, 'gi': 60}, # High sodium warning
    'yakisoba': {'carbs': 70, 'fats': 20, 'protein': 10, 'calories': 500, 'potassium': 150, 'sodium': 1400, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 65},
    'mac and cheese': {'carbs': 50, 'fats': 15, 'protein': 12, 'calories': 400, 'potassium': 200, 'sodium': 800, 'saturated_fat': 6, 'trans_fat': 0.5, 'gi': 65}, # Instant box
    'frozen pizza': {'carbs': 30, 'fats': 12, 'protein': 12, 'calories': 280, 'potassium': 150, 'sodium': 600, 'saturated_fat': 5, 'trans_fat': 0.3, 'gi': 60}, # Per slice
    'fish finger': {'carbs': 20, 'fats': 12, 'protein': 12, 'calories': 240, 'potassium': 200, 'sodium': 400, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 60},
    'nuggets': {'carbs': 20, 'fats': 18, 'protein': 16, 'calories': 300, 'potassium': 250, 'sodium': 500, 'saturated_fat': 4, 'trans_fat': 0.1, 'gi': 60},
    
    # More Filipino / Asian
    'tinola': {'carbs': 5, 'fats': 8, 'protein': 25, 'calories': 200, 'potassium': 300, 'sodium': 600, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 0},
    'nilaga': {'carbs': 8, 'fats': 15, 'protein': 25, 'calories': 280, 'potassium': 350, 'sodium': 700, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 0},
    'afritada': {'carbs': 12, 'fats': 15, 'protein': 20, 'calories': 260, 'potassium': 300, 'sodium': 600, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 45}, # Tomato sauce
    'menudo': {'carbs': 10, 'fats': 18, 'protein': 22, 'calories': 300, 'potassium': 350, 'sodium': 650, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 45},
    'caldereta': {'carbs': 12, 'fats': 20, 'protein': 25, 'calories': 350, 'potassium': 400, 'sodium': 700, 'saturated_fat': 8, 'trans_fat': 0.5, 'gi': 45},
    'paksiw': {'carbs': 5, 'fats': 10, 'protein': 20, 'calories': 200, 'potassium': 250, 'sodium': 500, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 0},
    'bicol express': {'carbs': 8, 'fats': 25, 'protein': 18, 'calories': 350, 'potassium': 300, 'sodium': 600, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 0}, # Coconut milk
    'laing': {'carbs': 10, 'fats': 20, 'protein': 5, 'calories': 250, 'potassium': 400, 'sodium': 500, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 15},
    'pinakbet': {'carbs': 15, 'fats': 8, 'protein': 6, 'calories': 160, 'potassium': 350, 'sodium': 600, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 40},
    'tortang talong': {'carbs': 8, 'fats': 15, 'protein': 10, 'calories': 210, 'potassium': 250, 'sodium': 400, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 15},
    'lugaw': {'carbs': 30, 'fats': 5, 'protein': 8, 'calories': 200, 'potassium': 100, 'sodium': 500, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 70}, # Rice porridge
    'arroz caldo': {'carbs': 30, 'fats': 8, 'protein': 15, 'calories': 250, 'potassium': 150, 'sodium': 600, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 70},
    'turon': {'carbs': 35, 'fats': 10, 'protein': 2, 'calories': 240, 'potassium': 150, 'sodium': 50, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 65},
    'halo-halo': {'carbs': 60, 'fats': 8, 'protein': 6, 'calories': 350, 'potassium': 200, 'sodium': 100, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 70},

    # Common Variations
    'steak': {'carbs': 0, 'fats': 20, 'protein': 25, 'calories': 280, 'potassium': 350, 'sodium': 60, 'saturated_fat': 8, 'trans_fat': 1, 'gi': 0},
    'roast chicken': {'carbs': 0, 'fats': 12, 'protein': 28, 'calories': 220, 'potassium': 250, 'sodium': 300, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 0},
    'grilled fish': {'carbs': 0, 'fats': 8, 'protein': 22, 'calories': 160, 'potassium': 350, 'sodium': 200, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 0},
    'salad': {'carbs': 5, 'fats': 10, 'protein': 2, 'calories': 120, 'potassium': 200, 'sodium': 150, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 20}, # Garden salad w/ dressing
    'caesar salad': {'carbs': 10, 'fats': 25, 'protein': 8, 'calories': 300, 'potassium': 250, 'sodium': 500, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 25},
    'soup': {'carbs': 10, 'fats': 2, 'protein': 4, 'calories': 80, 'potassium': 150, 'sodium': 600, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 40}, # Generic clear soup
    'mushroom soup': {'carbs': 12, 'fats': 10, 'protein': 4, 'calories': 150, 'potassium': 200, 'sodium': 700, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 45}, # Creamy
    'tomato soup': {'carbs': 15, 'fats': 4, 'protein': 2, 'calories': 100, 'potassium': 300, 'sodium': 600, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 45},

    # More Fruits/Veg/Nuts
    'strawberry': {'carbs': 8, 'fats': 0.3, 'protein': 0.7, 'calories': 32, 'potassium': 153, 'gi': 40},
    'blueberry': {'carbs': 14, 'fats': 0.3, 'protein': 0.7, 'calories': 57, 'potassium': 77, 'gi': 53},
    'raspberry': {'carbs': 12, 'fats': 0.7, 'protein': 1.2, 'calories': 52, 'potassium': 151, 'gi': 26}, # Low GI!
    'avocado': {'carbs': 9, 'fats': 15, 'protein': 2, 'calories': 160, 'potassium': 485, 'gi': 15},
    'cabbage': {'carbs': 6, 'fats': 0.1, 'protein': 1.3, 'calories': 25, 'potassium': 170, 'gi': 15},
    'kale': {'carbs': 9, 'fats': 0.9, 'protein': 4.3, 'calories': 49, 'potassium': 491, 'gi': 15},
    'cauliflower': {'carbs': 5, 'fats': 0.3, 'protein': 1.9, 'calories': 25, 'potassium': 299, 'gi': 15},
    'almonds': {'carbs': 22, 'fats': 49, 'protein': 21, 'calories': 579, 'potassium': 733, 'gi': 15},
    'peanuts': {'carbs': 16, 'fats': 49, 'protein': 26, 'calories': 567, 'potassium': 705, 'gi': 13},
    'cashews': {'carbs': 30, 'fats': 44, 'protein': 18, 'calories': 553, 'potassium': 660, 'gi': 25},
    'walnut': {'carbs': 14, 'fats': 65, 'protein': 15, 'calories': 654, 'potassium': 441, 'sodium': 2, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 15},
    'pecan': {'carbs': 14, 'fats': 72, 'protein': 9, 'calories': 691, 'potassium': 410, 'sodium': 0, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 10},
    'pistachio': {'carbs': 28, 'fats': 45, 'protein': 20, 'calories': 560, 'potassium': 1025, 'sodium': 1, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 15}, # High K!
    'hazelnut': {'carbs': 17, 'fats': 61, 'protein': 15, 'calories': 628, 'potassium': 680, 'sodium': 0, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 15},
    'macadamia': {'carbs': 14, 'fats': 76, 'protein': 8, 'calories': 718, 'potassium': 368, 'sodium': 5, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 10},
    
    # Local Snack & Nut Brands (PH/SG)
    'nagaraya': {'carbs': 46, 'fats': 25, 'protein': 12, 'calories': 457, 'potassium': 350, 'sodium': 450, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'nagaraya peanuts': {'carbs': 46, 'fats': 25, 'protein': 12, 'calories': 457, 'potassium': 350, 'sodium': 450, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'boy bawang': {'carbs': 65, 'fats': 18, 'protein': 9, 'calories': 460, 'potassium': 250, 'sodium': 750, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 70},
    'boy bawang corn nuts': {'carbs': 65, 'fats': 18, 'protein': 9, 'calories': 460, 'potassium': 250, 'sodium': 750, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 70},
    'sugo peanuts': {'carbs': 18, 'fats': 48, 'protein': 25, 'calories': 580, 'potassium': 650, 'sodium': 350, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 15},
    'growers peanuts': {'carbs': 18, 'fats': 48, 'protein': 25, 'calories': 580, 'potassium': 650, 'sodium': 350, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 15},
    'ding dong mixed nuts': {'carbs': 52, 'fats': 30, 'protein': 12, 'calories': 520, 'potassium': 450, 'sodium': 550, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 65},
    'camel peanuts': {'carbs': 16, 'fats': 49, 'protein': 26, 'calories': 567, 'potassium': 700, 'sodium': 350, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 15},
    'camel nuts': {'carbs': 16, 'fats': 49, 'protein': 26, 'calories': 567, 'potassium': 700, 'sodium': 350, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 15},
    'tong garden peanuts': {'carbs': 16, 'fats': 49, 'protein': 26, 'calories': 567, 'potassium': 700, 'sodium': 400, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 15},
    'tong garden nuts': {'carbs': 16, 'fats': 49, 'protein': 26, 'calories': 567, 'potassium': 700, 'sodium': 400, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 15},
    'tai sun nuts': {'carbs': 18, 'fats': 48, 'protein': 24, 'calories': 570, 'potassium': 680, 'sodium': 350, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 15},
    'tai sun peanuts': {'carbs': 18, 'fats': 48, 'protein': 24, 'calories': 570, 'potassium': 680, 'sodium': 350, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 15},
    'natures wonders baked almonds': {'carbs': 20, 'fats': 50, 'protein': 22, 'calories': 580, 'potassium': 730, 'sodium': 5, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 15},
    'natures wonders baked cashews': {'carbs': 30, 'fats': 45, 'protein': 18, 'calories': 560, 'potassium': 650, 'sodium': 5, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 25},

    # Desserts / Snacks
    'chocolate': {'carbs': 61, 'fats': 30, 'protein': 5, 'calories': 546, 'potassium': 372, 'gi': 49}, # Milk chocolate
    'dark chocolate': {'carbs': 46, 'fats': 43, 'protein': 8, 'calories': 598, 'potassium': 715, 'gi': 23},
    'snickers': {'carbs': 60, 'fats': 25, 'protein': 8, 'calories': 480, 'potassium': 300, 'sodium': 200, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 55}, # per 100g
    'twix': {'carbs': 65, 'fats': 24, 'protein': 5, 'calories': 500, 'potassium': 150, 'sodium': 200, 'saturated_fat': 14, 'trans_fat': 0, 'gi': 60}, # per 100g
    'mars bar': {'carbs': 70, 'fats': 17, 'protein': 4, 'calories': 450, 'potassium': 200, 'sodium': 180, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 65}, # per 100g
    'hersheys milk chocolate': {'carbs': 60, 'fats': 30, 'protein': 7, 'calories': 520, 'potassium': 350, 'sodium': 100, 'saturated_fat': 19, 'trans_fat': 0, 'gi': 55}, # per 100g
    'kitkat': {'carbs': 63, 'fats': 25, 'protein': 6, 'calories': 500, 'potassium': 280, 'sodium': 100, 'saturated_fat': 15, 'trans_fat': 0, 'gi': 60}, # per 100g
    'toblerone': {'carbs': 61, 'fats': 29, 'protein': 6, 'calories': 530, 'potassium': 350, 'sodium': 60, 'saturated_fat': 17, 'trans_fat': 0, 'gi': 60}, # per 100g
    'm&ms plain': {'carbs': 70, 'fats': 20, 'protein': 5, 'calories': 480, 'potassium': 200, 'sodium': 60, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 65}, # per 100g
    'm&ms peanut': {'carbs': 60, 'fats': 25, 'protein': 10, 'calories': 520, 'potassium': 300, 'sodium': 50, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 55}, # per 100g
    'skittles': {'carbs': 90, 'fats': 4, 'protein': 0, 'calories': 400, 'potassium': 0, 'sodium': 15, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 70}, # per 100g
    'cake': {'carbs': 50, 'fats': 15, 'protein': 4, 'calories': 350, 'potassium': 100, 'gi': 70}, # Sponge/Generic
    'cookie': {'carbs': 65, 'fats': 24, 'protein': 5, 'calories': 500, 'potassium': 100, 'gi': 75},
    'oreo': {'carbs': 70, 'fats': 20, 'protein': 5, 'calories': 480, 'potassium': 150, 'sodium': 500, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 75}, # per 100g
    'chips ahoy': {'carbs': 65, 'fats': 22, 'protein': 5, 'calories': 475, 'potassium': 150, 'sodium': 350, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 75}, # per 100g
    'ritz crackers': {'carbs': 60, 'fats': 25, 'protein': 7, 'calories': 500, 'potassium': 150, 'sodium': 750, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 70}, # per 100g
    'biscoff cookies': {'carbs': 73, 'fats': 19, 'protein': 5, 'calories': 484, 'potassium': 150, 'sodium': 370, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 75}, # per 100g
    'nutella': {'carbs': 58, 'fats': 31, 'protein': 5, 'calories': 539, 'potassium': 400, 'sodium': 40, 'saturated_fat': 11, 'trans_fat': 0, 'gi': 55}, # per 100g spread
    'pop tarts': {'carbs': 70, 'fats': 10, 'protein': 4, 'calories': 380, 'potassium': 100, 'sodium': 350, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 75}, # per 100g (varies by flavor)
    'milano cookies': {'carbs': 65, 'fats': 25, 'protein': 5, 'calories': 500, 'potassium': 150, 'sodium': 200, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 70}, # per 100g
    'gummy bears': {'carbs': 78, 'fats': 0, 'protein': 6, 'calories': 350, 'potassium': 0, 'sodium': 20, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 80}, # per 100g
    'sour patch kids': {'carbs': 90, 'fats': 0, 'protein': 0, 'calories': 360, 'potassium': 0, 'sodium': 40, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 80}, # per 100g
    'starburst': {'carbs': 85, 'fats': 8, 'protein': 0, 'calories': 390, 'potassium': 0, 'sodium': 10, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 80}, # per 100g
    'twizzlers': {'carbs': 80, 'fats': 1, 'protein': 3, 'calories': 340, 'potassium': 0, 'sodium': 250, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 75}, # per 100g
    'ice cream': {'carbs': 24, 'fats': 11, 'protein': 4, 'calories': 207, 'potassium': 199, 'gi': 60},

    # Fast Food & Restaurants
    'mcdonalds big mac': {'carbs': 46, 'fats': 30, 'protein': 25, 'calories': 550, 'potassium': 390, 'sodium': 1010, 'saturated_fat': 11, 'trans_fat': 1, 'gi': 65},
    'big mac': {'carbs': 46, 'fats': 30, 'protein': 25, 'calories': 550, 'potassium': 390, 'sodium': 1010, 'saturated_fat': 11, 'trans_fat': 1, 'gi': 65},
    'mcdonalds cheeseburger': {'carbs': 33, 'fats': 14, 'protein': 15, 'calories': 300, 'potassium': 200, 'sodium': 720, 'saturated_fat': 6, 'trans_fat': 0.5, 'gi': 65},
    'mcdonalds fries': {'carbs': 43, 'fats': 15, 'protein': 4, 'calories': 320, 'potassium': 450, 'sodium': 260, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 75},
    'mcdonalds chicken nuggets': {'carbs': 16, 'fats': 17, 'protein': 14, 'calories': 280, 'potassium': 300, 'sodium': 450, 'saturated_fat': 2.5, 'trans_fat': 0, 'gi': 60}, # 6 pc
    
    'burger king whopper': {'carbs': 49, 'fats': 40, 'protein': 28, 'calories': 650, 'potassium': 400, 'sodium': 980, 'saturated_fat': 11, 'trans_fat': 1.5, 'gi': 60},
    'whopper': {'carbs': 49, 'fats': 40, 'protein': 28, 'calories': 650, 'potassium': 400, 'sodium': 980, 'saturated_fat': 11, 'trans_fat': 1.5, 'gi': 60},
    'burger king fries': {'carbs': 48, 'fats': 17, 'protein': 4, 'calories': 380, 'potassium': 400, 'sodium': 570, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 75},
    
    'kfc original recipe chicken': {'carbs': 11, 'fats': 21, 'protein': 19, 'calories': 320, 'potassium': 200, 'sodium': 1130, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 40}, # 1 breast
    'kfc crispy chicken': {'carbs': 15, 'fats': 24, 'protein': 21, 'calories': 390, 'potassium': 250, 'sodium': 1190, 'saturated_fat': 4.5, 'trans_fat': 0, 'gi': 45},
    'kfc mashed potatoes': {'carbs': 15, 'fats': 4, 'protein': 2, 'calories': 120, 'potassium': 200, 'sodium': 530, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 80},
    
    'wendys baconator': {'carbs': 41, 'fats': 66, 'protein': 57, 'calories': 960, 'potassium': 500, 'sodium': 1540, 'saturated_fat': 27, 'trans_fat': 3, 'gi': 60},
    'wendys frosty': {'carbs': 53, 'fats': 8, 'protein': 8, 'calories': 310, 'potassium': 500, 'sodium': 160, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    
    'subway bmt': {'carbs': 46, 'fats': 16, 'protein': 20, 'calories': 410, 'potassium': 350, 'sodium': 1260, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 55}, # 6 inch
    'subway tuna': {'carbs': 44, 'fats': 25, 'protein': 19, 'calories': 470, 'potassium': 300, 'sodium': 790, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 55}, # 6 inch
    
    'pizza hut pepperoni pizza': {'carbs': 32, 'fats': 12, 'protein': 12, 'calories': 280, 'potassium': 150, 'sodium': 650, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 60}, # 1 slice medium
    'dominos pepperoni pizza': {'carbs': 34, 'fats': 13, 'protein': 12, 'calories': 300, 'potassium': 160, 'sodium': 680, 'saturated_fat': 5.5, 'trans_fat': 0, 'gi': 60}, # 1 slice medium

    # Convenience Stores (7-Eleven, Cheers) & Snacks
    '7-eleven slurpee': {'carbs': 34, 'fats': 0, 'protein': 0, 'calories': 130, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 85}, # Medium
    'slurpee': {'carbs': 34, 'fats': 0, 'protein': 0, 'calories': 130, 'potassium': 0, 'sodium': 10, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 85},
    '7-eleven big gulp': {'carbs': 52, 'fats': 0, 'protein': 0, 'calories': 200, 'potassium': 0, 'sodium': 55, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65}, # Regular Cola
    'big gulp': {'carbs': 52, 'fats': 0, 'protein': 0, 'calories': 200, 'potassium': 0, 'sodium': 55, 'saturated_fat': 0, 'trans_fat': 0, 'gi': 65},
    
    '7-eleven hotdog': {'carbs': 24, 'fats': 25, 'protein': 12, 'calories': 350, 'potassium': 150, 'sodium': 850, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 65}, # With bun
    'big bite hotdog': {'carbs': 24, 'fats': 25, 'protein': 12, 'calories': 350, 'potassium': 150, 'sodium': 850, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 65},
    '7-eleven siopao': {'carbs': 48, 'fats': 9, 'protein': 12, 'calories': 320, 'potassium': 100, 'sodium': 450, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 75}, # Asado/Bola-bola
    'siopao': {'carbs': 48, 'fats': 9, 'protein': 12, 'calories': 320, 'potassium': 100, 'sodium': 450, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 75},
    
    '7-eleven sandwich': {'carbs': 35, 'fats': 15, 'protein': 14, 'calories': 330, 'potassium': 180, 'sodium': 650, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 55}, # Tuna/Egg generic
    'cheers sandwich': {'carbs': 35, 'fats': 15, 'protein': 14, 'calories': 330, 'potassium': 180, 'sodium': 650, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 55},
    'onigiri': {'carbs': 35, 'fats': 2, 'protein': 4, 'calories': 180, 'potassium': 60, 'sodium': 300, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 80}, # Salmon/Tuna mayo
    '7-eleven onigiri': {'carbs': 35, 'fats': 2, 'protein': 4, 'calories': 180, 'potassium': 60, 'sodium': 300, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 80},
    
    'cup noodles': {'carbs': 45, 'fats': 14, 'protein': 7, 'calories': 330, 'potassium': 150, 'sodium': 1200, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65}, # Generic instant noodles
    'nissin cup noodles': {'carbs': 45, 'fats': 14, 'protein': 7, 'calories': 330, 'potassium': 150, 'sodium': 1200, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65},
    'maggi mee': {'carbs': 52, 'fats': 15, 'protein': 8, 'calories': 380, 'potassium': 180, 'sodium': 1500, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 65},
    
    'potato chips': {'carbs': 15, 'fats': 10, 'protein': 2, 'calories': 160, 'potassium': 350, 'sodium': 170, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 75}, # 1 oz / 28g serving
    'lays potato chips': {'carbs': 15, 'fats': 10, 'protein': 2, 'calories': 160, 'potassium': 350, 'sodium': 170, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 75},
    'lays sour cream and onion': {'carbs': 15, 'fats': 10, 'protein': 2, 'calories': 160, 'potassium': 350, 'sodium': 160, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 75},
    'lays barbecue': {'carbs': 15, 'fats': 10, 'protein': 2, 'calories': 150, 'potassium': 340, 'sodium': 150, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 75},
    'pringles original': {'carbs': 15, 'fats': 9, 'protein': 1, 'calories': 150, 'potassium': 100, 'sodium': 150, 'saturated_fat': 2.5, 'trans_fat': 0, 'gi': 70}, # 1 oz / ~15 crisps
    'pringles sour cream and onion': {'carbs': 15, 'fats': 9, 'protein': 1, 'calories': 150, 'potassium': 110, 'sodium': 130, 'saturated_fat': 2.5, 'trans_fat': 0, 'gi': 70},
    'doritos nacho cheese': {'carbs': 18, 'fats': 8, 'protein': 2, 'calories': 150, 'potassium': 50, 'sodium': 210, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 70}, # 1 oz / 28g
    'doritos cool ranch': {'carbs': 18, 'fats': 8, 'protein': 2, 'calories': 150, 'potassium': 50, 'sodium': 180, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 70},
    'cheetos crunchy': {'carbs': 15, 'fats': 10, 'protein': 2, 'calories': 160, 'potassium': 40, 'sodium': 250, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 70}, # 1 oz
    'cheetos flamin hot': {'carbs': 15, 'fats': 11, 'protein': 1, 'calories': 170, 'potassium': 40, 'sodium': 250, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 70},
    'tostitos tortilla chips': {'carbs': 19, 'fats': 7, 'protein': 2, 'calories': 140, 'potassium': 40, 'sodium': 115, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 65}, # 1 oz
    'ruffles original': {'carbs': 15, 'fats': 10, 'protein': 2, 'calories': 160, 'potassium': 350, 'sodium': 160, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 75},
    'ruffles cheddar and sour cream': {'carbs': 15, 'fats': 10, 'protein': 2, 'calories': 160, 'potassium': 320, 'sodium': 180, 'saturated_fat': 1.5, 'trans_fat': 0, 'gi': 75},

    # Philippine Fast Food & Restaurants
    # Jollibee
    'jollibee chickenjoy': {'carbs': 11, 'fats': 22, 'protein': 20, 'calories': 320, 'potassium': 210, 'sodium': 850, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 50}, # 1 pc with skin
    'chickenjoy': {'carbs': 11, 'fats': 22, 'protein': 20, 'calories': 320, 'potassium': 210, 'sodium': 850, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 50},
    'jollibee spicy chickenjoy': {'carbs': 12, 'fats': 24, 'protein': 20, 'calories': 340, 'potassium': 220, 'sodium': 950, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 50},
    'jollibee jolly spaghetti': {'carbs': 55, 'fats': 12, 'protein': 14, 'calories': 380, 'potassium': 350, 'sodium': 900, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'jolly spaghetti': {'carbs': 55, 'fats': 12, 'protein': 14, 'calories': 380, 'potassium': 350, 'sodium': 900, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'jollibee yum burger': {'carbs': 30, 'fats': 14, 'protein': 12, 'calories': 290, 'potassium': 180, 'sodium': 480, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'yum burger': {'carbs': 30, 'fats': 14, 'protein': 12, 'calories': 290, 'potassium': 180, 'sodium': 480, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 65},
    'jollibee burger steak': {'carbs': 35, 'fats': 18, 'protein': 14, 'calories': 350, 'potassium': 250, 'sodium': 850, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 70}, # 1 pc with rice
    'jollibee peach mango pie': {'carbs': 34, 'fats': 14, 'protein': 3, 'calories': 270, 'potassium': 120, 'sodium': 220, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 75},
    'peach mango pie': {'carbs': 34, 'fats': 14, 'protein': 3, 'calories': 270, 'potassium': 120, 'sodium': 220, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 75},
    
    # Mang Inasal
    'mang inasal paa': {'carbs': 0, 'fats': 24, 'protein': 38, 'calories': 370, 'potassium': 350, 'sodium': 950, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 0}, # Chicken leg quarter (no rice)
    'mang inasal pecho': {'carbs': 0, 'fats': 22, 'protein': 45, 'calories': 380, 'potassium': 400, 'sodium': 1050, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 0}, # Chicken breast quarter (no rice)
    'mang inasal pork bbq': {'carbs': 12, 'fats': 18, 'protein': 15, 'calories': 270, 'potassium': 250, 'sodium': 600, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 45}, # 2 sticks (no rice)
    'mang inasal halo halo': {'carbs': 85, 'fats': 12, 'protein': 10, 'calories': 480, 'potassium': 450, 'sodium': 250, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 80}, # Regular size
    
    # Chowking
    'chowking chao fan': {'carbs': 65, 'fats': 15, 'protein': 14, 'calories': 450, 'potassium': 280, 'sodium': 850, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 75}, # Pork Chao Fan
    'chowking siomai': {'carbs': 15, 'fats': 18, 'protein': 14, 'calories': 280, 'potassium': 150, 'sodium': 600, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 55}, # 4 pcs pork
    'chowking wanton mami': {'carbs': 55, 'fats': 12, 'protein': 16, 'calories': 390, 'potassium': 320, 'sodium': 1800, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65},
    'chowking halo halo': {'carbs': 90, 'fats': 14, 'protein': 12, 'calories': 520, 'potassium': 500, 'sodium': 280, 'saturated_fat': 9, 'trans_fat': 0, 'gi': 80},
    
    # Greenwich & Max's
    'greenwich hawaiian overload': {'carbs': 38, 'fats': 14, 'protein': 15, 'calories': 330, 'potassium': 200, 'sodium': 750, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 65}, # 1 slice Double
    'greenwich lasagna supreme': {'carbs': 42, 'fats': 18, 'protein': 20, 'calories': 410, 'potassium': 350, 'sodium': 900, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 55},
    'maxs fried chicken': {'carbs': 2, 'fats': 25, 'protein': 30, 'calories': 350, 'potassium': 300, 'sodium': 800, 'saturated_fat': 7, 'trans_fat': 0, 'gi': 0}, # Half chicken (no rice)

    # SM Mall of Asia / Major PH Mall Staples
    # Shakey's
    'shakeys thin crust pizza': {'carbs': 18, 'fats': 8, 'protein': 10, 'calories': 180, 'potassium': 120, 'sodium': 400, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 60}, # 1 slice Manager's Choice
    'shakeys mojos': {'carbs': 35, 'fats': 18, 'protein': 4, 'calories': 320, 'potassium': 600, 'sodium': 850, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 75}, # 1 serving
    'shakeys chicken \'n\' mojos': {'carbs': 40, 'fats': 35, 'protein': 25, 'calories': 580, 'potassium': 750, 'sodium': 1300, 'saturated_fat': 8, 'trans_fat': 0, 'gi': 65}, # 1 pc chicken + mojos

    # Yellow Cab
    'yellow cab new york classic': {'carbs': 35, 'fats': 15, 'protein': 18, 'calories': 350, 'potassium': 200, 'sodium': 800, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 60}, # 1 slice 14"
    'yellow cab charlie chan': {'carbs': 55, 'fats': 18, 'protein': 15, 'calories': 440, 'potassium': 300, 'sodium': 1100, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65}, # 1 serving pasta

    # Kenny Rogers Roasters
    'kenny rogers roasted chicken': {'carbs': 2, 'fats': 15, 'protein': 35, 'calories': 280, 'potassium': 350, 'sodium': 750, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 0}, # 1/4 chicken
    'kenny rogers corn muffin': {'carbs': 25, 'fats': 6, 'protein': 3, 'calories': 160, 'potassium': 80, 'sodium': 200, 'saturated_fat': 2, 'trans_fat': 0, 'gi': 65},
    
    # BonChon / Korean Fried Chicken
    'bonchon soy garlic chicken': {'carbs': 18, 'fats': 20, 'protein': 22, 'calories': 340, 'potassium': 250, 'sodium': 950, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 60}, # 2 pcs wings
    'bonchon bibimbowl': {'carbs': 65, 'fats': 12, 'protein': 20, 'calories': 450, 'potassium': 400, 'sodium': 850, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 55},

    # Manam (Filipino Comfort)
    'manam house crispy sisig': {'carbs': 5, 'fats': 35, 'protein': 20, 'calories': 410, 'potassium': 250, 'sodium': 850, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 20}, # 1 serving
    'manam watermelon sinigang': {'carbs': 15, 'fats': 18, 'protein': 22, 'calories': 310, 'potassium': 600, 'sodium': 1200, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 30}, # 1 bowl (pork)

    # Ooma (Modern Japanese)
    'ooma aburi maki': {'carbs': 45, 'fats': 15, 'protein': 12, 'calories': 360, 'potassium': 250, 'sodium': 650, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 60}, # 1 roll
    'ooma hanger steak': {'carbs': 10, 'fats': 25, 'protein': 35, 'calories': 400, 'potassium': 450, 'sodium': 700, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 20},

    # Tim Ho Wan (Dim Sum)
    'tim ho wan pork bun': {'carbs': 28, 'fats': 12, 'protein': 8, 'calories': 250, 'potassium': 100, 'sodium': 350, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 70}, # 1 baked bun
    'tim ho wan hakaw': {'carbs': 12, 'fats': 4, 'protein': 8, 'calories': 120, 'potassium': 80, 'sodium': 300, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 55}, # 3 pcs
    'tim ho wan siomai': {'carbs': 10, 'fats': 15, 'protein': 12, 'calories': 220, 'potassium': 120, 'sodium': 450, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 50}, # 3 pcs
    'hakaw': {'carbs': 4, 'fats': 1.5, 'protein': 2.5, 'calories': 40, 'potassium': 25, 'sodium': 100, 'saturated_fat': 0.5, 'trans_fat': 0, 'gi': 55}, # 1 pc shrimp dumpling
    
    # Din Tai Fung
    'din tai fung xiao long bao': {'carbs': 15, 'fats': 10, 'protein': 8, 'calories': 180, 'potassium': 90, 'sodium': 450, 'saturated_fat': 3, 'trans_fat': 0, 'gi': 55}, # 3 pcs
    'xiao long bao': {'carbs': 5, 'fats': 3.5, 'protein': 2.5, 'calories': 60, 'potassium': 30, 'sodium': 150, 'saturated_fat': 1, 'trans_fat': 0, 'gi': 55}, # 1 pc
    'din tai fung pork chop': {'carbs': 15, 'fats': 22, 'protein': 28, 'calories': 370, 'potassium': 350, 'sodium': 900, 'saturated_fat': 6, 'trans_fat': 0, 'gi': 45},

    # Pepper Lunch
    'pepper lunch beef pepper rice': {'carbs': 65, 'fats': 25, 'protein': 20, 'calories': 560, 'potassium': 300, 'sodium': 850, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 75},
    'beef pepper rice': {'carbs': 65, 'fats': 25, 'protein': 20, 'calories': 560, 'potassium': 300, 'sodium': 850, 'saturated_fat': 10, 'trans_fat': 0, 'gi': 75},
    
    # Ramen Nagi / Mendokoro (Generic Tonkotsu)
    'tonkotsu ramen': {'carbs': 75, 'fats': 30, 'protein': 25, 'calories': 670, 'potassium': 500, 'sodium': 1800, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 65}, # 1 bowl
    'ramen nagi butao': {'carbs': 75, 'fats': 35, 'protein': 28, 'calories': 720, 'potassium': 550, 'sodium': 2000, 'saturated_fat': 14, 'trans_fat': 0, 'gi': 65},

    # Conti's
    'contis mango bravo': {'carbs': 55, 'fats': 25, 'protein': 6, 'calories': 470, 'potassium': 180, 'sodium': 200, 'saturated_fat': 12, 'trans_fat': 0.5, 'gi': 75}, # 1 slice
    'mango bravo': {'carbs': 55, 'fats': 25, 'protein': 6, 'calories': 470, 'potassium': 180, 'sodium': 200, 'saturated_fat': 12, 'trans_fat': 0.5, 'gi': 75},

    # Mary Grace
    'mary grace ensaymada': {'carbs': 45, 'fats': 22, 'protein': 8, 'calories': 410, 'potassium': 120, 'sodium': 350, 'saturated_fat': 12, 'trans_fat': 0.5, 'gi': 70}, # 1 large piece
    'mary grace cheese roll': {'carbs': 35, 'fats': 18, 'protein': 6, 'calories': 320, 'potassium': 90, 'sodium': 250, 'saturated_fat': 9, 'trans_fat': 0.5, 'gi': 70},

    # Panda Express
    'panda express orange chicken': {'carbs': 51, 'fats': 23, 'protein': 18, 'calories': 490, 'potassium': 280, 'sodium': 820, 'saturated_fat': 4, 'trans_fat': 0, 'gi': 65}, # 1 serving
    'chow mein': {'carbs': 74, 'fats': 20, 'protein': 13, 'calories': 510, 'potassium': 270, 'sodium': 860, 'saturated_fat': 3.5, 'trans_fat': 0, 'gi': 65},

    # Potato Corner
    'potato corner cheese fries': {'carbs': 55, 'fats': 22, 'protein': 5, 'calories': 440, 'potassium': 550, 'sodium': 800, 'saturated_fat': 5, 'trans_fat': 0, 'gi': 75}, # Mega size
    'potato corner bbq fries': {'carbs': 58, 'fats': 22, 'protein': 5, 'calories': 450, 'potassium': 550, 'sodium': 850, 'saturated_fat': 4.5, 'trans_fat': 0, 'gi': 75}, # Mega size

    # S&R NY Style Pizza
    'snr cheese pizza': {'carbs': 65, 'fats': 28, 'protein': 25, 'calories': 610, 'potassium': 300, 'sodium': 1400, 'saturated_fat': 12, 'trans_fat': 0, 'gi': 60}, # 1 massive slice
    'snr pepperoni pizza': {'carbs': 66, 'fats': 34, 'protein': 28, 'calories': 680, 'potassium': 350, 'sodium': 1600, 'saturated_fat': 15, 'trans_fat': 0, 'gi': 60}, # 1 massive slice

    "patatim": {
        "name": "patatim",
        "calories": 122,
        "carbs": 22.97,
        "protein": 2.7,
        "fats": 2.7,
        "potassium": 0,
        "sodium": 1135.0,
        "saturated_fat": 1.35,
        "trans_fat": 0,
        "gi": 0
    },
    "1 jollibee burger": {"carbs": 30.0, "fats": 14.0, "protein": 16.0, "calories": 295.0, "potassium": 250.0, "sodium": 450.0, "saturated_fat": 5.0, "trans_fat": 0.5, "gi": 66.0},
    "2 eggs": {"carbs": 54.0, "fats": 21.0, "protein": 5.5, "calories": 419.0, "potassium": 0.0, "sodium": 284.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 0.0},
    "0.5 k beef": {"carbs": 0.0, "fats": 15.0, "protein": 26.0, "calories": 250.0, "potassium": 318.0, "sodium": 0.0, "saturated_fat": 0.0, "trans_fat": 0.0, "gi": 0.0},
    "pear barley": {"carbs": 28.0, "fats": 0.4, "protein": 2.3, "calories": 123.0, "potassium": 93.0, "sodium": 0.0, "saturated_fat": 0.0, "trans_fat": 0.0, "gi": 0.0},
    "bow of tinola": {"carbs": 5.0, "fats": 8.0, "protein": 25.0, "calories": 200.0, "potassium": 300.0, "sodium": 600.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 0.0},
    "1 cup quinoa": {"carbs": 21.0, "fats": 1.9, "protein": 4.4, "calories": 120.0, "potassium": 172.0, "sodium": 0.0, "saturated_fat": 0.0, "trans_fat": 0.0, "gi": 53.0},
    "longaniza": {"carbs": 10.0, "fats": 25.0, "protein": 12.0, "calories": 320.0, "potassium": 200.0, "sodium": 900.0, "saturated_fat": 10.0, "trans_fat": 0.0, "gi": 50.0},
    "unicorn burger": {"carbs": 30.0, "fats": 14.0, "protein": 16.0, "calories": 295.0, "potassium": 250.0, "sodium": 450.0, "saturated_fat": 5.0, "trans_fat": 0.5, "gi": 66.0},
    "patatim 1 cup": {"carbs": 22.97, "fats": 2.7, "protein": 2.7, "calories": 122.0, "potassium": 0.0, "sodium": 1135.0, "saturated_fat": 1.35, "trans_fat": 0.0, "gi": 0.0},
    "longanixa": {"carbs": 10.0, "fats": 25.0, "protein": 12.0, "calories": 320.0, "potassium": 200.0, "sodium": 900.0, "saturated_fat": 10.0, "trans_fat": 0.0, "gi": 50.0},
    "cup white rice": {"carbs": 28.0, "fats": 0.3, "protein": 2.7, "calories": 130.0, "potassium": 35.0, "sodium": 0.0, "saturated_fat": 0.0, "trans_fat": 0.0, "gi": 73.0},
    "eggs": {"carbs": 1.1, "fats": 11.0, "protein": 13.0, "calories": 155.0, "potassium": 126.0, "sodium": 0.0, "saturated_fat": 0.0, "trans_fat": 0.0, "gi": 0.0},
    "blueberries": {"carbs": 14.0, "fats": 0.3, "protein": 0.7, "calories": 57.0, "potassium": 77.0, "sodium": 0.0, "saturated_fat": 0.0, "trans_fat": 0.0, "gi": 53.0},
    "whole orange": {"carbs": 12.0, "fats": 0.1, "protein": 0.9, "calories": 47.0, "potassium": 181.0, "sodium": 0.0, "saturated_fat": 0.0, "trans_fat": 0.0, "gi": 40.0},
    "jollibee french fries": {"carbs": 41.0, "fats": 15.0, "protein": 3.4, "calories": 312.0, "potassium": 579.0, "sodium": 210.0, "saturated_fat": 2.3, "trans_fat": 0.1, "gi": 75.0},
    "pepperoni pizza and a root beer": {"carbs": 33.0, "fats": 10.0, "protein": 11.0, "calories": 266.0, "potassium": 170.0, "sodium": 600.0, "saturated_fat": 4.5, "trans_fat": 0.2, "gi": 60.0},
    "gatas": {"carbs": 56.140350877193, "fats": 12.280701754386, "protein": 5.26315789473684, "calories": 350.877192982456, "potassium": 0.087719298245614, "sodium": 263.15789473684197, "saturated_fat": 5.26315789473684, "trans_fat": 0.0, "gi": 0.0},
    "donut": {"carbs": 56.0, "fats": 20.0, "protein": 11.0, "calories": 463.0, "potassium": 0.0, "sodium": 600.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 0.0},
    "jollibee burger": {"carbs": 30.0, "fats": 14.0, "protein": 16.0, "calories": 295.0, "potassium": 250.0, "sodium": 450.0, "saturated_fat": 5.0, "trans_fat": 0.5, "gi": 66.0},
    "sinangag": {"carbs": 35.0, "fats": 7.0, "protein": 4.0, "calories": 220.0, "potassium": 50.0, "sodium": 180.0, "saturated_fat": 1.5, "trans_fat": 0.0, "gi": 80.0},
    "kikiam": {"carbs": 12.0, "fats": 18.0, "protein": 10.0, "calories": 250.0, "potassium": 150.0, "sodium": 300.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 55.0},
    
    # Singaporean Fish & Seafood
    "barramundi": {"carbs": 0.0, "fats": 2.5, "protein": 20.0, "calories": 105.0, "potassium": 300.0, "sodium": 70.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0}, # 100g raw (Asian seabass)
    "threadfin": {"carbs": 0.0, "fats": 1.5, "protein": 21.0, "calories": 100.0, "potassium": 320.0, "sodium": 65.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0}, # 100g raw (Ngoh Hiang fish)
    "batang": {"carbs": 0.0, "fats": 4.5, "protein": 19.0, "calories": 120.0, "potassium": 350.0, "sodium": 95.0, "saturated_fat": 1.2, "trans_fat": 0.0, "gi": 0.0}, # 100g raw (Spanish Mackerel)
    "mackerel": {"carbs": 0.0, "fats": 4.5, "protein": 19.0, "calories": 120.0, "potassium": 350.0, "sodium": 95.0, "saturated_fat": 1.2, "trans_fat": 0.0, "gi": 0.0}, 
    "pomfret": {"carbs": 0.0, "fats": 3.0, "protein": 18.0, "calories": 105.0, "potassium": 300.0, "sodium": 80.0, "saturated_fat": 1.0, "trans_fat": 0.0, "gi": 0.0}, # 100g raw
    "ikan bilis": {"carbs": 0.0, "fats": 5.0, "protein": 35.0, "calories": 190.0, "potassium": 250.0, "sodium": 1800.0, "saturated_fat": 1.5, "trans_fat": 0.0, "gi": 0.0}, # 100g dried anchovies
    "stingray": {"carbs": 0.0, "fats": 2.0, "protein": 17.0, "calories": 90.0, "potassium": 220.0, "sodium": 400.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0}, # 100g raw

    # Singaporean Seafood Dishes
    "sambal stingray": {"carbs": 8.0, "fats": 22.0, "protein": 30.0, "calories": 360.0, "potassium": 450.0, "sodium": 950.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 40.0}, # 1 serving
    "bbq stingray": {"carbs": 8.0, "fats": 22.0, "protein": 30.0, "calories": 360.0, "potassium": 450.0, "sodium": 950.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 40.0},
    "singapore chili crab": {"carbs": 25.0, "fats": 20.0, "protein": 22.0, "calories": 370.0, "potassium": 400.0, "sodium": 1400.0, "saturated_fat": 4.5, "trans_fat": 0.0, "gi": 50.0}, # 1 serving (sauce+meat)
    "black pepper crab": {"carbs": 12.0, "fats": 25.0, "protein": 24.0, "calories": 380.0, "potassium": 450.0, "sodium": 1100.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 35.0}, # 1 serving
    "cereal prawn": {"carbs": 22.0, "fats": 28.0, "protein": 18.0, "calories": 420.0, "potassium": 280.0, "sodium": 850.0, "saturated_fat": 12.0, "trans_fat": 0.5, "gi": 65.0}, # 1 serving
    " salted egg yolk crab": {"carbs": 15.0, "fats": 35.0, "protein": 22.0, "calories": 460.0, "potassium": 380.0, "sodium": 1300.0, "saturated_fat": 15.0, "trans_fat": 0.5, "gi": 45.0}, # 1 serving
    "fish head curry": {"carbs": 15.0, "fats": 30.0, "protein": 25.0, "calories": 430.0, "potassium": 550.0, "sodium": 900.0, "saturated_fat": 18.0, "trans_fat": 0.0, "gi": 40.0}, # 1 bowl
    "sliced fish soup": {"carbs": 10.0, "fats": 8.0, "protein": 22.0, "calories": 200.0, "potassium": 450.0, "sodium": 850.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 35.0}, # 1 bowl (clear)

    # Singaporean Ice Cream & Sweets
    "walls ice cream": {"carbs": 16.0, "fats": 7.0, "protein": 2.0, "calories": 130.0, "potassium": 150.0, "sodium": 50.0, "saturated_fat": 4.5, "trans_fat": 0.0, "gi": 65.0}, # 1/2 cup generic
    "wall's ice cream": {"carbs": 16.0, "fats": 7.0, "protein": 2.0, "calories": 130.0, "potassium": 150.0, "sodium": 50.0, "saturated_fat": 4.5, "trans_fat": 0.0, "gi": 65.0},
    "walls magnum": {"carbs": 26.0, "fats": 18.0, "protein": 3.0, "calories": 270.0, "potassium": 200.0, "sodium": 65.0, "saturated_fat": 12.0, "trans_fat": 0.0, "gi": 65.0}, # 1 stick classic
    "uncle ice cream": {"carbs": 42.0, "fats": 12.0, "protein": 5.0, "calories": 300.0, "potassium": 180.0, "sodium": 200.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 70.0}, # 1 block ice cream in bread/wafer
    "ice cream uncle bread": {"carbs": 42.0, "fats": 12.0, "protein": 5.0, "calories": 300.0, "potassium": 180.0, "sodium": 200.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 70.0}, # 1 block ice cream in bread
    "ice cream wafer block": {"carbs": 30.0, "fats": 10.0, "protein": 4.0, "calories": 220.0, "potassium": 150.0, "sodium": 120.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 75.0}, # 1 block in wafer
    "bengawan solo pandan cake": {"carbs": 35.0, "fats": 15.0, "protein": 4.0, "calories": 290.0, "potassium": 100.0, "sodium": 180.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 70.0}, # 1 slice
    "pandan chiffon cake": {"carbs": 35.0, "fats": 15.0, "protein": 4.0, "calories": 290.0, "potassium": 100.0, "sodium": 180.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 70.0}, # 1 slice
    "bengawan solo kueh lapis": {"carbs": 45.0, "fats": 35.0, "protein": 6.0, "calories": 520.0, "potassium": 150.0, "sodium": 280.0, "saturated_fat": 20.0, "trans_fat": 0.5, "gi": 65.0}, # 1 slice (very rich)
    "kueh lapis": {"carbs": 45.0, "fats": 35.0, "protein": 6.0, "calories": 520.0, "potassium": 150.0, "sodium": 280.0, "saturated_fat": 20.0, "trans_fat": 0.5, "gi": 65.0}, # 1 slice
    "bengawan solo ondeh ondeh": {"carbs": 30.0, "fats": 5.0, "protein": 2.0, "calories": 170.0, "potassium": 80.0, "sodium": 45.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 80.0}, # 3 pieces
    "ondeh ondeh": {"carbs": 30.0, "fats": 5.0, "protein": 2.0, "calories": 170.0, "potassium": 80.0, "sodium": 45.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 80.0}, # 3 pieces
    
    # Ice Cream Brands
    "selecta ice cream": {"carbs": 16.0, "fats": 7.0, "protein": 2.0, "calories": 130.0, "potassium": 150.0, "sodium": 50.0, "saturated_fat": 4.5, "trans_fat": 0.0, "gi": 65.0}, # 1/2 cup generic
    "selecta double dutch": {"carbs": 18.0, "fats": 8.0, "protein": 2.5, "calories": 150.0, "potassium": 160.0, "sodium": 60.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 65.0}, # 1/2 cup
    "selecta cookies and cream": {"carbs": 17.0, "fats": 7.5, "protein": 2.5, "calories": 145.0, "potassium": 140.0, "sodium": 80.0, "saturated_fat": 4.5, "trans_fat": 0.0, "gi": 65.0}, # 1/2 cup
    "selecta rocky road": {"carbs": 19.0, "fats": 8.0, "protein": 3.0, "calories": 160.0, "potassium": 170.0, "sodium": 65.0, "saturated_fat": 4.5, "trans_fat": 0.0, "gi": 65.0}, # 1/2 cup
    "selecta cornetto": {"carbs": 32.0, "fats": 14.0, "protein": 3.0, "calories": 260.0, "potassium": 200.0, "sodium": 120.0, "saturated_fat": 9.0, "trans_fat": 0.0, "gi": 70.0}, # 1 cone
    "selecta magnum": {"carbs": 26.0, "fats": 18.0, "protein": 3.0, "calories": 270.0, "potassium": 200.0, "sodium": 65.0, "saturated_fat": 12.0, "trans_fat": 0.0, "gi": 65.0}, # 1 stick classic
    "magnolia ice cream": {"carbs": 16.0, "fats": 7.0, "protein": 2.0, "calories": 130.0, "potassium": 150.0, "sodium": 50.0, "saturated_fat": 4.5, "trans_fat": 0.0, "gi": 65.0}, # 1/2 cup generic
    "magnolia ube quesong puti": {"carbs": 18.0, "fats": 8.5, "protein": 3.0, "calories": 160.0, "potassium": 150.0, "sodium": 110.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 65.0}, # 1/2 cup
    "magnolia avocado macchiato": {"carbs": 17.0, "fats": 8.0, "protein": 2.0, "calories": 150.0, "potassium": 180.0, "sodium": 60.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 60.0}, # 1/2 cup
    "arce dairy mantecado": {"carbs": 15.0, "fats": 10.0, "protein": 3.0, "calories": 160.0, "potassium": 140.0, "sodium": 60.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 55.0}, # 1/2 cup (carabao milk based)
    "arce dairy ube": {"carbs": 16.0, "fats": 10.0, "protein": 3.0, "calories": 165.0, "potassium": 160.0, "sodium": 55.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 55.0}, # 1/2 cup
    "arce dairy avocado": {"carbs": 14.0, "fats": 11.0, "protein": 3.0, "calories": 160.0, "potassium": 200.0, "sodium": 50.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 50.0}, # 1/2 cup
    "dq blizzard": {"carbs": 85.0, "fats": 20.0, "protein": 12.0, "calories": 580.0, "potassium": 450.0, "sodium": 350.0, "saturated_fat": 12.0, "trans_fat": 0.5, "gi": 75.0}, # Regular Oreo Blizzard
    "dairy queen blizzard": {"carbs": 85.0, "fats": 20.0, "protein": 12.0, "calories": 580.0, "potassium": 450.0, "sodium": 350.0, "saturated_fat": 12.0, "trans_fat": 0.5, "gi": 75.0},
    "dq dilly bar": {"carbs": 24.0, "fats": 15.0, "protein": 3.0, "calories": 240.0, "potassium": 150.0, "sodium": 75.0, "saturated_fat": 10.0, "trans_fat": 0.0, "gi": 65.0}, # 1 piece
    "dairy queen dilly bar": {"carbs": 24.0, "fats": 15.0, "protein": 3.0, "calories": 240.0, "potassium": 150.0, "sodium": 75.0, "saturated_fat": 10.0, "trans_fat": 0.0, "gi": 65.0},
    
    # Branded Cakes & Pastries
    "red ribbon black forest": {"carbs": 42.0, "fats": 16.0, "protein": 4.0, "calories": 330.0, "potassium": 180.0, "sodium": 220.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 70.0}, # 1 slice
    "red ribbon chocolate dedication cake": {"carbs": 45.0, "fats": 18.0, "protein": 4.0, "calories": 350.0, "potassium": 200.0, "sodium": 250.0, "saturated_fat": 9.0, "trans_fat": 0.0, "gi": 70.0}, # 1 slice
    "red ribbon ube dedidation cake": {"carbs": 44.0, "fats": 15.0, "protein": 4.0, "calories": 330.0, "potassium": 150.0, "sodium": 200.0, "saturated_fat": 7.0, "trans_fat": 0.0, "gi": 75.0}, # 1 slice
    "red ribbon ensaymada": {"carbs": 38.0, "fats": 18.0, "protein": 5.0, "calories": 330.0, "potassium": 120.0, "sodium": 280.0, "saturated_fat": 9.0, "trans_fat": 0.0, "gi": 75.0}, # 1 piece
    "red ribbon mamon": {"carbs": 28.0, "fats": 12.0, "protein": 4.0, "calories": 240.0, "potassium": 90.0, "sodium": 180.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 75.0}, # 1 butter mamon
    "goldilocks mocha roll": {"carbs": 35.0, "fats": 12.0, "protein": 3.0, "calories": 260.0, "potassium": 110.0, "sodium": 180.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 70.0}, # 1 slice
    "goldilocks ube roll": {"carbs": 36.0, "fats": 12.0, "protein": 3.0, "calories": 265.0, "potassium": 120.0, "sodium": 180.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 70.0}, # 1 slice
    "goldilocks chocolate roll": {"carbs": 38.0, "fats": 14.0, "protein": 4.0, "calories": 290.0, "potassium": 140.0, "sodium": 200.0, "saturated_fat": 7.0, "trans_fat": 0.0, "gi": 70.0}, # 1 slice
    "goldilocks ensaymada": {"carbs": 40.0, "fats": 16.0, "protein": 5.0, "calories": 320.0, "potassium": 110.0, "sodium": 260.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 75.0}, # 1 piece
    "goldilocks mamon": {"carbs": 26.0, "fats": 10.0, "protein": 4.0, "calories": 210.0, "potassium": 80.0, "sodium": 160.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 75.0}, # 1 fluffy mamon
    "goldilocks chocolate dedication cake": {"carbs": 44.0, "fats": 16.0, "protein": 4.0, "calories": 340.0, "potassium": 180.0, "sodium": 240.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 70.0}, # 1 slice

    "fishball": {"carbs": 3.0, "fats": 2.0, "protein": 1.5, "calories": 35.0, "potassium": 25.0, "sodium": 70.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 60.0}, # 1 pc

    "fishballs": {"carbs": 15.0, "fats": 10.0, "protein": 8.0, "calories": 180.0, "potassium": 120.0, "sodium": 350.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 60.0}, # 5 pcs
    "squid ball": {"carbs": 5.0, "fats": 2.5, "protein": 1.0, "calories": 45.0, "potassium": 20.0, "sodium": 90.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 65.0}, # 1 pc
    "chicken balls": {"carbs": 20.0, "fats": 15.0, "protein": 8.0, "calories": 250.0, "potassium": 100.0, "sodium": 400.0, "saturated_fat": 3.5, "trans_fat": 0.0, "gi": 60.0}, # 5 pcs
    "meatballs": {"carbs": 4.0, "fats": 18.0, "protein": 15.0, "calories": 240.0, "potassium": 150.0, "sodium": 450.0, "saturated_fat": 7.0, "trans_fat": 0.0, "gi": 30.0}, # 5 medium pcs

    # Frozen Foods & Fast Staples
    "chicken nuggets": {"carbs": 15.0, "fats": 18.0, "protein": 14.0, "calories": 280.0, "potassium": 250.0, "sodium": 500.0, "saturated_fat": 3.5, "trans_fat": 0.0, "gi": 65.0}, # 6 pcs
    "french fries": {"carbs": 45.0, "fats": 15.0, "protein": 4.0, "calories": 330.0, "potassium": 550.0, "sodium": 280.0, "saturated_fat": 2.5, "trans_fat": 0.1, "gi": 75.0}, # 1 medium serving
    "hash brown": {"carbs": 15.0, "fats": 9.0, "protein": 2.0, "calories": 140.0, "potassium": 200.0, "sodium": 300.0, "saturated_fat": 1.5, "trans_fat": 0.0, "gi": 70.0}, # 1 piece
    "hotdog": {"carbs": 2.0, "fats": 14.0, "protein": 6.0, "calories": 150.0, "potassium": 120.0, "sodium": 450.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 0.0}, # 1 piece standard
    "tender juicy hotdog": {"carbs": 4.0, "fats": 15.0, "protein": 6.0, "calories": 170.0, "potassium": 100.0, "sodium": 500.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 0.0}, # 1 piece Jumbo
    "maling": {"carbs": 3.0, "fats": 14.0, "protein": 6.0, "calories": 160.0, "potassium": 120.0, "sodium": 450.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 0.0}, # 1 slice luncheon meat
    "spam": {"carbs": 2.0, "fats": 16.0, "protein": 7.0, "calories": 180.0, "potassium": 150.0, "sodium": 790.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 0.0}, # 1 slice (56g)
    
    # Tofu / Tokwa
    "tofu": {"carbs": 2.0, "fats": 4.5, "protein": 8.0, "calories": 75.0, "potassium": 120.0, "sodium": 15.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 15.0}, # 100g firm raw
    "tokwa": {"carbs": 2.0, "fats": 4.5, "protein": 8.0, "calories": 75.0, "potassium": 120.0, "sodium": 15.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 15.0}, # 100g firm raw
    "fried tofu": {"carbs": 4.0, "fats": 20.0, "protein": 15.0, "calories": 260.0, "potassium": 150.0, "sodium": 50.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 15.0}, # 100g fried
    "pritong tokwa": {"carbs": 4.0, "fats": 20.0, "protein": 15.0, "calories": 260.0, "potassium": 150.0, "sodium": 50.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 15.0}, # 100g fried
    "sisig tofu": {"carbs": 8.0, "fats": 18.0, "protein": 12.0, "calories": 240.0, "potassium": 200.0, "sodium": 450.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 25.0}, # 1 serving

    "isaw": {"carbs": 0.0, "fats": 25.0, "protein": 15.0, "calories": 285.0, "potassium": 180.0, "sodium": 150.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 0.0},
    "taho": {"carbs": 15.0, "fats": 2.0, "protein": 5.0, "calories": 100.0, "potassium": 70.0, "sodium": 10.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 60.0},
    "suman": {"carbs": 45.0, "fats": 8.0, "protein": 3.0, "calories": 260.0, "potassium": 80.0, "sodium": 10.0, "saturated_fat": 7.0, "trans_fat": 0.0, "gi": 85.0},
    "puto": {"carbs": 50.0, "fats": 1.0, "protein": 3.0, "calories": 220.0, "potassium": 30.0, "sodium": 100.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 75.0},
    "kutsinta": {"carbs": 55.0, "fats": 0.5, "protein": 1.0, "calories": 230.0, "potassium": 20.0, "sodium": 50.0, "saturated_fat": 0.0, "trans_fat": 0.0, "gi": 70.0},
    "bibingka": {"carbs": 40.0, "fats": 10.0, "protein": 5.0, "calories": 270.0, "potassium": 100.0, "sodium": 150.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 80.0},
    "buko pandan": {"carbs": 25.0, "fats": 15.0, "protein": 2.0, "calories": 240.0, "potassium": 120.0, "sodium": 50.0, "saturated_fat": 12.0, "trans_fat": 0.0, "gi": 65.0},
    "leche flan": {"carbs": 30.0, "fats": 15.0, "protein": 6.0, "calories": 280.0, "potassium": 100.0, "sodium": 80.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 60.0},
    "chicharon": {"carbs": 0.0, "fats": 45.0, "protein": 40.0, "calories": 565.0, "potassium": 50.0, "sodium": 600.0, "saturated_fat": 15.0, "trans_fat": 0.0, "gi": 0.0},
    "chicharon bulaklak": {"carbs": 0.0, "fats": 60.0, "protein": 20.0, "calories": 620.0, "potassium": 40.0, "sodium": 400.0, "saturated_fat": 25.0, "trans_fat": 0.0, "gi": 0.0},
    "balut": {"carbs": 1.0, "fats": 14.0, "protein": 18.0, "calories": 200.0, "potassium": 150.0, "sodium": 150.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 0.0},
    "tapsilog": {"carbs": 18.0, "fats": 10.0, "protein": 12.0, "calories": 210.0, "potassium": 180.0, "sodium": 250.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 70.0},
    "longsilog": {"carbs": 18.0, "fats": 15.0, "protein": 10.0, "calories": 250.0, "potassium": 150.0, "sodium": 300.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 70.0},

    # --- 1. SG/MY Hawker Center Staples ---
    "hainanese chicken rice": {"carbs": 60.0, "fats": 25.0, "protein": 28.0, "calories": 620.0, "potassium": 350.0, "sodium": 1000.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 75.0}, # 1 serving
    "chicken rice": {"carbs": 60.0, "fats": 25.0, "protein": 28.0, "calories": 620.0, "potassium": 350.0, "sodium": 1000.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 75.0},
    "laksa": {"carbs": 55.0, "fats": 35.0, "protein": 25.0, "calories": 680.0, "potassium": 450.0, "sodium": 1600.0, "saturated_fat": 20.0, "trans_fat": 0.0, "gi": 60.0}, # 1 bowl
    "nasi lemak": {"carbs": 70.0, "fats": 32.0, "protein": 20.0, "calories": 650.0, "potassium": 300.0, "sodium": 1200.0, "saturated_fat": 15.0, "trans_fat": 0.0, "gi": 75.0}, # 1 serving
    "char kway teow": {"carbs": 75.0, "fats": 38.0, "protein": 22.0, "calories": 740.0, "potassium": 350.0, "sodium": 1400.0, "saturated_fat": 12.0, "trans_fat": 0.5, "gi": 65.0}, # 1 plate
    "hokkien mee": {"carbs": 65.0, "fats": 25.0, "protein": 30.0, "calories": 610.0, "potassium": 400.0, "sodium": 1500.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 60.0}, # 1 plate
    "bak kut teh": {"carbs": 5.0, "fats": 20.0, "protein": 35.0, "calories": 340.0, "potassium": 550.0, "sodium": 1100.0, "saturated_fat": 7.0, "trans_fat": 0.0, "gi": 0.0}, # 1 bowl soup+meat
    "mee rebus": {"carbs": 70.0, "fats": 18.0, "protein": 22.0, "calories": 550.0, "potassium": 450.0, "sodium": 1300.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 65.0}, # 1 bowl
    "nasi biryani": {"carbs": 85.0, "fats": 25.0, "protein": 30.0, "calories": 720.0, "potassium": 500.0, "sodium": 1200.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 55.0}, # 1 plate with chicken
    "roti prata": {"carbs": 40.0, "fats": 15.0, "protein": 6.0, "calories": 320.0, "potassium": 120.0, "sodium": 400.0, "saturated_fat": 6.0, "trans_fat": 0.5, "gi": 60.0}, # 1 plain piece
    "prata": {"carbs": 40.0, "fats": 15.0, "protein": 6.0, "calories": 320.0, "potassium": 120.0, "sodium": 400.0, "saturated_fat": 6.0, "trans_fat": 0.5, "gi": 60.0},
    "kaya toast": {"carbs": 35.0, "fats": 12.0, "protein": 5.0, "calories": 270.0, "potassium": 150.0, "sodium": 200.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 75.0}, # 2 slices with butter/kaya
    "kaya toast set": {"carbs": 36.0, "fats": 22.0, "protein": 18.0, "calories": 420.0, "potassium": 300.0, "sodium": 450.0, "saturated_fat": 9.0, "trans_fat": 0.0, "gi": 55.0}, # With soft boiled eggs
    "satay": {"carbs": 4.0, "fats": 6.0, "protein": 12.0, "calories": 110.0, "potassium": 150.0, "sodium": 200.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 25.0}, # 3 chicken/beef sticks
    "murtabak": {"carbs": 65.0, "fats": 35.0, "protein": 28.0, "calories": 690.0, "potassium": 350.0, "sodium": 1100.0, "saturated_fat": 14.0, "trans_fat": 0.5, "gi": 55.0}, # 1 portion

    # --- 2. The Filipino "Panaderia" (Local Bakery) & Sweets ---
    "pandesal": {"carbs": 25.0, "fats": 3.0, "protein": 4.0, "calories": 140.0, "potassium": 60.0, "sodium": 180.0, "saturated_fat": 1.0, "trans_fat": 0.0, "gi": 75.0}, # 1 medium piece
    "monay": {"carbs": 55.0, "fats": 8.0, "protein": 8.0, "calories": 320.0, "potassium": 120.0, "sodium": 250.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 75.0}, # 1 large piece
    "spanish bread": {"carbs": 38.0, "fats": 12.0, "protein": 5.0, "calories": 280.0, "potassium": 80.0, "sodium": 200.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 75.0}, # 1 piece
    "pan de coco": {"carbs": 42.0, "fats": 14.0, "protein": 5.0, "calories": 310.0, "potassium": 100.0, "sodium": 180.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 70.0}, # 1 piece
    "tasty bread": {"carbs": 13.0, "fats": 1.0, "protein": 3.0, "calories": 70.0, "potassium": 40.0, "sodium": 130.0, "saturated_fat": 0.0, "trans_fat": 0.0, "gi": 75.0}, # 1 slice white bread
    "hopia mongo": {"carbs": 35.0, "fats": 9.0, "protein": 5.0, "calories": 240.0, "potassium": 150.0, "sodium": 120.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 60.0}, # 1 piece
    "hopia ube": {"carbs": 36.0, "fats": 8.0, "protein": 4.0, "calories": 235.0, "potassium": 140.0, "sodium": 110.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 65.0}, # 1 piece
    "hopia baboy": {"carbs": 32.0, "fats": 14.0, "protein": 4.0, "calories": 270.0, "potassium": 90.0, "sodium": 150.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 65.0}, # 1 piece
    "biscocho": {"carbs": 45.0, "fats": 20.0, "protein": 6.0, "calories": 380.0, "potassium": 80.0, "sodium": 220.0, "saturated_fat": 12.0, "trans_fat": 0.5, "gi": 80.0}, # 1 serving pack
    "otap": {"carbs": 30.0, "fats": 12.0, "protein": 3.0, "calories": 240.0, "potassium": 60.0, "sodium": 150.0, "saturated_fat": 5.0, "trans_fat": 0.5, "gi": 75.0}, # 2 pieces
    "halo halo": {"carbs": 75.0, "fats": 12.0, "protein": 8.0, "calories": 420.0, "potassium": 300.0, "sodium": 150.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 65.0}, # 1 regular glass
    "halo-halo": {"carbs": 75.0, "fats": 12.0, "protein": 8.0, "calories": 420.0, "potassium": 300.0, "sodium": 150.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 65.0},
    "ube halaya": {"carbs": 45.0, "fats": 12.0, "protein": 4.0, "calories": 310.0, "potassium": 250.0, "sodium": 60.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 55.0}, # 1/2 cup
    "choc nut": {"carbs": 12.0, "fats": 6.0, "protein": 2.0, "calories": 110.0, "potassium": 50.0, "sodium": 20.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 50.0}, # 2 small pieces
    "flat tops": {"carbs": 15.0, "fats": 8.0, "protein": 2.0, "calories": 140.0, "potassium": 40.0, "sodium": 30.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 60.0}, # 3 pieces
    
    # --- 3. Dim Sum & Chinese Takeout ---
    "siomai": {"carbs": 15.0, "fats": 12.0, "protein": 14.0, "calories": 230.0, "potassium": 150.0, "sodium": 600.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 55.0}, # 4 pieces pork
    "shumai": {"carbs": 15.0, "fats": 12.0, "protein": 14.0, "calories": 230.0, "potassium": 150.0, "sodium": 600.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 55.0},
    "hakaw": {"carbs": 18.0, "fats": 4.0, "protein": 15.0, "calories": 170.0, "potassium": 180.0, "sodium": 450.0, "saturated_fat": 1.0, "trans_fat": 0.0, "gi": 55.0}, # 4 pieces shrimp
    "har gow": {"carbs": 18.0, "fats": 4.0, "protein": 15.0, "calories": 170.0, "potassium": 180.0, "sodium": 450.0, "saturated_fat": 1.0, "trans_fat": 0.0, "gi": 55.0}, # 4 pieces shrimp
    "xiao long bao": {"carbs": 24.0, "fats": 14.0, "protein": 12.0, "calories": 270.0, "potassium": 160.0, "sodium": 550.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 55.0}, # 4 pieces
    "siopao asado": {"carbs": 55.0, "fats": 12.0, "protein": 15.0, "calories": 390.0, "potassium": 180.0, "sodium": 750.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 65.0}, # 1 large jumbo
    "siopao bola bola": {"carbs": 52.0, "fats": 18.0, "protein": 16.0, "calories": 430.0, "potassium": 190.0, "sodium": 800.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 65.0}, # 1 large jumbo
    "egg tart": {"carbs": 25.0, "fats": 14.0, "protein": 4.0, "calories": 240.0, "potassium": 80.0, "sodium": 120.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 60.0}, # 1 piece
    "sesame ball": {"carbs": 35.0, "fats": 12.0, "protein": 4.0, "calories": 260.0, "potassium": 100.0, "sodium": 80.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 70.0}, # 1 large piece (Buchi)
    "buchi": {"carbs": 35.0, "fats": 12.0, "protein": 4.0, "calories": 260.0, "potassium": 100.0, "sodium": 80.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 70.0}, # 1 large piece
    "radish cake": {"carbs": 18.0, "fats": 10.0, "protein": 3.0, "calories": 170.0, "potassium": 120.0, "sodium": 450.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 65.0}, # 2 pan fried slices
    "taro puff": {"carbs": 22.0, "fats": 14.0, "protein": 4.0, "calories": 230.0, "potassium": 150.0, "sodium": 280.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 60.0}, # 1 piece
    "sweet and sour pork": {"carbs": 35.0, "fats": 25.0, "protein": 18.0, "calories": 440.0, "potassium": 300.0, "sodium": 750.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 65.0}, # 1 serving

    # --- 4. Asian Noodles & Comfort Soups ---
    "ramen": {"carbs": 70.0, "fats": 22.0, "protein": 28.0, "calories": 600.0, "potassium": 450.0, "sodium": 1800.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 60.0}, # Tonkotsu generic bowl
    "tonkotsu ramen": {"carbs": 70.0, "fats": 22.0, "protein": 28.0, "calories": 600.0, "potassium": 450.0, "sodium": 1800.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 60.0},
    "shoyu ramen": {"carbs": 75.0, "fats": 15.0, "protein": 24.0, "calories": 530.0, "potassium": 400.0, "sodium": 2100.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 60.0},
    "ramyeon": {"carbs": 80.0, "fats": 16.0, "protein": 10.0, "calories": 500.0, "potassium": 250.0, "sodium": 1900.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 70.0}, # Korean Instant Pack
    "tteokbokki": {"carbs": 95.0, "fats": 6.0, "protein": 12.0, "calories": 520.0, "potassium": 350.0, "sodium": 1200.0, "saturated_fat": 1.5, "trans_fat": 0.0, "gi": 75.0}, # 1 serving
    "jajangmyeon": {"carbs": 110.0, "fats": 25.0, "protein": 20.0, "calories": 740.0, "potassium": 450.0, "sodium": 1400.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 65.0}, # 1 bowl
    "kimchi jjigae": {"carbs": 25.0, "fats": 18.0, "protein": 22.0, "calories": 350.0, "potassium": 550.0, "sodium": 1600.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 40.0}, # 1 bowl with pork
    "pho": {"carbs": 65.0, "fats": 12.0, "protein": 30.0, "calories": 480.0, "potassium": 500.0, "sodium": 1500.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 50.0}, # 1 bowl beef pho
    "pad thai": {"carbs": 85.0, "fats": 22.0, "protein": 20.0, "calories": 620.0, "potassium": 400.0, "sodium": 1100.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 65.0}, # 1 serving chicken/shrimp
    "tom yum": {"carbs": 15.0, "fats": 10.0, "protein": 22.0, "calories": 240.0, "potassium": 450.0, "sodium": 1400.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 30.0}, # 1 bowl clear specific

    # --- 5. Condiments, Sauces & Spreads ---
    "mang tomas": {"carbs": 4.0, "fats": 1.0, "protein": 0.0, "calories": 25.0, "potassium": 30.0, "sodium": 140.0, "saturated_fat": 0.0, "trans_fat": 0.0, "gi": 60.0}, # 1 tbsp lechon sauce
    "lechon sauce": {"carbs": 4.0, "fats": 1.0, "protein": 0.0, "calories": 25.0, "potassium": 30.0, "sodium": 140.0, "saturated_fat": 0.0, "trans_fat": 0.0, "gi": 60.0},
    "banana ketchup": {"carbs": 5.0, "fats": 0.0, "protein": 0.0, "calories": 20.0, "potassium": 45.0, "sodium": 150.0, "saturated_fat": 0.0, "trans_fat": 0.0, "gi": 65.0}, # 1 tbsp
    "sweet chili sauce": {"carbs": 9.0, "fats": 0.0, "protein": 0.0, "calories": 35.0, "potassium": 20.0, "sodium": 180.0, "saturated_fat": 0.0, "trans_fat": 0.0, "gi": 70.0}, # 1 tbsp
    "chili garlic oil": {"carbs": 1.0, "fats": 14.0, "protein": 0.0, "calories": 130.0, "potassium": 20.0, "sodium": 80.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 0.0}, # 1 tbsp
    "mayonnaise": {"carbs": 0.5, "fats": 11.0, "protein": 0.0, "calories": 100.0, "potassium": 5.0, "sodium": 90.0, "saturated_fat": 1.5, "trans_fat": 0.0, "gi": 0.0}, # 1 tbsp regular
    "peanut butter": {"carbs": 6.0, "fats": 16.0, "protein": 7.0, "calories": 190.0, "potassium": 200.0, "sodium": 140.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 30.0}, # 2 tbsp
    "cheez whiz": {"carbs": 3.0, "fats": 7.0, "protein": 3.0, "calories": 90.0, "potassium": 50.0, "sodium": 280.0, "saturated_fat": 3.5, "trans_fat": 0.0, "gi": 45.0}, # 2 tbsp
    "condensed milk": {"carbs": 22.0, "fats": 3.0, "protein": 3.0, "calories": 130.0, "potassium": 140.0, "sodium": 50.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 65.0}, # 2 tbsp
    "nutella": {"carbs": 21.0, "fats": 11.0, "protein": 2.0, "calories": 200.0, "potassium": 120.0, "sodium": 15.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 55.0}, # 2 tbsp
    "kaya spread": {"carbs": 18.0, "fats": 3.5, "protein": 2.0, "calories": 110.0, "potassium": 80.0, "sodium": 35.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 60.0}, # 2 tbsp coconut jam

    # --- 6. Popular Local Junk Food & Chips ---
    "piattos": {"carbs": 55.0, "fats": 25.0, "protein": 5.0, "calories": 460.0, "potassium": 250.0, "sodium": 650.0, "saturated_fat": 12.0, "trans_fat": 0.0, "gi": 75.0}, # 1 large bag (85g)
    "nova": {"carbs": 60.0, "fats": 18.0, "protein": 6.0, "calories": 420.0, "potassium": 300.0, "sodium": 550.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 65.0}, # 1 large bag (78g)
    "chippy": {"carbs": 65.0, "fats": 28.0, "protein": 6.0, "calories": 530.0, "potassium": 150.0, "sodium": 800.0, "saturated_fat": 14.0, "trans_fat": 0.0, "gi": 75.0}, # 1 large bag (110g)
    "boy bawang": {"carbs": 18.0, "fats": 22.0, "protein": 4.0, "calories": 280.0, "potassium": 180.0, "sodium": 400.0, "saturated_fat": 10.0, "trans_fat": 0.0, "gi": 60.0}, # 100g pack
    "vcut": {"carbs": 52.0, "fats": 28.0, "protein": 5.0, "calories": 480.0, "potassium": 350.0, "sodium": 700.0, "saturated_fat": 12.0, "trans_fat": 0.0, "gi": 75.0}, # 1 large bag
    "roller coaster": {"carbs": 55.0, "fats": 25.0, "protein": 5.0, "calories": 460.0, "potassium": 200.0, "sodium": 650.0, "saturated_fat": 11.0, "trans_fat": 0.0, "gi": 75.0}, # 1 large bag
    "oishi prawn crackers": {"carbs": 65.0, "fats": 18.0, "protein": 6.0, "calories": 450.0, "potassium": 150.0, "sodium": 750.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 75.0}, # 1 large bag
    "irvins salted egg chips": {"carbs": 60.0, "fats": 35.0, "protein": 8.0, "calories": 580.0, "potassium": 450.0, "sodium": 850.0, "saturated_fat": 16.0, "trans_fat": 0.0, "gi": 65.0}, # 100g portion
    "stick-o": {"carbs": 25.0, "fats": 8.0, "protein": 2.0, "calories": 180.0, "potassium": 80.0, "sodium": 100.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 75.0}, # 10 sticks
    "fudgee barr": {"carbs": 24.0, "fats": 8.0, "protein": 2.0, "calories": 180.0, "potassium": 60.0, "sodium": 120.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 75.0}, # 1 piece (40g)
    "ding dong": {"carbs": 55.0, "fats": 28.0, "protein": 12.0, "calories": 520.0, "potassium": 350.0, "sodium": 650.0, "saturated_fat": 14.0, "trans_fat": 0.0, "gi": 55.0}, # 100g mixed nuts/snacks

    "tocilog": {"carbs": 25.0, "fats": 12.0, "protein": 10.0, "calories": 250.0, "potassium": 100.0, "sodium": 350.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 75.0},
    "bangsilog": {"carbs": 15.0, "fats": 10.0, "protein": 15.0, "calories": 220.0, "potassium": 200.0, "sodium": 300.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 65.0},
    "danggit": {"carbs": 0.0, "fats": 5.0, "protein": 50.0, "calories": 245.0, "potassium": 300.0, "sodium": 2000.0, "saturated_fat": 1.0, "trans_fat": 0.0, "gi": 0.0},
    "bagoong": {"carbs": 5.0, "fats": 5.0, "protein": 15.0, "calories": 125.0, "potassium": 100.0, "sodium": 4000.0, "saturated_fat": 1.0, "trans_fat": 0.0, "gi": 30.0},
    "bistek tagalog": {"carbs": 3.0, "fats": 15.0, "protein": 25.0, "calories": 250.0, "potassium": 300.0, "sodium": 400.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 20.0},
    "dinuguan": {"carbs": 5.0, "fats": 18.0, "protein": 20.0, "calories": 260.0, "potassium": 250.0, "sodium": 350.0, "saturated_fat": 7.0, "trans_fat": 0.0, "gi": 30.0},
    "palabok": {"carbs": 30.0, "fats": 8.0, "protein": 10.0, "calories": 240.0, "potassium": 150.0, "sodium": 400.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 70.0},
    "batchoy": {"carbs": 20.0, "fats": 10.0, "protein": 12.0, "calories": 230.0, "potassium": 200.0, "sodium": 450.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 65.0},
    "lomi": {"carbs": 25.0, "fats": 10.0, "protein": 10.0, "calories": 240.0, "potassium": 180.0, "sodium": 400.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 65.0},
    "mami": {"carbs": 20.0, "fats": 5.0, "protein": 10.0, "calories": 180.0, "potassium": 150.0, "sodium": 350.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 60.0},
    "sopas": {"carbs": 18.0, "fats": 7.0, "protein": 8.0, "calories": 170.0, "potassium": 150.0, "sodium": 300.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 60.0},
    "goto": {"carbs": 20.0, "fats": 5.0, "protein": 10.0, "calories": 180.0, "potassium": 150.0, "sodium": 300.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 70.0},
    "ginataang kalabasa": {"carbs": 10.0, "fats": 15.0, "protein": 3.0, "calories": 187.0, "potassium": 250.0, "sodium": 150.0, "saturated_fat": 12.0, "trans_fat": 0.0, "gi": 45.0},
    "ginataang sitaw": {"carbs": 5.0, "fats": 15.0, "protein": 3.0, "calories": 170.0, "potassium": 200.0, "sodium": 150.0, "saturated_fat": 12.0, "trans_fat": 0.0, "gi": 35.0},
    "tortang dulong": {"carbs": 3.0, "fats": 12.0, "protein": 15.0, "calories": 180.0, "potassium": 180.0, "sodium": 300.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 30.0},
    "inihaw na liempo": {"carbs": 0.0, "fats": 35.0, "protein": 25.0, "calories": 425.0, "potassium": 250.0, "sodium": 200.0, "saturated_fat": 12.0, "trans_fat": 0.0, "gi": 0.0},
    "chicken inasal": {"carbs": 2.0, "fats": 15.0, "protein": 25.0, "calories": 240.0, "potassium": 250.0, "sodium": 250.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 20.0},
    "pinapaitan": {"carbs": 1.0, "fats": 15.0, "protein": 20.0, "calories": 220.0, "potassium": 200.0, "sodium": 300.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 15.0},
    "papaitan": {"carbs": 1.0, "fats": 15.0, "protein": 20.0, "calories": 220.0, "potassium": 200.0, "sodium": 300.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 15.0},
    "igado": {"carbs": 5.0, "fats": 12.0, "protein": 20.0, "calories": 210.0, "potassium": 250.0, "sodium": 350.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 30.0},
    "bulalo": {"carbs": 3.0, "fats": 20.0, "protein": 20.0, "calories": 270.0, "potassium": 280.0, "sodium": 250.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 20.0},
    "kansi": {"carbs": 3.0, "fats": 20.0, "protein": 20.0, "calories": 270.0, "potassium": 280.0, "sodium": 250.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 20.0},

    # Fish & Seafood Varieties
    "seabass": {"carbs": 0.0, "fats": 2.0, "protein": 18.0, "calories": 95.0, "potassium": 250.0, "sodium": 65.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0}, # 100g raw
    "sea bass": {"carbs": 0.0, "fats": 2.0, "protein": 18.0, "calories": 95.0, "potassium": 250.0, "sodium": 65.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0},
    "salmon": {"carbs": 0.0, "fats": 13.0, "protein": 20.0, "calories": 205.0, "potassium": 360.0, "sodium": 60.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 0.0}, # 100g raw
    "tuna": {"carbs": 0.0, "fats": 1.0, "protein": 24.0, "calories": 110.0, "potassium": 250.0, "sodium": 40.0, "saturated_fat": 0.2, "trans_fat": 0.0, "gi": 0.0}, # 100g raw
    "bangus": {"carbs": 0.0, "fats": 5.0, "protein": 20.0, "calories": 150.0, "potassium": 320.0, "sodium": 80.0, "saturated_fat": 1.5, "trans_fat": 0.0, "gi": 0.0}, # Milkfish 100g raw
    "milkfish": {"carbs": 0.0, "fats": 5.0, "protein": 20.0, "calories": 150.0, "potassium": 320.0, "sodium": 80.0, "saturated_fat": 1.5, "trans_fat": 0.0, "gi": 0.0},
    "tilapia": {"carbs": 0.0, "fats": 1.5, "protein": 20.0, "calories": 95.0, "potassium": 300.0, "sodium": 50.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0}, # 100g raw
    "galunggong": {"carbs": 0.0, "fats": 4.0, "protein": 18.0, "calories": 110.0, "potassium": 280.0, "sodium": 90.0, "saturated_fat": 1.0, "trans_fat": 0.0, "gi": 0.0}, # Mackerel scad 100g raw
    "lapu lapu": {"carbs": 0.0, "fats": 1.0, "protein": 18.0, "calories": 90.0, "potassium": 350.0, "sodium": 60.0, "saturated_fat": 0.2, "trans_fat": 0.0, "gi": 0.0}, # Grouper 100g raw
    "grouper": {"carbs": 0.0, "fats": 1.0, "protein": 18.0, "calories": 90.0, "potassium": 350.0, "sodium": 60.0, "saturated_fat": 0.2, "trans_fat": 0.0, "gi": 0.0},
    "tuyo": {"carbs": 0.0, "fats": 8.0, "protein": 30.0, "calories": 200.0, "potassium": 200.0, "sodium": 2500.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 0.0}, # Dried fish
    "daing na bangus": {"carbs": 2.0, "fats": 15.0, "protein": 22.0, "calories": 240.0, "potassium": 300.0, "sodium": 600.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 0.0}, # 1 serving
    "shrimp": {"carbs": 1.0, "fats": 1.5, "protein": 20.0, "calories": 100.0, "potassium": 200.0, "sodium": 800.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0}, # 100g raw
    "hipon": {"carbs": 1.0, "fats": 1.5, "protein": 20.0, "calories": 100.0, "potassium": 200.0, "sodium": 800.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0},
    "crab": {"carbs": 0.0, "fats": 1.0, "protein": 18.0, "calories": 85.0, "potassium": 250.0, "sodium": 650.0, "saturated_fat": 0.2, "trans_fat": 0.0, "gi": 0.0}, # 100g raw crab meat
    "alimango": {"carbs": 0.0, "fats": 1.0, "protein": 18.0, "calories": 85.0, "potassium": 250.0, "sodium": 650.0, "saturated_fat": 0.2, "trans_fat": 0.0, "gi": 0.0},
    "alimasag": {"carbs": 0.0, "fats": 1.0, "protein": 18.0, "calories": 85.0, "potassium": 250.0, "sodium": 650.0, "saturated_fat": 0.2, "trans_fat": 0.0, "gi": 0.0},
    "squid": {"carbs": 3.0, "fats": 1.5, "protein": 16.0, "calories": 90.0, "potassium": 200.0, "sodium": 40.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0}, # 100g raw
    "pusit": {"carbs": 3.0, "fats": 1.5, "protein": 16.0, "calories": 90.0, "potassium": 200.0, "sodium": 40.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0},
    "mussels": {"carbs": 7.0, "fats": 2.0, "protein": 12.0, "calories": 85.0, "potassium": 300.0, "sodium": 280.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0}, # 100g raw
    "tahong": {"carbs": 7.0, "fats": 2.0, "protein": 12.0, "calories": 85.0, "potassium": 300.0, "sodium": 280.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0},
    "oysters": {"carbs": 4.0, "fats": 1.5, "protein": 5.0, "calories": 50.0, "potassium": 90.0, "sodium": 100.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0}, # 100g raw
    "talaba": {"carbs": 4.0, "fats": 1.5, "protein": 5.0, "calories": 50.0, "potassium": 90.0, "sodium": 100.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 0.0},
    "clams": {"carbs": 2.5, "fats": 1.0, "protein": 12.0, "calories": 75.0, "potassium": 150.0, "sodium": 550.0, "saturated_fat": 0.2, "trans_fat": 0.0, "gi": 0.0}, # 100g raw
    "halaan": {"carbs": 2.5, "fats": 1.0, "protein": 12.0, "calories": 75.0, "potassium": 150.0, "sodium": 550.0, "saturated_fat": 0.2, "trans_fat": 0.0, "gi": 0.0},

    # Seafood Dishes
    "sinigang na bangus": {"carbs": 8.0, "fats": 12.0, "protein": 22.0, "calories": 240.0, "potassium": 500.0, "sodium": 800.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 30.0}, # 1 bowl
    "sinigang na hipon": {"carbs": 5.0, "fats": 5.0, "protein": 20.0, "calories": 150.0, "potassium": 450.0, "sodium": 950.0, "saturated_fat": 1.0, "trans_fat": 0.0, "gi": 30.0}, # 1 bowl
    "sweet and sour fish": {"carbs": 25.0, "fats": 15.0, "protein": 18.0, "calories": 300.0, "potassium": 300.0, "sodium": 550.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 65.0}, # 1 serving
    "escabeche": {"carbs": 25.0, "fats": 15.0, "protein": 18.0, "calories": 300.0, "potassium": 300.0, "sodium": 550.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 65.0},
    "adobong pusit": {"carbs": 5.0, "fats": 8.0, "protein": 18.0, "calories": 180.0, "potassium": 250.0, "sodium": 700.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 35.0}, # 1 serving
    "calamares fritos": {"carbs": 25.0, "fats": 18.0, "protein": 14.0, "calories": 320.0, "potassium": 210.0, "sodium": 400.0, "saturated_fat": 3.5, "trans_fat": 0.0, "gi": 60.0}, # 1 serving
    "buttered shrimp": {"carbs": 2.0, "fats": 22.0, "protein": 20.0, "calories": 280.0, "potassium": 250.0, "sodium": 850.0, "saturated_fat": 12.0, "trans_fat": 0.0, "gi": 0.0}, # 1 serving
    "chili crab": {"carbs": 15.0, "fats": 18.0, "protein": 20.0, "calories": 310.0, "potassium": 350.0, "sodium": 1200.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 45.0}, # 1 serving (sauce+meat)
    "baked tahong": {"carbs": 5.0, "fats": 15.0, "protein": 14.0, "calories": 210.0, "potassium": 300.0, "sodium": 450.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 20.0}, # 1 serving with cheese/garlic
    "kinilaw": {"carbs": 4.0, "fats": 5.0, "protein": 22.0, "calories": 150.0, "potassium": 350.0, "sodium": 450.0, "saturated_fat": 1.0, "trans_fat": 0.0, "gi": 15.0}, # 1 bowl (ceviche)
    "paksiw na bangus": {"carbs": 3.0, "fats": 10.0, "protein": 20.0, "calories": 190.0, "potassium": 350.0, "sodium": 650.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 20.0}, # 1 bowl
    "fish fillet": {"carbs": 20.0, "fats": 15.0, "protein": 15.0, "calories": 280.0, "potassium": 250.0, "sodium": 450.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 60.0}, # Breaded & Fried
    

    # Additional Philippine Street Food
    "kwek kwek": {"carbs": 15.0, "fats": 12.0, "protein": 6.0, "calories": 190.0, "potassium": 65.0, "sodium": 300.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 65.0}, # 3 pcs
    "tokneneng": {"carbs": 18.0, "fats": 14.0, "protein": 12.0, "calories": 250.0, "potassium": 120.0, "sodium": 350.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 65.0}, # 1 large egg
    "proben": {"carbs": 10.0, "fats": 16.0, "protein": 8.0, "calories": 220.0, "potassium": 100.0, "sodium": 400.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 60.0}, # 1 stick
    "proven": {"carbs": 10.0, "fats": 16.0, "protein": 8.0, "calories": 220.0, "potassium": 100.0, "sodium": 400.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 60.0},
    "squid balls": {"carbs": 25.0, "fats": 12.0, "protein": 5.0, "calories": 230.0, "potassium": 110.0, "sodium": 450.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 65.0}, # 1 stick
    "calamares": {"carbs": 20.0, "fats": 18.0, "protein": 14.0, "calories": 300.0, "potassium": 210.0, "sodium": 380.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 60.0}, # 1 serving
    "adidas": {"carbs": 0.0, "fats": 15.0, "protein": 18.0, "calories": 210.0, "potassium": 80.0, "sodium": 250.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 0.0}, # 1 stick (chicken feet)
    "betamax": {"carbs": 1.0, "fats": 8.0, "protein": 15.0, "calories": 140.0, "potassium": 90.0, "sodium": 300.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 0.0}, # 1 stick (blood)
    "helmet": {"carbs": 0.0, "fats": 12.0, "protein": 14.0, "calories": 160.0, "potassium": 70.0, "sodium": 200.0, "saturated_fat": 3.5, "trans_fat": 0.0, "gi": 0.0}, # 1 piece (chicken head)
    "turon": {"carbs": 42.0, "fats": 12.0, "protein": 2.0, "calories": 280.0, "potassium": 400.0, "sodium": 15.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 75.0}, # 1 piece
    "banana cue": {"carbs": 38.0, "fats": 8.0, "protein": 1.5, "calories": 230.0, "potassium": 380.0, "sodium": 10.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 70.0}, # 1 stick (2 pcs)
    "camote cue": {"carbs": 45.0, "fats": 10.0, "protein": 2.0, "calories": 280.0, "potassium": 350.0, "sodium": 20.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 65.0}, # 1 stick (2 pcs)
    "maruya": {"carbs": 35.0, "fats": 14.0, "protein": 3.0, "calories": 280.0, "potassium": 300.0, "sodium": 150.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 75.0}, # 1 piece
    "carioca": {"carbs": 40.0, "fats": 15.0, "protein": 2.0, "calories": 300.0, "potassium": 50.0, "sodium": 80.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 85.0}, # 1 stick (3 balls)
    "iskrambol": {"carbs": 40.0, "fats": 6.0, "protein": 2.0, "calories": 220.0, "potassium": 90.0, "sodium": 120.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 80.0}, # 1 cup
    "ice scramble": {"carbs": 40.0, "fats": 6.0, "protein": 2.0, "calories": 220.0, "potassium": 90.0, "sodium": 120.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 80.0}, # 1 cup
    "sorbetes": {"carbs": 25.0, "fats": 10.0, "protein": 3.0, "calories": 200.0, "potassium": 150.0, "sodium": 85.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 70.0}, # 1 cone
    
    # Carinderia / Eatery Staples & Lugawan
    "lugaw": {"carbs": 28.0, "fats": 2.0, "protein": 4.0, "calories": 150.0, "potassium": 80.0, "sodium": 400.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 75.0}, # 1 bowl plain
    "arroz caldo": {"carbs": 30.0, "fats": 8.0, "protein": 12.0, "calories": 250.0, "potassium": 180.0, "sodium": 600.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 70.0}, # 1 bowl chicken
    "goto laman": {"carbs": 28.0, "fats": 7.0, "protein": 14.0, "calories": 230.0, "potassium": 150.0, "sodium": 550.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 70.0},
    "tokawat baboy": {"carbs": 12.0, "fats": 25.0, "protein": 18.0, "calories": 320.0, "potassium": 200.0, "sodium": 850.0, "saturated_fat": 7.0, "trans_fat": 0.0, "gi": 45.0}, # 1 serving
    "tokwa't baboy": {"carbs": 12.0, "fats": 25.0, "protein": 18.0, "calories": 320.0, "potassium": 200.0, "sodium": 850.0, "saturated_fat": 7.0, "trans_fat": 0.0, "gi": 45.0},
    "lumpiang shanghai": {"carbs": 20.0, "fats": 22.0, "protein": 15.0, "calories": 350.0, "potassium": 150.0, "sodium": 500.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 60.0}, # 5 small pcs
    "lumpiang gulay": {"carbs": 24.0, "fats": 12.0, "protein": 5.0, "calories": 220.0, "potassium": 300.0, "sodium": 400.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 50.0}, # 2 rolls fried
    "chopsuey": {"carbs": 15.0, "fats": 10.0, "protein": 8.0, "calories": 180.0, "potassium": 450.0, "sodium": 600.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 40.0}, # 1 cup (meat/veg mix)
    "pinakbet": {"carbs": 14.0, "fats": 12.0, "protein": 9.0, "calories": 190.0, "potassium": 500.0, "sodium": 750.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 35.0}, # 1 cup
    "ginisang munggo": {"carbs": 28.0, "fats": 8.0, "protein": 12.0, "calories": 230.0, "potassium": 450.0, "sodium": 550.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 35.0}, # 1 cup
    "monggo": {"carbs": 28.0, "fats": 8.0, "protein": 12.0, "calories": 230.0, "potassium": 450.0, "sodium": 550.0, "saturated_fat": 2.5, "trans_fat": 0.0, "gi": 35.0},
    "tortang talong": {"carbs": 8.0, "fats": 15.0, "protein": 8.0, "calories": 200.0, "potassium": 300.0, "sodium": 350.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 45.0}, # 1 eggplant
    "bicol express": {"carbs": 5.0, "fats": 28.0, "protein": 18.0, "calories": 340.0, "potassium": 320.0, "sodium": 650.0, "saturated_fat": 15.0, "trans_fat": 0.0, "gi": 30.0}, # 1 serving
    "laing": {"carbs": 12.0, "fats": 22.0, "protein": 6.0, "calories": 260.0, "potassium": 450.0, "sodium": 500.0, "saturated_fat": 14.0, "trans_fat": 0.0, "gi": 35.0}, # 1 serving
    "sisig": {"carbs": 4.0, "fats": 35.0, "protein": 22.0, "calories": 420.0, "potassium": 280.0, "sodium": 700.0, "saturated_fat": 12.0, "trans_fat": 0.0, "gi": 25.0}, # 1 serving (pork)
    "lechon kawali": {"carbs": 0.0, "fats": 45.0, "protein": 25.0, "calories": 520.0, "potassium": 250.0, "sodium": 650.0, "saturated_fat": 15.0, "trans_fat": 0.0, "gi": 0.0}, # 1 serving
    "adobong baboy": {"carbs": 8.0, "fats": 28.0, "protein": 24.0, "calories": 380.0, "potassium": 350.0, "sodium": 950.0, "saturated_fat": 9.0, "trans_fat": 0.0, "gi": 30.0}, # 1 serving pork adobo
    "adobong manok": {"carbs": 8.0, "fats": 15.0, "protein": 28.0, "calories": 290.0, "potassium": 320.0, "sodium": 850.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 25.0}, # 1 serving chicken adobo
    "pork sinigang": {"carbs": 10.0, "fats": 22.0, "protein": 20.0, "calories": 320.0, "potassium": 550.0, "sodium": 900.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 35.0}, # 1 bowl
    "chicken tinola": {"carbs": 8.0, "fats": 12.0, "protein": 24.0, "calories": 240.0, "potassium": 400.0, "sodium": 700.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 35.0}, # 1 bowl
    "kare kare": {"carbs": 22.0, "fats": 25.0, "protein": 20.0, "calories": 400.0, "potassium": 650.0, "sodium": 800.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 45.0}, # 1 serving (beef/tripe)
    "menudo": {"carbs": 12.0, "fats": 18.0, "protein": 22.0, "calories": 300.0, "potassium": 450.0, "sodium": 650.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 40.0}, # 1 serving
    "afritada": {"carbs": 15.0, "fats": 16.0, "protein": 22.0, "calories": 310.0, "potassium": 480.0, "sodium": 600.0, "saturated_fat": 4.5, "trans_fat": 0.0, "gi": 45.0}, # 1 serving (chicken or pork)
    "caldereta": {"carbs": 14.0, "fats": 20.0, "protein": 25.0, "calories": 340.0, "potassium": 500.0, "sodium": 750.0, "saturated_fat": 6.0, "trans_fat": 0.0, "gi": 40.0}, # 1 serving beef
    
    # Pansit Variants
    "pansit canton": {"carbs": 45.0, "fats": 15.0, "protein": 12.0, "calories": 360.0, "potassium": 250.0, "sodium": 850.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 65.0}, # 1 cup
    "pancit canton": {"carbs": 45.0, "fats": 15.0, "protein": 12.0, "calories": 360.0, "potassium": 250.0, "sodium": 850.0, "saturated_fat": 5.0, "trans_fat": 0.0, "gi": 65.0},
    "pansit bihon": {"carbs": 50.0, "fats": 8.0, "protein": 10.0, "calories": 310.0, "potassium": 200.0, "sodium": 600.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 60.0}, # 1 cup
    "pancit bihon": {"carbs": 50.0, "fats": 8.0, "protein": 10.0, "calories": 310.0, "potassium": 200.0, "sodium": 600.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 60.0},
    "pansit malabon": {"carbs": 48.0, "fats": 12.0, "protein": 14.0, "calories": 350.0, "potassium": 280.0, "sodium": 800.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 65.0}, # 1 cup
    "pancit malabon": {"carbs": 48.0, "fats": 12.0, "protein": 14.0, "calories": 350.0, "potassium": 280.0, "sodium": 800.0, "saturated_fat": 4.0, "trans_fat": 0.0, "gi": 65.0},
    "pansit luglug": {"carbs": 45.0, "fats": 10.0, "protein": 12.0, "calories": 320.0, "potassium": 220.0, "sodium": 750.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 65.0}, # 1 cup
    "pancit habhab": {"carbs": 42.0, "fats": 12.0, "protein": 8.0, "calories": 300.0, "potassium": 190.0, "sodium": 650.0, "saturated_fat": 3.5, "trans_fat": 0.0, "gi": 60.0}, # 1 serving
    "sotanghon guisado": {"carbs": 40.0, "fats": 10.0, "protein": 8.0, "calories": 280.0, "potassium": 150.0, "sodium": 550.0, "saturated_fat": 2.0, "trans_fat": 0.0, "gi": 55.0}, # 1 cup

    # More Kakanin & Rice Cakes
    "biko": {"carbs": 65.0, "fats": 12.0, "protein": 4.0, "calories": 380.0, "potassium": 180.0, "sodium": 150.0, "saturated_fat": 9.0, "trans_fat": 0.0, "gi": 85.0}, # 1 slice (glutinous rice with coconut milk)
    "maja blanca": {"carbs": 45.0, "fats": 10.0, "protein": 3.0, "calories": 280.0, "potassium": 120.0, "sodium": 80.0, "saturated_fat": 8.0, "trans_fat": 0.0, "gi": 75.0}, # 1 slice (coconut pudding with corn)
    "sapin sapin": {"carbs": 55.0, "fats": 14.0, "protein": 4.0, "calories": 360.0, "potassium": 150.0, "sodium": 100.0, "saturated_fat": 11.0, "trans_fat": 0.0, "gi": 80.0}, # 1 slice
    "sapin-sapin": {"carbs": 55.0, "fats": 14.0, "protein": 4.0, "calories": 360.0, "potassium": 150.0, "sodium": 100.0, "saturated_fat": 11.0, "trans_fat": 0.0, "gi": 80.0}, 
    "pichi pichi": {"carbs": 35.0, "fats": 2.0, "protein": 1.0, "calories": 160.0, "potassium": 200.0, "sodium": 40.0, "saturated_fat": 1.0, "trans_fat": 0.0, "gi": 70.0}, # 2 small pcs (cassava/coconut)
    "pichi-pichi": {"carbs": 35.0, "fats": 2.0, "protein": 1.0, "calories": 160.0, "potassium": 200.0, "sodium": 40.0, "saturated_fat": 1.0, "trans_fat": 0.0, "gi": 70.0},
    "cassava cake": {"carbs": 48.0, "fats": 15.0, "protein": 4.0, "calories": 340.0, "potassium": 250.0, "sodium": 180.0, "saturated_fat": 10.0, "trans_fat": 0.0, "gi": 75.0}, # 1 slice
    "palitaw": {"carbs": 38.0, "fats": 4.0, "protein": 2.0, "calories": 200.0, "potassium": 80.0, "sodium": 20.0, "saturated_fat": 3.0, "trans_fat": 0.0, "gi": 80.0}, # 2 flat oval pieces
    "kutsinta": {"carbs": 32.0, "fats": 1.0, "protein": 2.0, "calories": 140.0, "potassium": 40.0, "sodium": 80.0, "saturated_fat": 0.5, "trans_fat": 0.0, "gi": 75.0}, # Already updated a better estimation
    "kalamay": {"carbs": 58.0, "fats": 12.0, "protein": 2.0, "calories": 340.0, "potassium": 160.0, "sodium": 50.0, "saturated_fat": 9.0, "trans_fat": 0.0, "gi": 80.0}, # 1 sticky serving
    "bilo bilo": {"carbs": 55.0, "fats": 15.0, "protein": 4.0, "calories": 360.0, "potassium": 400.0, "sodium": 100.0, "saturated_fat": 12.0, "trans_fat": 0.0, "gi": 70.0}, 

    # Massive Global Food Import
    "ants climbing a tree": {"carbs": 25, "fats": 12, "protein": 8, "calories": 240, "potassium": 150, "sodium": 650, "saturated_fat": 3, "trans_fat": 0, "gi": 45},
    "baked potato": {"carbs": 21, "fats": 0.1, "protein": 2, "calories": 93, "potassium": 391, "sodium": 10, "saturated_fat": 0, "trans_fat": 0, "gi": 85},
    "baozi": {"carbs": 35, "fats": 8, "protein": 10, "calories": 250, "potassium": 150, "sodium": 300, "saturated_fat": 2, "trans_fat": 0, "gi": 70},
    "beetroot": {"carbs": 10, "fats": 0.2, "protein": 1.6, "calories": 43, "potassium": 325, "sodium": 78, "saturated_fat": 0, "trans_fat": 0, "gi": 64},
    "brussels sprouts": {"carbs": 9, "fats": 0.3, "protein": 3.4, "calories": 43, "potassium": 389, "sodium": 25, "saturated_fat": 0.1, "trans_fat": 0, "gi": 15},
    "chamomile tea": {"carbs": 0.2, "fats": 0, "protein": 0, "calories": 1, "potassium": 9, "sodium": 1, "saturated_fat": 0, "trans_fat": 0, "gi": 0},
    "oolong tea": {"carbs": 0, "fats": 0, "protein": 0, "calories": 1, "potassium": 12, "sodium": 3, "saturated_fat": 0, "trans_fat": 0, "gi": 0},
    "cranberry juice": {"carbs": 12, "fats": 0.1, "protein": 0.4, "calories": 46, "potassium": 77, "sodium": 2, "saturated_fat": 0, "trans_fat": 0, "gi": 50},
    "apple juice": {"carbs": 11, "fats": 0.1, "protein": 0.1, "calories": 46, "potassium": 101, "sodium": 4, "saturated_fat": 0, "trans_fat": 0, "gi": 40},
    "almond milk": {"carbs": 0.3, "fats": 1.1, "protein": 0.4, "calories": 15, "potassium": 16, "sodium": 73, "saturated_fat": 0.1, "trans_fat": 0, "gi": 25},
    "coconut milk": {"carbs": 3, "fats": 21, "protein": 2, "calories": 197, "potassium": 263, "sodium": 15, "saturated_fat": 19, "trans_fat": 0, "gi": 45},
    "soy milk": {"carbs": 3.3, "fats": 1.8, "protein": 3.3, "calories": 43, "potassium": 141, "sodium": 34, "saturated_fat": 0.2, "trans_fat": 0, "gi": 34},
    "chimichanga": {"carbs": 25, "fats": 15, "protein": 12, "calories": 280, "potassium": 250, "sodium": 650, "saturated_fat": 5, "trans_fat": 0, "gi": 65},
    "chocolate chip cookie": {"carbs": 65, "fats": 23, "protein": 5, "calories": 490, "potassium": 150, "sodium": 350, "saturated_fat": 11, "trans_fat": 0.2, "gi": 75},
    "oatmeal raisin cookie": {"carbs": 68, "fats": 15, "protein": 6, "calories": 430, "potassium": 250, "sodium": 300, "saturated_fat": 6, "trans_fat": 0, "gi": 60},
    "cracker": {"carbs": 70, "fats": 15, "protein": 8, "calories": 450, "potassium": 100, "sodium": 800, "saturated_fat": 5, "trans_fat": 0.1, "gi": 70},
    "bok choy": {"carbs": 2.2, "fats": 0.2, "protein": 1.5, "calories": 13, "potassium": 252, "sodium": 65, "saturated_fat": 0, "trans_fat": 0, "gi": 15},
    "bagel": {"carbs": 50, "fats": 1.5, "protein": 10, "calories": 250, "potassium": 120, "sodium": 450, "saturated_fat": 0.3, "trans_fat": 0, "gi": 70},
    "cornbread": {"carbs": 45, "fats": 12, "protein": 6, "calories": 300, "potassium": 150, "sodium": 650, "saturated_fat": 3, "trans_fat": 0, "gi": 75},
    "garlic bread": {"carbs": 40, "fats": 15, "protein": 8, "calories": 330, "potassium": 120, "sodium": 550, "saturated_fat": 4, "trans_fat": 0.1, "gi": 70},
    "banana bread": {"carbs": 52, "fats": 10, "protein": 4, "calories": 310, "potassium": 180, "sodium": 350, "saturated_fat": 2, "trans_fat": 0, "gi": 65},
    "croissant": {"carbs": 45, "fats": 21, "protein": 8, "calories": 400, "potassium": 118, "sodium": 400, "saturated_fat": 12, "trans_fat": 0.5, "gi": 70},
    "baguette": {"carbs": 55, "fats": 1.4, "protein": 10, "calories": 270, "potassium": 110, "sodium": 600, "saturated_fat": 0.3, "trans_fat": 0, "gi": 75},
    "pretzel": {"carbs": 80, "fats": 3, "protein": 10, "calories": 380, "potassium": 100, "sodium": 1200, "saturated_fat": 0.5, "trans_fat": 0, "gi": 80},
    "toast": {"carbs": 50, "fats": 4, "protein": 10, "calories": 280, "potassium": 130, "sodium": 420, "saturated_fat": 1, "trans_fat": 0, "gi": 75},
    "naan": {"carbs": 50, "fats": 6, "protein": 9, "calories": 290, "potassium": 100, "sodium": 450, "saturated_fat": 2, "trans_fat": 0, "gi": 70},
    "baked beans": {"carbs": 25, "fats": 1.5, "protein": 6, "calories": 140, "potassium": 350, "sodium": 420, "saturated_fat": 0.2, "trans_fat": 0, "gi": 40},
    "burrito": {"carbs": 30, "fats": 10, "protein": 12, "calories": 250, "potassium": 280, "sodium": 550, "saturated_fat": 4, "trans_fat": 0, "gi": 60},
    "sauerkraut": {"carbs": 4, "fats": 0.1, "protein": 0.9, "calories": 19, "potassium": 170, "sodium": 660, "saturated_fat": 0, "trans_fat": 0, "gi": 15},
    "cheesecake": {"carbs": 25, "fats": 22, "protein": 5, "calories": 320, "potassium": 90, "sodium": 300, "saturated_fat": 13, "trans_fat": 0.5, "gi": 50},
    "carrot cake": {"carbs": 45, "fats": 20, "protein": 4, "calories": 380, "potassium": 150, "sodium": 350, "saturated_fat": 6, "trans_fat": 0, "gi": 60},
    "red velvet cake": {"carbs": 52, "fats": 18, "protein": 4, "calories": 390, "potassium": 120, "sodium": 380, "saturated_fat": 8, "trans_fat": 0, "gi": 70},
    "cupcake": {"carbs": 55, "fats": 16, "protein": 3, "calories": 380, "potassium": 80, "sodium": 320, "saturated_fat": 7, "trans_fat": 0.5, "gi": 70},
    "white chocolate": {"carbs": 59, "fats": 32, "protein": 6, "calories": 540, "potassium": 280, "sodium": 90, "saturated_fat": 19, "trans_fat": 0, "gi": 45},
    "pancake": {"carbs": 28, "fats": 10, "protein": 6, "calories": 220, "potassium": 130, "sodium": 400, "saturated_fat": 2, "trans_fat": 0.1, "gi": 65},
    "brie": {"carbs": 0.5, "fats": 28, "protein": 21, "calories": 334, "potassium": 150, "sodium": 620, "saturated_fat": 17, "trans_fat": 0.5, "gi": 0},
    "feta": {"carbs": 4.1, "fats": 21, "protein": 14, "calories": 264, "potassium": 62, "sodium": 1116, "saturated_fat": 15, "trans_fat": 0, "gi": 0},
    "blue cheese": {"carbs": 2.3, "fats": 29, "protein": 21, "calories": 353, "potassium": 256, "sodium": 1395, "saturated_fat": 19, "trans_fat": 0.5, "gi": 0},
    "butter chicken": {"carbs": 5, "fats": 14, "protein": 16, "calories": 200, "potassium": 250, "sodium": 550, "saturated_fat": 6, "trans_fat": 0, "gi": 25},
    "peking duck": {"carbs": 3, "fats": 28, "protein": 18, "calories": 330, "potassium": 200, "sodium": 350, "saturated_fat": 9, "trans_fat": 0, "gi": 0},
    "donuts": {"carbs": 50, "fats": 25, "protein": 5, "calories": 450, "potassium": 150, "sodium": 300, "saturated_fat": 12, "trans_fat": 1, "gi": 75},
    "wonton": {"carbs": 25, "fats": 10, "protein": 12, "calories": 240, "potassium": 180, "sodium": 500, "saturated_fat": 3, "trans_fat": 0, "gi": 55},
    "cantaloupe": {"carbs": 8, "fats": 0.2, "protein": 0.8, "calories": 34, "potassium": 267, "sodium": 16, "saturated_fat": 0, "trans_fat": 0, "gi": 65},
    "watermelon": {"carbs": 7.6, "fats": 0.2, "protein": 0.6, "calories": 30, "potassium": 112, "sodium": 1, "saturated_fat": 0, "trans_fat": 0, "gi": 72},
    "avocado": {"carbs": 8.5, "fats": 14.7, "protein": 2, "calories": 160, "potassium": 485, "sodium": 7, "saturated_fat": 2.1, "trans_fat": 0, "gi": 15},
    "mango": {"carbs": 15, "fats": 0.4, "protein": 0.8, "calories": 60, "potassium": 168, "sodium": 1, "saturated_fat": 0.1, "trans_fat": 0, "gi": 51},
    "raspberry": {"carbs": 12, "fats": 0.7, "protein": 1.2, "calories": 52, "potassium": 151, "sodium": 1, "saturated_fat": 0, "trans_fat": 0, "gi": 32},
    "blackberry": {"carbs": 10, "fats": 0.5, "protein": 1.4, "calories": 43, "potassium": 162, "sodium": 1, "saturated_fat": 0, "trans_fat": 0, "gi": 25},
    "cranberry": {"carbs": 12, "fats": 0.1, "protein": 0.4, "calories": 46, "potassium": 85, "sodium": 2, "saturated_fat": 0, "trans_fat": 0, "gi": 45},
    "poutine": {"carbs": 30, "fats": 18, "protein": 10, "calories": 350, "potassium": 450, "sodium": 850, "saturated_fat": 8, "trans_fat": 0, "gi": 70},
    "gravy": {"carbs": 8, "fats": 5, "protein": 2, "calories": 80, "potassium": 150, "sodium": 600, "saturated_fat": 2, "trans_fat": 0, "gi": 45},
    "popcorn": {"carbs": 74, "fats": 4.5, "protein": 11, "calories": 380, "potassium": 250, "sodium": 800, "saturated_fat": 0.5, "trans_fat": 0, "gi": 65},
    "kale": {"carbs": 9, "fats": 0.9, "protein": 4.3, "calories": 49, "potassium": 491, "sodium": 38, "saturated_fat": 0.1, "trans_fat": 0, "gi": 15},
    "mashed potatoes": {"carbs": 15, "fats": 4, "protein": 2, "calories": 110, "potassium": 350, "sodium": 300, "saturated_fat": 2, "trans_fat": 0, "gi": 80},
    "salami": {"carbs": 1, "fats": 35, "protein": 20, "calories": 400, "potassium": 300, "sodium": 1500, "saturated_fat": 14, "trans_fat": 0, "gi": 0},
    "pepperoni": {"carbs": 1, "fats": 44, "protein": 20, "calories": 480, "potassium": 350, "sodium": 1600, "saturated_fat": 17, "trans_fat": 0, "gi": 0},
    "bacon": {"carbs": 1.5, "fats": 40, "protein": 35, "calories": 520, "potassium": 550, "sodium": 1700, "saturated_fat": 14, "trans_fat": 0, "gi": 0},
    "buffalo wing": {"carbs": 5, "fats": 18, "protein": 15, "calories": 240, "potassium": 200, "sodium": 850, "saturated_fat": 6, "trans_fat": 0, "gi": 0},
    "sausage": {"carbs": 2, "fats": 25, "protein": 14, "calories": 300, "potassium": 250, "sodium": 900, "saturated_fat": 9, "trans_fat": 0, "gi": 0},
    "shrimp": {"carbs": 0, "fats": 1.5, "protein": 24, "calories": 120, "potassium": 260, "sodium": 110, "saturated_fat": 0.3, "trans_fat": 0, "gi": 0},
    "english muffin": {"carbs": 40, "fats": 1.5, "protein": 8, "calories": 200, "potassium": 100, "sodium": 350, "saturated_fat": 0.3, "trans_fat": 0, "gi": 75},
    "eggs": {"carbs": 1.1, "fats": 10.6, "protein": 12.6, "calories": 143, "potassium": 138, "sodium": 142, "saturated_fat": 3.1, "trans_fat": 0, "gi": 0},
    "scrambled egg": {"carbs": 1.5, "fats": 11, "protein": 10, "calories": 150, "potassium": 140, "sodium": 180, "saturated_fat": 3.5, "trans_fat": 0, "gi": 0},
    "omelette": {"carbs": 2, "fats": 12, "protein": 11, "calories": 160, "potassium": 150, "sodium": 200, "saturated_fat": 4, "trans_fat": 0, "gi": 0},
    "oatmeal": {"carbs": 12, "fats": 1.5, "protein": 2.5, "calories": 70, "potassium": 60, "sodium": 5, "saturated_fat": 0.2, "trans_fat": 0, "gi": 55},
    "onion rings": {"carbs": 40, "fats": 25, "protein": 5, "calories": 400, "potassium": 250, "sodium": 600, "saturated_fat": 4, "trans_fat": 0, "gi": 65},
    "mac and cheese": {"carbs": 25, "fats": 12, "protein": 8, "calories": 250, "potassium": 150, "sodium": 450, "saturated_fat": 7, "trans_fat": 0, "gi": 60},
    "apple pie": {"carbs": 35, "fats": 15, "protein": 2.5, "calories": 280, "potassium": 110, "sodium": 250, "saturated_fat": 7, "trans_fat": 0, "gi": 65},
    "key lime pie": {"carbs": 42, "fats": 18, "protein": 6, "calories": 350, "potassium": 150, "sodium": 300, "saturated_fat": 9, "trans_fat": 0, "gi": 60},
    "blt": {"carbs": 25, "fats": 20, "protein": 12, "calories": 330, "potassium": 350, "sodium": 850, "saturated_fat": 6, "trans_fat": 0, "gi": 60},
    "panini": {"carbs": 30, "fats": 12, "protein": 18, "calories": 300, "potassium": 280, "sodium": 750, "saturated_fat": 4, "trans_fat": 0, "gi": 65},
    "tomato soup": {"carbs": 7, "fats": 2, "protein": 1, "calories": 45, "potassium": 220, "sodium": 400, "saturated_fat": 0.5, "trans_fat": 0, "gi": 45},
    "taco": {"carbs": 18, "fats": 12, "protein": 10, "calories": 220, "potassium": 250, "sodium": 450, "saturated_fat": 5, "trans_fat": 0, "gi": 55},
    "tortilla chips": {"carbs": 65, "fats": 25, "protein": 8, "calories": 500, "potassium": 200, "sodium": 450, "saturated_fat": 3, "trans_fat": 0, "gi": 70},
    "waffle": {"carbs": 33, "fats": 14, "protein": 8, "calories": 290, "potassium": 160, "sodium": 500, "saturated_fat": 3, "trans_fat": 0, "gi": 75},
    "greek yogurt": {"carbs": 4, "fats": 0.4, "protein": 10, "calories": 60, "potassium": 140, "sodium": 35, "saturated_fat": 0.1, "trans_fat": 0, "gi": 25},
    "youtiao": {"carbs": 55, "fats": 25, "protein": 8, "calories": 480, "potassium": 100, "sodium": 600, "saturated_fat": 4, "trans_fat": 0, "gi": 75},
    # Baked Goods & European Pastries
    "eclair": {"carbs": 30, "fats": 15, "protein": 6, "calories": 260, "potassium": 120, "sodium": 180, "saturated_fat": 8, "trans_fat": 0.5, "gi": 70},
    "cannoli": {"carbs": 35, "fats": 12, "protein": 8, "calories": 280, "potassium": 110, "sodium": 140, "saturated_fat": 6, "trans_fat": 0, "gi": 65},
    "macaron": {"carbs": 12, "fats": 4, "protein": 2, "calories": 90, "potassium": 40, "sodium": 15, "saturated_fat": 1, "trans_fat": 0, "gi": 75},
    "macaroon": {"carbs": 14, "fats": 6, "protein": 1, "calories": 110, "potassium": 50, "sodium": 20, "saturated_fat": 3, "trans_fat": 0, "gi": 75},
    "fruit tart": {"carbs": 42, "fats": 14, "protein": 4, "calories": 300, "potassium": 150, "sodium": 120, "saturated_fat": 7, "trans_fat": 0.5, "gi": 60},
    "pound cake": {"carbs": 45, "fats": 18, "protein": 5, "calories": 360, "potassium": 110, "sodium": 250, "saturated_fat": 9, "trans_fat": 0.5, "gi": 70},
    "angel food cake": {"carbs": 55, "fats": 0.5, "protein": 5, "calories": 250, "potassium": 150, "sodium": 650, "saturated_fat": 0.1, "trans_fat": 0, "gi": 65},
    "tiramisu slice": {"carbs": 40, "fats": 22, "protein": 6, "calories": 400, "potassium": 100, "sodium": 110, "saturated_fat": 12, "trans_fat": 0, "gi": 60},
    "tres leches": {"carbs": 48, "fats": 12, "protein": 6, "calories": 320, "potassium": 180, "sodium": 200, "saturated_fat": 6, "trans_fat": 0, "gi": 70},
    "crepe": {"carbs": 25, "fats": 12, "protein": 5, "calories": 230, "potassium": 90, "sodium": 150, "saturated_fat": 6, "trans_fat": 0, "gi": 65},
    "profiterole": {"carbs": 28, "fats": 16, "protein": 5, "calories": 270, "potassium": 110, "sodium": 160, "saturated_fat": 8, "trans_fat": 0, "gi": 70},
    "madeleine": {"carbs": 12, "fats": 5, "protein": 2, "calories": 100, "potassium": 30, "sodium": 80, "saturated_fat": 2.5, "trans_fat": 0, "gi": 75},

    # Exotics & Rare Fruits
    "dragonfruit": {"carbs": 15, "fats": 0.4, "protein": 1.2, "calories": 60, "potassium": 210, "sodium": 0, "saturated_fat": 0, "trans_fat": 0, "gi": 50},
    "starfruit": {"carbs": 7, "fats": 0.3, "protein": 1.0, "calories": 31, "potassium": 133, "sodium": 2, "saturated_fat": 0, "trans_fat": 0, "gi": 45},
    "passionfruit": {"carbs": 23, "fats": 0.7, "protein": 2.2, "calories": 97, "potassium": 348, "sodium": 0, "saturated_fat": 0, "trans_fat": 0, "gi": 30},
    "honeydew": {"carbs": 9, "fats": 0.1, "protein": 0.5, "calories": 36, "potassium": 228, "sodium": 18, "saturated_fat": 0, "trans_fat": 0, "gi": 62},
    "lychee": {"carbs": 16, "fats": 0.4, "protein": 0.8, "calories": 66, "potassium": 171, "sodium": 1, "saturated_fat": 0, "trans_fat": 0, "gi": 50},
    "fig": {"carbs": 19, "fats": 0.3, "protein": 0.8, "calories": 74, "potassium": 232, "sodium": 1, "saturated_fat": 0, "trans_fat": 0, "gi": 61},
    "dates": {"carbs": 75, "fats": 0.4, "protein": 2.5, "calories": 282, "potassium": 656, "sodium": 2, "saturated_fat": 0, "trans_fat": 0, "gi": 42},
    "persimmon": {"carbs": 18, "fats": 0.2, "protein": 0.6, "calories": 70, "potassium": 161, "sodium": 1, "saturated_fat": 0, "trans_fat": 0, "gi": 50},
    "guava": {"carbs": 14, "fats": 1.0, "protein": 2.6, "calories": 68, "potassium": 417, "sodium": 2, "saturated_fat": 0.3, "trans_fat": 0, "gi": 31},
    "jackfruit": {"carbs": 23, "fats": 0.6, "protein": 1.7, "calories": 95, "potassium": 448, "sodium": 2, "saturated_fat": 0.1, "trans_fat": 0, "gi": 75},
    "mangosteen": {"carbs": 18, "fats": 0.6, "protein": 0.6, "calories": 73, "potassium": 48, "sodium": 7, "saturated_fat": 0, "trans_fat": 0, "gi": 50},
    "rambutan": {"carbs": 21, "fats": 0.2, "protein": 0.7, "calories": 82, "potassium": 42, "sodium": 11, "saturated_fat": 0, "trans_fat": 0, "gi": 50},
    "durian": {"carbs": 27, "fats": 5.3, "protein": 1.5, "calories": 147, "potassium": 436, "sodium": 2, "saturated_fat": 0, "trans_fat": 0, "gi": 49},

    # Additional Vegetables & Root Crops
    "artichoke": {"carbs": 11, "fats": 0.2, "protein": 3.3, "calories": 47, "potassium": 370, "sodium": 94, "saturated_fat": 0, "trans_fat": 0, "gi": 15},
    "okra": {"carbs": 7, "fats": 0.2, "protein": 1.9, "calories": 33, "potassium": 299, "sodium": 7, "saturated_fat": 0, "trans_fat": 0, "gi": 20},
    "bitter gourd": {"carbs": 4, "fats": 0.2, "protein": 1.0, "calories": 17, "potassium": 296, "sodium": 5, "saturated_fat": 0, "trans_fat": 0, "gi": 15},
    "ampalaya": {"carbs": 4, "fats": 0.2, "protein": 1.0, "calories": 17, "potassium": 296, "sodium": 5, "saturated_fat": 0, "trans_fat": 0, "gi": 15},
    "sayote": {"carbs": 4.5, "fats": 0.1, "protein": 0.8, "calories": 19, "potassium": 125, "sodium": 2, "saturated_fat": 0, "trans_fat": 0, "gi": 15},
    "chayote": {"carbs": 4.5, "fats": 0.1, "protein": 0.8, "calories": 19, "potassium": 125, "sodium": 2, "saturated_fat": 0, "trans_fat": 0, "gi": 15},
    "taro": {"carbs": 26, "fats": 0.2, "protein": 1.5, "calories": 112, "potassium": 591, "sodium": 11, "saturated_fat": 0.1, "trans_fat": 0, "gi": 55},
    "yam": {"carbs": 28, "fats": 0.2, "protein": 1.5, "calories": 118, "potassium": 816, "sodium": 9, "saturated_fat": 0, "trans_fat": 0, "gi": 51},
    "parsnip": {"carbs": 18, "fats": 0.3, "protein": 1.2, "calories": 75, "potassium": 375, "sodium": 10, "saturated_fat": 0.1, "trans_fat": 0, "gi": 52},
    "rutabaga": {"carbs": 9, "fats": 0.2, "protein": 1.1, "calories": 38, "potassium": 305, "sodium": 12, "saturated_fat": 0, "trans_fat": 0, "gi": 72},
    "turnip": {"carbs": 6, "fats": 0.1, "protein": 0.9, "calories": 28, "potassium": 191, "sodium": 67, "saturated_fat": 0, "trans_fat": 0, "gi": 62},
    "water chestnut": {"carbs": 24, "fats": 0.1, "protein": 1.4, "calories": 97, "potassium": 584, "sodium": 14, "saturated_fat": 0, "trans_fat": 0, "gi": 60},
    "lotus root": {"carbs": 17, "fats": 0.1, "protein": 2.6, "calories": 74, "potassium": 556, "sodium": 40, "saturated_fat": 0, "trans_fat": 0, "gi": 33},

    # Additional Nuts & Seeds
    "chestnut": {"carbs": 44, "fats": 1.3, "protein": 1.6, "calories": 196, "potassium": 484, "sodium": 2, "saturated_fat": 0.2, "trans_fat": 0, "gi": 54},
    "brazil nut": {"carbs": 12, "fats": 66, "protein": 14, "calories": 656, "potassium": 659, "sodium": 3, "saturated_fat": 15, "trans_fat": 0, "gi": 10},
    "pine nut": {"carbs": 13, "fats": 68, "protein": 14, "calories": 673, "potassium": 597, "sodium": 2, "saturated_fat": 5, "trans_fat": 0, "gi": 15},
    "hemp seed": {"carbs": 9, "fats": 49, "protein": 31, "calories": 553, "potassium": 1200, "sodium": 5, "saturated_fat": 5, "trans_fat": 0, "gi": 4},
    "poppy seed": {"carbs": 28, "fats": 42, "protein": 18, "calories": 525, "potassium": 719, "sodium": 26, "saturated_fat": 5, "trans_fat": 0, "gi": 35},
    "mustard seed": {"carbs": 28, "fats": 36, "protein": 26, "calories": 508, "potassium": 738, "sodium": 13, "saturated_fat": 2, "trans_fat": 0, "gi": 35},

    # Salty Snacks & Meaty Bites
    "cheese puffs": {"carbs": 15, "fats": 9, "protein": 2, "calories": 150, "potassium": 40, "sodium": 260, "saturated_fat": 1.5, "trans_fat": 0, "gi": 75},
    "cheesepuffs": {"carbs": 15, "fats": 9, "protein": 2, "calories": 150, "potassium": 40, "sodium": 260, "saturated_fat": 1.5, "trans_fat": 0, "gi": 75},
    "pita chips": {"carbs": 19, "fats": 5, "protein": 3, "calories": 130, "potassium": 50, "sodium": 270, "saturated_fat": 0.5, "trans_fat": 0, "gi": 65},
    "corn chips": {"carbs": 16, "fats": 9, "protein": 2, "calories": 150, "potassium": 45, "sodium": 150, "saturated_fat": 1.5, "trans_fat": 0, "gi": 70},
    "fritos": {"carbs": 16, "fats": 9, "protein": 2, "calories": 150, "potassium": 45, "sodium": 150, "saturated_fat": 1.5, "trans_fat": 0, "gi": 70},
    "mixed nuts": {"carbs": 6, "fats": 15, "protein": 5, "calories": 170, "potassium": 160, "sodium": 110, "saturated_fat": 2, "trans_fat": 0, "gi": 15},
    "pork rinds": {"carbs": 0, "fats": 9, "protein": 17, "calories": 150, "potassium": 35, "sodium": 520, "saturated_fat": 3, "trans_fat": 0, "gi": 0},
    "chicharrones": {"carbs": 0, "fats": 9, "protein": 17, "calories": 150, "potassium": 35, "sodium": 520, "saturated_fat": 3, "trans_fat": 0, "gi": 0},
    "beef jerky": {"carbs": 3, "fats": 7, "protein": 9, "calories": 116, "potassium": 167, "sodium": 600, "saturated_fat": 3, "trans_fat": 0, "gi": 40},
    "fruit snacks": {"carbs": 21, "fats": 0, "protein": 1, "calories": 80, "potassium": 0, "sodium": 10, "saturated_fat": 0, "trans_fat": 0, "gi": 80},
    "rice cracker": {"carbs": 22, "fats": 3, "protein": 2, "calories": 120, "potassium": 40, "sodium": 250, "saturated_fat": 0.5, "trans_fat": 0, "gi": 85},

    # Deli & Cold Cuts
    "prosciutto": {"carbs": 0, "fats": 10, "protein": 8, "calories": 120, "potassium": 160, "sodium": 600, "saturated_fat": 4, "trans_fat": 0, "gi": 0},
    "ham": {"carbs": 1, "fats": 3, "protein": 6, "calories": 60, "potassium": 120, "sodium": 350, "saturated_fat": 1, "trans_fat": 0, "gi": 0},
    "turkey breast": {"carbs": 1, "fats": 1, "protein": 8, "calories": 45, "potassium": 100, "sodium": 300, "saturated_fat": 0.3, "trans_fat": 0, "gi": 0},
    "turkey ham": {"carbs": 1, "fats": 1, "protein": 8, "calories": 45, "potassium": 100, "sodium": 300, "saturated_fat": 0.3, "trans_fat": 0, "gi": 0},
    "pastrami": {"carbs": 0.5, "fats": 8, "protein": 6, "calories": 100, "potassium": 110, "sodium": 450, "saturated_fat": 3.5, "trans_fat": 0, "gi": 0},
    "bologna": {"carbs": 1, "fats": 8, "protein": 3, "calories": 90, "potassium": 50, "sodium": 280, "saturated_fat": 3, "trans_fat": 0, "gi": 0},
    "mortadella": {"carbs": 1, "fats": 8, "protein": 4, "calories": 90, "potassium": 60, "sodium": 300, "saturated_fat": 3, "trans_fat": 0, "gi": 0},

    # Cheese Additions
    "gouda": {"carbs": 0.6, "fats": 8, "protein": 7, "calories": 100, "potassium": 34, "sodium": 230, "saturated_fat": 5, "trans_fat": 0, "gi": 0},
    "provolone": {"carbs": 0.6, "fats": 7, "protein": 7, "calories": 100, "potassium": 40, "sodium": 250, "saturated_fat": 4.5, "trans_fat": 0, "gi": 0},
    "swiss cheese": {"carbs": 1.5, "fats": 8, "protein": 8, "calories": 110, "potassium": 22, "sodium": 55, "saturated_fat": 5, "trans_fat": 0, "gi": 0},
    "pepper jack": {"carbs": 0.5, "fats": 8, "protein": 7, "calories": 100, "potassium": 25, "sodium": 180, "saturated_fat": 5, "trans_fat": 0, "gi": 0},
    "edam": {"carbs": 0.4, "fats": 8, "protein": 7, "calories": 100, "potassium": 53, "sodium": 270, "saturated_fat": 5, "trans_fat": 0, "gi": 0},
    "ricotta": {"carbs": 1.5, "fats": 4, "protein": 3, "calories": 50, "potassium": 35, "sodium": 35, "saturated_fat": 2.5, "trans_fat": 0, "gi": 0},

    # Other Global Staples
    "couscous": {"carbs": 22, "fats": 0.2, "protein": 4, "calories": 112, "potassium": 58, "sodium": 5, "saturated_fat": 0, "trans_fat": 0, "gi": 65},
    "tabbouleh": {"carbs": 18, "fats": 6, "protein": 3, "calories": 130, "potassium": 200, "sodium": 180, "saturated_fat": 1, "trans_fat": 0, "gi": 50},
    "falafel": {"carbs": 15, "fats": 8, "protein": 6, "calories": 160, "potassium": 280, "sodium": 250, "saturated_fat": 1, "trans_fat": 0, "gi": 45},
    "moussaka": {"carbs": 15, "fats": 12, "protein": 8, "calories": 200, "potassium": 350, "sodium": 400, "saturated_fat": 5, "trans_fat": 0, "gi": 45},
    "spanakopita": {"carbs": 20, "fats": 15, "protein": 8, "calories": 250, "potassium": 150, "sodium": 350, "saturated_fat": 4, "trans_fat": 0, "gi": 60},

    # General Desserts
    "rice pudding": {"carbs": 25, "fats": 4, "protein": 5, "calories": 150, "potassium": 120, "sodium": 80, "saturated_fat": 2.5, "trans_fat": 0, "gi": 65},
    "bread pudding": {"carbs": 28, "fats": 6, "protein": 6, "calories": 190, "potassium": 130, "sodium": 150, "saturated_fat": 3, "trans_fat": 0, "gi": 70},
    "churros": {"carbs": 40, "fats": 18, "protein": 4, "calories": 340, "potassium": 80, "sodium": 250, "saturated_fat": 4, "trans_fat": 0, "gi": 80},
    "funnel cake": {"carbs": 42, "fats": 16, "protein": 4, "calories": 330, "potassium": 90, "sodium": 260, "saturated_fat": 3, "trans_fat": 0, "gi": 80},

    # Breakfast Cereals
    "corn flakes": {"carbs": 24, "fats": 0.5, "protein": 2, "calories": 110, "potassium": 20, "sodium": 200, "saturated_fat": 0, "trans_fat": 0, "gi": 81},
    "bran flakes": {"carbs": 23, "fats": 0.5, "protein": 3, "calories": 100, "potassium": 160, "sodium": 180, "saturated_fat": 0, "trans_fat": 0, "gi": 74},
    "frosted flakes": {"carbs": 26, "fats": 0, "protein": 1, "calories": 110, "potassium": 15, "sodium": 150, "saturated_fat": 0, "trans_fat": 0, "gi": 85},
    "cheerios": {"carbs": 20, "fats": 2, "protein": 3, "calories": 100, "potassium": 180, "sodium": 140, "saturated_fat": 0.5, "trans_fat": 0, "gi": 74},
    "froot loops": {"carbs": 26, "fats": 0.5, "protein": 1, "calories": 110, "potassium": 20, "sodium": 130, "saturated_fat": 0, "trans_fat": 0, "gi": 85},
    "cinnamon toast crunch": {"carbs": 25, "fats": 3, "protein": 1, "calories": 130, "potassium": 50, "sodium": 170, "saturated_fat": 0.5, "trans_fat": 0, "gi": 80},
    "lucky charms": {"carbs": 26, "fats": 1, "protein": 1, "calories": 110, "potassium": 30, "sodium": 150, "saturated_fat": 0.5, "trans_fat": 0, "gi": 85},
    "rice krispies": {"carbs": 26, "fats": 0, "protein": 2, "calories": 110, "potassium": 20, "sodium": 150, "saturated_fat": 0, "trans_fat": 0, "gi": 82},
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

    # 3. Plural -ies -> -y (e.g. berries -> berry)
    if query.endswith('ies') and query[:-3] + 'y' in FOOD_DB:
        return FOOD_DB[query[:-3] + 'y']
    
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
