# Work Activity Unit Classification

* evaluate
    * inspect
    * check
    * test & analysis
* sample or data collection
* investigate cause
* repair or service [^1]
    * calibrated
    * clean
    * exercise
    * replace part
    * flush
    * etc...
* replace or move
    * install
    * remove / decommission [^2]
    * move
    * replace
* modify
    * setpoint modification
    * physical design modification
* preparation or safety
    * coordinate or notify
    * setup or takedown
    * safety preparation
* informational
    * formal work report
    * system design or redesign
    * PM review and revision
    * asset record valiation
* travel

[^1]: at 2023, the vertical facilities will only need to see as far as this level.
[^2]: MUST indicate if asset is removed from site or abondoned in place.

## Work in Progress
To consider the following proposing for using work processes to manage asset records. 
    - Process for adding new asset records: all new asset, role, and space records are added and their status set by one of two processes streams
        - Stream 1 
          - specification 
            - process by which we created the record for role or asset
          - OPTIONAL: approval 
            - for role or asset
          - OPTIONAL: receiving 
            - for asset only; 
            - (only makes sense if we have robust and transparent inventory and project inventory; set status="in hand / usable")
          - OPTIONAL: realization 
            - for asset or space only
            - set status = "realized"
          - OPTIONAL: installation 
            - for asset only 
            - set status = "in hand / usable"
          - commmissioning/test
            - for role-asset together or separately
            - NOT for space, 
            - set role status = "realized"
            - set asset's (either independent or occupying the role) status = "in hand / usable" 
        - Stream 2
          - data reconciliation 
            - (meaning the record is added much later, in a effort to make corrections to reflect the reality)
      a (series of) work order(s) should be recorded for each processes stream, to collect information on people and other things involved in the processes
