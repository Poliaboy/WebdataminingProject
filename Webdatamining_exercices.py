from rdflib import Graph, RDF, Namespace, Literal
from rdflib.plugins.sparql import prepareQuery

# Define your namespace
NS = Namespace("http://www.leonard-and-alex-project.com/foodDelivery#")

# Initialize the graph
g = Graph()

# Load the ontology structure
ontology_path = "ontology.owl"
g.parse(ontology_path, format="xml")

# Load the instance data
data_path = "FoodDelivery.owl"
g.parse(data_path, format="xml")

# Exercise 1
print("Exercise 1")
for customer in g.subjects(RDF.type, NS.Customer):
    name = g.value(customer, NS.name)
    print(f"Person Name: {name} (Type: Customer)")
for delivery_person in g.subjects(RDF.type, NS.DeliveryPerson):
    name = g.value(delivery_person, NS.name)
    print(f"Person Name: {name} (Type: Delivery Person)")
		
# Exercise 2
print("Exercise 2")
query = """
PREFIX ns: <http://www.leonard-and-alex-project.com/foodDelivery#>
SELECT ?name ?type WHERE {
  {
    ?person a ns:Customer.
    BIND("Customer" AS ?type)
  } UNION {
    ?person a ns:DeliveryPerson.
    BIND("Delivery Person" AS ?type)
  }
  ?person ns:name ?name.
}
"""

for row in g.query(query):
    print(f"Person Name: {row.name} (Type: {row.type})")



#Execice 3
print("Exercise 3")
for restaurant in g.subjects(RDF.type, NS.Restaurant):
    offers_food_items = g.objects(restaurant, NS.offersFoodItem)
    for food_item in offers_food_items:
        if "Italian" in str(g.value(food_item, NS.hasCuisineType)):
            print(f"Italian Restaurant: {g.value(restaurant, NS.name)}")

# Exercise 4
print("Exercise 4")

# The food item we're interested in, sanitized to match the URI format
food_name = "Pizza Margherita"
sanitized_food_name = food_name.replace(" ", "")  # Assuming your sanitation logic is similar to your data example
food_uri = NS[sanitized_food_name]  # Construct the URI directly based on naming convention
print("Fot the food item: ", food_uri)
# Check if the food item exists in the graph
if (food_uri, RDF.type, NS.FoodItem) in g:
    # Now find restaurants that offer this food item
    restaurants = g.subjects(NS.offersFoodItem, food_uri)
    for restaurant in restaurants:
        restaurant_name = g.value(restaurant, NS.name)  # Assuming you have a 'name' property for restaurants
        print(f"Restaurant: {restaurant_name}")

        # For each restaurant, find the delivery services
        delivery_services = g.subjects(NS.deliversFor, restaurant)  # Adjusted line
        for service in delivery_services:
            print(f"Delivery Service: {g.value(service, NS.name)}")

        # Find offers that include this food item (if this is a relevant query for your data)
        offers = g.subjects(NS.includesFoodItem, food_uri)
        for offer in offers:
            offer_description = g.value(offer, NS.description)  # Assuming offers have a 'description' property
            print(f"Offer: {offer_description}")
else:
    print(f"Error: Food item {food_name} does not exist.")
    
# Exercise 5
print("Exercise 5")
query_str = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX ns: <http://www.leonard-and-alex-project.com/foodDelivery#>

    SELECT ?entity
    WHERE {
        ?entity rdf:type ns:Restaurant ;
                rdf:type ns:DeliveryService .
    }
"""

# Prepare and execute the SPARQL query
query = prepareQuery(query_str)
results = g.query(query)

# Display the results
for row in results:
    print(row["entity"])
    
# Exos sparql
# A function to execute and print results of a query
def execute_sparql_query(graph, query, message, query_type="SELECT"):
    
    print(f"--- {message} ---")
    if query_type == "SELECT":
        for row in g.query(query):
            print(row)
    elif query_type == "ASK":
        result = g.query(query)
        print(bool(result))
    elif query_type in ["CONSTRUCT", "DESCRIBE"]:
        result = g.query(query)
        for stmt in result:
            print(stmt)
    print("\n")

q1 = """
PREFIX ns: <http://www.leonard-and-alex-project.com/foodDelivery#>
SELECT ?foodProduct ?offer ?customer
WHERE {
  ?foodProduct rdf:type ns:FoodItem .
  ?offer rdf:type ns:Offer .
  ?customer rdf:type ns:Customer .
}
"""

q2 = """
PREFIX ns: <http://www.leonard-and-alex-project.com/foodDelivery#>
SELECT ?restaurantName
WHERE {
  ?restaurant rdf:type ns:Restaurant.
  ?restaurant ns:locatedIn ?location.
  ?restaurant ns:name ?restaurantName.
  FILTER (LCASE(STR(?location)) = "new delhi")
}

"""

q3 = """
PREFIX ns: <http://www.leonard-and-alex-project.com/foodDelivery#>
SELECT ?restaurantName ?deliveryService
WHERE {
  ?restaurant rdf:type ns:Restaurant ;
              ns:servesCuisine ?cuisine ;
              ns:name ?restaurantName .
  FILTER ( ?cuisine = "Bakery" )
  OPTIONAL { ?restaurant ns:deliveredBy ?deliveryService . }
}
"""


q4 = """
PREFIX ns: <http://www.leonard-and-alex-project.com/foodDelivery#>
SELECT ?deliverymanName
WHERE {
  ?deliveryman rdf:type ns:DeliveryPerson ;
               ns:age ?age ;
               ns:worksFor ?deliveryService .
  ?deliveryService ns:deliveryArea ?deliveryArea .
  ?deliveryman ns:name ?deliverymanName .
  FILTER (?age > 18)
  FILTER (LCASE(STR(?deliveryArea)) = "new delhi and surrounding areas")
}
"""

q5 = """
PREFIX ns: <http://www.leonard-and-alex-project.com/foodDelivery#>
SELECT ?restaurantName ?location
WHERE {
  ?restaurant rdf:type ns:Restaurant ;
              ns:name ?restaurantName ;
              ns:servesCuisine ?cuisine ;
              ns:locatedIn ?location .
FILTER ( ?cuisine = "Italian" )
}

"""

q6 = """
PREFIX ns: <http://www.leonard-and-alex-project.com/foodDelivery#>
SELECT ?restaurant ?manager ?chef
WHERE {
  ?restaurant rdf:type ns:Restaurant .
  OPTIONAL { ?restaurant ns:managedBy ?manager . }
  OPTIONAL { ?restaurant ns:hasChef ?chef . }
}
"""

q7 = """
PREFIX ns: <http://www.leonard-and-alex-project.com/foodDelivery#>

SELECT ?item
WHERE {
  {
    ?item rdf:type ns:FoodItem .
  } UNION {
    ?item rdf:type ns:Offer .
  }
}
"""

q8 = """
PREFIX ns: <http://www.leonard-and-alex-project.com/foodDelivery#>
CONSTRUCT {
  ?restaurant ns:offersCuisine ?cuisine .
}
WHERE {
  ?restaurant rdf:type ns:Restaurant ;
              ns:servesCuisine ?cuisine .
}
"""

q9 = """
PREFIX ns: <http://www.leonard-and-alex-project.com/foodDelivery#>
ASK {
  ?restaurant rdf:type ns:Restaurant ;
              ns:locatedIn ?location .
            FILTER (LCASE(STR(?location)) = "gurgaon")
}
"""

q10 = """
PREFIX ns: <http://www.leonard-and-alex-project.com/foodDelivery#>

DESCRIBE <http://www.leonard-and-alex-project.com/foodDelivery#Restaurant>

"""



# Execute and print results for each query
execute_sparql_query(g, q1, "Instances of Food Products, Offers, and Customers")
execute_sparql_query(g, q2, "Names of All New Dehli Restaurants")
execute_sparql_query(g, q3, "Names of All Bakery Restaurants and Their Delivery Services")
execute_sparql_query(g, q4, "Deliverymen Older Than 51 Years Delivering in New Dehli")
execute_sparql_query(g, q5, "Restaurants Serving Italian Food for a Specific Day")
execute_sparql_query(g, q6, "Query with Optional Graph Patterns")
execute_sparql_query(g, q7, "Query with Alternatives and Conjunctions")
execute_sparql_query(g, q8, "Construct Query Example", query_type="CONSTRUCT")
execute_sparql_query(g, q9, "Ask Query Example", query_type="ASK")
execute_sparql_query(g, q10, "Describe Query Example", query_type="DESCRIBE")
