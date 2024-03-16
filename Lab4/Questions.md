Part I: executing SPARQL queries using a given program


Load the family ontology you have defined Check the checkbox �with OWL inference�.

If you don�t have a version of the family ontology you can use this family.owl.



Write and execute SPARQL queries to response to the following:

List the instances of the class Son
List the instances of the class Daughter
List the instances of the class Parent
List the instances of the class Father
List the instances of the class Mother
List the instances of the class Grandmother
List the instances of the class Grandfather
List the instances of the class Brother
List the instances of the class Sister
OPTIONAL: if the result is empty, rewrite a more complex SPARQL query, or an SWRL rule to return non empty result if possible



Write and execute SPARQL queries (several conditions in WHERE) to response to the following:



List (name, age) of children of Peter
List of persons whose father is more that 40 years old
List (name, age) of all French citizens. For each one, if he/she is married, display the name of his wife/her husband
List of the name of persons who are brother of someone
List of the name of persons who are daughter of someone
List of the name of persons who are uncle of someone
List of the name of persons who are married

Part 2: Programming using the Jena API


-        Download this version of Jena

-        Launch Eclipse

-        Create a new Java project

-        Create a new folder called data

-        Create the file owlrules.txt in the folder data (content is given below)

-        Create the file rules.txt in the folder data (content is given below)

-        Create the file query.txt in the folder data (content is given below)

-        Create the file family.owl in the folder data

-        Create a new package tools

-        Open the menu Project/Properties/Java Build Path. In the tab Libraries, click on add external jars. Add all the lib of Jena (see the folder in which Jena is installed).

-        Create a new class FileTool in tools package

-        Create a new class JenaEngine in tools package

-        Create a new package applications

-        Create a new class Main in application package

-        Execute the Main class





File owlrules.txt
@include <OWLMicro>.

File ourrules.txt
@prefix ns: <http://www.owl-ontologies.com/unnamed.owl#>.

@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.



[rule1: (?per rdf:type ns:Person) (?per ns:age ?age) greaterThan(?age, 60)-> (?per rdf:type ns:PersonneAge)]

File query.txt
PREFIX ns: <http://www.owl-ontologies.com/unnamed.owl#>

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?user ?age

WHERE {

?user rdf:type ns:PersonneAge.

?user ns:age ?age.

}





-        Create query files that correspond to query from Part1 of this lab. Modify the Main class to refer to these query (one by one) and execute the Main program (compare the results with the ones obtained in Part 1)

-        Add a new functionality in the JenaEngine class that allows to read the value of property of type ObjectType (see the javadoc of the Jena API)

-        Add a new functionality in the JenaEngine class that allows to read the value of property of type DataType (see the javadoc of the Jena API)

-        Create a new class in the application package that

a.    Read a name of a person

b.    Display his/her parents, brothers and sisters.

c.    If this person is married, display the name and age of her husband/his wife

d.    If this person is not married Display all the persons

�  whose gender is different,

�  whose age is close (+/- 5 years) and

�  is not married