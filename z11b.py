import argparse
import zlib

parser = argparse.ArgumentParser(prog="z11b",description="z11b is Python tool to deal with zlib")
parser.add_argument('-o','--output',help="Output to this file [ex: --output filename.txt]",default='output.txt')
parser.add_argument('-d','--decompress',help="Decompress the zlib data [ex: --decompress filename.txt]")
parser.add_argument('-c','--compress',help="Compress the given text file [ex: --compress filename.txt]")


args=parser.parse_args()
if args.decompress:
    file=open(args.decompress,'rb')
    zlib_data=file.read()
    decompressed_data=zlib.decompress(zlib_data).decode()
    file.close()
    file=open(args.output,'w')
    file.write(decompressed_data.decode())
    file.close()
    print("File decompressed successfully...\nThe output is written into ",args.output)

if args.compress:
    file=open(args.compress,"r")
    data = file.read().encode()
    compressed_data=zlib.compress(data)
    file.close()
    file=open(args.output,'w')
    file.write(compressed_data)
    file.close()
    print("File compressed successfully...\nThe output is written into ",args.output)
