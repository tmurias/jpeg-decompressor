import sys

def main():
    # TODO: Check number of args
    jpg_filename = sys.argv[1]
    # TODO: Check if filename is jpg

    blocks = dict()
    with open(jpg_filename, 'rb') as jpg_file:
        buf = b''
        while True:
            curr_byte = jpg_file.read(1)
            if not curr_byte:
                break
            buf += curr_byte
            if len(buf) < 3:
                continue
            if buf[-2] == 0xFF:
                if not get_block_name(buf[-1]):
                    continue
                blocks[get_block_name(buf[1])] = buf[:-2]
                buf = buf[-2:]
        blocks[get_block_name(buf[1])] = buf
    for byte in blocks['DHT']:
        print(byte)
    for block_name, block_data in blocks.items():
        print(block_name + ': ' + str(len(block_data)))


def get_block_name(byte2):
    if byte2 == 0xD8:
        return 'SOI'
    if byte2 == 0xC0:
        return 'SOF0'
    if byte2 == 0xC2:
        return 'SOF2'
    if byte2 == 0xC4:
        return 'DHT'
    if byte2 == 0xDB:
        return 'DQT'
    if byte2 == 0xDD:
        return 'DRI'
    if byte2 == 0xDA:
        return 'SOS'
    if (byte2 & 0b11111000) == 0xD0:
        return 'RST' + str(byte2 & 0b111)
    if (byte2 & 0b11110000) == 0xE0:
        return 'APP' + str(byte2 & 0b1111)
    if byte2 == 0xFE:
        return 'COM'
    if byte2 == 0xD9:
        return 'EOI'

if __name__ == '__main__':
    main()
