# Detailed Asset Classification Hierarchy
## Introductory Notes
In the content section, asset classes name written in lower case represents a natural classes, and asset classes name written title case is a coined term that denotes a defined class of asset. 

## Content

* asset
    * Distribution and Collection Specific [^1] [^4]
        * hydrant system
        * water service
        * sewer service
        * weir
        * water main {force main?}
        * sewer main {Q: should we have subclasses? or just attributes?} {force main?}
            * trunk sewers
            * local sewers
        * oil and grease separator {subclass: separator}
        * pond
        * underground access chamber
        * manhole [^5]
            * TW Sewer Manhole {Note: remove this and map to a manhole+attribute}
        * outfall
        * backflow preventer
        * Sewer Inlet or Catch Basin
        * TW Water Fitting [^5] {Note: remove this and map to a pipe fitting + attribute}
        * TW Sewer Large Chamber {Note: need to match subtypes to class}
        * TW Sewer Fitting
        * well
    * HVAC System Specific
        * air handling unit
        * air conditioner unit {hasPart: outdoor condensor unit, indoor evaporator unit}
            * AC condensor unit
            * AC evaporator unit
        * air damper
        * damper actuator
        * dehumidifier {subclass: demister or air dryer}
        * condensate trap
        * heat pump unit {hasPart: outdoor unit, indoor unit}
        * air filtration unit {hasPart: air filter}
        * variable air volumn unit
        * air exchange unit [^6]
            * energy recovery ventilator
        * zone controller unit or thermostat
    * Building or Structure
        * building {purpose: industrial, office, mixed}
        * free-standing structure
            * stack
            * tower
        * access ramp
        * tunnel
        * fence section
        * structural process equipment
            * structural tank
        * retaining wall
        * culvert
    * part of building or structure
        * elevator
        * fixed ladder
        * roof
        * railing
        * loading dock
        * door
            * fire door
            * roll-up door
        * manhole [^5]
    * Security or Access Control System Terms
        * camera
        * motion sensor
        * entry access control unit [^6]
            * card reader
        * security camera
        * controlled door access
        * controlled barrier {type: person, vehicular}     
    * Land or Surface Feature
        * segment of paved road
        * piece of lawn
        * planting space
    * safety or environmental harm prevention
        * hazardous gas monitoring device {subclass: atmospheric gas sensor}
            * personal gas meter
            * fixed gas detector
        * explosion prevention equipment
            * flame arrestor
            * rupture disk
        * chemical protection
            * emergency eyewash or shower
            * chemical suit
            * spill kit
        * electrical safety
            * rubber insulating gloves
            * rubber insultaing sleeves
            * voltage surge suppressor
            * protection relay
            * grounding equipment
            * high voltage stick
            * high volatge tester
            * switchgear ground and test device
        * respiratory hazard protection
            * supplied air respirator
            * self-contained breathing apparatus (SCBA)
            * respirator mask
            * powered air respirator
            * air scrubber
        * fall protection equipment
            * horizontal lifeline
            * vertical lifeline
            * self-retractig lifeline
            * davit arm {subclass: lift; isMobile:mobile, fixed}
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
            * first aim kit
            * automatic external defibrillator
            * voltage tester
            * hot stick
        * silencer
    * transportation device
        * passenger vehicle
        * pickup truck
        * golf cart
        * boat
        * water trailer
    * asset by general function [^2][^3]        
        * material flow or pressure control
            * compressor {fuel?}
            * valve
            * backflow preventer
            * gate {type:sluice gate, knife gate,pinch gate, check gate}
            * drain
        * material conveyance or distribution
            * manifold structure
            * pump
            * conveyor
                * screw conveyor (Note:define a new class, instead of using just attribute, when you are likely to collect different set of data)
            * blower or fan
            * pipe section
            * air duct section
            * air channel section
            * material distribution panel
        * pipe element [^6]
            * quencher
            * steam trap
            * pulsation dampener
            * strainer
            * sampling point
            * trap priming device
            * pipe fitting
        * material source and dosing
            * dosing system [^6]
                * chlorinator system
                * ozonator system
                * sulphonator system
            * ozone generator {subclassof:chemical reactor}
            * dosing pump {subclassof:pump}
            * injector or eductor 
        * heating or cooling
            * boiler
            * heater
            * heat exchanger
            * cooling tower {structural?}
            * chiller [^6]
                * absorption chiller
                * vapour compression chiller
            * chiller component
                * evaporator
                * condenser
        * material processing, mixing, or separation
            * separator or collector [^6] (Note: the intention of having this level of classification is to be able to apply this class to a new class of ... say separator.)
                * clarification tank    
                * flocculation tank
                * classifier
                * screw press
                * centrifuge
                * dust collector unit
                * gas collector
                * grit collector {type: mechanical, vortex}
                * vortex or cyclone
            * wastewater collector mechanism [^6]
                * vortex or cyclone mechanism
                * chain and flight mechanism
                * traveling screen mechanism 
                * traveling bridge mechanism
            * filter unit or mechanism [^6] }(presented here as mechanism )                
                * water treatment filter 
                    * biofilter
                    * aerobic filter (Note: used instead of "biofilter", typically refers to aerobic #Emily)
                    * anaerobic filter
                    * bar screen
                * air treatment filter
            * replacement filter medium (Note: show only for parts inventory classification)
            * chemical reactor  [^6]
                * coagulation/flocculation tank
            * biological reactor [^6]
                * aeration tank
                * digester tank
            * mixing or agitator [^6]
                * sliding frame agitator
                * vortex mixer
                * mixing tank
            * wastewater grinder or comminutor
            * compactor
            * demister or air dryer
            * incinerator
            * UV disinfection assembly
        * material storage and surge supression
            * detention tank
            * super pipe
            * pumping wet well
            * storage tank [^6]
                * fuel tank {natural gas, diesel, gasoline}
            * gas cylinder
            * lagoon
        * driving or mechanical energy conversion
            * actuator
            * electrical motor
            * engine
            * combustion turbine
            * generator {fuel type: diesel, natural gas, bi-fuel}
        * power control, regulation, storage or distribution
            * electrical distribution panel
                * lighting panel
                * motor control centre
                * switchgear panel
            * capacitor
            * breaker
            * cable section
            * electrical conduit section
            * eletrical duct bank section
            * disconnect switch
                * load break switch
            * harmonic filter
            * motor starter
            * motor drive or VFD
            * transformer
            * transfer switch
            * welding receptacle
            * uninterrupted power supply
            * battery bank
            * battery charger
        * lifting
            * mobile lift [^6]
                * forklift
                * manlift [^6]
                    * scissors lift
            * crane [^6] {fixed?, type: type: jib, gantry, davit, bridge}
        * panel or enclosure 
            *'comment: reason that we have separate classes - we often do not index what is inside
            * control panel
            * local control panel
            * material distribution panel
            * electrical distribution panel
            * network (acccess) panel
    * information handling and control
        * sensor/meter/switch/analyzer, single-variable
            * flowmeter {venturi, magmeter, ...}
            * level sensor {...}
            * temperature sensor {...}
            * position sensor
            * flame or combustion sensor
            * pressure sensor {...}
            * gas sensor {...}
            * weight scale
            * camera
            * counter
            * turbidity meter
            * total suspended solids (TSS) sensor
            * total dissolved solids (TDS) sensor
            * residual chlorine sensor
            * dissolved oxygen sensor
            * pH sensor
        * sensor/meter/switch/analyzer, multi-variable
        * sensor/meter/switch/analyzer, features (Note: added because of 1 to many relationship with an analyzer. But doe we need to know?)
            * industrial network interface  
                * HART
                * Ethernet
            * analog interface
                * dry contact interface
                * analog transmitter interface
        * information recording and storage
            * recorder
            * network storage appliance    
        * information processing and control
            * remote terminal unit (RTU)
            * programmable logic controller (PLC)
            * controller
            * computer {Operator Interface Terminal}
            * application server appliance
        * general networking device
            * network switch
            * network router
            * wireless access point
        * display, indication, or alarm
            * gauge
            * display
            * alarm
            * PA system speaker
            * intercom unit
        * control panel 
            * {contains: BMS controller, process control PLC, lighting controller, ...}
    * tool (non-EHS)
        * portable ladder
        * infrared camera
        * power washer
        * portable scaffolding
        * scuba equipment
        * compressed gas cylinder
        * stationary machine tool
        * vacuum cleaner
        * pipette
    * collection of discrete assets
        * facility
            * pumping station
            * water treatment facility
            * wastewater treatment facility
            * lab
            * yard
        * system
            * localized primary function system
            * distributed primary function system
                * industrial control network
                * eletrical distribution network
                * material distribution network
                    * water distribution network
                    * water collection network
        * system train
        * line
            * simple line
            * main path line
        * junction/header
        * defined set of asset
            * assets of a organization
            * route



## Working Notes
### Creator's intentions
- 

### To Think Through

[ ] - consider removal of certain domain-specific terms for classes, because (1) peopele woudld search by the more generic class name anyways (2) the location in the system communicates what it is (e.g. camera in a security system is a security camera) (3) we don't care about the convenience of pulling out just that specific class of assets e.g. air filter
        * dry polymer separation unit
        * grit classifier

[ ] - Think throught the implication of considering every type of asset as a potential part of another type of asset

[ ] - We should add parts of assets that experience very different life-cycle curve from the whole. E.g. sludge collector on a sedimentation tank or agitator in a digester

[ ] - need to incorporate logseq://graph/LogSeq?block-id=646b90ee-6b09-48e3-bec5-9fccfb6bd8d8

### Arguments to Corp
- This structure is always changing, new classes and necessary fields are constainly being added or changed. How do we keep track of changes and data collection forms in multiple applications (GIS, WMS, capital data collection spreadsheet)?

### Footnotes
[^1]: Under the categories whose name ends in "specific", you will find term denoting assets used in a particular specialized system (such as HVAC or security for example), or assets designed to support a certain common category of human goal (such as safety).
[^2]: Under this category, you will find term denoting discrete assets that perform a low-level technical functions within a diverse range of systems that are in service of a open set of human goals.
[^3]: For some classes, you may not be able to clearly distinguish whether it is a "discrete general purpose asset" class or "specific" application asset class. An example is the class *pressure relieve valve*, you may recognize it as a *safety or hazard prevention specific* or a *general purpose discrete asset > flow or pressure control* asset. In cases like this, you will find the class under more than one branch of the tree.
[^4]: individual assets come from the GIS
[^5]: an class that appears in multiple places on this classification hierarchy
[^6]: though not a lowest level class, can be instantiated as an asset class #Debbie
[^7]: AK: should we inlcude for future?