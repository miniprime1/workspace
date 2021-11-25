import hashlib

print("Hasher, version 1.0")
print("Copright (c) 2020 miniprime1\n")

source = input("Input: ")
print("")

md5 = hashlib.md5()
md5.update(source.encode())
print("MD5:", md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update(source.encode())
print("SHA1:", sha1.hexdigest())

sha224 = hashlib.sha224()
sha224.update(source.encode())
print("SHA224:", sha224.hexdigest())

sha256 = hashlib.sha256()
sha256.update(source.encode())
print("SHA256:", sha256.hexdigest())

sha384 = hashlib.sha384()
sha384.update(source.encode())
print("SHA384:", sha384.hexdigest())

sha512 = hashlib.sha512()
sha512.update(source.encode())
print("SHA512:", sha512.hexdigest())