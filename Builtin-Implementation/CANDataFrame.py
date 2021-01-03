class CANDataFrame:
    def __init__(self):
        # TODO Structure under something that easy to count and sum
        self.SOF = 0b1
        self.identifier = 0b00000000001
        self.RTR = 0b1
        self.IDE = 0b0
        self.r = 0b0
        self.DLC = 0b0001
        self.data_field = 0xdfefaf1ff2ff3fff
        self.CRC_field = 0x000a
        self.ACK_field = 0b11
        self.EOF = 0b0000000

    def __bytes__(self):
        return "{0:b}{1:b}{2:b}{3:b}{4:b}{5:04b}{6:064b}{7:016b}{8:07b}".format(self.SOF, self.identifier, self.RTR,
                                                                                self.IDE, self.r,
                                                                                self.DLC, self.data_field,
                                                                                self.CRC_field, self.ACK_field,
                                                                                self.EOF).encode("utf-8")

def main():
    data = CANDataFrame()
    print(bytes(data))