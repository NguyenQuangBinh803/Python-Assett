""" The following bit-manipulation methods are written to take a tuple as input, which is provided by the Bitfield class. The construct
looks weired, however the call to a setBit() looks ok and the editor (PyCharm) suggests all
possible bit names. I did not find a more elegant solution that calls the setBit()-function and needs
only one argument.
Example call:
    setBit( STW1.bm01NoOff2() ) """

def setBit(TupleBitField_BitMask):
    # word = word | bit_mask
    TupleBitField_BitMask[0].word = TupleBitField_BitMask[0].word | TupleBitField_BitMask[1]


def isBit(TupleBitField_BitMask):
    # (word & bit_mask) != 0
    return (TupleBitField_BitMask[0].word & TupleBitField_BitMask[1]) !=0


def clrBit(TupleBitField_BitMask):
    #word = word & (~ BitMask)
    TupleBitField_BitMask[0].word = TupleBitField_BitMask[0].word & (~ TupleBitField_BitMask[1])


def toggleBit(TupleBitField_BitMask):
    #word = word ^ BitMask
    TupleBitField_BitMask[0].word = TupleBitField_BitMask[0].word ^ TupleBitField_BitMask[1]

""" Create a Bitfield type for each control word of the application. (e.g. 16bit length). 
Assign a name for each bit in order that the editor (e.g. PyCharm) suggests the names from outside. 
The bits are defined as methods that return the corresponding bit mask in order that the bit masks are read-only
and will not be corrupted by chance.
The return of each "bit"-function is a tuple (handle to bitfield, bit_mask) in order that they can be 
sent as arguments to the single bit manipulation functions (see above): isBit(), setBit(), clrBit(), toggleBit()
The complete word of the Bitfield is accessed from outside by xxx.word.
Examples:
    STW1 = STW1Type(0x1234) # instanciates and inits the bitfield STW1, STW1.word = 0x1234
    setBit(STW1.bm00() )    # set the bit with the name bm00(), e.g. bm00 = bitmask 0x0001
    print("STW1.word =", hex(STW1.word))
"""

class STW1Type():
    # assign names to the bit masks for each bit (these names will be suggested by PyCharm)
    #    tip: copy the application's manual description here
    def __init__(self, word):
        # word = initial value, e.g. 0x0000
        self.word = word

    # define all bits here and copy the description of each bit from the application manual. Then you can jump
    #    to this explanation with "F3"
    #    return the handle to the bitfield and the BitMask of the bit.
    def bm00NoOff1_MeansON(self):
        # 0001 0/1= ON (edge)(pulses can be enabled)
        #        0 = OFF1 (braking with ramp-function generator, then pulse suppression & ready for switching on)
        return self, 0x0001

    def bm01NoOff2(self):
        # 0002  1 = No OFF2 (enable is possible)
        #       0 = OFF2 (immediate pulse suppression and switching on inhibited)
        return self, 0x0002

    def bm02NoOff3(self):
        # 0004  1 = No OFF3 (enable possible)
        #       0 = OFF3 (braking with the OFF3 ramp p1135, then pulse suppression and switching on inhibited)
        return self, 0x0004

    def bm03EnableOperation(self):
        # 0008  1 = Enable operation (pulses can be enabled)
        #       0 = Inhibit operation (suppress pulses)
        return self, 0x0008

    def bm04RampGenEnable(self):
        # 0010  1 = Hochlaufgeber freigeben (the ramp-function generator can be enabled)
        #       0 = Inhibit ramp-function generator (set the ramp-function generator output to zero)
        return self, 0x0010

    def b05RampGenContinue(self):
        # 0020  1 = Continue ramp-function generator
        #       0 = Freeze ramp-function generator (freeze the ramp-function generator output)
        return self, 0x0020

    def b06RampGenEnable(self):
        # 0040  1 = Enable speed setpoint; Drehzahlsollwert freigeben
        #       0 = Inhibit setpoint; Drehzahlsollwert sperren (set the ramp-function generator input to zero)
        return self, 0x0040

    def b07AcknowledgeFaults(self):
        # 0080 0/1= 1. Acknowledge faults; 1. Quittieren Störung
        return self, 0x0080

    def b08Reserved(self):
        # 0100 Reserved
        return self, 0x0100

    def b09Reserved(self):
        # 0200 Reserved
        return self, 0x0200

    def b10ControlByPLC(self):
        # 0400  1 = Control by PLC; Führung durch PLC
        return self, 0x0400

    def b11SetpointInversion(self):
        # 0800  1 = Setpoint inversion; Sollwert Invertierung
        return self, 0x0800

    def b12Reserved(self):
        # 1000 Reserved
        return self, 0x1000

    def b13MotorPotiSPRaise(self):
        # 2000 1 = Motorized potentiometer setpoint raise; (Motorpotenziometer Sollwert höher)
        return self, 0x2000

    def b14MotorPotiSPLower(self):
        # 4000 1 = Motorized potentiometer setpoint lower; (Motorpotenziometer Sollwert tiefer)
        return self, 0x4000

    def b15Reserved(self):
        # 8000 Reserved
        return self, 0x8000


""" test the constrution and methods """
STW1 = STW1Type(0xff1f)
print("STW1.word                =", hex(STW1.word))

clrBit(STW1.bm00NoOff1_MeansON())
print("STW1.word                =", hex(STW1.word))

STW1.word = 0x1234
print("STW1.word                =", hex(STW1.word))

setBit( STW1.bm00NoOff1_MeansON() )
print("STW1.word                =", hex(STW1.word))

clrBit( STW1.bm00NoOff1_MeansON() )
print("STW1.word                =", hex(STW1.word))

toggleBit(STW1.bm03EnableOperation())
print("STW1.word                =", hex(STW1.word))

toggleBit(STW1.bm03EnableOperation())
print("STW1.word                =", hex(STW1.word))

print("STW1.bm00ON              =", isBit(STW1.bm00NoOff1_MeansON() ) )
print("STW1.bm04                =", isBit(STW1.bm04RampGenEnable()  ) )
