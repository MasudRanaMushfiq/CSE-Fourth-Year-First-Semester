import hashlib

message = b"Hello, world!"

md5_hash = hashlib.md5(message).hexdigest()
sha1_hash = hashlib.sha1(message).hexdigest()
sha256_hash = hashlib.sha256(message).hexdigest()

if md5_hash == hashlib.md5(message).hexdigest() :
    print("MD5 hash is consistent")
else :
    print("MD5 hash is inconsistent")
    
    

if len(md5_hash) == 32 :
    print("MD5 hash is 32 characters long")
else :
    print("MD5 hash is not 32 characters long")
    
    
if sha1_hash == hashlib.sha1(message).hexdigest():
    print("SHA-1 hash is consistent")
else:
    print("SHA-1 hash is inconsistent")
    
    
if len(sha1_hash) == 40:
    print("SHA-1 hash is 40 characters long")
else:
    print("SHA-1 hash is not 40 characters long")
    

if sha256_hash == hashlib.sha256(message).hexdigest():
    print("SHA-256 hash is consistent")
else:
    print("SHA-256 hash is inconsistent")


if len(sha256_hash) == 64:
    print("SHA-256 hash is 64 characters long")
else:
    print("SHA-256 hash is not 64 characters long")