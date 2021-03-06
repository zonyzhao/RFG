from ADI_GPIB.GPIBObject import GPIBObjectBaseClass as GPIBObjectBaseClass
import time
import string

class AgilentE5071C(GPIBObjectBaseClass):
    def __init__(self, addr=-1, delay=0.1):
        GPIBObjectBaseClass.__init__(self, 'N6705B', addr)
        self.__delay__ = delay

        # VNA.__SetSweepType(1, 'LOG')#
        # VNA.__SetStartf__(1, 10e06)#
        # VNA.__SetStopf__(1, 10.01e09)#
        # VNA.__SetNumPoints__(1, 1e3)
        # VNA.__SetAvg__(1, 16)
        # VNA.__SetTime__(1, 1)
        # VNA.__SetTrigType__('MAN')
        # VNA.__SetContinuous__(1, False)
        # VNA.__EnableAvg(1, True)
        # VNA.__EnableTrigAvg__(True)

    def __CheckStatus__(self):
        return int(self.instr.ask('*OPC?'))

    def __SetSweepType__(self, trace, type):  # May be different for PXA - see [:SENSe]:SWEep:TYPE FFT|SWEep***
        self.instr.write(':SENS%d:SWE:TYPE %s' % (trace, type))

    def __SetStartf__(self, trace, freq):  # Same on PXA
        self.instr.write(':SENS%d:FREQ:STAR %g' % (trace, freq))

    def __SetStopf__(self, trace, freq):  # Same on PXA
        self.instr.write(":SENS%d:FREQ:STOP %g" % (trace, freq))

    def __SetNumPoints__(self, trace, pts):  # Same on PXA
        self.instr.write(":SENS%d:SWE:POIN %g" % (trace, pts))

    def __SetAvg__(self, trace, num):  # Same on PXA
        self.instr.write(":SENS%d:AVER:COUN %g" % (trace, num))

    def __SetAutoTime__(self, trace, enab):  # Same on PXA
        self.instr.write(":SENS%d:SWE:TIME:AUTO %d" % (trace, enab))

    def __SetTrigType__(self, typ):  # Same on PXA (I think?)
        self.instr.write(":TRIG:SOUR %s" % typ)

    def __SetContinuous__(self, trace, enab):  # Same on PXA
        if enab:
            self.instr.write(":INIT%d:CONT ON" % trace)
        else:
            self.instr.write(":INIT%d:CONT OFF" % trace)

    def __EnableAvg__(self, trace, enab):  # Same on PXA
        if enab:
            self.instr.write(":SENS%d:AVER ON" % trace)
        else:
            self.instr.write(":SENS%d:AVER OFF" % trace)

    def __EnableTrigAvg__(self, enab):  # Can't find on PXA***
        if enab:
            self.instr.write(":TRIG:AVER ON")
        else:
            self.instr.write(":TRIG:AVER OFF")

    def __SetActiveTrace__(self, channel, trace):  # Can't find on PXA***
        self.instr.write(":CALC%d:PAR%d:SEL" % (channel, trace))

    def __SetBBalParam__(self, channel, trace, param):  # Can't find on PXA***
        self.instr.write(":CALC%d:FSIM:BAL:PAR%d:BBAL %s" % (channel, trace, param))

    def __SetActiveFormat__(self, channel, format):  # Can't find on PSA: see CALCulate:EVM:MARKer[1]|2|...|12:CFORmat RECTangular|POLar***
        self.instr.write(":CALC%d:FORM %s" % (channel, format))

    def __InitMeas__(self, channel):  # Same on PXA
        self.instr.write('INIT%d' % channel)

    def __SingleTrig__(self):   # Can't find on PXA***
        self.instr.write(':TRIG:SING')

    def __GetData__(self, channel):  # Can't find on PXA***
        return self.instr.ask("CALC%d:DATA:FDAT?" % channel)
