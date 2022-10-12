## Location Weights

For the project, we chose three locations with similar significance. They are Eastern regions for the United States and we split them into 3 locations. New England, Middle Atlantic, and South Atlantic. To balance our weights between each location, we assigned a weight to each of them based off of their current population:

#### New England Population: 14 Million
#### Middle Atlantic Population: 60 Million
#### South Atlantic Population: 62 Million

* New England Weight = .10
* Middle Atlantic Weight = .44
* South Atlantic Weight = .46


## Item Weights

The items that we chose for this project represents college students or graduate students. For each location we measure food and gas, which are neccessities for any student. Then, we study two unique products for each location that relate to students. Many students who live off campus need to deal with fuel/utility bills and/or energy bills for their house. Also, many students tend to eat on the go, and therefore we study "food away from home." Apparrel, nonalcaholic beverages, and recreation could also be potential leisure products for students and are worth studying as well. 

New England
* Food (CUUR0110SAF1) = .50
* Gas (CUUR0110SS47014) = .25
* Fuels/Utilities (CUUR0110SAH) = .15
* Apparrel (CUUR0110SAA) = .10

Middle Atlantic
* Food (CUUR0120SAF1) = .45
* Gas (CUUR0120SS47014) = .35
* Nonalcaholic Beverages (CUUR0120SAF114) = .05
* Food Away From Home (CUUR0120SEFV) = .15

South Atlantic
* Food (CUUR0350SAF1) = .40
* Gas (CUUR0350SS47014) = .30
* Energy Services (CUUR0350SEHF) = .20
* Recreation (CUUR0350SAR) = .10

## Total Weights

The formula below represents our weighted aggregate CPI that we will be studying. Each variable is a combination of an item, and the location we used for that item. Our weights were based off the region's population and our assigned weights representing the importance of each item in each location. 

* Formula = .432(Food-NE/MA/SA) + .317(Gas-NE/MA/SA) + .015(Fuels/Utilities-NE) + .01(Apparrel-NE) + .022(Nonalcaholic Beverages-MA) + .066(Food Away From Home-MA) + .092(Energy Services-SA) + .046(Recreation-SA)
             
