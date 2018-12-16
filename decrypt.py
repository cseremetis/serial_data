max_data = 248 #maximum data size in bytes

#for decrypting epc, tag crc, and message crc
def setCRC(message, offset, length):
    crc = 0xffff
    
    for i in range(offset, offset+length):
        crc = ((crc << 4) | ((message[i] >> 4) & 0xf)) ^ crcTable[crc >> 12]
        crc &= 0xffff
        crc = ((crc << 4) | ((message[i] >> 0) & 0xf)) ^ crcTable[crc >> 12]
        crc &= 0xffff

    return crc

def translate(hex):
    #...