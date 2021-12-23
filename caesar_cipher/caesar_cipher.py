from caesar_cipher.corpus_loader import real_names, real_words
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
            encrypted_text += encrypted_letter     
        elif letter_code >= 97 and letter_code <= 122:
            new_code = letter_code + shift
            encrypted_letter = chr(new_code)
            encrypted_text += encrypted_letter
        
        else:
            encrypted_letter = letter
            encrypted_text += encrypted_letter
    return encrypted_text



def decrypt(encrpyted_text, shift):
    return encrypt(encrpyted_text, -shift)


def crack(encrypted_text):
    #check decrypt with each shift, compare results against words list
    shift = 1
    pool = []
    while shift < 26:
        result = decrypt(encrypted_text, -shift)
        pool.append(result)
        shift += 1
    for phrase in pool:
        num_words = count_words(phrase)
        accuracy = int(num_words / len(phrase.split()) * 100)
        if accuracy > 65:
            return phrase
    if accuracy < 65:
        return ""
        






def count_words(text):
    num_words = 0
    word_pool = text.split()

    for word in word_pool:
        word = re.sub(r"[^A-Za-z]+", "", word)
        if word.lower() in real_words or word in real_names:
            num_words += 1
        else:
            pass

    return num_words

##************************CRACKING*******************************