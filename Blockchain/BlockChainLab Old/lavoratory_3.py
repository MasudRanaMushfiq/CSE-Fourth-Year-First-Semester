import hashlib
string = "Hello World!"
hash_object = hashlib.sha256()
hash_object.update(string.encode('utf-8'))
hex_dig = hash_object.hexdigest()
print("String: {}".format(string))
print("hash value (SHA-256): {}".format(hex_dig))
