# Asset Classification
## Introductory Notes
In the content section, asset classes name written in lower case represents a natural classes, and asset classes name written title case isA coined term, define usually with respect to one or more natural classes. 

## Content

* Asset
    * Distribution and Collection Network Asset
        * easement
        * hydrant system
        * hydrant [^3]
        * water service connection [^3]
        * sewer service connection 
        * storm service connection 
        * weir structure
        * watermain [^3]
        * manufactured treatment device (MTD)
            * oil grease separator MTD
            * filter MTD
        * pond
        * sewer
        * wet weather flow storage
            * super-pipe
                * #necessaryProperties:
                    * InlineOfPipe: Yes
            * detention tank
                * #necessaryProperties:
                    * isA: surge tank [^3]
                    * InlineOfPipe: No 
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
    * Water or Wastewater Treatment 
        * Material Addition or Dosing [^9]
            * #properties:
                * dosedMaterial:
                    * enum:
                        * oxygen
                        * chlorine
                        * sodium bisulfite
                        * ...
            * dosing injector
            * dosing eductor
            * dosing pump
            * gas diffuser
            * gas diffuser grid assembly
            * dosing or metering pump
            * dosing system unit [^4]
            * dosing system assembly
                * chlorinator assembly
                    * #necessaryProperties:
                        * dosedMaterial: chlorine
                * sulphinator assembly
                    * #necessaryProperties:
                        * dosedMaterial: sodium bisulfite
                * polymer dosing assembly
        * Dewatering
            * dewatering centrifuge
            * rotory drum thickener
            * screw press
            * polymer mixing tank
        * Solids Separation
            * vortex separator
            * clarification tank
            * sedimentation tank
            * classifier
            * bar screen unit
            * traveling screen unit
        * Filtration
            * treatment filter unit
                * #properties:
                    * filterMedium:
                    * type: array
                    * open list: yes
                    * enum:
                        * sand
                        * charcoal
                        * membrane
            * treatment filter bank
                * #comment:
                    * see example: https://www.istockphoto.com/photo/interior-of-reverse-osmosis-water-purification-plant-gm157396373-7912728?phrase=reverse+osmosis+plant
            * a loose portion of granular filterMedium
                * #properties:
                    * filterMedium:
                    * type: array
                    * open list: yes
                    * enum:
                        * sand
                        * charcoal
            * filtration tank assembly
        * Named Biological or Chemical Treatment
            * #necessaryProperties:
                * isA: reactor
            * disinfection tank
            * UV disinfection assembly
            * UV disinfection lamp unit
            * coagulation or flocculation tank
            * aeration reactor tank
            * digester reactor tank
            * ozone generator
        * Other Unnamed Types of Reactor
            * reactor
                * #properties:
                    * actively mixed: type: boolean
                    * aerated: type: boolean
                    * #oneOf:
                        * Packed bed reactor: type: boolean
                        * Fluidized Bed Reactors (FBRs): type: boolean
                    * Sequencing Batch Reactors (SBRs): type: boolean
                    * Membrane Bioreactors (MBRs): type: boolean
        * incinerator
        * ash lagoon
        * grinder or comminutor [^6]
    * HVAC, Building, or Grounds Service Asset
        * HVAC System Asset
            * air handling unit
            * Air Filtration
                * air filtration unit
                    * #necessaryProperties:
                        * hasPart: replaceable filter cartrige
            * Air Conditioning
                * AC condenser unit
                    * #comment: technically a heat exchanger [^3]
                * AC evaporator unit
                * AC packaged unit 
                * AC system
                    * #necessaryProperties:
                        * hasPart: SOME (AC condensor unit)
                        * hasPart: SOME (AC evaporator unit)
            * air damper
            * actuator 
                * #comment: a type of motor or energy conversion device [^3]
            * boiler
            * condensate trap
            * dehumidifier 
                * #necessaryProperties:
                    * isA: demister or air dryer
            * heat pump unit
                * #necessaryProperties:
                    * hasPart: outdoor unit
                    * hasPart: indoor unit
            * variable air volumn unit
            * air exchange unit [^6]
            * energy recovery ventilator
            * thermostat or zone controller unit
        * Security or Access Control Asset
            * security camera
            * motion sensor
            * entry access control unit [^6]
                * card reader
            * security camera
            * controlled door access
            * controlled access barrier
        * building automation system controller
        * lighting unit
        * road segment
    * Green Infrastructure Asset
        * piece of lawn
        * planting space
        * soil cell
    * Safety or Environmental Harm Prevention Asset
        * Hazardous Gas Monitoring Device 
            * #necessaryProperties:
                * isA: gas instrumentation 
            * personal gas meter [^6]
            * fixed gas detector
        * Explosion Prevention Equipment
            * flame arrestor
            * rupture disk
        * emergency eyewash or shower
            * #properties:
                * portable: type: boolean
        * Chemical Protection
            * chemical suit
            * spill kit
        * Electrical Safety
            * rubber insulating gloves
            * rubber insultaing sleeves
            * voltage surge suppressor
            * protection relay [^5]
            * grounding equipment
            * high voltage stick
            * high volatge tester
            * switchgear grounding device [^3]
        * Respiratory Hazard Protection
            * supplied air respirator
            * self-contained breathing apparatus (SCBA)
            * respirator mask
            * powered air respirator
            * air scrubber
        * Fall Protection Equipment
            * horizontal lifeline
            * vertical lifeline
            * self-retractig lifeline
            * fall arrest davit arm [^3]
                * #necessaryProperties:
                    * isA: lift
                    * isMobile: yes
            * fall restricting system
            * fall arrest lanyard
            * fall arrest harness
            * rope or cable grab
            * full-body harness
            * anchorage connector
        * Floatation Equipment
            * personal floatation device
            * life right
            * life jacket
        * First-aid Equipment
            * first aid station equipment
            * first aid room equipment
            * first aid kit
            * automatic external defibrillator
    * Electrical Asset or Component
        * generator 
            * #properties:
                * fuelType: enum:
                    * diesel
                    * natural gas 
                    * bi-fuel
        * lighting panel
        * motor control centre
        * switchgear distribution bus
        * battery bank
        * uninterrupted power supply
        * welding receptacle
        * battery charger
        * breaker
        * protection relay
            * #necessaryProperties:
                * isA: electrical current instrumentation [^3]
        * capacitor [^1] [^2]
        * cable section
        * fuse [^1]
        * electrical conduit section
            * #comment: if classifed by function, this would be under a category called "linear function" - extremely counter-intuitive to find [^3]
        * eletrical duct bank section
        * disconnect switch
            * load break switch
        * power harmonic filter
        * motor starter
        * motor drive or VFD
        * transformer
        * transfer switch
    * Building or Structure
        * building
            * #properties
                * useOfBuilding: enum: {industrial, office, mixed}
        * stack
        * tower
        * bridge
        * tunnel
        * fence section
        * structural tank
        * retaining wall
        * culvert
    * Part of Building or Structure
        * #comment:
            * TH: I have included assets that are (1) independently replaceable AND (2) has a different (shorter) life-cycle compared the structure itself (e.g.roof) OR must be tracked at inidividual level for compliance reasons (e.g. fire door, fixed ladder), BUT NOT the assets that satisfies (1) and (2) above, but isn't the object of a a regular inspection or maintenance work order AND .
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
            * #comment: a type of filter [^3]
        * trap priming device
            * #comment: usually a pipe section [^3]
        * valve
    * General Mechanical Component
        * bearing
        * belt
        * seal or gasket
        * replaceable filter cartrige [^1]
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
    * GENERIC CROSS-DOMAIN ASSET TERMS
        * #comment: 
            * For some classes, you may not be able to clearly distinguish whether it isA "discrete general purpose asset" class or "specific" application asset class. An example is the class *pressure relieve valve*, you may recognize it as a *safety or hazard prevention specific* or a *general purpose discrete asset > flow or pressure control* asset. In cases like this, you will find the class under more than one branch of the tree. Under this category, you will find term denoting discrete assets that perform a low-level technical functions within a diverse range of systems that are in service of a open set of human goals.
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
            * cooling tower
            * chiller
            * chiller evaporator
            * chiller condenser
            * centrifuge
            * dust collector unit
            * air scrubber
            * air filter unit
            * mixer or agitator
                * vortex mixer Emily:What are you calling oxygen diffusers in the aeration tank (oxygenation is the primary function and diffusion and mixing is secondary)?  
                * mixing tank
            * compactor
            * grinder
            * air dryer
        * Material Storage or Surge Suppression
            * #properties:
                * containedMaterial: enum: {...}
            * storage tank
                * fuel storage tank 
                    * #properties:
                        * fuelType: enum: {natural gas, diesel, gasoline}
            * surge tank
            * tank component [^1]
                * necessaryProperties:
                    * isPartOf: ONLY (OR(storage tank, reactor, surge tank))
            * compressed gas cylinder
                * #properties:
                    * containedMaterial: enum: {...}
        * Mechanical Energy and Motion 
            * actuator [^1]
            * motor [^1]
            * engine [^1]
            * combustion turbine [^1]
        * Sensing (Information Capture)
            * single-variable instrumentation
                * #properties:
                    * hasAnalyzer: type: boolean 
                    * hasSensorElement: type: boolean
                    * hasInstrumentationComponent:
                        * type: array
                        * items:
                            * $ref: "objectDefs/asset"
                    * hasInterfaceComponent: enum: {HART, Ethernet, dry contact, analog transmitter} 
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
                * electrical current instrumentation
                * voltage instrumentation
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
                * remote terminal unit (RTU) "To PCS is thisA glorified terminal block or processing features too"
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
            * mobile lift
                * forklift
                * manlift
                    * scissors lift
            * crane #TH fixed{yes, no}, type:{jib, gantry, davit, bridge}
        






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

[ ] - consider removal of certain domain-specific terms for classes, because (1) peopele woudld search by the more generic class name anyways (2) the location in the system communicates what it is (e.g. camera in a security system isA security camera) (3) we don't care about the convenience of pulling out just that specific class of assets e.g. air filter
        * dry polymer separation unit
        * grit classifier

[ ] - Think throught the implication of considering every type of asset as a potential part of another type of asset

[ ] - We should add parts of assets that experience very different life-cycle curve from the whole. E.g. sludge collector on a sedimentation tank or agitator in a digester

[ ] Classificaion of assets,composed of a collection of assets are specified in the role classifcation file. 
[ ] what about
    * watercourse - what is the parent CATegory? 
    * easement

### Arguments to Corp
- This structure isAlways changing, new classes and necessary fields are constainly being added or changed. How do we keep track of changes and data collection forms in multiple applications (GIS, WMS, capital data collection spreadsheet)?

### List of Properties used
* hasPart
* isPartOf
* isA
* dosedMaterial
* containedMaterial
* filterMedium
* isMobile
* fuelType
* tankType
* useOfBuilding
* hasInstrumentationComponent
* hasInterfaceComponent


### Terms to be Defined
* component

### Footnotes
[^1]: COMPONENT: An asset that is never a stand alone unit, but always a part of a larger unit.

[^2]: TRACKED_COMP: An class of component, some instances of which are tracked like an asset unit, for either its movement, or work history

[^3]: COMMON_NAME: Example of a class, bearing a common name, which if subsumed under a functional classification category (under GENERIC CROSS-DOMAIN ASSET TERMS), would be hard to find.

[^4]: COMPONENT/UNIT/ASSEMBLY: Example where "unit" or "assembly" is explictly called out in the naming, to avoid ambiguity. For more examples, ctrl + F for "unit" or assembly.

[^5]: MULTI_PLACE: Example of a class that appears in multiple places on this classification hierarchy

[^6]: NOT_LOWEST: Example of a class that can be used on an asset record, but not at the lowest level of the classification

[^10]: INTERESTING: an example of something interesting. 