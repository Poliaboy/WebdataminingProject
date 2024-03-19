from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD
import pandas as pd
import random
import names

# Namespace definition
NS = Namespace("http://www.leonard-and-alex-project.com/foodDelivery#")

# Create a new RDF graph
g = Graph()


# Function to sanitize input for URI creation
def sanitize_for_uri(text):
		return ''.join(e for e in text if e.isalnum())


# Load dataset
df = pd.read_csv('zomato.csv', encoding='ISO-8859-1').sample(100)

# Simplified food items by cuisine type for demonstration
food_items_by_cuisine = {
    "Italian": ["Pizza Margherita", "Spaghetti Carbonara", "Lasagna"],
    "Japanese": ["Sushi", "Ramen", "Tempura"],
    "French": ["Croissant", "Coq au vin", "Bouillabaisse"],
    "Chinese": ["Dim Sum", "Peking Duck", "Hot Pot"],
    "Indian": ["Butter Chicken", "Palak Paneer", "Chole"],
    "Seafood": ["Grilled Salmon", "Lobster Bisque", "Fish Tacos"],
    "Asian": ["Pad Thai", "Curry Laksa", "Bibimbap"],
    "European": ["Wiener Schnitzel", "Ratatouille", "Paella"],
    "Filipino": ["Adobo", "Sinigang", "Lechon"],
    "American": ["Burger", "BBQ Ribs", "Apple Pie"],
    "Korean": ["Kimchi", "Bulgogi", "Bibimbap"],
    "Cafe": ["Cappuccino", "Croissant", "Avocado Toast"],
    "Fast Food": ["Burger", "Fried Chicken", "Pizza"],
    "Bakery": ["Baguette", "Croissant", "Sourdough Bread"],
    "Brazilian": ["Feijoada", "Churrasco", "Moqueca"],
    "Pizza": ["Margherita", "Pepperoni", "Hawaiian"],
    "Arabian": ["Shawarma", "Falafel", "Hummus"],
    "Bar Food": ["Nachos", "Chicken Wings", "Burger"],
    "Mexican": ["Tacos", "Guacamole", "Chiles en Nogada"],
    "International": ["Paella", "Sushi", "Burger"],
    "Peruvian": ["Ceviche", "Lomo Saltado", "Aji de Gallina"],
    "Desserts": ["Cheesecake", "Tiramisu", "Macarons"],
    "Juices": ["Orange Juice", "Green Smoothie", "Mango Lassi"],
    "Beverages": ["Coffee", "Tea", "Smoothie"],
    "Lebanese": ["Tabbouleh", "Kebab", "Baklava"],
    "Burger": ["Cheeseburger", "Veggie Burger", "Bacon Burger"],
    "Steak": ["Ribeye Steak", "T-bone Steak", "Filet Mignon"],
    "Sushi": ["Nigiri", "Maki Rolls", "Sashimi"],
    "BBQ": ["Pulled Pork", "Brisket", "Grilled Chicken"],
    "Gourmet Fast Food": ["Gourmet Burger", "Truffle Fries", "Artisan Pizza"],
    "Vegan": ["Quinoa Salad", "Tofu Stir Fry", "Veggie Burger"],
}

delivery_companies_by_country = {}

# Function to add food items and create an offer for each restaurant
def add_food_items_and_offer(restaurant_uri, cuisine):
		if cuisine in food_items_by_cuisine:
				food_items = food_items_by_cuisine[cuisine]
				selected_items = random.sample(food_items, min(len(food_items), 3))  # Select up to 3 food items
				for food_item in selected_items:
						food_item_uri = NS[sanitize_for_uri(food_item)]
						g.add((food_item_uri, RDF.type, NS.FoodItem))
						g.add((food_item_uri, NS['hasCuisineType'], Literal(cuisine, datatype=XSD.string)))
						g.add((restaurant_uri, NS['offersFoodItem'], food_item_uri))
				
				# Create an offer for the first two selected food items
				offer_uri = NS[sanitize_for_uri("Offer_for_" + restaurant_uri.split('#')[-1])]
				g.add((offer_uri, RDF.type, NS.Offer))
				offer_description = "Special offer for " + " and ".join(selected_items[:2])
				g.add((offer_uri, NS.description,
							 Literal(offer_description, datatype=XSD.string)))  # Add this line to set a description
				for food_item in selected_items[:2]:  # Apply offer on the first two food items
						food_item_uri = NS[sanitize_for_uri(food_item)]
						g.add((offer_uri, NS.includesFoodItem, food_item_uri))


# Function to add customers with preferences corresponding to the restaurant's cuisine
def add_customers_to_restaurant(restaurant_uri, cuisine):
		# Assume that the cuisine preference is based on the primary cuisine of the restaurant
		for _ in range(2):  # Add 2 customers for each restaurant
				customer_name = names.get_full_name()
				customer_uri = NS[sanitize_for_uri(customer_name)]
				g.add((customer_uri, RDF.type, NS.Customer))
				g.add((customer_uri, NS.name, Literal(customer_name)))
				
				# Generate preference based on the restaurant's cuisine
				preference_name = "Preference_" + cuisine
				preference_uri = NS[sanitize_for_uri(preference_name)]
				g.add((preference_uri, RDF.type, NS.CuisinePreference))
				g.add((preference_uri, NS.preferredCuisine, Literal(cuisine)))
				
				# Link the customer to their preference
				g.add((customer_uri, NS.hasPreference, preference_uri))


# Function to add delivery service and delivery person per restaurant
def add_delivery_service_and_person(restaurant_uri, country_code, delivery_area):
		country_code_str = str(country_code)
		# Check if a delivery service exists for this country
		if country_code_str not in delivery_companies_by_country:
				# Create a new delivery service for this country
				delivery_service_name = "DeliveryService_" + country_code_str
				delivery_service_uri = NS[sanitize_for_uri(delivery_service_name)]
				g.add((delivery_service_uri, RDF.type, NS.DeliveryService))
				g.add((delivery_service_uri, NS.name, Literal(delivery_service_name)))
				g.add((delivery_service_uri, NS.deliveryArea, Literal(delivery_area)))
				delivery_companies_by_country[country_code_str] = delivery_service_uri
		else:
				# Use the existing delivery service for this country
				delivery_service_uri = delivery_companies_by_country[country_code_str]
		
		# Link the restaurant to the delivery service
		g.add((restaurant_uri, NS.deliveredBy, delivery_service_uri))
		g.add((delivery_service_uri, NS.deliversFor, restaurant_uri))
		
		# Generate a random name and age for the delivery person
		random_name = names.get_full_name()
		random_age = random.randint(18, 60)  # Random age between 18 and 60
		
		delivery_person_name = "DeliveryPerson_" + sanitize_for_uri(random_name)
		delivery_person_uri = NS[sanitize_for_uri(delivery_person_name)]
		g.add((delivery_person_uri, RDF.type, NS.DeliveryPerson))
		g.add((delivery_person_uri, NS.name, Literal(random_name)))
		g.add((delivery_person_uri, NS.age, Literal(random_age, datatype=XSD.int)))
		g.add((delivery_person_uri, NS.worksFor, delivery_service_uri))


# Function to create dual-role entities with additional properties
def create_dual_entities(entity_name, address, cuisine, delivery_area):
		entity_uri = NS[sanitize_for_uri(entity_name)]
		
		# Add the entity as both a Restaurant and a DeliveryService
		g.add((entity_uri, RDF.type, NS.Restaurant))
		g.add((entity_uri, RDF.type, NS.DeliveryService))
		
		# Adding common attributes
		g.add((entity_uri, NS.name, Literal(entity_name)))
		g.add((entity_uri, NS.locatedIn, Literal(address)))
		g.add((entity_uri, NS.servesCuisine, Literal(cuisine)))
		g.add((entity_uri, NS.deliveryArea, Literal(delivery_area)))


# Example of creating dual-role entities with additional properties
create_dual_entities("PizzaPlaceAndDelivery", "123 Pizza St, Pizzatown", "Italian", "Pizzatown and surrounding areas")
create_dual_entities("SushiSpotExpress", "456 Sushi Rd, Sushiburg", "Japanese", "Sushiburg and nearby neighborhoods")
create_dual_entities("BurgerGrillCourier", "789 Burger Blvd, Burgercity", "American", "Burgercity and adjacent areas")

# Main loop to process restaurants
for index, row in df.iterrows():
		restaurant_name = sanitize_for_uri(row['Restaurant Name'])
		restaurant_uri = NS[restaurant_name + "_" + str(row['Restaurant ID'])]
		g.add((restaurant_uri, RDF.type, NS.Restaurant))
		g.add((restaurant_uri, NS.name, Literal(row['Restaurant Name'], datatype=XSD.string)))
		g.add((restaurant_uri, NS.locatedIn, Literal(row['City'], datatype=XSD.string)))
		g.add((restaurant_uri, NS.servesCuisine, Literal(row['Cuisines'], datatype=XSD.string)))
		cuisine = row['Cuisines'].split(", ")[0] if pd.notnull(row['Cuisines']) else "Various"
		country = row['Country Code'] if pd.notnull(row['Country Code']) else "Unknown"
		delivery_area = row['City'] + " and surrounding areas"
		
		add_food_items_and_offer(restaurant_uri, cuisine)
		add_customers_to_restaurant(restaurant_uri, cuisine)
		add_delivery_service_and_person(restaurant_uri, country, delivery_area)

# Serializing the graph to RDF/XML
output_path = 'FoodDelivery.owl'
g.serialize(destination=output_path, format='pretty-xml')
print(f"RDF data generated and saved to: {output_path}")
