from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, XSD, FOAF

# Load the OWL ontology
g = Graph()
g.parse("familyR.owl", format="xml")  # Adjust the file name as necessary

# Namespace definition based on your OWL ontology
NS = Namespace("http://www.owl-ontologies.com/unnamed.owl#")
g.bind("ont", NS)


# Helper function to execute and print results of a SPARQL query
def execute_sparql(query):
		for row in g.query(query):
				print(row)


# Queries
queries = {
    "Son": """
        PREFIX ont: <http://www.owl-ontologies.com/unnamed.owl#>
        SELECT ?individual WHERE { ?individual ont:isSonOf ?parent . }
    """,
    "Daughter": """
        PREFIX ont: <http://www.owl-ontologies.com/unnamed.owl#>
        SELECT ?individual WHERE { ?individual ont:isDaughterOf ?parent . }
    """,
    "Parent (generic, based on having any child)": """
        PREFIX ont: <http://www.owl-ontologies.com/unnamed.owl#>
        SELECT DISTINCT ?parent WHERE {
            { ?child ont:isSonOf ?parent . }
            UNION
            { ?child ont:isDaughterOf ?parent . }
        }
    """,
    "Father": """
    PREFIX ont: <http://www.owl-ontologies.com/unnamed.owl#>
    SELECT ?father WHERE {
        { ?child ont:isSonOf ?father . ?father a ont:Male . }
        UNION
        { ?child ont:isDaughterOf ?father . ?father a ont:Male . }
    }
		""",
		"Mother": """
				PREFIX ont: <http://www.owl-ontologies.com/unnamed.owl#>
				SELECT ?mother WHERE {
						{ ?child ont:isSonOf ?mother . ?mother a ont:Female . }
						UNION
						{ ?child ont:isDaughterOf ?mother . ?mother a ont:Female . }
				}
		""",
    "Grandmother": """
    PREFIX ont: <http://www.owl-ontologies.com/unnamed.owl#>
    SELECT DISTINCT ?grandmother WHERE {
        ?parent ont:isChildOf ?grandmother .
        ?child ont:isChildOf ?parent .
        ?grandmother a ont:Female .
    }
		""",

		"Grandfather": """
    PREFIX ont: <http://www.owl-ontologies.com/unnamed.owl#>
    SELECT DISTINCT ?grandfather WHERE {
        ?parent ont:isChildOf ?grandfather .
        ?child ont:isChildOf ?parent .
        ?grandfather a ont:Male .
    }
""",

"Brother": """
    PREFIX ont: <http://www.owl-ontologies.com/unnamed.owl#>
    SELECT DISTINCT ?brother WHERE {
        ?child ont:isChildOf ?parent .
        ?brother ont:isChildOf ?parent .
        ?brother a ont:Male .
        FILTER(?child != ?brother)
    }
		""",

		"Sister": """
    PREFIX ont: <http://www.owl-ontologies.com/unnamed.owl#>
    SELECT DISTINCT ?sister WHERE {
        ?child ont:isChildOf ?parent .
        ?sister ont:isChildOf ?parent .
        ?sister a ont:Female .
        FILTER(?child != ?sister)
    }
	"""
}

# Execute queries
for description, query in queries.items():
		print(description)
		execute_sparql(query)
		print("\n")


# Functionality to read object and datatype properties of individuals
def read_properties(individual_uri):
		individual = URIRef(individual_uri)
		print(f"Properties of individual: {individual}")
		
		# Read and print all properties of the individual
		for p, o in g.predicate_objects(individual):
				print(f"Property: {p}, Value: {o}")


def display_family_and_marital_status_and_potential_matches(individual_id):
    individual_uri = URIRef(f"{NS}{individual_id}")

    print(f"Information for {individual_id}:")

    # Determine the gender of the individual
    gender = "Male" if (individual_uri, RDF.type, NS.Male) in g else "Female"
    print(f"Gender: {gender}")

    # Display Parents (assuming gender-specific properties for parent-child relationships)
    parent_predicates = [NS.isSonOf, NS.isDaughterOf] if gender == "Male" else [NS.isDaughterOf, NS.isSonOf]
    parents = set()
    for predicate in parent_predicates:
        for parent in g.objects(individual_uri, predicate):
            parents.add(parent)
            print(f"Parent: {parent}")

    # Display Siblings directly using the isSiblingOf property
    siblings = set(g.objects(individual_uri, NS.isSiblingOf))
    for sibling in siblings:
        sibling_name = g.value(sibling, NS.name)
        print(f"Sibling: {sibling_name if sibling_name else sibling}")

    # Check Marital Status
    spouse = g.value(individual_uri, NS.isMarriedWith, None)
    if spouse:
        spouse_name = g.value(spouse, NS.name, None)
        spouse_age = g.value(spouse, NS.age, None)
        print(f"Married to: {spouse_name if spouse_name else spouse}, Age: {spouse_age}")
    else:
        print(f"{individual_id} is not married.")
        # Display potential matches considering unmarried individuals of the opposite gender within a 5-year age difference
        potential_matches = find_potential_matches(individual_uri, gender, g)
        for match in potential_matches:
            print(f"Potential match: {match}")


def find_potential_matches(individual_uri, gender, graph):
		matches = []
		individual_age = int(g.value(individual_uri, NS.age))
		
		print(f"Looking for matches for: {individual_uri}, Gender: {gender}, Age: {individual_age}")
		
		for person in graph.subjects(RDF.type, NS.Person):
				if person == individual_uri:
						continue  # Skip the same individual
				
				married = g.value(person, NS.isMarriedWith, None)
				if married:
						continue  # Skip married individuals
				
				person_gender = "Male" if (person, RDF.type, NS.Male) in graph else "Female"
				if person_gender == gender:
						continue  # Skip same gender
				
				person_age_literal = g.value(person, NS.age)
				if person_age_literal:
						person_age = int(person_age_literal)
						if abs(person_age - individual_age) <= 5:
								person_name = g.value(person, NS.name, None) or str(person)
								matches.append(f"Name: {person_name}, Age: {person_age}, Gender: {person_gender}")
		
		return matches


# Example usage
individual_uri = "http://www.owl-ontologies.com/unnamed.owl#Tom"
read_properties(individual_uri)
individual_name = "Alex"
display_family_and_marital_status_and_potential_matches(individual_name)

