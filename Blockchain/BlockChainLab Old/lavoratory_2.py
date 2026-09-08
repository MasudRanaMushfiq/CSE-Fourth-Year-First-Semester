import hashlib

def solve_puzzle(string, leading_zeros):
    nonce=0
    while True:
        nonce_str = str(nonce)
        data=string+nonce_str
        hash_value = hashlib.sha256(data.encode()).hexdigest()
        if hash_value.startswith("0"* leading_zeros):
            return nonce_str ,hash_value 
        nonce+=1

# get input from the user 
input_string = input("Enter the string:")
input_zeros = int(input("Enter the number of leading zeros:"))

#solve the puzzle 
nonce_value,hash_result= solve_puzzle(input_string,input_zeros)

#print the result
print("Input String:",input_string)
print("Nonce value for which the puzzle is solved:",nonce_value)
print("Generated hash:",hash_result)
      