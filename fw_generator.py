# prototype for JVFW

import source_loader as sl
import enum
import sys

# fw layout
import fw_layout

# fw number
# class FwNumber(enum.IntEnum):
#     boot_loader = enum.auto()
#     main_fw_h0 = enum.auto()
#     main_fw_h1 = enum.auto()
#     main_fw_h2 = enum.auto()
#     main_fw_h3 = enum.auto()
#     main_fw_f0 = enum.auto()

if __name__ == '__main__':
    fw_image = fw_layout.FwImage()
    output_file = open('OneBinary.bin', 'wb')
    for x in range(fw_image.__len__()):
        source_file = sl.SourceLoader(0)
        source_file = open(source_file.load_binary(), 'rb')
        print ('bl size : ', fw_image[x].__len__())
        # fw_image.append(source_file.read(sys.getsizeof(fw_image[2])))
        binary_buffer = source_file.read(fw_image[x].__len__())
        for y in range(binary_buffer.__len__()):
            fw_image[x][y] = binary_buffer[y]
        source_file.close()
    for x in fw_image:
        output_file.write(x)
    output_file.close()


# EOF