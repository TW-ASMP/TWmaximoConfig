# TW Maximo Data Model 

## Introduction

The data model in this repository represents a comprehensive WMS information structure, covering assets, roles, space, etc., and the relations between them.  We developed this data model in response to the need for a coherent framework - big picture view - of the future state of our WMS.  

Beyond the big pictre, a set of precisely formulated and internally consistent metadata is fused into the model, in the form of class definitions and dropdown values. This set of information has been developed and refined over the last couple of years to address actual asset and work management challenges (or "use-cases" in the context of solution implementation).

> [!NOTE]
> Go to https://github.com/orgs/TW-ASMP/projects/3/views/1 for current project status

## Overview of Content

The following diagram illustrates the key pieces of the data model definition as of July 2024. More pieces will be added to the data model progressively throughout 2024. 

![image](https://github.com/user-attachments/assets/84ad15b7-4f7d-45b5-a20e-bdf5810d21c7)


## Comments on Information Format

The schema portions of the data model is documented in JSON-Schema serialized in YAML format. The entity classification trees and structural hierarchy are documented in Markdown format. We chose Markdown because it is simple to manipulate and enables multi-party change tracking and real-time sharing over Github.  We chose JSON-Schema and YAML instead of a Word document on one hand or an entity-relational schema on the other for the following reasons.

* [standardized syntax](https://json-schema.org/overview/what-is-jsonschema) for precise descriptions - useful for deep references to other parts of the schema and logical expressions - while preserving human readability
* specification in a JSON document can be extracted as data - for example, business rules specified across the schema files
* a direct foundation of test script development
* **critically**, a direct foundation for data migration mapping scripts from the current WMS. (Also note that a precise Maximo relational schema will not be available, until it is too late for data mapping.) 
