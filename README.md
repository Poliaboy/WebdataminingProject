# Web Datamining & Semantics Project

## Overview

The Semantic Web project is a comprehensive and hands-on exercise designed to integrate various components discussed in initial sessions into a unified application. Participants will work in pairs to ensure rapid progress covering all aspects.

### Main Objectives

- **Design a food delivery discovery service:** The service will involve several entities including food products, offers (individual items or combos), restaurants, businesses, delivery services (individuals or companies like Delivroo, Uber Eats), and customers along with their preferences.

- **Develop an application:** The application will recommend where to order food based on the customer's description at the time of the request.

### Pedagogical Objectives

- Engage in software development using Semantic Web programming frameworks.
- Set up and interact with an RDF database.
- Leverage multiple sources of heterogeneous data.
- Present information online with rich metadata.

## Part I: Modeling the Ontology

Create an ontology using the Protégé editor to model the food delivery discovery service. This includes:

- **Class and Property Hierarchies:** Define at least three hierarchies and restrictions.
- **Class Restrictions:** Implement at least three restrictions such as disjoint, existential, universal, etc.
- **Property Types:** If necessary, define at least three property types like transitive, symmetric, inverseOf, etc.

Ensure your application follows Linked Data principles, starting with Schema.org instances and adhering to data availability and standard vocabulary principles. Validate your ontology with PELLET for consistency.

## Part II: Populating the Ontology

Populate your knowledge base by:

- **Manually:** Create RDF instances in Protégé.
- **Other Sources:** Convert data from non-RDF formats into RDF, utilizing online data sources like CoopCycle for bike delivery coops information. Enhance JSON files with Json Context for RDF conversion, using SPARQL Update queries for data addition.

## Part III: Querying the Ontology

Develop SPARQL queries to:

1. List instances of food products, offers, and customers.
2. Identify all Paris restaurants and vegetarian restaurants, including their delivery services.
3. Find deliverymen over 51 who can deliver in Lyon in under 15 minutes.
4. Discover restaurants serving Italian food on a specific day, including availability.

Propose five SPARQL queries featuring various query forms and patterns, such as Optional Graph Patterns, alternatives, CONSTRUCT, ASK, and DESCRIBE.

## Part IV: Manipulating the Ontology with Jena

Using Jena, implement functionalities to:

- Load the ontology, displaying all Persons and Restaurants serving Italian food, with and without the use of queries and inference.
- Develop a program to handle food searches, displaying error messages or relevant restaurant, delivery service, and offer information.
- Implement a rule to define a new class RestDelivery and specify three different rules in a Java program.

## Submission Details

- Full-time project work during remaining sessions.
- Final delivery includes all working files, a presentation, and a demo on the last course session, along with a report detailing your choices and functionalities. A deadline will be provided by professors.
- Submit an archive (`name1-name2-name3.zip`) containing the .owl file, SPARQL queries, Eclipse src and data folders, and the presentation file in DVO deposit.
