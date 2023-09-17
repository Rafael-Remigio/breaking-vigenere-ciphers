import sys

# Alphabet used only contains CAPPS letters
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(plaintext: str, key: str) -> str:
    ciphertext = ''
    for i in range(len(plaintext)):
        letter = ALPHABET.index(plaintext[i])  # get character alphabet index

        # iterate throught the key in a Round Robin fashion 
        shift_size = ALPHABET.index(key[i % len(key)]) # get shift value from key value and position

        new_letter = (letter + shift_size) % 26 # preform shift

        ciphertext += ALPHABET[new_letter]

    return ciphertext


if __name__ == "__main__":

    # get args from command line
    argv = sys.argv
    # if inputFile in not present
    if len(argv) != 3:
        print("Usage: python3 vigenere_encryption.py plainTextFile key")
        sys.exit(2)

    # get string from inputFile
    input_file_string = argv[1]
    key = argv[2]

    plaintext = ""
    with open(input_file_string) as file:
        for line in file:
            plaintext += line.rstrip()


    encrypted = encrypt(plaintext,key)

    print(encrypted)