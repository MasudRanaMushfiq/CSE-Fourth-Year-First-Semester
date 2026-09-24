import hashlib

message= b"hello, world!"
sha3_256 = hashlib.sha3_256()

sha3_256.update(message)

digest = sha3_256.digest()

hexdigest = digest.hex()

print(hexdigest)