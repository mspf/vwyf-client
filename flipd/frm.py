class Frm:

    WDTH = 28
    HGHT = 7

    def __init__(self, adrs=0xff, white=False):
        self.b = bytearray([
            0x80,  # header
            0x83,  # 28 bytes refresh
            int(adrs), # sanity check address
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, # 28 bytes data
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
            0x8F # EOT
        ])

        if white:
            self.b[3:31] = [0xff] * 28

    def __setitem__(self, i, b):
        self.b[i+3] = b

    def __str__(self):
        s = ""
        for x in range(3, 31):
            c = ""
            for y in range(7):
                if self.b[x] & (0x1 << y):
                    c = "o" + c
                else:
                    c = "." + c
            s += c + "\n"
        return s
