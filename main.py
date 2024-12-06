import hashlib

from blockchain import Blockchain
from utils import *

# Create a blockchain
blockchain = Blockchain()

# Generate keys for a user
public_key, private_key = gen_keys()

# Add a transaction
transaction = "Tigran sends 100 dollars to Anna"
print("The message is:" )
print(transaction)
p, g, y = public_key


print("Private key is:")
print(private_key)
print("Public key is:")
print(public_key)

hashed_message = hashlib.sha256(transaction.encode()).hexdigest()
print("The hash of a message is:")
print(hashed_message)
r, s = elgamal_sign(int(hashed_message, 16), p, g, private_key)
signed_transaction = {"transaction": transaction, "signature": (r, s)}
print("The signed hash message is:")
print(signed_transaction)
blockchain.add_new_transaction(signed_transaction)

# Mine a block
blockchain.mine()

# Verify the signature in the block
block = blockchain.chain[-1]
for tx in block.transactions:
    hashed_message = hashlib.sha256(tx["transaction"].encode()).hexdigest()
    M = int(hashed_message, 16)  # Convert hexadecimal hash to integer
    assert elgamal_verify(M, *tx["signature"], *public_key)
