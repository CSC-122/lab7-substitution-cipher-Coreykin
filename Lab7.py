# CSC 122
# Substitution Cipher
# By <Your Name>

"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""
def main():
    # Encrypt the message
    message = input("Enter the message to be encrypted: ")
    encrypted_message = ""
    for char in message:
        encrypted_message += chr(ord(char) + 3)
    print(f"Encrypted message = {encrypted_message}\n")

    # Decrypt the message
    cipher = input("Enter the cipher to be decrypted: ")
    decrypted_message = ""
    for char in cipher:
        decrypted_message += chr(ord(char) - 3)
    print(f"Decrypted message = {decrypted_message}\n")

if __name__ == "__main__":
    main()
