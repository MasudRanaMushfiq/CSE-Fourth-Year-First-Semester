import struct
import binascii

def text_to_binary(text):
    """Convert input text to binary based on ASCII."""
    return ''.join(f'{ord(c):08b}' for c in text)

def pad_binary_message(binary_message):
    """Add padding to binary message according to the MD5 algorithm."""
    original_length = len(binary_message)  # Original length in bits
    
    # Append a single '1' bit
    binary_message += '1'
    
    # Add '0' bits until length is congruent to 448 mod 512
    while len(binary_message) % 512 != 448:
        binary_message += '0'
    
    # Append the original length as a 64-bit binary number
    binary_message += f'{original_length:064b}'
    return binary_message

def split_into_blocks(binary_message):
    """Split binary message into 512-bit blocks."""
    return [binary_message[i:i+512] for i in range(0, len(binary_message), 512)]

def split_block_into_words(block):
    """Split a 512-bit block into 16 32-bit words."""
    return [block[i:i+32] for i in range(0, len(block), 32)]

def md5_preprocessing(input_text):
    """MD5 preprocessing steps."""
    print(f"Input text: {input_text}")
    
    # Convert to binary
    binary_message = text_to_binary(input_text)
    print(f"Binary representation: {binary_message}")
    
    # Pad the message
    padded_message = pad_binary_message(binary_message)
    print(f"Padded binary message (length {len(padded_message)}): {padded_message}")
    
    # Split into 512-bit blocks
    blocks = split_into_blocks(padded_message)
    print(f"Number of 512-bit blocks: {len(blocks)}")
    
    # Split the first block into 16 32-bit words
    words = split_block_into_words(blocks[0])
    print("Words in the first block:")
    for i, word in enumerate(words):
        print(f"M{i}: {word} (hex: {hex(int(word, 2))[2:]})")
    
    return blocks

# Example usage
input_text = "They are deterministic"
md5_preprocessing(input_text)
