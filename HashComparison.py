import time, hashlib, zlib

inputFile = "G:\ISO and Installers\pfSense-CE-2.4.4-RELEASE-p3-amd64.iso.gz"

output = "the hash will go here"

#cobbled Functions

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha1(fname):
    hash_sha1 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha1.update(chunk)
    return hash_sha1.hexdigest()

def sha512(fname):
    hash_sha512 = hashlib.sha512()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha512.update(chunk)
    return hash_sha512.hexdigest()

def adler32(fname):
    in_file = open(inputFile, "rb") 
    data = in_file.read()
    in_file.close()
    return zlib.adler32(data)

def ripemd160(fname):
    hash_ripemd160 = hashlib.new('ripemd160')
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_ripemd160.update(chunk)
    return hash_ripemd160.hexdigest()

def crc32(fname):
    in_file = open(inputFile, "rb") 
    data = in_file.read()
    in_file.close()
    return zlib.crc32(data)

def whirlpool(fname):
    hash_whirlpool = hashlib.new('whirlpool')
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_whirlpool.update(chunk)
    return hash_whirlpool.hexdigest()

def shake128(fname):
    hash_shake128 = hashlib.new('shake_128')
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_shake128.update(chunk)
    return hash_shake128.hexdigest(128)

def blake2b(fname):
    hash_blake2b = hashlib.new('blake2b')
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_blake2b.update(chunk)
    return hash_blake2b.hexdigest()



#######
#output
#######

#MD5
md5Start = time.perf_counter()
output = md5(inputFile)
md5Stop = time.perf_counter()
print("############################################################")
print("MD5")
print(output)
print(md5Stop - md5Start)
print("############################################################")

#SHA1
sha1Start = time.perf_counter()
output = sha1(inputFile)
sha1Stop = time.perf_counter()
print("############################################################")
print("SHA-1")
print(output)
print(sha1Stop - sha1Start)
print("############################################################")

#SHA512
sha1Start = time.perf_counter()
output= sha512(inputFile)
sha1Stop = time.perf_counter()
print("############################################################")
print("SHA-512")
print(output)
print(sha1Stop - sha1Start)
print("############################################################")

#looked like 'pip install tiger' might give me a library for this but
#it requires python 2.4 and I'm running in 3.x
#tiger requires python 2
#Tiger
#tigerStart = time.perf_counter()
#insert hash function
#tigerStop = time.perf_counter()
#print("############################################################")
#print("Tiger")
#print(output)
#print(tigerStop - tigerStart)
#print("############################################################")

#Adler32
adler32Start = time.perf_counter()
output = adler32(inputFile)
adler32Stop = time.perf_counter()
print("############################################################")
print("Adler32")
print(output)
print(adler32Stop - adler32Start)
print("############################################################")

#RipeMD160
ripemd160Start = time.perf_counter()
output = ripemd160(inputFile)
ripemd160Stop = time.perf_counter()
print("############################################################")
print("ripemd160")
print(output)
print(ripemd160Stop - ripemd160Start)
print("############################################################")

#crc32
crc32Start = time.perf_counter()
output = crc32(inputFile)
crc32Stop = time.perf_counter()
print("############################################################")
print("crc32")
print(output)
print(crc32Stop - crc32Start)
print("############################################################")

#whirlpool
whirlpoolStart = time.perf_counter()
output = whirlpool(inputFile)
whirlpoolStop = time.perf_counter()
print("############################################################")
print("whirlpool")
print(output)
print(whirlpoolStop - whirlpoolStart)
print("############################################################")

#shake_128
shake128Start = time.perf_counter()
output = shake128(inputFile)
shake128Stop = time.perf_counter()
print("############################################################")
print("shake_128")
print(output)
print(shake128Stop - shake128Start)
print("############################################################")

#BLAKE2b
BLAKE2bStart = time.perf_counter()
output=blake2b(inputFile)
BLAKE2bStop = time.perf_counter()
print("############################################################")
print("BLAKE2b")
print(output)
print(BLAKE2bStop - BLAKE2bStart)
print("############################################################")





      
