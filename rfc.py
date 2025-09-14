def KSA(key):
    """Key Scheduling Algorithm (KSA)"""
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # swap
    return S

def PRGA(S):
    """Pseudo-Random Generation Algorithm (PRGA)"""
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key, data):
    """Encrypt or Decrypt data with RC4"""
    key = [ord(c) for c in key]
    S = KSA(key)
    keystream = PRGA(S)
    res = []
    for c in data:
        val = c ^ next(keystream)  # XOR with keystream
        res.append(val)
    return bytes(res)


# Main program
if __name__ == "__main__":
    fixed_key = "lasya"   # 🔹 Fixed key stored in the program

    entered_key = input("Enter key to continue: ")

    if entered_key != fixed_key:
        print("❌ Wrong key! Access denied.")
    else:
        print("✅ Key accepted.")
        plaintext = input("Enter plaintext: ")

        # Encryption
        ciphertext = RC4(fixed_key, plaintext.encode())
        print("Ciphertext (hex):", ciphertext.hex())

        # Decryption
        decrypted = RC4(fixed_key, ciphertext)
        print("Decrypted text:", decrypted.decode())
