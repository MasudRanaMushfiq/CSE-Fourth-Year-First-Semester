import hashlib
import math

# Function to compute SHA-256 hash of given data
def sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Function to split file content into fixed-size blocks
def split_into_blocks(text, block_size=64):
    return [text[i:i+block_size] for i in range(0, len(text), block_size)]

# Function to build Merkle Tree and return root
def build_merkle_root(leaves):
    if len(leaves) == 0:
        return None
    
    # If odd number of leaves, duplicate last one
    while len(leaves) > 1:
        temp = []
        for i in range(0, len(leaves), 2):
            left = leaves[i]
            right = leaves[i+1] if i+1 < len(leaves) else left
            combined = sha256(left + right)
            temp.append(combined)
        leaves = temp
    return leaves[0]

# Function to compute Merkle Root for a text file
def get_merkle_root_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into blocks
    blocks = split_into_blocks(content)
    print("\n[+] File split into", len(blocks), "blocks")

    # Hash each block
    leaf_hashes = [sha256(block) for block in blocks]
    print("\n[+] Leaf Hashes:")
    for i, h in enumerate(leaf_hashes):
        print(f"Block {i+1}: {h}")

    # Build Merkle Root
    root = build_merkle_root(leaf_hashes)
    print("\n[+] Merkle Root:", root)
    return root

# ---------------- MAIN PROGRAM ---------------- #
if __name__ == "__main__":
    # Original file integrity check
    filename = "sample.txt"   # <-- Put your text file name here
    print("=== Merkle Tree File Integrity Check ===")
    original_root = get_merkle_root_from_file(filename)

    # Simulate tampering: modify the file slightly
    # with open(filename, "a", encoding="utf-8") as f:
    #     f.write("\nTampered content!")  # Add extra text

    print("\n--- After Tampering ---")
    tampered_root = get_merkle_root_from_file(filename)

    # Verify integrity
    print("\n=== Integrity Verification ===")
    if original_root == tampered_root:
        print("✅ File integrity verified (No changes detected).")
    else:
        print("❌ File integrity failed (File has been modified!).")
