import sys
import matplotlib.pyplot as plt

# Alphabet used only contains CAPPS letters
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Get index of coincidence value from a given text
def index_of_coincidence(text: str):
    counts = [0]*26
    for char in text:
        counts[ord(char) - 65] += 1
    number = 0
    total = 0
    for i in range(26):
        number += counts[i]*(counts[i]-1)
        total += counts[i]
    return 26*number / (total*(total-1))

# get IoC for different key lenghts of a certain ciphertext
# it will test key length up to the size of 20
def index_of_coincidence_for_key_lengths(ciphertext: str) -> dict:
    # dictionary will contain period, ioc pairs
    dictionary = {}

    period = 1
    # iterate througth all the periods starting at 1
    while period < 20:
        period += 1

        # Calculate the IoC from each separate slice in the period
        # if the period is 3 for example, calculate 3 word slices
        # for period = 3 the slices[0] will contain the letters 1,4,7,10,... 
        slices = ['']*period
        for i in range(len(ciphertext)):
            slices[i%period] += ciphertext[i]
        # sum all the IoC's generated
        sum = 0
        for i in range(period):
            sum += index_of_coincidence(slices[i])
        # get the average of the IoC's
        ioc = sum / period

        # add them to the dict
        dictionary[period] = ioc

    return dictionary



if __name__ == "__main__":

    # get args from command line
    argv = sys.argv
    # if inputFile in not present
    if len(argv) != 2:
        print("Usage: python3 key_length_calculation.py cipherText")
        sys.exit(2)

    # get string from inputFile
    input_file_string = argv[1]


    baseline_text = ""
    book = "booksInTXT/maias_cleaned.txt"
    with open(book) as file:
        for line in file:
            baseline_text += line.rstrip()
    base_line_IoC = index_of_coincidence(baseline_text)

    print("Baseline IOC from book");
    print("Portugues book: " + book + " IOC: " + str(base_line_IoC))


    baseline_text = ""
    book = "booksInTXT/moby_dick_cleaned.txt"
    with open(book) as file:
        for line in file:
            baseline_text += line.rstrip()
    base_line_IoC = index_of_coincidence(baseline_text)

    print("Baseline IOC from book");
    print("English book: " + book + " IOC: " + str(base_line_IoC))

    ciphertext = ""
    with open(input_file_string) as file:
        for line in file:
            ciphertext += line.rstrip()


    frequencies = index_of_coincidence_for_key_lengths(ciphertext)


    names = list(frequencies.keys())
    values = list(frequencies.values())

    plt.bar(range(len(frequencies)), values, tick_label=names)
    plt.show()

    print(frequencies)