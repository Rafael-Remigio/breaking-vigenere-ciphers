import itertools
import sys
import matplotlib.pyplot as plt
from frequency_calculator import calculateFrequencies
from key_length_calculation import index_of_coincidence_for_key_lengths
from vigenere_decryption import decrypt
from math import log
from calculate_text_fitness import fitness


# Alphabet used only contains CAPPS letters
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

BASELINE_FREQUENCIES = {}

CIPHERTEXT = ""

FTINESS_LENGTH = 0

BASELINE_FITNESS = 0

ATTEMPTS = 0;

def plotIoC(frequencies):
    names = list(frequencies.keys())
    values = list(frequencies.values())

    plt.bar(range(len(frequencies)), values, tick_label=names)
    plt.show()


def brute_force(ciphertext,password_length,fitness_length,baseline_fitness,baseline_text):

    global BASELINE_FREQUENCIES, CIPHERTEXT,FTINESS_LENGTH ,BASELINE_FITNESS,ATTEMPTS
    
    BASELINE_FREQUENCIES = calculateFrequencies(baseline_text,fitness_length)
    CIPHERTEXT = ciphertext
    FTINESS_LENGTH = fitness_length
    BASELINE_FITNESS = baseline_fitness
    ATTEMPTS = 0

    print("Number of keys to bruteforce:", 26**password_length)
    
    iterable = itertools.product(ALPHABET, repeat=password_length)

    for i in iterable:

        function(key=i)
        
    return



def fitness_with_frequencies(text:str,length:int):
    
    result = 0
    
    for i in range(len(text)-(length-1)):
        # generate tetragram, trigram, (...), from current position
        xgram = text[i:i+length]

        # get frequencies of such xgram
        if xgram not in  BASELINE_FREQUENCIES:
            result += -15 # some large negative number
        else:
            y = BASELINE_FREQUENCIES.get(xgram)
            result += log(y) 

    result = result / (len(text) - (length-1))
    return result


def function(key):
    key = ''.join(key)
    plain_text_guess = decrypt(CIPHERTEXT,key)

    plain_text_fitness = fitness_with_frequencies(plain_text_guess,FTINESS_LENGTH)

    if BASELINE_FITNESS +1 > plain_text_fitness > BASELINE_FITNESS -1:
        print(key,plain_text_fitness)
        

    return


if __name__ == "__main__":

    # get args from command line
    argv = sys.argv
    # if inputFile in not present
    if len(argv) != 2:
        print("Usage: python3 vigenere_solver.py cipherTextFile")
        sys.exit(2)

    # get cipher from inputFile
    cipherText_file = argv[1]
    ciphertext = ""
    with open(cipherText_file) as file:
        for line in file:
            ciphertext += line.rstrip()


    print("############################################")
    print("Ciphertext basic info:")
    print("Ciphertext > " + ciphertext)
    print("Cipher Lenght > " + str(len(ciphertext)))

    print("############################################")
    print("Calculating Indexes of coincidence")
    print("Lengths from 2 to 20")


    frequencies = index_of_coincidence_for_key_lengths(ciphertext)

    print("To continue close the plot")

    plotIoC(frequencies)

    print("\n\nSelect key lengths/periods to continue the attack with:")

    print("Input should be integers and written as length1,length2:")
    lengths = input()  

    lengths_to_brute_force = [int(i) for i in lengths.split(",")]

    print("############################################")
    print("Insert a language baseline, this must be a large text for the language we are trying to decrypt to:")
    print("Example the book Moby Dick")
    baseLineInpput = input("File name: ")

    baseline_text = ""
    with open(baseLineInpput) as file:
        for line in file:
            baseline_text += line.rstrip()


    print("############################################")
    print("Insert length to calculate fitness with")
    print("(Recommended is 2 or 4)")
    fitness_length = int(input())
 
    print()
    print("############################################")


    # Calculate baseline of what a normal text should look like with such lenght
    base_line_book = ""
    print("(Language, Portuguese 1, English 2)")
    language = int(input())

    baselinebook = ""
    if language == 1:
        baselinebook = "booksInTXT/collection_portuguese_cleaned.txt"
    else: 
        baselinebook = "booksInTXT/romeo_and_juliet_cleaned.txt"
    with open(baselinebook) as file:
        for line in file:
            base_line_book += line.rstrip()

    


    base_line_fitness_value = fitness(baseline_text,base_line_book,fitness_length)
    print("Baseline Fitness value for "+ baselinebook)
    print("For length "+ str(fitness_length) + " the value is "+ str(base_line_fitness_value))
    print("############################################")

    for password_length in lengths_to_brute_force:

        print(brute_force(ciphertext,password_length,fitness_length,base_line_fitness_value,baseline_text))