# Purpose of Avantis Schemas

This folder contains the specifications of the form and shape of Avantis information - i.e., PMs and assets - expected to be migrated into Maximo.  An overview of the data mapping process is illustrated in the diagram below. (The term "Avantis PM Data Spec" represent the schema in this folder.)

<br/><br/>

![image](https://github.com/user-attachments/assets/861cfe8d-fcc7-460c-a7b2-e6c819453b73)

<br/><br/>

Data form the srouce and destination systems are converted to JSON, in the role of a data interchange format, because

* human readability making it easier to review
* easier to develop mapping scripts
* much easier to develop pre-migration source data validation (feature present in JSON schema)
* and critically, the precise Maximo schema is unknown until implementation 
