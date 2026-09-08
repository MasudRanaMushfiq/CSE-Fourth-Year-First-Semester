import hashlib

# Function to hash data using SHA-256
def sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Function to compute Merkle Root
def merkle_root(transactions):
    if not transactions:
        return None
    
    # Hash all transactions first
    hashes = [sha256(tx) for tx in transactions]

    # Keep reducing until one root remains
    while len(hashes) > 1:
        # If odd number of hashes, duplicate last one
        if len(hashes) % 2 != 0:
            hashes.append(hashes[-1])

        # Pairwise hash
        new_hashes = []
        for i in range(0, len(hashes), 2):
            combined = hashes[i] + hashes[i+1]
            new_hashes.append(sha256(combined))

        hashes = new_hashes

    return hashes[0]  # Final Merkle Root


# ---- Main program ----
transactions = []

# Ask user for number of transactions
n = int(input("Enter number of transactions: "))

# Take transaction inputs
for i in range(n):
    tx = input(f"Enter transaction {i+1}: ")
    transactions.append(tx)

# Compute Merkle Root
root = merkle_root(transactions)

# Print results
print("\nMerkle Root:", root)
print("Transactions:")
for tx in transactions:
    print(" -", tx)
