def custom_hash(data: bytes) -> str:
    """
    A simple custom hash function.
    """
    hash_value = 0
    for byte in data:
        hash_value = (hash_value * 31 + byte) % (2**32)
    return hex(hash_value)

# Example usage
if __name__ == "__main__":
    sample_data = b"Hello, world!"
    print(f"Custom Hash: {custom_hash(sample_data)}")


