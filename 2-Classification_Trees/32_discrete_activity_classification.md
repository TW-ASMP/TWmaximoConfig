## Top-Level Discrete Activity Classification
* Condition Evaluation*
  * quick check
  * inspection and evaluation
  * test and analysis
  * condition analysis
* sample collection
* cause investigation
* repair or service [^1]
  * calibration
  * asset replacement
  * asset part replacement 
  * asset part movement 
* Move or Replace*
  * new asset installation
  * asset movement
  * asset part movement
  * asset replacement
  * asset part replacement
  * asset hand-over
* Life Event Process*
  * asset commissioning
  * asset hand-over [^3]
  * final asset decommissioning 
* Asset Modification*
  * modify asset set-point
  * physical modification to asset
  * physical modification to building or structure [^2]
* asset assignment
* Contributory Work*
  * item procurement
  * work coordination
  * safety preparation
  * setup
  * takedown of setup
  * travel
* design or redesign
  * creation of new role
  * removal of existing role
* Asset Data*
  * record information correction
  * record retirement



## Requirements for Implementer

```yaml
  rule_spec:
  - name: Valid Assignment of an Asset
    spec_ID: 01JDCNEFAED17CWF2K851ZAJKW
    type: [assertion]
    description: |
      classes names specified with an asterisk symbol shall have the their .property.appliable_to_individual value set to false
```


### Footnotes
[^1]: more will be added before the final implementation. 
[^2]: the physical modification of a building or a structure may result in the creation and removal of a space, hence it is singled out. 
[^3]: the process by which a asset's ownership is transferred from a capital project to Toronto Water. 
