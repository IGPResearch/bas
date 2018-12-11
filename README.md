The British Antarctic Survey contributed a number of elements to the Iceland-Greenland seas Project, including climate modelling. 
Code in this repository was developed at BAS for use in publications for the IGP project.  

Here we replicate code that is also available here: https://github.com/japopeBAS/Heat_Flux

Heat Flux README
An algorithm for determining the the frequency of events that meet a selection of criteria. This is an example for Heat Fluxes and includes example data.

In this folder you can view:

Run_Algorithm.py This is the file that is run to analyse a .csv file of heat flux data. Within in this file you can set the limits that represent the threshold value for a heat flux event and the boundary values for bracketing each heat flux events. These values are free for a user to adjust.

Identify_Events.py Called by Run_Algorithm.py, this file details the code for the algorithm. It is important to note that this code assumes the convention that a positive heat flux represents a transfer of energy from the ocean into the atmosphere. A note in the code documents where changes need to be made if this is not accurate (particularly if you are using ERA-Interim data).

Example_Heat_Flux_Inputs.csv Example data that can be used to test the use of the algorithm before making your own modifications.

This code was developed in the summer of 2018 at the British Antarctic Survey by James Pope and Tony Philips.
