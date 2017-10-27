import sys, visa, time
sys.path.append('../Common')
from ADI_GPIB.AgilentN5181A import *
from ADI_GPIB.AgilentN9030A import *

# Supply = E3631A(23)
Source1 = AgilentN5181A(20)
Source2 = AgilentN5181A(11)
Analyzer = AgilentN9030A(18)

# Source1.__SetState__(1)
# Source2.__SetState__(1)
# print Source1.__GetState__()
# print Source2.__GetState__()
# time.sleep(0.5)
# Source1.__SetState__(0)
# Source2.__SetState__(0)
# print Source1.__GetState__()
# print Source2.__GetState__()

# Analyzer.__StoreState__('BS_Test_State')
# time.sleep(1)
# Analyzer.__LoadState__('BS_Test_State')
# Source1.__SetFreq__(3.999e9)
# Source2.__SetFreq__(4.001)
# print Source1.__GetFreq__()

# print Analyzer.__Setfc__(4.03e9)
# Analyzer.__SetMarkerFreq__(1, 4.003e9)
# print Analyzer.__GetMarkerAmp__(1)
# Analyzer.__MarkerMax__(1)
# print Analyzer.__GetSpan__()
# print Analyzer.__SetSpan__(10e9)
# print Analyzer.__Setfc__(4.03e9)
# Analyzer.__LoadState__('BS_Test_State')

# Analyzer.__LoadState__('BS_Test_State')
Source1.__SetFreq__(99e6)
Source2.__SetFreq__(101e6)
Analyzer.__SetSpan__(10e3)
Analyzer.__Setfc__(97e6)
Analyzer.__SetMarkerFreq__(1, 97e6)
time.sleep(1)
print Analyzer.__GetMarkerAmp__(1)
Analyzer.__Setfc__(103e6)
Analyzer.__SetMarkerFreq__(1, 103e6)
time.sleep(1)
print Analyzer.__GetMarkerAmp__(1)
