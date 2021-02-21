# prototype for JVFW

import source_loader as sl
import enum

# fw number
class FwNumber(enum.IntEnum):
    boot_loader = enum.auto()
    main_fw_h0 = enum.auto()
    main_fw_h1 = enum.auto()
    main_fw_h2 = enum.auto()
    main_fw_h3 = enum.auto()
    main_fw_f0 = enum.auto()

if __name__ == '__main__':
    source_list = list()
    for x in FwNumber:
        # source_list.append(sl.SourceLoader())
        source_list.append(x)
    for x in source_list:
        print(x)


# EOF