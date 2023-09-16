
import sys, argparse



def load_words(dictionary: str):
    with open(dictionary) as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':

    english_words = load_words("dictionaries/words_alpha.txt")
    # demo print
    print('fate' in english_words)



    

