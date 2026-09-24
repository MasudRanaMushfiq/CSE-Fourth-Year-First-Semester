
import hashlib 
class UTXO: 
   def __init__(self, txid, index, value): 
     self.txid = txid 
     self.index = index 
     self.value = value 
   def __str__(self): 
    return f"UTXO ({self.txid}:{self.index}) with value {self.value}" 
class Transaction: 
  def __init__(self, inputs, outputs): 
    self.inputs = inputs 
    self.outputs = outputs
  def __str__(self): 
    return f"Transaction with {len(self.inputs)} inputs and {len(self.outputs)} outputs" 
  def hash(self): 
    
     tx_input = ''.join([str(inp.txid) + str(inp.index) 
     for inp in self.inputs]) 
     tx_output = ''.join([str(out.value) for out in 
     self.outputs]) 
     tx_data = tx_input + tx_output 
     return hashlib.sha256(tx_data.encode('utf-8')).hexdigest() 
 
 
utxo1 = UTXO('txid1', 0, 10) 
utxo2 = UTXO('txid2', 1, 20) 
input1 = [utxo1] 
output1 = [UTXO('txid3', 0, 25), UTXO('txid3', 1, 5)] 
tx1 = Transaction(input1, output1) 
input2 = [utxo2] 
output2 = [UTXO('txid4', 0, 15), UTXO('txid4', 1, 5)] 
tx2 = Transaction(input2, output2)  
print(utxo1) 
print(utxo2) 
print(tx1) 
print(tx2) 
print(tx1.hash()) 
print(tx2.hash()) 