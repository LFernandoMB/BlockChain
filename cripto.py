from hashlib import sha256


def criptografia(block: int = 0, information: str = '', last_hash: int = 0):
    return sha256((block + information + last_hash).encode('ascii')).hexdigest()
