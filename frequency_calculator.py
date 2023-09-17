import sys


# Calculate frequencies of letters or combination of letters in a given text
def calculateFrequencies(text: str, number_of_letters: int) -> dict:

    # Create empty dictionary/hashmap
    frequencies_dictionary = {}

    # iterate throught the all the text
    for i in range(len(text) - (number_of_letters-1)):
        combination = "" 
        # iterate throught the combination 
        for j in range(number_of_letters):
            letterIndex = i + j # get index of letter from the starting letter of the combination
            combination += text[letterIndex]

        if combination in frequencies_dictionary: 
            # if the combination already exists in the map increase its value 
            frequencies_dictionary[combination] = frequencies_dictionary.get(combination) + 1
        else:
            # if it is the first occurence add it to the map as 1
            frequencies_dictionary[combination] = 1

    # make it a value from 0 to 1
    for key in frequencies_dictionary.keys():
        frequencies_dictionary[key] = frequencies_dictionary.get(key) / (len(text) - (number_of_letters - 1))

    return frequencies_dictionary

if __name__ == "__main__":

    # get args from command line
    argv = sys.argv
    # if inputFile in not present
    if len(argv) != 3:
        print("Usage: python3 frequency_calculator.py cleanFileInput numberOfLetters")
        sys.exit(2)

    # get string from inputFile
    input_file_string = argv[1]
    numberOfLetters = int(argv[2])

    text = ""
    with open(input_file_string) as file:
        for line in file:
            text += line.rstrip()
    frequencies = calculateFrequencies(text,numberOfLetters)
    print(frequencies)