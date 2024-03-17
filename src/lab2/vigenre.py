def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    num_ind = 0
    if len(keyword) < len(plaintext):
        keyword = keyword * (len(plaintext)//len(keyword)) + keyword[:len(plaintext)%len(keyword)]
    for i in range(len(plaintext)):
        if 97 <= ord(keyword[num_ind].lower()) <= 122:
            shift = ord(keyword[num_ind].lower()) - 97
        else:
            shift = 0
        num_ord = ord(plaintext[i])
        if plaintext[i].isalpha() and (65 <= num_ord <= 90 or 97 <= num_ord <= 122):
            # translate large letters into small ones
            if plaintext[i].isupper():
                plaintext[i].lower()
                num_ord += 32
            num_ord += shift
            # ord 'z' 122 - higher limit
            while num_ord > 122:
                num_ord = 96 + (num_ord - 122)
            num_ind += 1
        if plaintext[i].isupper():
            ciphertext += chr(num_ord).upper()
        else:
            ciphertext += chr(num_ord)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    num_ind = 0
    if len(keyword) < len(ciphertext):
        keyword = keyword * (len(ciphertext) // len(keyword)) + keyword[:len(ciphertext) % len(keyword)]
    for i in range(len(ciphertext)):
        if 97 <= ord(keyword[num_ind].lower()) <= 122:
            shift = ord(keyword[num_ind].lower()) - 97
        else:
            shift = 0
        num_ord = ord(ciphertext[i])
        if ciphertext[i].isalpha() and (65 <= num_ord <= 90 or 97 <= num_ord <= 122):
            # translate large letters into small ones
            if ciphertext[i].isupper():
                ciphertext[i].lower()
                num_ord += 32
            num_ord -= shift
            # ord 'a' 97 - lower limit
            while num_ord < 97:
                num_ord = 122 - (96 - num_ord)
            num_ind += 1
        if ciphertext[i].isupper():
            plaintext += chr(num_ord).upper()
        else:
            plaintext += chr(num_ord)
    return plaintext