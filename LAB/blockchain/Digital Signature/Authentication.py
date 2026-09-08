# “Encrypt” with private key , “Decrypt” with public key

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

# ------------------ Generate Keys ------------------
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
print("Private Key generated.", private_key)
public_key = private_key.public_key()
print("Public Key generated.", public_key)
# ------------------ Message ------------------
message = b"This is a secret message"

# ------------------ 'Private Key (Sign) ------------------
signature = private_key.sign(
    message,
    padding.PKCS1v15(), 
    hashes.SHA256()
)
print("Signature (hex):", signature.hex())
message = b"This is a secret message Intercepted"
# ------------------ 'Public Key (Verify) ------------------
try:
    public_key.verify(
        signature,  
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("✅ Signature is valid!")
except Exception:
    print("❌ Signature is invalid!")
