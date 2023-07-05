# Detailed Asset Classification Hierarchy
## Introductory Notes
In the content section, asset classes name written in lower case represents a natural classes, and asset classes name written title case is a coined term, define usually with respect to one or more natural classes. 

## Content

* Asset
    * Assets by Domain [^1] [^4]
        * Distribution and Collection Network
            * hydrant system {subclass: localized primary function system}
            * valve
            * water service {subclass: localized primary function system}
            * sewer service {subclass: localized primary function system}
            * weir
            * water main {force main?}
            * sewer main {Q: should we have subclasses? or just attributes?} {force main?}
                * trunk sewers
                * local sewers
            * treatment devices
                * oil gas separator
                * filter
            * pond
            * detention tank
            * superpipe
            * underground access chamber
            * manhole [^5]
                * TW Sewer Manhole {Note: remove this and map to a manhole+attribute}
            * outfall
            * pipe fitting
            * backflow preventer
            * Sewer Inlet or Catch Basin
            * TW Water Fitting [^5] {Note: remove this and map to a pipe fitting + attribute}
            * TW Sewer Large Chamber {Note: need to match subtypes to class}
            * TW Sewer Fitting
            * well
            * wet weather storage
            * drinking water storage
                * reservoir
                * elevated tank
        * Building or Structure
            * building {purpose: industrial, office, mixed}
            * free-standing structure
                * stack
                * tower
            * access ramp
            * tunnel
            * fence section
            * structural process equipment
                * structural processing tank
                * strucural storage stank
            * retaining wall
            * culvert
            * part of building or structure 
                * COMMENT: "Pete: this cat. being under Building and Structure is more intuitive more normal ppl"
                * elevator
                * fixed ladder
                * roof
                * railing
                * loading dock
                * door
                    * fire door
                    * roll-up door
                * manhole [^5]
        * Building Service or Grounds Service
            * HVAC System 
                * "rationale for having this category: (1) the majority of terms in this domain are specialized (2) the domain gets use a lot "
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
            * Security or Access Control
                * camera
                * motion sensor
                * entry access control unit [^6]
                    * card reader
                * security camera
                * controlled door access
                * controlled barrier {type: person, vehicular}
            * BAS controller
            * Lighting 'STEPHEN: did CREM take over lighting?
        * Land Surface Feature
            * COMMENT: "Pete: ask AK about green infrastructure assets"
            * segment of paved road
            * piece of lawn
            * planting space
            * soil cell 
        * Safety or Environmental Harm Prevention
            * hazardous gas monitoring device {subclass: atmospheric gas sensor}
                * personal gas meter
                * fixed gas detector
            * explosion prevention equipment
                * flame arrestor
                * rupture disk
            * emergency eyewash or shower
            * chemical protection
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
                * first aid kit
                * automatic external defibrillator
            * silencer "#Pete when is silencer used"
        * Facility Piping or Material Distibution
            * pipe section
            * air duct section
            * air channel section
            * material distribution panel
            * pipe manifold
            * Piping System Component
                * condensate trap
                * pipe fitting
                * pulsation dampener
                * quencher
                * sampling point
                * steam trap
                * strainer
                * trap priming device
                * valve
        * Transportation or Lifting
            * passenger vehicle
            * pickup truck
            * golf cart
            * boat
            * water trailer
            * mobile lift [^6]
                * forklift
                * manlift [^6]
                    * scissors lift
            * crane [^6] {fixed?, type: type: jib, gantry, davit, bridge}
            * elevator
        * Tracked Tool
            * portable ladder
            * infrared camera
            * power washer
            * portable scaffolding
            * scuba equipment
            * compressed gas cylinder
            * vacuum cleaner
            * pipette
            * stationary machine tool
        * Enclosure or Panel
            * control panel
            * local control panel
            * material distribution panel
            * electrical distribution panel
            * network (acccess) panel
    * Assets by Function
        * Material or Energy Handling Asset [^2] [^3]
            * material flow control or pressure control
                * pump
                * conveyor [^6]
                    * screw conveyor (Note:define a new class, instead of using just attribute, when you are likely to collect different set of data)
                * blower or fan
                * compressor {...}
                * valve
                * backflow preventer
                * gate {type:sluice gate, knife gate,pinch gate, check gate}
                * drain EMILY:how is this term used
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
            * physical processing
                * separator [^6]
                    * centrifuge
                    * clarification tank
                    * coagulation/flocculation tank
                    * classifier
                    * vortex or cyclone separator
                    * screw press
                * filter [^6]  
                    * water treatment filter 
                    * biofilter EMILY:fair as a bio reactor? Also, could the filters be a part of a class of tank?
                    * aerobic filter 
                        * !COMMENT: Note: used instead of "biofilter", typically refers to aerobic #Emily
                    * anaerobic filter
                    * bar screen
                    * air treatment filter
                    * replaceable filter medium
                * collector [^6] 
                    * dust collector unit
                    * gas collector 
                    * chain and flight assembly
                    * traveling screen assembly 
                    * traveling bridge assembly
                * mixer or agitator [^6]
                    * sliding frame agitator assembly
                        * COMMENT: through this is a part of a larger asset, it has its own lifecycle and is not a consumable, like tires
                    * vortex mixer
                    * mixing tank
                * grinder or comminutor [^6]
                * compactor
                * demister or air dryer
                * incinerator
                * UV disinfection assembly EMILY: could this be a part of a class of tank?
            * biological or chemical reaction
                * chemical reactor [^6]
                    * coagulation/flocculation tank
                * biological reactor [^6]
                    * aeration tank
                    * digester tank
            * storage
                * wastewater detention tank
                * super pipe
                * pumping wet well
                * storage tank [^6]
                    * fuel tank {natural gas, diesel, gasoline}
                * lagoon
                * gas cylinder
            * material dosing ro addition
                * dosing system [^6]
                    * chlorinator system
                    * ozonator system
                    * sulphonator system
                * ozone generator {subclassof:chemical reactor}
                * dosing pump {subclassof:pump}
                * injector or eductor 
            * motion or mechanical energy conversion
                * COMMENTS:
                    * "Pete: 'driving' seems off (would ppls conflate with cars?), motion or prime mover may be better"
                * actuator
                * motor
                * engine
                * combustion turbine
                * generator {fuel type: diesel, natural gas, bi-fuel}
            * electrical power control, storage, or distribution
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
        * Instrumentation or Information Handling Asset
            * instrumentation, single-variable {hasAnalyzer, hasSensorElement, has...}
                * flowmeter {venturi, magmeter, ...}
                * level instrumentation {...}
                * temperature instrumentation {...}
                * position instrumentation
                * flame or combustion instrumentation
                * pressure instrumentation {...}
                * gas instrumentation {...}
                * weight scale
                * camera
                * vibration instrumentation
                * counter
                * turbidity meter
                * total suspended solids instrumentation
                * total dissolved solids instrumentation
                * residual chlorine instrumentation
                * dissolved oxygen instrumentation
                * pH instrumentation
            * instrumentation, multi-variable
            * functional part of instrumentation
                * industrial network interface
                    * HART
                    * Ethernet
                * analog interface
                    * dry contact interface
                    * analog transmitter interface
                * analyzer [^6]
                    * vibration analyzer
                    * pH analyzer
                    * turbidity analyzer
                    * conductivity analyzer
                    * dissolved chemical analyzer
                        * dissolved oxygen analyzer
                        * nitrate / nitrite analyzer
                        * phosphate analyzer
                        * chlorine analyzer
                        * heavy mental analyzer
                    * EMILY: Are these valid? What else need to be here?
                * sensor
                    * level instrumentation {...}
                    * temperature sensor {...}
                    * position sensor
                    * flame or combustion sensor
                    * pressure sensor {...}
                    * gas sensor {...}
                    * disolved chemical sensor
                    * vibration sensor
                    * residual chlorine instrumentation
                    * dissolved oxygen instrumentation
                    * pH sensor
                * industrial network interface
                    * HART
                    * Ethernet
                * analog interface
                    * dry contact interface
                    * analog transmitter interface                
            * information recording and storage
                * recorder 'Pete: most of these are paper recorder; Steph: there are power recorder" EMILY: what do you think?
            * information processing and control
                * remote terminal unit (RTU) "To PCS is this a glorified terminal block or processing features too"
                * programmable logic controller (PLC)
                * controller
                * computer {Operator Interface Terminal}
            * general networking device
                * COMMENTS:
                    * "Pete: we may want to make this in the separate cat."
                * network switch
                * network router
                * wireless access point
                * server
                    * application server appliance
                    * network storage appliance
            * display, indication, or alarm
                * gauge
                * display
                * alarm
                * PA system speaker "should conssider this to be a part of building system"
                * Annunciator
                * intercom unit
            * control panel
                * {contains: BMS controller, process control PLC, lighting controller, ...}
    * Collection of Discrete Assets
        * facility
            * pumping station
            * water treatment facility
            * wastewater treatment facility
            * lab
            * yard
        * system
            * hierarchal system 'used to be: localized primary function system
            * network system 'used to be: distributed primary function system
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
### Conversation with Debbie
* on the issue to of applying non-terminal nodes in the classification tree as a class to an asset record, Debbie suggests that we "built the business rule is maintainable by Toronto Water the front-end", instead of levels that we don't have access to as user. (We control visibility, usability and selectability)
* TSD controls all value lists, and control the data field in the domain but not the attributes. We can control the classification record attribute data fields with the caveat that we can't control the value lists that go into them.
* we can control want classes can be applied to a record, and what only serves a a "path" name. 
* We can specify many specs to a single asset.  THis will be useful for the case: a sensor has pressure sensing and temperature sensing and multiple communication protocols. 
    

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
[^6]: though not a lowest level class, can be instantiated as an asset class
[^7]: AK: should we inlcude for future?