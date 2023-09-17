
# Alphabet used only contains CAPPS letters
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Get index of coincidence value from a given text
def index_of_coincidence(text: str):
    counts = [0]*26
    for char in text:
        counts[ALPHABET.index(char)] += 1
    number = 0
    total = 0
    for i in range(26):
        number += counts[i]*(counts[i]-1)
        total += counts[i]
    return 26*number / (total*(total-1))


def index_of_coincidence_for_key_lengths(ciphertext: str) -> dict:
    # dictionary will contain period, ioc pairs
    dictionary = {}

    period = 0
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