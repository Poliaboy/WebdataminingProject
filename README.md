# Web Data Mining & Semantics Project

## Overview

The Semantic Web project is an extensive, practical exercise designed to incorporate various elements covered in initial sessions into a unified application. This project involves working in pairs to ensure efficient progress and comprehensive coverage of the required materials.

### Main Objectives

- **Design a Food Delivery Discovery Service:** Develop a service that identifies various entities relevant to food delivery, including food products, offers (individual items or combos), restaurants, businesses, delivery services (e.g., Delivroo, Uber Eats), and customer preferences.
- **Develop an Application:** Create an application that recommends where to order food based on a customer's description at the time of request.

### Pedagogical Objectives

- Engage in software development using Semantic Web programming frameworks.
- Set up and interact with an RDF database.
- Utilize multiple sources of heterogeneous data.
- Present information online with rich metadata.

## Part I: Modeling the Ontology

### Goals

- Create an ontology with the Protégé editor, focusing on class hierarchy, properties, and restrictions.

### Indications

- Define at least three hierarchies and three restrictions for classes and properties.
- Implement various property types (e.g., transitive, symmetric, inverseOf) as needed.
- Ensure your application adheres to Linked Data principles, utilizing Schema.org for class instances.
- Verify ontology consistency with PELLET.

## Part II: Populating the Ontology

### Tasks

- Manually create RDF instances in Protégé.
- Convert and load data from non-RDF formats to RDF, using SPARQL Update queries for programmatic additions.
- Utilize JSON Context for converting data from open sources like CoopCycle.

## Part III: Querying the Ontology

### Objectives

- Write SPARQL queries to retrieve information about food products, offers, customers, and specific restaurant details.

### Propose 5 SPARQL Queries

1. A query with at least 2 Optional Graph Patterns.
2. A query featuring at least 2 alternatives and conjunctions.
3. A query with a CONSTRUCT query form.
4. A query using an ASK query form.
5. A query employing a DESCRIBE query form.

## Part IV: Manipulating the Ontology using Jena

### Develop Functionalities

- Load the ontology to display all Persons (with and without using queries).
- Load the ontology to display all Restaurants serving Ita
