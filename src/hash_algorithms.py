import hashlib

def sha256_hash(data: bytes) -> str:
    """
    Returns the SHA-256 hash of the given data.
    """
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

# Example usage
if __name__ == "__main__":
    sample_data = b"Hello, world!"
    print(f"SHA-256 Hash: {sha256_hash(sample_data)}")
