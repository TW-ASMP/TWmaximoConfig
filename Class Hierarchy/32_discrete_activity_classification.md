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
  * new assset installation
  * asset movement
  * asset part movement
  * asset replacement
  * asset part replacement
  * asset hand-over
* Life Event Process*
  * asset commissioning
  * asset hand-over 
  * final asset decommissioning 
* Asset Modification*
  * modify asset setpoint
  * physical modification to asset
  * physical modification to building or structure [^2]
* asset assignment
* Contributory Work*
  * work coordination and notification
  * safety preparation
  * setup
  * takedown of setup
  * travel
* design or redesign
  * creation of new role
  * removal of existing role
* Informational*
  * add or correct record info
  * record retirement



## Requirements for Implementer

[]REQ Nyh7RPjEgl #IMP "classes names specified in camel-case and with an asterik symbol shall have the appliable to individual property, found in the class object, set to false"


## Notes

TODO[] #TW "In the work specification stage, need specify at least one class of activity as a function, which take a certain state of the world S1 (for example, the property of a certain asset) and transforms to another state S2"

### Footnotes
[^1]: more will be added before the final implementation. 
[^2]: the physical modification of a building or a structure may result in the creation and removal of a space, hence it is singled out. 
