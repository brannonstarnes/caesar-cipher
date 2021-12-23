from inspect import EndOfBlock
import re 

# code 65-90 A-Z, 97-122 a-z
#chr(65-90) chr(97-122)
# ord(A-Z) ord(a-z)
def encrypt(plain_text, shift):
    encrypted_text = ""
    for letter in plain_text:
        letter_code = ord(letter)
        new_code = letter_code + shift
        
        if letter_code < 90 and new_code > 90:
            new_code = (new_code - 90) + 64
            encrypted_letter = chr(new_code)
            encrypted_text += encrypted_letter
        elif letter_code >= 65 and letter_code <= 90:
            new_code = letter_code + shift
            encrypted_letter = chr(new_code)
            encrypted_text += encrypted_letter
        
        elif letter_code < 122 and new_code > 122:
            new_code = (new_code - 122) + 96
            encrypted_letter = chr(new_code)
            print("endcoded letter: ", encrypted_letter)
            encrypted_text += encrypted_letter     
        elif letter_code >= 97 and letter_code <= 122:
            new_code = letter_code + shift
            encrypted_letter = chr(new_code)
            print("endcoded letter: ", encrypted_letter)
            encrypted_text += encrypted_letter
        
        else:
            encrypted_letter = letter
            encrypted_text += encrypted_letter
    return encrypted_text



def decrypt():
    pass






def count_words(text):
    num_words = 0
    word_pool = text.split()

    for word in word_pool:
        word = re.sub(r"[^A-Za-z]+", "", word)
        if word.lower() in words or word in names:
            num_words += 1
        else:
            pass

    return num_words

##************************CRACKING*******************************
def crack():
    pass