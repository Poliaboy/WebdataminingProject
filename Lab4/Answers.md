To address your request, we'll proceed step by step. First, we need to formulate SPARQL queries for each of the scenarios you've outlined. Given the ontology and the types of queries you're interested in, here's how we can approach them:

### 1. List the instances of the class Son

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://www.owl-ontologies.com/unnamed.owl#>

SELECT ?son
WHERE {
  ?son rdf:type :Son .
}
```

### 2. List the instances of the class Daughter

```sparql
SELECT ?daughter
WHERE {
  ?daughter rdf:type :Daughter .
}
```

### 3. List the instances of the class Parent

```sparql
SELECT ?parent
WHERE {
  ?parent rdf:type :Parent .
}
```

### 4. List the instances of the class Father

```sparql
SELECT ?father
WHERE {
  ?father rdf:type :Father .
}
```

### 5. List the instances of the class Mother

```sparql
SELECT ?mother
WHERE {
  ?mother rdf:type :Mother .
}
```

### 6. List the instances of the class Grandmother

```sparql
SELECT ?grandmother
WHERE {
  ?grandmother rdf:type :Grandmother .
}
```

### 7. List the instances of the class Grandfather

```sparql
SELECT ?grandfather
WHERE {
  ?grandfather rdf:type :Grandfather .
}
```

### 8. List the instances of the class Brother

```sparql
SELECT ?brother
WHERE {
  ?brother rdf:type :Brother .
}
```

### 9. List the instances of the class Sister

```sparql
SELECT ?sister
WHERE {
  ?sister rdf:type :Sister .
}
```

For executing these queries, you'd typically use a SPARQL endpoint or a software tool that supports SPARQL queries against your ontology, such as Apache Jena Fuseki or Protege with the SPARQL plugin.

Now, let's move on to the more complex queries with several conditions in the WHERE clause.

### List (name, age) of children of Peter

```sparql
SELECT ?name ?age
WHERE {
  ?child :isChildOf ?parent .
  ?parent :name "Peter" .
  ?child :name ?name .
  ?child :age ?age .
}
```

### List of persons whose father is more than 40 years old

```sparql
SELECT ?person
WHERE {
  ?person :isSonOf/:isDaughterOf ?father .
  ?father :age ?age .
  FILTER(?age > 40)
}
```

### List (name, age) of all French citizens. For each one, if he/she is married, display the name of his wife/her husband

```sparql
SELECT ?personName ?personAge ?partnerName
WHERE {
  ?person :nationality "French" .
  ?person :name ?personName .
  ?person :age ?personAge .
  OPTIONAL {
    ?person :isMarriedWith ?partner .
    ?partner :name ?partnerName .
  }
}
```

### List of the name of persons who are brother of someone

```sparql
SELECT DISTINCT ?brotherName
WHERE {
  ?brother :isBrotherOf ?sibling .
  ?brother :name ?brotherName .
}
```

### List of the name of persons who are daughter of someone

```sparql
SELECT DISTINCT ?daughterName
WHERE {
  ?daughter :isDaughterOf ?parent .
  ?daughter :name ?daughterName .
}
```

### List of the name of persons who are uncle of someone

```sparql
SELECT DISTINCT ?uncleName
WHERE {
  ?uncle :isBrotherOf ?parent .
  ?child :isChildOf ?parent .
  ?uncle :name ?uncleName .
}
```

### List of the name of persons who are married

```sparql
SELECT DISTINCT ?personName
WHERE {
  ?person :isMarriedWith ?partner .
  ?person :name ?personName .
}
```

Executing these queries would give you the insights based on the relationships and attributes defined in your ontology. If you're using Protege, you can run these queries in the SPARQL Query tab after loading your ontology and ensuring that OWL reasoning is enabled to get inferencing support.