# CURRENTLY IN DEVELOPMENT

## List of procedures to create

- Per RULE VkiDyJcSxg, a procedure should to be created to allow the recursive elimination of a role and all of its children. 


## Notes on Movement Transaction

RULE: The serial number must be populated when an asset experiences a movement (except for movement for removal or initial installation), or when it is being check into a storeroom.

## Notes on add or correct record info Transaction

The reason for retirement must be represented
When we remove an asset or other type of record, we need to set the value reason for removal. These can come from "record retirement reason", formerly on the asset specification. 
     enum: >
      - "missing asset confirmed as lost"*
      - "existing asset removed"
      - "planned asset never received"*
      - "record created by mistake"*
      - "duplicate record"*
If the record is a duplication of other record, it must be specified

When we remove an role record, we need to set the value reason for removal. These can come from "record retirement reason", 
    enum:
      - "existing role eliminated"
      - "planned role never realized"
      - "record created by mistake"
      - "duplicate record"

When we remove an space record, we need to set the value reason for removal. These can come from "record retirement reason",
    type: string
    hidden: TRUE
    enum:
      - existing space eliminated
      - planned space never realized
      - record created by mistake
      - "duplicate record"*

Ditto for org, item, and tool. 

  In Work Transactions
    We collect the SN forany asset being moved. The serial will be collected in the work transaction log, and must updates the asset record. any asset being entered into the inventory. 

  "duplicate record of": #should be an array?
    oneOf: [$ref: roleObject, type: null]

  when we move a previously in commission asset into a storeroom location, it must be linked with an item record that tell us about its basic OEM information(note 1), it should also have all the required specifications fill-out.  
    Note 1 - we could also consider having this set of information represent in the asset schema as well, but the disadvantage is that the info cannot be re-used
