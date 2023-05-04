# Detailed Asset Classification Hierarchy

Note that lower case is use for natural classes and title case is use for defined classes. 

* asset
    * Water or Wastewater Treatment Specific [^1]
    * Water, Wastewater, or Stormwater Network Specific [^4]
        * [hydrant system]()
        * water service 
        * sewer service 
        * sewer weir 
        * water main 
        * sewer main {sewer force main:y/n; sewer gravity main:y/n; ??:storm/sanitary/combined}
            * trunk sewers
            * local sewers
        * oil and grease separator
        * pond
        * catch basin {aka: sewer inlet}
        * access chamber
        * manhole [^5]
            * TW Sewer Manhole
        * outfall 
        * water fitting 
        * backflow preventer
        * TW Sewer Large Chamber
        * TW Water Fitting 
        * TW Sewer Fitting 
    * Security or Access Control System Specific
        * motion sensor
        * entry access control unit
        * security camera
        * controlled door lock
        * controlled barrier {type: person, vehicular}
    * HVAC System Specific
        * air handling unit
        * air conditioner unit {part of AC: outdoor condensor unit, indoor evaporator unit}
        * damper
        * damper actuator
        * dehumidifier
        * heat pump unit {part of heat pump: outdoor unit, indoor unit}
        * air filtration unit
        * variable air valve
        * energy recovery ventilator
        * zone controller unit or thermostat
    * other building service specific
        * BAS controller unit
        * PA system speaker
        * intercom unit
    * Building or Structure
        * building {purpose: industrial, office, mixed}
        * free-standing structure
            * stack
            * tower
        * access ramp
        * tunnel
        * structural process equipment
            * structural tank
        * retaining wall
    * Piece of Land or Surface Feature
        * segment of paved road
        * lawn
        * planting space
    * part of building or structure
        * elevator
        * fixed ladder
        * roof
        * foundation
        * railing
        * door
            * fire door
            * roll-up door
    * safety or hazard prevention specific
        * gas detection equipment
            * personal gas meter
            * fixed gas detector
        * chemical protection
            * emergency eyewash or shower
            * chemical suit
        * eletrical protection
            * rubber insulating gloves
            * rubber insultaing sleeves
        * electrical hazard detection equipment
        * respiratory hazard protection
            * supplied air respirator
            * self-contained breathing apparatus (SCBA)
            * respirator mask
            * powered air respirator
        * fall protection equipment
            * horizontal lifeline
            * vertical lifeline
            * self-retractig lifeline
            * davit arm {mobile, fixed}
            * fall restricting system {hasParts: }
            * fall arrest lanyard {sameAs:lanyard}
            * fall arrest harness
            * rope or cable grab
            * full-body harness
            * anchorage connector
        * floataion equipment
            * personal floatation device
            * life right
            * life jacket
        * first-aid equipment
            * first aid station equipment
            * first aid room equipment
            * first aim kit or box
            * automatic external defibrillator
        * spill kit
            * voltage tester
            * hot stick
    * transportation specific
        * passenger vehicle
        * pickup truck
        * golf cart
    * general purpose discrete asset [^2][^3]
        * material flow or pressure control
            * compressor {fuel?}
            * valve
            * backflow preventer
            * 
        * active material conveyance
            * pump
            * conveyor
            * blower or fan
        * material heating and cooling
            * boiler
            * heat exchanger
            * chiller
                * absorption chiller
                * vapour compression chiller
        * material processing
            * 
        * discrete linear segment
        * storage
            * fuel tank {natural gas, diesel, gasoline}
            * 
        * driving or rotating
            * actuator
            * electrical motor
            * engine
        * sensing, measurement, or control
        * electrical generation and distribution
            * generator
        * lifting specific
            * lift
        * panel
            * control panel {contains: BMS controller, process control PLC, lighting controller, ...}
            * network or server
            * 
        * communication or computing
        * general purpose tool
            * portable ladder
            * portable scaffolding
            * scuba equipment
            * compressed gas cylinder
            * large floor stationary tool
    * collection of discrete assets
        * facility
            * pumping station
            * water treatment facility
            * wastewater treatment facility
            * lab
            * yard
        * system
            * localized function system
            * distributed / distribution system
        * system train
        * line
            * simple line
            * main path line
        * header
        * defined set of asset
            * assets of a organization
            * route

### Working Notes


### Footnotes
[^1]: Under the categories whose name ends in "specific", you will find term denoting assets used in a particular specialized system (such as HVAC or security for example), or assets designed to support a certain common category of human goal (such as safety).
[^2]: Under this category, you will find term denoting discrete assets that perform a low-level technical functions within a diverse range of systems that are in service of a open set of human goals.
[^3]: For some classes, you may not be able to clearly distinguish whether it is a "discrete general purpose asset" class or "specific" application asset class. An example is the class *pressure relieve valve*, you may recognize it as a *safety or hazard prevention specific* or a *general purpose discrete asset > flow or pressure control* asset. In cases like this, you will find the class under more than one branch of the tree.
[^4]: individual assets come from the GIS
[^5]: an class that appears in multiple places on this classification hierarchy