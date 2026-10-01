import hashlib 
 
 # Define the Merkle Tree 
merkle_tree = { 
   'root': 'e12f41f456d48c058ea1e1f2d8b4bb3c3b4f4d9b', 
   'levels':[ 
   ['2d0d2e33e58209a957e83c5e5e5d5a36a7c1b130', 
   'd64ee0abce60be7e75a97c1f56bbd57bc9ac2c0c', 
   '17600fcdefe24fcf129a7728ca84f0c70de7321a', 
   '7f8a3a75369f3b529d3fb3277a8f01b969b7d1d1'], 
   ['054a1ea24f240d7eafee90a01b7f75b77a21c7a6', 
   '6a644c6e5b631d2c6a5d6b55833c8e8285c13fa5'], 
   ['67b7e8a847f858cde48b659cea6991a2c6c17b3b'] 
   ] 
 } 
 
 # Define the element to be proved 
element = 'hello' 
 
 # Compute the hash of the element 
element_hash = hashlib.sha256(element.encode()).hexdigest() 
 
 # Define a function to generate the Merkle proof for a 
 given element 
 def generate_merkle_proof(element_hash, merkle_tree): 
  proof = [] 
  current_hash = element_hash 
 
 for level in merkle_tree['levels']: 
   if len(level) == 1: 
    break 
 
   if current_hash in level: 
    sibling_index = level.index(current_hash) - 1 
 
 if sibling_index < 0: 
   sibling_index = 1
   proof.append(sibling_hash) 

 current_hash = hashlib.sha256((current_hash + 
 sibling_hash). 
 encode()).hexdigest() 
return proof 

 # Generate the Merkle proof for the element 
proof = generate_merkle_proof(element_hash, merkle_tree) 
 
 # Verify the proof of membership 
current_hash = element_hash 
 
for sibling in proof: 
 current_hash = hashlib.sha256((current_hash + sibling). 
 encode()). 
 hexdigest() 
 
 if current_hash == merkle_tree[’root’]: 
 print(f"{element} is a member of the blockchain") 
 else: 
 print(f"{element} is not a member of the blockchain") 
 
 # Define an element that is not in the blockchain 
 non_member_element = ’world’ 
 
 # Compute the hash of the non-member element 
 non_member_element_hash = hashlib.sha256(non_member_element. 
 encode()). 
 hexdigest() 
 
 # Generate the Merkle proof for the non-member element 
 non_member_proof = generate_merkle_proof(non_member_element_hash, 
 merkle_tree) 
# Verify the proof of non-membership 
current_hash = non_member_element_hash 

 for sibling in non_member_proof: 
 current_hash = hashlib.sha256((current_hash + 
 sibling).encode()). 
 hexdigest() 
 
 if current_hash == merkle_tree['root']: 
   print(f"{non_member_element} is a member of the blockchain") 
 else: 
   print(f"{non_member_element} is not a member of the blockchain")