# Toronto Water Highest Level Hierarchy

## The Hierarchy
- [Toronto Water System]  
	- [Drinking Water Network]  
		- {Pumping Stations for Drinking Water} [^2] 
	- {Drinking Water Treatment Plants} [^1]
		- {Storage Assets in Drinking Water Supply Network} [^3]  
	- [Waste and Storm Water Network]  
		- {Pumping Stations in Sewer Network} [^4]
		- {Chambers in Sewer Network}  
		- {Storages of Wet Whether Flow} [^5]
	- {Wastewater Treatment Plants} [^6]
	- {Yards}
	- {Independent Buildings}


## Notation Usage

- {x}  
	- set of all x  
	- e.g. {WTR-PLANT} set of all water treatment plants  
- [x]  
	- a system (or more precisely a fn structure) named x  
	- e.g. [TAB-AER] - TAB secondary aeration system  

  [^1]: i.e. {[FCL]}, {[FIS]}, {[FHO]}, {[FHA]}
  [^2]: the set of 18 pumping stations
  [^3]: the set of all reservoirs and elevated tanks
  [^4]: pumping station for waste and storm water
  [^5]: the set of all wet-whether storage, inline an offline.
  [^6]: i.e. {[THC]}, {[THR]}, {[TAB]}, {[TNT]}