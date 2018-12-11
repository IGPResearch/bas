# This file runs the algorithm, calling the file identify_events.py
# In this file you:
#   1. Provide the location of the .csv file containing the heat flux data
#   2. Set your constraints for defining a heat flux event (in Wm-2)
# The example test data I have provided is anomaly data (as defined in the readme)
# This code was developed in association with Tony Philips at the British Antarctic Survey.

import identify_events
 

from identify_events import identify_events, show_events
import numpy as np    # need to do this as if you only import the functions from the script, it doesn't import numpy for you
import pandas as pd

# Import the data as a .csv file
all_data = pd.read_csv('PATH_TO_FILE/Example_Heat_Flux_Inputs.csv')

# Determine the column from the .csv input file to be run through the algorithm.  In the example data columns are labelled by year!
north_data = all_data['2000']

# The first number defines the threshold (or smallest magnitude) that defines an event
# In this example, 50 Wm-2 or higher is an event. 
# The second number defines the value that bounds an event either side of the threshold value. 
# In this example, 20 Wm-2 is the lowest value that counts, ie 3.0 24.0 45.0 67.0 67.0 95.0 20.0 -2.0 would be a 6 day event with a peak magnitude of 95 Wm-2
events_north = identify_events(north_data, 50., 20.)

# Show events prints the results to the terminal window. 
show_events(north_data, *events_north)                    # note the * which means "unpack the tuple into separate parameters"

# The user has complete freedom to edit the numbers definding events.  In the example data here, we use the convention that a positive heat flux represents a transfer of energy from the ocean into the atmosphere.
# If this is not the case, then edits are required to identify_events.py (see coments there)
