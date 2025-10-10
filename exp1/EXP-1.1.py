# Function to generate the repeating key
def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

# Function to encrypt the text
def vigenere_encrypt(text, key):
    cipher_text = []
    key = generate_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():
            shift = (ord(text[i].upper()) - ord('A') + ord(key[i].upper()) - ord('A')) % 26
            cipher_char = chr(shift + ord('A'))
            cipher_text.append(cipher_char)
        else:
            cipher_text.append(text[i])
    return "".join(cipher_text)

# Function to decrypt the text
def vigenere_decrypt(cipher_text, key):
    orig_text = []
    key = generate_key(cipher_text, key)
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = (ord(cipher_text[i].upper()) - ord(key[i].upper()) + 26) % 26
            orig_char = chr(shift + ord('A'))
            orig_text.append(orig_char)
        else:
            orig_text.append(cipher_text[i])
    return "".join(orig_text)

# Example usage
if __name__ == "__main__":
    text = "HELLOWORLD"
    key = "KEY"

    encrypted = vigenere_encrypt(text, key)
    print("Encrypted:", encrypted)

    decrypted = vigenere_decrypt(encrypted, key)
    print("Decrypted:", decrypted)
