import itertools
import sys
import matplotlib.pyplot as plt
from calculate_text_fitness import fitness, fitness_with_frequencies
from frequency_calculator import calculateFrequencies
from key_length_calculation import index_of_coincidence_for_key_lengths
from vigenere_decryption import decrypt

# Alphabet used only contains CAPPS letters
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def plotIoC(frequencies):
    names = list(frequencies.keys())
    values = list(frequencies.values())

    plt.bar(range(len(frequencies)), values, tick_label=names)
    plt.show()


def brute_force(ciphertext,password_length,fitness_length,baseline_fitness,baseline_text):
    attempts = 0
    dictionary = {}

    baseline_frequencies = calculateFrequencies(baseline_text,fitness_length)


    print("Number of keys to bruteforce:", 26**password_length)
    

    for key in itertools.product(ALPHABET, repeat=password_length):
        attempts +=1
        if (attempts%100000 == 0):
            print("Number of attempts", attempts/( 26**password_length))
        key = ''.join(key)
        plain_text_guess = decrypt(ciphertext,key)

        plain_text_fitness = fitness_with_frequencies(plain_text_guess,fitness_length,baseline_frequencies=baseline_frequencies)

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
    romeo_and_juliet = ""
    with open("booksInTXT/romeo_and_juliet_cleaned.txt") as file:
        for line in file:
            romeo_and_juliet += line.rstrip()

    


    base_line_fitness_value = fitness(baseline_text,romeo_and_juliet,fitness_length)
    print("Baseline Fitness value for Romeo and Juliet book")
    print("For length "+ str(fitness_length) + " the value is "+ str(base_line_fitness_value))
    print("############################################")

    for password_length in lengths_to_brute_force:

        print(brute_force(ciphertext,password_length,fitness_length,base_line_fitness_value,baseline_text))