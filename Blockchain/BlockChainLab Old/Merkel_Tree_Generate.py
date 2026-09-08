import hashlib

def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def merkle_tree(transactions):
    hashes = [sha256(tx) for tx in transactions]

    print("Leaf Level:")
    for h in hashes:
        print(h)
    print()

    while len(hashes) > 1:
        if len(hashes) % 2 == 1:
            hashes.append(hashes[-1])

        new_hashes = []
        for i in range(0, len(hashes), 2):
            new_hashes.append(sha256(hashes[i] + hashes[i + 1]))

        hashes = new_hashes

        print("Next Level:")
        for h in hashes:
            print(h)
        print()

    return hashes[0]

transactions = [
    "Masud",
    "Plabon",
    "Mosabbeer"
]

print("Merkle Tree:")
root = merkle_tree(transactions)

print("Merkle Root:")
print(root)


