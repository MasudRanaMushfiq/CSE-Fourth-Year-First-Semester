import hashlib

# Function to compute SHA-256 hash
def sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Split file into blocks
def split_into_blocks(text, block_size=64):
    return [text[i:i+block_size] for i in range(0, len(text), block_size)]

# Build Merkle Tree
def build_merkle_root(leaves):
    if len(leaves) == 0:
        return None

    while len(leaves) > 1:
        temp = []
        for i in range(0, len(leaves), 2):
            left = leaves[i]
            right = leaves[i+1] if i+1 < len(leaves) else left
            temp.append(sha256(left + right))
        leaves = temp

    return leaves[0]

def generate_merkle_root(filename, root_file="merkle_root.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = split_into_blocks(content)
    leaf_hashes = [sha256(block) for block in blocks]

    root = build_merkle_root(leaf_hashes)

    # Save root into file
    with open(root_file, "w") as f:
        f.write(root)

    print("Merkle Root Generated:", root)
    print(f"Saved to {root_file}")

if __name__ == "__main__":
    generate_merkle_root("sample.txt")