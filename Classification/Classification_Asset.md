# Top-Level Asset Classification Hierarchy
* asset
    * water or wastewater treatment specific [^1]
    * water, wastewater, or stormwater network specific
    * physical security system specific
    * HVAC system specific
    * structural or building specific
    * safety or hazard prevention specific
    * transportation or lifting specific
    * shop and hand tool specific
    * general purpose discrete asset [^2][^3]
        * flow or pressure control
        * active material conveyance
        * discrete linear segment
        * storage
        * driving or rotating
        * sensing, measurement, or control
        * electrical power handling
        * communication or computing
    * collection of discrete assets
        * facility
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


### Footnotes
[^1]: Under the categories whose name ends in "specific", you will find term denoting assets used in a particular specialized system (such as HVAC or security for example), or assets designed to support a certain common category of human goal (such as safety).
[^2]: Under this category, you will find term denoting discrete assets that perform a low-level technical functions within a diverse range of systems that are in service of a open set of human goals.
[^3]: For some classes, you may not be able to clearly distinguish whether it is a "discrete general purpose asset" class or "specific" application asset class. An example is the class *pressure relieve valve*, you may recognize it as a *safety or hazard prevention specific* or a *general purpose discrete asset > flow or pressure control* asset. In cases like this, you will find the class under more than one branch of the tree.