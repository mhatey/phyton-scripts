import hashlib
import time

# Parameters for the genesis block
pszTimestamp = "The Times 27/Sept/2024 Brink of a reset"
nonce = 0
nTime = int(time.time())  # Current Unix timestamp
nBits = 0x1d00ffff  # Difficulty target
version = 1  # Block version

# Generate a Merkle Root for the Genesis Block
# For simplicity, using an empty transaction Merkle Root
merkle_root = hashlib.sha256("".encode('utf-8')).hexdigest()

# Helper function to hash data using SHA-256
def sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Create the block header data string
def create_genesis_block_header(pszTimestamp, nTime, nBits, nonce, version, merkle_root):
    data = f"{pszTimestamp}{nTime}{nBits}{nonce}{version}{merkle_root}"
    return sha256(data)

# Find the genesis block hash with a valid proof of work
def find_genesis_block():
    global nonce
    while True:
        hash_result = create_genesis_block_header(pszTimestamp, nTime, nBits, nonce, version, merkle_root)
        # Check if hash meets difficulty requirement (simplified for demonstration)
        if hash_result.startswith('00'):
            print(f"Genesis Block Found!")
            print(f"Hash: {hash_result}")
            print(f"Nonce: {nonce}")
            print(f"Merkle Root: {merkle_root}")
            print(f"Timestamp: {pszTimestamp}")
            print(f"Time: {nTime}")
            break
        nonce += 1

if __name__ == "__main__":
    print("Generating genesis block...")
    find_genesis_block()
    print(f"Genesis block generation completed with nonce: {nonce}")
