# breaking-vigenere-ciphers
An example of classical cryptography and how to break polyalphabetic ciphers such as Vigenère's cipher


## What is the vigenère cipher

Wikipedia defines it has: ***a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key.***

### But what is a Caesar cipher:
A monoalphabetic shift cipher. One of the simplest modes of encrytpion. It's an encryption where we swap each letter in a text of a given alphabet in to another. This swap is given by an integer of the displacment of shifth that needs to be done.

For example if we have the alphabet:
* ABCDEFGHIJKLMNOPQRSTUVWXYZ

A shift with a key 3 (can also be represented as 3) will give us the corresponding alphabet 

* XYZABCDEFGHIJKLMNOPQRSTUVW

In this case any text encrypted with 3 the letter A will correspond to X, B will correspond to Y, ... ( and so on )

|With a key of 3||
|--|--|
|PlainText|THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG|
|CipherText|QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD|

This cipher is a **monoalphabetic substitution**.

To decrypt we perform the operation in the oposite way

### Vigenère cipher

The vigenère cipher is base on the Caesar cipher but instead of being a monoalphabetic substitution, it's a **polyalphabetic substitution**. The key to decrypting and encryption is not one single number of letter evaluating a shift, but combination of numbers representing shifts.

For example:

* Given a text such as ***thequickbrownfoxjumpsoverthelazydog*** and a key like ***lmao*** we can encrypt this as such

    Shifts are preform with the key in a round robin way because the key is shorter than the plaintext

    | T | H | E | Q | U | (...) |
    |---|---|---|---|---|---|
    |shift with L|shift with M|shift with A| shift with O| shift with L|(...)|
    |E|T|E|E|F|(...)|

* The result will be ***eteefucymdokyrolugmddavscfhswmzmoag***

## Before encryption

Before encrypting a plain text with a key its important to clean and standardize them to use the same alphabet.
Example: 

```
Yes, I'm officially on vacation. I will be on vacation for five glorious days because I am clever. I am smart and have actually managed to schedule several of these 4-5 day vacations through the rest of the year.

I have two days off during the week because working the weekends if fucking ridiculously easy and I can't believe more people don't want to do it. But that's okay, we won't say shit to them about how wonderful it is. We'll continue to tell them how horrid it is, "Oh yah, working the weekend while everyone else is off and out and about doing their thing...man it totally sucks!"
```

Should be cleaned to be represented like this: 

```
YESIMOFFICIALLYONVACATIONIWILLBEONVACATIONFORFIVEGLORIOUSDAYSBECAUSEIAMCLEVERIAMSMARTANDHAVEACTUALLYMANAGEDTOSCHEDULESEVERALOFTHESEDAYVACATIONSTHROUGHTHERESTOFTHEYEARIHAVETWODAYSOFFDURINGTHEWEEKBECAUSEWORKINGTHEWEEKENDSIFFUCKINGRIDICULOUSLYEASYANDICANTBELIEVEMOREPEOPLEDONTWANTTODOITBUTTHATSOKAYWEWONTSAYSHITTOTHEMABOUTHOWWONDERFULITISWELLCONTINUETOTELLTHEMHOWHORRIDITISOHYAHWORKINGTHEWEEKENDWHILEEVERYONEELSEISOFFANDOUTANDABOUTDOINGTHEIRTHINGMANITTOTALLYSUCKS
```

There is a python script available that will do just this.

Usage:
```
$ python3 plain_text_cleaner.py dirtyExample.txt 

YESIMOFFI(...)TTOTALLYSUCKS
```

## Encryption 
Function example
```
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
```
Usage:
```
$ python3 vigenere_encryption.py cleanPlainText/wikipediaExample.txt LMAO 

ETEEFUCYMDOKYROLUGMDDAVSCFHSWMZMOAG
```

## Decryption 
Function
```
# Alphabet used only contains CAPPS letters
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(ciphertext: str, key: str) -> str:
    plaintext = ''
    for i in range(len(ciphertext)):
        letter = ALPHABET.index(ciphertext[i])  # get character alphabet index

        shift_value = ALPHABET.index(key[i%len(key)]) # get shift value from key value and position

        # iterate throught the key in a Round Robin fashion 
        char = (letter - shift_value) % 26 # preform inverse shift

        plaintext += ALPHABET[char]

    return plaintext
```

Usage:
```
$ python3 vigenere_decryption.py ciphertext LMAO

THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG
```
