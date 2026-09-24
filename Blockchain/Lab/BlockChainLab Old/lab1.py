import struct

def to_bits(message):
    return ''.join(f'{ord(c):08b}' for c in message)

def pad_binary_message(binary_message):
    """Add padding to binary message according to the MD5 algorithm."""
    original_length = len(binary_message)  # Original length in bits

def pad_message(message):
    message_bits = to_bits(message)
    original_length = len(message_bits)
    message_bits += '1'
    while len(message_bits) % 512 != 448:
        message_bits += '0'
    length_bits = f'{original_length:064b}'
    message_bits += length_bits
    return message_bits, original_length

def split_into_32bit_segments(padded_message):
    segments = [padded_message[i:i+32] for i in range(0, len(padded_message), 32)]
    return segments

def print_segments(segments):
    for i, segment in enumerate(segments):
        print(f'M{i + 1}: {segment}')

message = "They "
padded_message, original_length = pad_message(message)

print(f"Original message: {message}")
print(f"Original message length (in bits): {original_length}")
print(f"512-bit padded message:\n{padded_message}\n")

segments = split_into_32bit_segments(padded_message)
print("\nMessage in 512-bit block, split into 16 segments (16-bit each):")
print_segments(segments)
