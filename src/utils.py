# src/utils.py

def bytes_to_hex(data: bytes) -> str:
    """
    Converts bytes to a hexadecimal string.
    """
    return data.hex()

def hex_to_bytes(hex_str: str) -> bytes:
    """
    Converts a hexadecimal string to bytes.
    """
    return bytes.fromhex(hex_str)
