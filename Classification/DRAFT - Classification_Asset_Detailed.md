# Detailed Asset Classification Hierarchy
* asset
    * water or wastewater treatment specific terms [^1]
    * water, wastewater, or stormwater network specific
        * hydrant unit
        * hydrant system
        * catch basin
        * manhole
        * underground access chamber
        * 
    * security or access control system terms
        * motion sensor
        * entry access control unit
        * security camera
        * controlled lock
        * controlled barrier ***(person, vehicular))
    * HVAC system specific terms
        * air handling unit
        * air conditioner unit ***(outdoor condensor unit, indoor evaporator unit)
        * damper
        * damper actuator
        * dehumidifier
        * heat pump unit ***(outdoor unit, indoor unit)
        * air filtration unit
        * variable air valve
        * energy recovery ventilator ****
        * zone controller unit or thermostat
    * other building service asset terms
        * BMS controller unit
        * PA system speaker
        * intercom unit
    * term denoting structure or building
        * building ***(industrial, office, mixed)
        * free-standing structure
            * stack
            * tower
        * access ramp
        * tunnel
        * structural tank
    * safety or hazard prevention specific
    * transportation specific
        * passenger vehicle
        * pickup truck
        * golf cart
    * lifting specific
        * 
        * 
    * hand tool
    * large shop floor tool
    * general purpose discrete asset [^2][^3]
        * material flow or pressure control
            * compressor
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
            * fuel tank ***(natural gas, diesel, gasoline)
            * 
        * driving or rotating
            * actuator
            * electrical motor
            * engine
        * sensing, measurement, or control
        * electrical power handling
        * panel
            * control panel ***(contains: BMS controller, process control PLC, lighting controller, ...)
            * network or server
            * 
        * communication or computing
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
            * main path
        * header
        * defined set of asset
            * assets of a organization
            * route
### Working Notes

(***) - will have some attribute associated
(****) - new

### Footnotes
[^1]: Under the categories whose name ends in "specific", you will find term denoting assets used in a particular specialized system (such as HVAC or security for example), or assets designed to support a certain common category of human goal (such as safety).
[^2]: Under this category, you will find term denoting discrete assets that perform a low-level technical functions within a diverse range of systems that are in service of a open set of human goals.
[^3]: For some classes, you may not be able to clearly distinguish whether it is a "discrete general purpose asset" class or "specific" application asset class. An example is the class *pressure relieve valve*, you may recognize it as a *safety or hazard prevention specific* or a *general purpose discrete asset > flow or pressure control* asset. In cases like this, you will find the class under more than one branch of the tree.