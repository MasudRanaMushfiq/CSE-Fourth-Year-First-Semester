import hashlib
data = "Markel Tree"

hash_object = hashlib.sha256(data.encode())
hash_hex=hash_object.hexdigest()

print("Input : ", data)
print("Hash Object: ", hash_object)
print("SHA 256 Hash: ", hash_hex)

# Output:
# Hash Object:  <sha256 _hashlib.HASH object @ 0x0000024A55A899F0>
# SHA 256 Hash:  625da44e4eaf58d61cf048d168aa6f5e492dea166d8bb54ec06c30de07db57e1

#A= 559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd
#B=df7e70e5021544f4834bbee64a9e3789febc4be81470df629cad6ddb03320a5c

#AB = 38164fbd17603d73f696b8b4d72664d735bb6a7c88577687fd2ae33fd6964153