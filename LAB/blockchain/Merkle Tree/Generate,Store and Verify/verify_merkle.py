import hashlib

def sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def split_into_blocks(text, block_size=64):
    return [text[i:i+block_size] for i in range(0, len(text), block_size)]

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

def verify_file(filename, root_file="merkle_root.txt"):
    # Read stored root
    with open(root_file, "r") as f:
        saved_root = f.read().strip()

    # Compute new root
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = split_into_blocks(content)
    leaf_hashes = [sha256(block) for block in blocks]
    new_root = build_merkle_root(leaf_hashes)

    # Compare
    print("Stored Root:", saved_root)
    print("Current Root:", new_root)

    if saved_root == new_root:
        print("✅ Integrity Verified: No change detected")
    else:
        print("❌ Integrity Failed: File has been modified!")

if __name__ == "__main__":
    verify_file("sample.txt")
