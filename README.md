Project
Web datamining & semantics Project
The Semantic Web project is a large and long practical exercise that consists in integrating all the pieces that have been seen during the first sessions into a consolidated application. To make sure you can advance sufficiently fast to cover everything, you will work by pair.   

Main objectives

Design a food delivery discovery service : We will describe different kinds of entities that are useful for the food delivery discovery service: food products, offers for the food items (including a single item or combos), restaurants and businesses that offer the food items; delivery services (deliveryman, or company: Delivroo, Uber Eats, ...) that work with the restaurants and business to deliver their food items; customers with their customers’s preferences.
Develop an application that provide, given a customer’s description, the place where to order food at the time of request.
Pedagogical objectives

Do a little software development, using Semantic Web programming frameworks
Setup and interact with an RDF database
Exploit multiple sources of heterogeneous data
Present information online with rich metadata

Part I: Modeling the ontology

In this part, we aim to create an ontology, using the Protégé editor, which models the food delivery discovery schema in terms of classes hierarchy, properties and restrictions.  

Indications :

Define different class and propertie hiearchies (at leat three hiearchies and three restrictions)
Define different class restrictions (eg. disjoint, existential and universal restrictions and other conditions on defined classes, ...)  (at leat three)
Define at leat three different type  of the properties (transitive, symmetric, inverseOf, etc.) if necessary.
You application should follows the Linked Data principles:
As a starting point, individuals are recommeded to be described as instances of classes in Schema.org  schemaorg.owl. For instance, food products, be instances of schema:Product; 
User preferences with respect to location, time, price range and, optionally, type of food should be stored in the Linked Data Platform. An example of preferences is provided in the pref-charpenay resource.
The data of the service should be available online and represented in a standard vocabulary that any application can process. 
Check the consistency of your ontology with PELLET
Part II: Populating the ontology
You will populate you knowledge phase by :

Manually: RDF instances that you could be manually created  in Protégé
Other sources: From non-RDF formats, you convert online available  data (from open data sources, see bellow) into RDF, and load the resulting data. You can simply generate an RDF file that you load it manually, or (better) add the RDF programmatically using SPARQL Update queries. You need for instance to add Json Context to the different available Json files from open data sources, such us :
CoopCycle 
CoopCycle is a federation of bike delivery coops, all over the world. Bike delivery coops are associations of cyclist who propose their service to restaurants and other businesses to deliver products to customers at home. From this page, you will have to find a JSON document that describes all the coops of this federation. Hint: use advanced capabilities of your browser.
From the JSON file found from the web page above, it is possible to find the URIs of each coop, usually associated with a city or agglomeration. From there, CoopCycle exposes information in JSON-LD about local businesses whose products are delivered by the coop. To collect that information, you will have to write an HTML parser that is able to navigate and/or to extract JSON-LD.

Part III: Querying the ontology
Write SPARQL queries to response to the following:

List the instances of the class food products, offers and customers
List the name of all Paris restaurants.
List the name of all vegetarian restaurant, for each one, display their delivery services
List the name of deliverymen older than 51 years and thay can deliver in Lyon in less that 15 minutes
List of restaurant that serve Italian food for a specific day and where and until when
Propose 5 SPARQL queries:

A query that contains at least 2 Optional Graph Patterns
A query that contains at least 2 alternatives and conjunctions
A query that contains a CONSTRUCT query form
A query that contains an ASK query form
A query that contains a DESCRIBE query form
 

Part IV: Manipulating the ontology using Jena
 

Using Jena develop the following functionalities that:

Loads the ontology and displays all the Persons (without using queries, without inference).
Loads the ontology and displays all the Persons (using a query, without inference). Create the used query in text file under the data folder.
Loads the ontology and displays all the Restaurants serving Italian food (without using queries, using inference).
Develops a program that :
Reads a name of a food
If it doesn’t exist displays an error message
Else, display its restaurants, delivery services, and offers
Display their availability where and when
Displays all entities that are restaurant and delivery compagny. Do this using a rule that defines a new class RestDelivery. The rule file must be saved in the data folder.
Specifies 3 different rules and implement them in a java program
These instructions assume that you are programming in Java, preferably with Eclipse, using the Apache Jena libraries. You may also use RDF4J in Java, RDFlib in Python, or Redland RDF libary in C, or dotNetRDF in C♯, or EasyRDF for PHP, or N3.js for JavaScript, or Ruby RDF for Ruby, or SWI-Prolog Semantic Web Library, etc.



Work to send:


You will be working on your project full time during the remaining sessions.
On your last course session, you will deliver all of your working files, and give a presentation and a demo. You must additionally provide a written report explaining your choices, the functionalities, etc. A deadline will be specified later by your professors. Everything that comes after this deadline will be rejected as if nothing was delivered.
Create an archive name1-name2-name3.zip with:

The *.owl file generated by Protégé (part I and II)
A (*.txt or *.doc) file containing the SPARQL queries (part III)
The eclipse src and data folders of (part IV and V)
The presentation file *.ppt
Upload you archive in DVO deposit;
