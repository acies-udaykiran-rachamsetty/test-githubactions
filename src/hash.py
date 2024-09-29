import hashlib

def commutative_hash(int_list):
    # Choose a large prime number
    prime = 31
    
    # Initialize accumulators for different operations
    sum_acc = 0
    xor_acc = 0
    mul_acc = 1
    
    # Loop through the list of integers
    for num in int_list:
        sum_acc += num             # Addition is commutative
        xor_acc ^= num             # XOR is commutative
        mul_acc *= num + prime     # Ensure non-zero multiplication, and commutativity
    
    # Combine the accumulators into a single string representation
    combined_string = f"{sum_acc}-{xor_acc}-{mul_acc}"
    
    # Hash the combined string using a standard hash function (SHA-256 here)
    hash_object = hashlib.sha256(combined_string.encode())
    
    # Return the hexadecimal digest of the hash
    return hash_object.hexdigest()

# Example usage with the same numbers in different orders
input_list_1 = [92233720368547758079223372036854775807, 9223372036854775807 + 9223372036854775807, 9223372036854775807 + 2]
input_list_2 = [9223372036854775807 + 2, 92233720368547758079223372036854775807, 9223372036854775807 + 9223372036854775807]

# Print the hash of both lists
hash_1 = commutative_hash(input_list_1)
hash_2 = commutative_hash(input_list_2)

print("Hash 1:", hash_1)
print("Hash 2:", hash_2)

# Compare the two hashes
print("Are the hashes equal?", hash_1 == hash_2)
