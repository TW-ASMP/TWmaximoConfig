# Asset Classification
## Introductory Notes
In the content section, asset classes name written in lower case represents a natural classes, and asset classes name written title case is a coined term, define usually with respect to one or more natural classes. 

## Content

* Asset
    * Distribution and Collection Network Asset
        * easement
        * hydrant system
        * hyrdant
        * water service connection
        * sewer service connection
        * storm service connection
        * weir structure
        * watermain
        * manufactured treatment device (MTD)
            * oil grease separator MTD
            * filter MTD
        * pond
        * sewer
        * wet weather flow storage
            * super-pipe
            * detention tank
        * infiltration trench
        * chamber
        * manhole [^5]
        * outfall or discharge point
        * backflow preventer
        * catch basin
        * pipe fitting
        * well
        * valve
        * culvert
        * wet weather storage
        * pump wet well
        * drinking water storage
            * reservoir
            * water tower / elevated tank
    * Specialized Water or Wastewater Treatment 
        * Material Addition or Dosing [^9]
            * dosing injector
            * dosing eductor
            * oxidation diffuser
            * oxidation diffuser grid assembly 
            * dosing or metering pump
            * ozone generator [^12]
            * dosing pump
            * assembled dosing system[^10]
                * #comment: note, we are not distinguishing chlorintor, sulphinator, or other type of dosing systems
        * solid separation
            * centrifuge
            * clarification tank
            * vortex separator 
            * screw press
            * sedimentation tank
        * filtering
            * treatment filter unit 
                * #properties:
                    * medium: sand/membrane/charcoal... 
                    * structuralTank: yes/no
                * biological treatment filter unit
                    * aerobic filter unit
                    * anaerobic filter unit
                * mechanical treatment filter unit
            * treatment filter bank assembly
                * #comment:
                    * see example: https://www.istockphoto.com/photo/interior-of-reverse-osmosis-water-purification-plant-gm157396373-7912728?phrase=reverse+osmosis+plant
            * a portion of filter medium
        * screening and removal
            * classifier unit
            * bar screen unit
            * traveling screen unit
        * disinfection
            * disinfection tank
            * UV disinfection unit #EZ: could this be a part of a class of tank?
            * part of UV disinfection assembly
            * ...
        * reactor assembly
            * #Properties:
                * Type ():
                    * Continuous Stirred-Tank Reactor (CSTR)
                    * Plug Flow Reactor (PFR)
                    * Contact tank
                    * Sequencing Batch Reactors (SBRs)
                    * Fluidized Bed Reactors (FBRs)
                    * Membrane Bioreactors (MBRs)
                    * 
            * aeration tank
            * digester tank
            * membrane aerated biofilm reactor 
                * #comment: 
                    * Emily: piloted at North Toronto - biofilm grows on the membrane. 
            * #comment: 
                * Emily:chemical don't really always go in to a reactor tank unless reaction is required
            * coagulation / flocculation tank
            * ozone generator
        * sludge incinerator
        * comminutor [^6]
        * ash lagoon
        * New: backwash treatment - has settling tank, solids removal, chemical
    * HVAC, Building, or Grounds Service Asset
        * HVAC System Asset
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
            * boiler
        * Security or Access Control Asset {Divsion 28}
            * security camera
            * motion sensor
            * entry access control unit [^6]
                * card reader
            * security camera
            * controlled door access
            * controlled barrier {type: person, vehicular}
        * building automation system controller
        * Lighting Unit
        * road segment
    * Green Infrastructure Asset
        * piece of lawn
        * planting space
        * soil cell
    * Safety or Environmental Harm Prevention Asset
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
    * Electrical Asset or Component
        * generator {fuel type: diesel, natural gas, bi-fuel}
        * lighting panel
        * motor control centre
        * switchgear distribution bus
        * battery bank
        * uninterrupted power supply
        * welding receptacle
        * battery charger
        * breaker
        * capacitor
        * cable section
        * electrical conduit section
        * eletrical duct bank section
        * disconnect switch
            * load break switch
        * power harmonic filter
        * motor starter
        * motor drive or VFD
        * transformer
        * transfer switch
    * Building or Structure
        * building #TH:{purpose: industrial, office, mixed}
        * stack
        * tower
        * bridge
        * tunnel
        * fence section
        * structural tank
        * retaining wall
        * culvert
    * Part of Building or Structure [^8] 
        * elevator
        * roof
        * fixed ladder
        * fire-rated door
        * loading dock
        * roll-up door
    * Part of Process Piping
        * pipe section
        * material distribution panel
        * pipe manifold
        * condensate trap
        * pipe fitting
        * expansion joint
        * pulsation dampener
        * quencher
        * sampling point
        * steam trap
        * strainer
        * trap priming device
        * valve
    * Mechanical Component
        * bearing
        * belt
        * seal or gasket
        * air filter medium
        * motor
        * mechanical fitting
        * mechanical assembly
    * General Networking Asset
        * network switch
        * network router
        * wireless access point
        * server appliance
    * Common Tool
        * portable ladder
        * portable scaffolding
        * portable gas detector
        * power washer
        * vacuum cleaner
        * pipette
        * stationary machine tool
        * wrench
    * Road Vehicle or Transportation Tool
        * passenger vehicle
        * pickup truck
        * golf cart
        * boat
        * water trailer
    * GENERIC CROSS-DOMAIN ASSET [^2] [^3]
        * assembled unit [^11]
        * Material Flow or Pressure Control
            * pump
            * blower or fan
            * compressor
            * valve
            * air damper
            * backflow preventer
            * gate
                * #TH:{type enum:sluice gate, knife gate,pinch gate, check gate}
        * Path of Material Flow
            * pipe segment
            * air duct segment
            * segment of watercourse
            * open channel segment
        * Material Processing, Heating, or Cooling
            * boiler
            * heater
            * heat exchanger
            * cooling tower {structural?}
            * chiller [^6]
            * chiller evaporator
            * chiller condenser
            * Material Separation and Removal
                * centrifuge
                * dust collector unit
                * air scrubber
            * Filtering
                * air filter unit
                * replaceable filter medium {for: air/oil/...}
            * mixer or agitator
                * vortex mixer Emily:What are you calling oxygen diffusers in the aeration tank (oxygenation is the primary function and diffusion and mixing is secondary)?  
                * mixing tank
            * compactor
            * grinder
            * air dryer
            * reactor tank
        * Material Storage or Surge Suppression
            * storage tank @Tony:{open to air, closed}, structure?, medium type?
                * fuel tank {natural gas, diesel, gasoline}
                * compressed gas cylinder
            * processor tank @Tony:{open, closed}
            * surge tank @Tony:{open, closed}
        * Mechanical Energy and Motion
            * actuator
            * motor
            * engine
            * combustion turbine
        * Sensing (Information Capture)
            * single-variable instrumentation
                * #TH: {component enum: hasAnalyzer, hasSensorElement, has...}
                * #TH: {interface enum: HART, Ethernet, dry contact interface, analog transmitter interface} 
                * flowmeter {venturi, magmeter, ...}
                * level instrumentation {...}
                * temperature instrumentation {...}
                * position instrumentation
                * flame or combustion instrumentation
                * pressure instrumentation {...}
                * gas instrumentation {...}
                * weight scale
                * camera
                    * infrared camera
                * vibration instrumentation
                * counter
                * turbidity meter
                * total suspended solids instrumentation
                * total dissolved solids instrumentation
                * residual chlorine instrumentation
                * dissolved oxygen instrumentation
                * pH instrumentation
            * multi-variable instrumentation
                * #TH: {component enum: hasAnalyzer, hasSensorElement, has...}
                * #TH: {interface enum: HART, Ethernet, dry contact interface, analog transmitter interface} 
        * Information Processing and Analysis
            * analyzer [^6]
                * vibration analyzer
                * pH analyzer
                * turbidity analyzer
                * conductivity analyzer
                * dissolved chemical analyzer
                    * #TH: EMILY: Are these valid? What else need to be here?
                    * dissolved oxygen analyzer
                    * nitrate / nitrite analyzer
                    * phosphate analyzer
                    * chlorine analyzer
                    * heavy mental analyzer
            * controller
                * remote terminal unit (RTU) "To PCS is this a glorified terminal block or processing features too"
                * programmable logic controller (PLC)
            * computer
                * application server appliance
                * network storage appliance
        * Information Recording or Storage
            * recorder #PL:most of these are paper recorder #SB:there are power recorder #TH:EZ,what do you think?
        * Information Output
            * gauge
            * display
            * alarm
            * PA system speaker "should conssider this to be a part of building system"
            * Annunciator
            * intercom unit
        * Enclosure
            * process control panel
                * instrument air or pneumatic control panel
            * equipment local control panel
            * material distribution panel
            * electrical distribution or motor control panel
            * network panel (access closet)
        * Material Lifting or Transport
            * conveyor [^6]
                * screw conveyor (Note:define a new class, instead of using just attribute, when you are likely to collect different set of data)
            * mobile lift [^6]
                * forklift
                * manlift [^6]
                    * scissors lift
            * crane [^6] #TH fixed{yes, no}, type:{jib, gantry, davit, bridge}
        






## Working Notes
### Creator's intentions
### Conversation with Debbie
* on the issue to of applying non-terminal nodes in the classification tree as a class to an asset record, Debbie suggests that we "built the business rule is maintainable by Toronto Water the front-end", instead of levels that we don't have access to as user. (We control visibility, usability and selectability)
* TSD controls all value lists, and control the data field in the domain but not the attributes. We can control the classification record attribute data fields with the caveat that we can't control the value lists that go into them.
* we can control want classes can be applied to a record, and what only serves a a "path" name. 
* We can specify many specs to a single asset.  THis will be useful for the case: a sensor has pressure sensing and temperature sensing and multiple communication protocols. 
### Conversation with Emily
* Notes found in Base version from discussion with Emly: https://github.com/TW-ASMP/TWmaximoConfig/commit/e7416c7b69751d5573506bf536a08ce595d7f26c
    

### To Think Through

[ ] - consider removal of certain domain-specific terms for classes, because (1) peopele woudld search by the more generic class name anyways (2) the location in the system communicates what it is (e.g. camera in a security system is a security camera) (3) we don't care about the convenience of pulling out just that specific class of assets e.g. air filter
        * dry polymer separation unit
        * grit classifier

[ ] - Think throught the implication of considering every type of asset as a potential part of another type of asset

[ ] - We should add parts of assets that experience very different life-cycle curve from the whole. E.g. sludge collector on a sedimentation tank or agitator in a digester

[ ] Classificaion of assets,composed of a collection of assets are specified in the role classifcation file. 
[ ] what about
    * watercourse - what is the parent CATegory? 
    * easement

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
[^8]: TH: I have included assets that are (1) independently replaceable AND (2) has a different (shorter) life-cycle compared the structure itself (e.g.roof) OR must be tracked at inidividual level for compliance reasons (e.g. fire door, fixed ladder), BUT NOT the assets that satisfies (1) and (2) above, but isn't the object of a a regular inspection or maintenance work order AND .
[^9]: #EZ:gas chlorine dosing system has a lot complexity - not just eductor - see chlorinator
[^10]: note, we are not distinguishing chlorintor, sulphinator, or other type of dosing
[^11]: Could be a large processing tank or a substation on a skid.
[^12]: {subclassof:chemical reactor}