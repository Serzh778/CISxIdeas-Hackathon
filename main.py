from personalization_algorithm import GoxipPersonalizationAlgorithm
from product_recommendation_algorithm import GoxipProductRecommendationAlgorithm

#sample database
product_database = [
    {'id': 1, 'name': 'Product 1', 'clothing_types': ['casual'], 'preferred_brands': ['Brand A']},
    {'id': 2, 'name': 'Product 2', 'clothing_types': ['formal'], 'preferred_brands': ['Brand B']},
    {'id': 3, 'name': 'Product 3', 'clothing_types': ['sportswear'], 'preferred_brands': ['Brand A']},

]

personalization_algorithm = GoxipPersonalizationAlgorithm()

# Simulate user activities and update preferences
personalization_algorithm.update_preferences("user1", "filter: clothing_types: casual")
personalization_algorithm.update_preferences("user1", "filter: preferred_brands: Brand A")

# Create the product recommendation algorithm instance
recommendation_algorithm = GoxipProductRecommendationAlgorithm(product_database, personalization_algorithm)

# Suggest products for the user
suggested_products = recommendation_algorithm.suggest_products("user1", 3)

print("Suggested products:")
for product in suggested_products:
    print(product['name'])
