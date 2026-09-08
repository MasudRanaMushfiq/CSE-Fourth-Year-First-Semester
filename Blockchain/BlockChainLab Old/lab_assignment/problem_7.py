import hashlib 
import time 

class Block: 
 def __init__(self, data, previous_hash): 
  self.timestamp = time.time() 
  self.data = data 
  self.previous_hash = previous_hash 
  self.hash = self.generate_hash() 
 
 def generate_hash(self): 
  block_contents = str(self.timestamp) + str(self.data) + str(self.previous_hash) 
  block_hash = hashlib.sha256(block_contents.encode()).hexdigest() 
  return block_hash 
class Blockchain: 
 def __init__(self): 
  self.chain = [self.create_genesis_block()] 
 
 def create_genesis_block(self): 
  return Block("Genesis Block", "0") 
 
 def get_latest_block(self): 
  return self.chain[-1] 
 
 def add_block(self, new_block): 
  new_block.previous_hash = self.get_latest_block().hash 
  new_block.hash = new_block.generate_hash() 
  self.chain.append(new_block) 
 
 def is_chain_valid(self): 
  for i in range(1, len(self.chain)): 
      current_block = self.chain[i] 
      previous_block = self.chain[i - 1]  
      if current_block.hash != current_block.generate_hash(): 
        return False
      if current_block.previous_hash != previous_block.hash: 
        return False 
  return True 
 
if __name__ == '__main__': 
 blockchain = Blockchain() 

 print("Mining block 1...") 
 block1 = Block("Transaction 1", "") 
 blockchain.add_block(block1) 
 
 print("Mining block 2...") 
 block2 = Block("Transaction 2", "") 
 blockchain.add_block(block2) 
 print("Mining block 3...") 
 block3 = Block("Transaction 3", "") 
 blockchain.add_block(block3) 
 print("Is blockchain valid? {}".format(blockchain.is_chain_valid()))