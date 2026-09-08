import hashlib
import json
import time


class Blockheader:
    def __init__(self, version, difficulty, previous_hash="0", merkle_root="dummy_merkle_root", timestamp=None):
        self.version = version
        self.difficulty = difficulty
        self.previous_hash = previous_hash
        self.merkle_root = merkle_root
        self.timestamp = timestamp if timestamp else int(time.time())


class Block:
    def __init__(self, data, blockheader):
        self.data = data
        self.blockheader = blockheader
        self.nonce = 0
        self.hash = ""
        self.mine(self.blockheader.difficulty)

    def mine(self, difficulty):
        while self.hash[0:difficulty] != '0' * difficulty:
            self.nonce += 1
            hash_string = (
                str(self.data) +
                str(self.blockheader.previous_hash) +
                str(self.blockheader.merkle_root) +
                str(self.blockheader.timestamp) +
                str(self.nonce) +
                str(self.blockheader.version)
            )
            self.hash = hashlib.sha256(hash_string.encode()).hexdigest()
            print(f"Mining... Nonce: {self.nonce}, Hash: {self.hash}", end="\r")
        return self.hash

    def serialize(self):
        block_dict = {
            "data": self.data,
            "blockheader": self.blockheader.__dict__,
            "nonce": self.nonce,
            "hash": self.hash
        }
        return block_dict  


class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_header = Blockheader(version=1, difficulty=self.difficulty, previous_hash="0")
        genesis_block = Block("Genesis Block", genesis_header)
        self.chain.append(genesis_block)

    def add_block(self, data):
        previous_hash = self.chain[-1].hash
        blockheader = Blockheader(version=1, difficulty=self.difficulty, previous_hash=previous_hash)
        new_block = Block(data, blockheader)
        self.chain.append(new_block)

    def serialize_chain(self):
        blockchain_dict = [block.serialize() for block in self.chain]
        return json.dumps(blockchain_dict,indent=1)
    

# Example usage
my_blockchain = Blockchain(difficulty=3)
my_blockchain.add_block("First real block")
my_blockchain.add_block("Second real block")
my_blockchain.add_block("Third real block")
my_blockchain.add_block("Fourth real block")
my_blockchain.add_block("Fifth real block")


print(my_blockchain.serialize_chain())
