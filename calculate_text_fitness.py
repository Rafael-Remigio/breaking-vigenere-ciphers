import sys
from math import log
from frequency_calculator import calculateFrequencies
from vigenere_decryption import decrypt

# Alphabet used only contains CAPPS letters
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Calculate fitness of a certain text with a certain length
# [baseline] is used for generating the baseline frequencies for each combination of letters
# [baseline] should be a big enough text so that it is representative of the language 
def fitness(base_line_text: str,text:str,length:int):
    
    result = 0
    
    baseline_frequencies = calculateFrequencies(base_line_text,length)

    for i in range(len(text)-(length-1)):
        # generate tetragram, trigram, (...), from current position
        xgram = text[i:i+length]

        # get frequencies of such xgram
        if xgram not in  baseline_frequencies:
            result += -15 # some large negative number
        else:
            y = baseline_frequencies.get(xgram)
            result += log(y) 

    result = result / (len(text) - (length-1))
    return result


if __name__ == "__main__":

    # get args from command line
    argv = sys.argv
    # if inputFile in not present
    if len(argv) != 5:
        print("Usage: python3 calculate_text_fitness.py baselineText cipherText key length")
        sys.exit(2)



    baseline_text = ""
    book = argv[1]
    with open(book) as file:
        for line in file:
            baseline_text += line.rstrip()

    # get length used for calculations
    length = int(argv[4])

    # Calculate baseline of what a normal text should look like with such lenght
    romeo_and_juliet = ""
    with open("booksInTXT/romeo_and_juliet_cleaned.txt") as file:
        for line in file:
            romeo_and_juliet += line.rstrip()


    base_line_fitness_value = fitness(baseline_text,romeo_and_juliet,length)
    print("Baseline Fitness value for Romeo and Juliet book")
    print("############################################")
    print("For length "+ str(length) + " the value is "+ str(base_line_fitness_value))

    print()
    print("############################################")


    # get string from inputFile
    input_file_string = argv[2]

    ciphertext = ""
    with open(input_file_string) as file:
        for line in file:
            ciphertext += line.rstrip()
    
    key = argv[3]


    plaintext = decrypt(ciphertext,key)

    fitness_value = fitness(baseline_text,plaintext,length)

    print("Result: " + str(fitness_value))

