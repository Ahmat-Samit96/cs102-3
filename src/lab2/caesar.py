def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        num_ord = ord(char)
        if char.isalpha() and (65 <= num_ord <= 90 or 97 <= num_ord <= 122):
            # translate large letters into small ones
            if char.isupper():
                char.lower()
                num_ord += 32
            num_ord += shift
            # ord 'z' 122 - higher limit
            while num_ord > 122:
                num_ord = 96 + (num_ord - 122)
        if char.isupper():
            ciphertext += chr(num_ord).upper()
        else:
            ciphertext += chr(num_ord)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        num_ord = ord(char)
        if char.isalpha() and (65 <= num_ord <= 90 or 97 <= num_ord <= 122):
            # translate large letters into small ones
            if char.isupper():
                char.lower()
                num_ord += 32
            num_ord -= shift
            # ord 'a' 97 - lower limit
            while num_ord < 97:
                num_ord = 122 - (96 - num_ord)
        if char.isupper():
            plaintext += chr(num_ord).upper()
        else:
            plaintext += chr(num_ord)

    return plaintext