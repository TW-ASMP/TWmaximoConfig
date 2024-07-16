# TWmaximoConfig Repository

A repository containing
* Maximo object configurations expressed in JSON-SCHEMA / YAML format
* An outline of asset classification hierarchy in Markdown format

Draft Content Note
* see JSON schema for rule syntax
* not all class values are filled in, focus is to establish the structure first.
* we align with Bentley's data standard
* we are in the middle of data transformation, delay by the inflexibility of Avantis. In summary, we are interested in implementing the schema and rules, full suite of metadata will come later
* This spells out what the data can be exported to look like, it is agnostic to the underlying schema.
    e.g.
          "primary function criticality":
            type: [$ref: criticalityVal, type: null]
            enum:
            - "rating": 1
                "description": "TBD"
            - "rating": 2
                "description": "TBD"
            - "rating": 3
                "description": "TBD"
            - "rating": 4
                "description": "TBD"
            - "rating": 5
                "description": "TBD"
* Implementer is encourages to fit the data field onto Maximo's existing data field.
* Data field audit on by default, unless mentioned otherwise
* Format of rule specification
* Interpretation of NULL values
* Rule Types: validation, implication, process
* Difference between lack of knowledge and non-existence known and how NULL, none, and other variables are used to specify these. 