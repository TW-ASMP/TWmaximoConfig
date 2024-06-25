## Work Order Classification

* preventive
* corrective
* emergency [^1]
* investigative
* informational
* project
  * modification by staff
  * contractor support 
  * commmissioning [^2]

## Requirements for Implementer

[]REQ Nyh7RPjEgl #IMP "classes names specified in camel-case and with an asterik symbol shall have the appliable property, found in the class object, set to false"

## Notes
[^1]: An emergency work order is technically a corrective work that must be done urgently; may also involve an investigative component (not unlike other corrective work orders).
[^2]: 8/12: "commissioining" work type is added after discussion with Debbie. The thinking is that this would formalize the process of new asset onboarding, and ensure that we accurately record the "first day of operation" of assets. 