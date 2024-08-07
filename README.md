# Battery Charging Characteristics of WAS 2.0 project

The project intends to study the charging charaacteristics of the battery in WAS 2.0 project. Battery characteristics is necessary to implement proper Battery Management System (BMS), increase the stability of the system, indicate battery health. 

## Results

I measured charging current, voltage of battery and temperature of battery in the project. Charging of battery was conducted at three C-rate (1C, 0.5C and 0.25C). We have used H18650CQ Li-ion cell with 2550 mAh and 9.18 Wh rating in series in our system.

The charging current, voltages and temperature data were logged to SD Card and analysed, following are the results.

![Charging current](<https://github.com/ParuHangRai-PRI/Battery-Charger-Analysis/blob/main/output.png> "Charging current over time")

                    *Fig 1: Charging current over time*

![Voltage](<https://github.com/ParuHangRai-PRI/Battery-Charger-Analysis/blob/main/output1.png> "Voltage across cell over time")

                    *Fig 2: Voltage across cell over time*

![Temperature](<https://github.com/ParuHangRai-PRI/Battery-Charger-Analysis/blob/main/tempr.png> "Cell temperature over time")
                    
                    *Fig 3: Cell temperature over time*

## Discussion

From the graph plotted we can see the charging characteristics of battery aligns with the Li-Ion characteristics described and thus, our implemented system works as intended. 

The circuit however has issues regarding actual voltage measurement. The voltage measurement is plagued with error when we start charging and the voltage measured by circuit is higher than actual cell voltage. This is because, the battery negative terminal and the PCB ground has a potential difference between them. As the current increaes the potential difference also increases.

|C-rate | While charging (mV)| While not charging (mV)|
|---|---|---|
|1C|274|4|
|0.5C|84|4|
|0.25C|36|4|

This maybe due to the common **impedance coupling**, **ground loop** or **Some other parasitic resistive elements between them.** 

Thus, charging current or discharging current will be suitable method to implement in BMS system to maintain battery at optimum health. We can estimate the battery health from the amount of current discharged or charged in a unit time and compare it to the rated charging or discharging capacity to get accurate measurement of battery status. This method however requires an initial estimation of the battery status, which should be measured with the battery voltage level.

The operating temperature at 1C reaches ~38°C max but at 0.5C it only reaches ~29°C max so, if we want temperature stability 0.5C is better C-rate with less maximum temperature and wider stable temperature region. 0.25C is unfortunately takes too much time to consider for our purpose.

## Future prospects

This project lights an insight into the WAS BMS and the ways to imporove it. The improvement that can be done to WAS BMS based on the results of this projects are:

1. Implement battery percentage and health monitor
2. Change voltage based battery health monitoring to current based monitoring 
3. Find the sources of noise in WAS charging circuitry
4. Fine tune optimal charging rate

We also can look to solve PCB ground and battery negative terminal potential difference.


