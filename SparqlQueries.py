from rdflib import Graph, RDF, Namespace, Literal
from rdflib.plugins.sparql import prepareQuery

# Define your namespace
NS = Namespace("http://www.leonard-and-alex-project.com/foodDelivery#")

# Initialize the graph
g = Graph()

# Load the ontology structure
ontology_path = "ontology.owl"
g.parse(ontology_path, format="xml")


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
