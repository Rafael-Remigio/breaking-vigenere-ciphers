import sys


# Alphabet used only contains CAPPS letters
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(ciphertext: str, key: str) -> str:
    plaintext = ''
    for i in range(len(ciphertext)):
        letter = ord(ciphertext[i]) - 65  # get character alphabet index

        shift_value = ord(key[i%len(key)]) - 65 # get shift value from key value and position

        # iterate throught the key in a Round Robin fashion 
        char = (letter - shift_value) % 26 # preform inverse shift

        plaintext += ALPHABET[char]

    return plaintext

if __name__ == "__main__":

    # get args from command line
    argv = sys.argv
    # if inputFile in not present
    if len(argv) != 3:
        print("Usage: python3 vigenere_decryption.py cipherTextFile key")
        sys.exit(2)

    # get string from inputFile
    input_file_string = argv[1]
    key = argv[2]

    cipherText = ""
    with open(input_file_string) as file:
        for line in file:
            cipherText += line.rstrip()

    decrypted = decrypt(cipherText,key)

    print(decrypted)