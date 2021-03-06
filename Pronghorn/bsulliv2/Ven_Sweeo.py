# Author: Ben Sullivan
# Date: 11/03/2017

# Necessary module and instrument imports
import sys, visa, time
sys.path.append('../Common')
from ADI_GPIB.AgilentN6705B import *

# Initializes supply
Supply = AgilentN6705B(26)

voltagelist = []    # Initializes array

# Sets up suplly
# Vsupply = Ch1, Ven = Ch2, Vcom = Ch3
Supply.__SetV__(5, 1)
Supply.__SetI__(0.25, 1)
Supply.__SetI__(0.25, 2)


for i in range(3):  # Repeat test 3 times
    level = 1.3     # Starting voltage
    Supply.__SetV__(level, 2)
    Supply.__Enable__(True, (1, 2))
    Isupply = float(Supply.__GetI__(1))     # Find current value
    while Isupply < 0.1:        # When current exceeds this value the device is operational
        level = level+0.0001    # Increment voltage by 0.1 mV
        Supply.__SetV__(level, 2)
        time.sleep(0.1)
        Isupply = float(Supply.__GetI__(1))     # Find current value
        if level >= 3.5:    # Voltage exceeding safe operating levels
            raise Exception ('Voltage higher than expected')

    print ('Enabled at Ven = %g' % level)

    # Repeats same exact test in the opposite direction
    level = 1.4
    Supply.__SetV__(level, 2)
    Supply.__Enable__(True, (1, 2))
    Isupply = float(Supply.__GetI__(1))
    while Isupply > 0.1:
        # print Isupply
        level = level-0.0001
        Supply.__SetV__(level, 2)
        time.sleep(0.1)
        Isupply = float(Supply.__GetI__(1))
        if level <= 0.5:
            raise Exception ('Voltage lower than expected')

    print ('Disabled at Ven = %g' % level)
