
# make byte array
byteBuffer = bytearray(b'testbinary file3')

# make binary file
out_file = open('testBin3.bin', 'wb')

# byte array (byteBuffer) -> output_file x10
for x in range(0, 100):
    out_file.write(byteBuffer)

# close output file
out_file.close()