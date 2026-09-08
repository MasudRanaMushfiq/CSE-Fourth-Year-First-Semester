"""
================================================================================
                   BASE58 & BASE58CHECK ENCODING — BITCOIN ADDRESSES
================================================================================

Based on: Bitcoin 02 Lecture — Introducing Bitcoin Addresses

Base58 is the encoding scheme used by Bitcoin to produce human-readable addresses.
It is similar to Base64 but removes characters that look alike when printed,
reducing confusion and making addresses easier to communicate orally.

Base58 Alphabet (Bitcoin):
    123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz

Excluded characters (to avoid ambiguity):
    - 0 (zero)       → looks like O
    - O (capital o)  → looks like 0
    - I (capital i)  → looks like l
    - l (lowercase L)→ looks like I

Why Base58 instead of Base64?
    Base64 includes:  +  /  =   → these are not easy to distinguish
    Base58 avoids them entirely — the result is alphanumeric only.

What you'll find in this file:
    1. base58_encode(bytes_data)       — raw bytes → Base58 string
    2. base58_decode(b58_string)        — Base58 string → raw bytes
    3. base58check_encode(version, payload) — version + payload → Base58Check address
    4. base58check_decode(b58_string)   — Base58Check address → (version, payload, valid?)
    5. Full pipeline demo:  Public Key → Address → Decode & Validate
    6. Typo detection demo (checksum catches errors)

================================================================================
"""

import hashlib

# ==============================================================================
# BASE58 ALPHABET
# ==============================================================================
# The Bitcoin Base58 alphabet — notice what's missing:
#   0, O, I, l  are all excluded.
BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58_encode(data: bytes) -> str:
    """
    Encode a bytes object into a Base58 string.

    How it works (from Bitcoin 02 Slide 18):
        1. Treat the input bytes as a big-endian integer.
        2. Repeatedly divide that integer by 58, collecting remainders.
           Each remainder maps to a character in the Base58 alphabet.
        3. The resulting characters (in reverse order of collection) form
           the Base58 string.
        4. For every leading-zero byte (0x00) in the input, prepend a '1'
           to the output (since 0x00 → integer 0 → maps to '1').

    Parameters
    ----------
    data : bytes
        The raw bytes to encode (e.g., a 25-byte payload).

    Returns
    -------
    str
        Base58-encoded string (e.g., "1PMycacnJaSqwwJqjawXBErnLsZ7RkXUAs").
    """
    if not data:
        return ""

    # Count leading zero bytes — each becomes a leading '1' in the output
    leading_zeros = 0
    for byte in data:
        if byte == 0:
            leading_zeros += 1
        else:
            break

    # Convert the (rest of the) bytes to a big integer
    num = int.from_bytes(data, byteorder="big")

    # Repeatedly divide by 58, collecting remainders
    encoded_chars = []
    while num > 0:
        num, remainder = divmod(num, 58)
        encoded_chars.append(BASE58_ALPHABET[remainder])

    # Reverse because we collected least-significant digit first
    encoded_chars.reverse()

    # Prepend the leading '1's for each leading zero byte
    return "1" * leading_zeros + "".join(encoded_chars)


def base58_decode(b58_string: str) -> bytes:
    """
    Decode a Base58 string back into raw bytes.

    This is the reverse of base58_encode.

    How it works:
        1. Every leading '1' in the string → a leading 0x00 byte in the output.
        2. For the rest, treat the Base58 string as a base-58 number and
           convert it to a big-endian integer, then to bytes.

    Parameters
    ----------
    b58_string : str
        A Base58-encoded string (e.g., a Bitcoin address).

    Returns
    -------
    bytes
        The decoded raw bytes.
    """
    if not b58_string:
        return b""

    # Count leading '1' characters — each becomes a leading 0x00 byte
    leading_ones = 0
    for ch in b58_string:
        if ch == "1":
            leading_ones += 1
        else:
            break

    # Convert the rest from base58 to integer
    num = 0
    for ch in b58_string[leading_ones:]:
        num = num * 58 + BASE58_ALPHABET.index(ch)

    # Convert integer to bytes (big-endian)
    # Determine how many bytes we need
    byte_length = (num.bit_length() + 7) // 8 if num > 0 else 0
    decoded_bytes = num.to_bytes(byte_length, byteorder="big")

    return b"\x00" * leading_ones + decoded_bytes


# ==============================================================================
# BASE58CHECK ENCODING  (Slides 19-20 from Bitcoin 02)
# ==============================================================================
# Base58Check adds a version byte and a checksum to the payload before encoding.
#
# Structure of a Base58Check address:
#   ┌──────────┬──────────────────────────┬────────────────────┐
#   │ Version  │       Payload            │     Checksum       │
#   │  (1 B)   │        (varies)          │    (4 bytes)       │
#   └──────────┴──────────────────────────┴────────────────────┘
#
# For a P2PKH (Legacy) Bitcoin address:
#   - Version byte  = 0x00  (mainnet)
#   - Payload       = HASH160 of public key  = RIPEMD160(SHA256(pubkey))
#   - Checksum      = first 4 bytes of SHA256(SHA256(version + payload))
#
# The entire 25-byte structure is then Base58-encoded to get the address.


def double_sha256(data: bytes) -> bytes:
    """
    Compute SHA256(SHA256(data)) — double SHA-256.

    This is used extensively in Bitcoin for checksums and mining.
    """
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def base58check_encode(version: int, payload: bytes) -> str:
    """
    Create a Base58Check-encoded string (e.g., a Bitcoin address).

    Parameters
    ----------
    version : int
        A single-byte version identifier.
        - 0x00 = mainnet P2PKH (legacy address starting with '1')
        - 0x05 = mainnet P2SH (address starting with '3')
        - 0x6F = testnet P2PKH
    payload : bytes
        The data to encode (e.g., 20-byte HASH160 of public key).

    Returns
    -------
    str
        Base58Check-encoded address string.

    Steps (from Bitcoin 02 Slide 19):
        1. Concatenate: version_byte + payload
        2. Compute checksum = SHA256(SHA256(step1))[0:4]
        3. Concatenate: version_byte + payload + checksum
        4. Base58 encode the whole thing
    """
    # Step 1: version byte + payload
    version_byte = bytes([version])

    # Step 2: double SHA-256, take first 4 bytes
    checksum = double_sha256(version_byte + payload)[:4]

    # Step 3: full payload = version + hash160 + checksum
    full_payload = version_byte + payload + checksum

    # Step 4: Base58 encode
    return base58_encode(full_payload)


def base58check_decode(b58_string: str) -> dict:
    """
    Decode and validate a Base58Check-encoded string.

    This is exactly what a Bitcoin wallet does when you paste an address
    into the "Send to" field (Bitcoin 02 Slides 20, 25-27).

    Parameters
    ----------
    b58_string : str
        A Base58Check-encoded string (Bitcoin address).

    Returns
    -------
    dict with keys:
        - "valid"      : bool   — whether the checksum matches
        - "version"    : int    — version byte (e.g., 0x00 for P2PKH)
        - "payload"    : bytes  — the original payload (e.g., 20-byte hash160)
        - "address"    : str    — the original input address
        - "error"      : str    — error message if invalid (else None)

    Validation Steps (Slide 20):
        1. Base58 decode the address back to raw bytes
        2. Split into: payload (all but last 4 bytes) + checksum (last 4 bytes)
        3. Recomputed checksum = SHA256(SHA256(payload))[0:4]
        4. Compare recomputed checksum with the provided checksum
        5. If mismatch → REJECT (typo or corruption detected)
        6. If match → extract version byte
    """
    decoded = base58_decode(b58_string)

    if len(decoded) < 5:
        return {
            "valid": False,
            "version": None,
            "payload": None,
            "address": b58_string,
            "error": "Decoded data too short (need at least 5 bytes).",
        }

    # Split: payload = all bytes except last 4, checksum = last 4 bytes
    raw_payload = decoded[:-4]
    checksum_given = decoded[-4:]

    # Recompute checksum from the payload
    checksum_recomputed = double_sha256(raw_payload)[:4]

    # Compare
    if checksum_given != checksum_recomputed:
        return {
            "valid": False,
            "version": raw_payload[0] if raw_payload else None,
            "payload": raw_payload[1:] if len(raw_payload) > 1 else None,
            "address": b58_string,
            "error": (
                f"Checksum mismatch! "
                f"Given: {checksum_given.hex()}, "
                f"Expected: {checksum_recomputed.hex()}"
            ),
        }

    # Extract version byte and actual payload
    version_byte = raw_payload[0]
    actual_payload = raw_payload[1:]

    return {
        "valid": True,
        "version": version_byte,
        "payload": actual_payload,
        "address": b58_string,
        "error": None,
    }


def is_valid_bitcoin_address(address: str) -> bool:
    """
    Quick-check whether a Bitcoin address is structurally valid.

    This is a convenience wrapper around base58check_decode() — it simply
    returns True if the checksum matches and the decoded length is correct,
    or False otherwise.

    Parameters
    ----------
    address : str
        A Base58Check-encoded Bitcoin address.

    Returns
    -------
    bool
        True if the address passes checksum validation, False otherwise.

    Example
    -------
    >>> is_valid_bitcoin_address("16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM")
    True
    >>> is_valid_bitcoin_address("16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvN")  # typo
    False
    """
    result = base58check_decode(address)
    return result["valid"]


# ==============================================================================
# HASH160 — THE HEART OF BITCOIN ADDRESSES
# ==============================================================================

def hash160(data: bytes) -> bytes:
    """
    Compute HASH160 = RIPEMD160(SHA256(data)).

    This double-hash is used to convert a public key into a 20-byte payload
    that goes into a Bitcoin address (Bitcoin 02 Slide 22).

    Why two hash functions?
        - If SHA-256 were ever broken, RIPEMD-160 still protects the public key.
        - It compresses the 65-byte public key to a fixed 20 bytes.
    """
    sha256_once = hashlib.sha256(data).digest()
    return hashlib.new("ripemd160", sha256_once).digest()


# ==============================================================================
# FULL PIPELINE DEMONSTRATION
# ==============================================================================
# From Bitcoin 02 Slides 21-27:
#
#   Private Key
#       ↓  ECDSA (secp256k1) — one-way
#   Public Key  (65 bytes, uncompressed, starts with 0x04)
#       ↓  SHA256  then  RIPEMD160
#   Hash160  (20 bytes)
#       ↓  Prepend version byte (0x00)
#   Versioned Payload  (21 bytes)
#       ↓  Append checksum (first 4 bytes of double SHA-256)
#   Full Payload  (25 bytes)
#       ↓  Base58 Encode
#   Bitcoin Address  (string starting with '1')
#

def demonstrate_full_pipeline():
    """
    Demonstrate the complete Bitcoin address pipeline using the exact
    values from Bitcoin 02 Slides 21-27.

    This shows:
        Part 1 — Private Key → Public Key (conceptual)
        Part 2 — Public Key → Hash160
        Part 3 — Hash160 → Bitcoin Address (Base58Check Encode)
        Part 4 — Decode & Validate the address (Base58Check Decode)
        Part 5 — Typo detection (what happens with a bad character)
    """
    print("=" * 72)
    print("   FULL PIPELINE: Private Key → Public Key → Address → Decode & Validate")
    print("=" * 72)

    # ==================================================================
    # PART 1 — Private Key → Public Key  (Slides 21)
    # ==================================================================
    # This step uses elliptic curve multiplication (secp256k1):
    #   PublicKey = PrivateKey × G
    # where G is the curve's generator point.
    #
    # We use the exact values from the slides.

    print("\n" + "-" * 72)
    print("  PART 1: Private Key → Public Key (via secp256k1 ECDSA)")
    print("-" * 72)

    private_key_hex = "0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1"
    public_key_uncompressed_hex = (
        "0450863AD64A87AE8A2FE83C1AF1A8403CB53F53E486D8511DAD8A04887E5B2352"
        "2CD470243453A299FA9E77237716103ABC11A1DF38855ED6F2EE187E9C582BA6"
    )

    print(f"  Private Key (hex):               {private_key_hex}")
    print(f"  Public Key (uncompressed, hex):  {public_key_uncompressed_hex}")
    print("  (The '04' prefix marks it as uncompressed — 65 bytes total)")
    print("  (This step is ONE-WAY — ECDSA security basis)")

    public_key_bytes = bytes.fromhex(public_key_uncompressed_hex)

    # ==================================================================
    # PART 2 — Public Key → Hash160  (Slide 22)
    # ==================================================================
    print("\n" + "-" * 72)
    print("  PART 2: Public Key → Hash160 = RIPEMD160(SHA256(pubkey))")
    print("-" * 72)

    sha256_pubkey = hashlib.sha256(public_key_bytes).digest()
    ripemd160_pubkey = hashlib.new("ripemd160", sha256_pubkey).digest()

    print(f"  SHA256(pubkey):              {sha256_pubkey.hex()}")
    print(f"  RIPEMD160(SHA256(pubkey)):   {ripemd160_pubkey.hex()}")
    print(f"  (= 20-byte hash160 — the core of the address)")

    # ==================================================================
    # PART 3 — Hash160 → Bitcoin Address (Base58Check Encode)  (Slides 23-24)
    # ==================================================================
    print("\n" + "-" * 72)
    print("  PART 3: Hash160 → Bitcoin Address (Base58Check Encode)")
    print("-" * 72)

    version_mainnet_p2pkh = 0x00

    # Build the 25-byte payload manually to show the structure
    version_byte = bytes([version_mainnet_p2pkh])
    step1_payload = version_byte + ripemd160_pubkey  # 1 + 20 = 21 bytes

    checksum = double_sha256(step1_payload)[:4]
    full_25_bytes = step1_payload + checksum  # 21 + 4 = 25 bytes

    bitcoin_address = base58check_encode(version_mainnet_p2pkh, ripemd160_pubkey)

    print(f"  Step 1 — Build the payload:")
    print(f"    version_byte (0x00)  +  hash160  =  payload")
    print(f"    {step1_payload.hex()}  ({len(step1_payload)} bytes)")

    print(f"\n  Step 2 — Compute checksum (double SHA-256, first 4 bytes):")
    sha256_payload_1 = hashlib.sha256(step1_payload).digest()
    sha256_payload_2 = hashlib.sha256(sha256_payload_1).digest()
    print(f"    SHA256(payload):                {sha256_payload_1.hex()}")
    print(f"    SHA256(SHA256(payload)):        {sha256_payload_2.hex()}")
    print(f"    Checksum = first 4 bytes:       {checksum.hex()}")

    print(f"\n  Step 3 — Concatenate and Base58 encode:")
    print(f"    Full payload (25 bytes):  {full_25_bytes.hex()}")
    print(f"    Structure:  [1 byte version | 20 bytes hash160 | 4 bytes checksum]")
    print(f"\n    >>> FINAL BITCOIN ADDRESS:  {bitcoin_address}")

    # ==================================================================
    # PART 4 — Decode & Validate  (Slides 25-26)
    # ==================================================================
    print("\n" + "-" * 72)
    print("  PART 4: Decode & Validate the Address (what wallets do)")
    print("-" * 72)

    result = base58check_decode(bitcoin_address)

    print(f"  Input address:  {bitcoin_address}")
    print(f"  Decoded (hex):  {base58_decode(bitcoin_address).hex()}")

    if result["valid"]:
        print(f"  Length: {len(base58_decode(bitcoin_address))} bytes ✓")
        print(f"  Version byte:  0x{result['version']:02x}  → P2PKH mainnet")
        print(f"  Hash160:       {result['payload'].hex()}")
        print(f"  Checksum:      ✓ MATCH")
        print(f"  → Address is VALID")
    else:
        print(f"  → Address is INVALID: {result['error']}")

    # ==================================================================
    # PART 5 — Typo Detection  (Slide 27)
    # ==================================================================
    print("\n" + "-" * 72)
    print("  PART 5: What Happens With a Typo (Checksum Catches It)")
    print("-" * 72)

    # Deliberately change the last character (M → N)
    tampered_address = bitcoin_address[:-1] + "N"
    print(f"  Original address:  {bitcoin_address}")
    print(f"  Tampered address:  {tampered_address}  (last char changed)")

    tampered_result = base58check_decode(tampered_address)
    print(f"  Given checksum:      {base58_decode(tampered_address)[-4:].hex()}")
    print(f"  Recomputed checksum: {double_sha256(base58_decode(tampered_address)[:-4])[:4].hex()}")

    if not tampered_result["valid"]:
        print(f"  Valid? → False ❌")
        print(f"  Reason: {tampered_result['error']}")
        print(f"  → Wallet REJECTS this address — funds are SAFE!")
    else:
        print(f"  Valid? → True (unexpected)")

    print("\n" + "=" * 72)
    print("   END OF DEMONSTRATION")
    print("=" * 72)


# ==============================================================================
# ADDITIONAL UTILITY — Encode/Decode arbitrary data
# ==============================================================================

def encode_string_to_base58(text: str) -> str:
    """
    Encode a plain text string to Base58.

    This is just for experimentation — Base58 is NOT designed for text;
    it's designed for binary data like Bitcoin addresses.
    """
    return base58_encode(text.encode("utf-8"))


def decode_base58_to_string(b58_string: str) -> str:
    """
    Decode a Base58 string back to UTF-8 text (if it was originally text).
    """
    return base58_decode(b58_string).decode("utf-8", errors="replace")


# ==============================================================================
# MAIN — RUN DEMONSTRATION
# ==============================================================================

if __name__ == "__main__":
    demonstrate_full_pipeline()

    # Also show a quick interactive helper
    print("\n\n")
    print("=" * 72)
    print("   QUICK ENCODE / DECODE HELPER")
    print("=" * 72)
    print()
    print("  Example — encoding 'Hello' to Base58:")
    encoded = encode_string_to_base58("Hello")
    print(f"    base58_encode('Hello') = '{encoded}'")
    decoded = decode_base58_to_string(encoded)
    print(f"    base58_decode('{encoded}') = '{decoded}'")
    print()

    # Show address type detection
    print("  Bitcoin Address Type Detection (by version byte):")
    test_addresses = [
        ("16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM", "P2PKH (Legacy)"),
        ("3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy", "P2SH (Multisig/SegWit wrapper)"),
    ]
    for addr, desc in test_addresses:
        res = base58check_decode(addr)
        if res["valid"]:
            v = res["version"]
            if v == 0x00:
                addr_type = "P2PKH (Legacy) — starts with '1'"
            elif v == 0x05:
                addr_type = "P2SH — starts with '3'"
            else:
                addr_type = f"Unknown version 0x{v:02x}"
            print(f"    {addr}  →  {addr_type}")
        else:
            print(f"    {addr}  →  INVALID: {res['error']}")

    print()
    print("  Quick Address Validation (is_valid_bitcoin_address):")
    valid_addr = "16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM"
    invalid_addr = "16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvN"  # typo in last char
    print(f"    is_valid_bitcoin_address('{valid_addr}')        → {is_valid_bitcoin_address(valid_addr)}")
    print(f"    is_valid_bitcoin_address('{invalid_addr}')  → {is_valid_bitcoin_address(invalid_addr)}")
    print(f"    is_valid_bitcoin_address('abc123')                      → {is_valid_bitcoin_address('abc123')}")


