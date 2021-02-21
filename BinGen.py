import os.path

# make byte array
byteBuffer = bytearray([1, 2, 3, 4])

# make binary file
out_file = open('testBin.bin', 'wb')

# byte array (byteBuffer) -> output_file x10
for x in range(0, 10):
    out_file.write(byteBuffer)

# close output file
out_file.close()