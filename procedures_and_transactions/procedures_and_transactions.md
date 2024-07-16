## List of procedures to create

- Per RULE VkiDyJcSxg, a procedure should to be created to allow the recursive elimination of a role and all of its children. 


## Notes on Movement Transaction

RULE: The serial number must be populated when an asset experiences a movement (except for movement for removal or initial installation), or when it is being check into a storeroom.

## Notes on add or correct record info Transaction

When we remove an asset record, we need to set the value reason for removal. These can come from "record retirement reason", formally on the asset specification
     enum: >
      - "missing asset confirmed as lost"*
      - "existing asset removed"
      - "planned asset never received"*
      - "record created by mistake"*
      - "duplicate record"*
If the record is a duplication of other record, it must be specified

When we remove an role record, we need to set the value reason for removal. These can come from "record retirement reason", formally on the asset specification
    enum:
      - "existing role eliminated"
      - "planned role never realized"
      - "record created by mistake"


  "duplicate record of": #should be an array?
    oneOf: [$ref: .objectDefs/role, type: null]