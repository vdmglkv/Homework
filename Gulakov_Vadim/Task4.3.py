"""Task 4.3 Implement The Keyword encoding and decoding for latin alphabet. The Keyword Cipher uses a Keyword to
rearrange the letters in the alphabet. Add the provided keyword at the begining of the alphabet. A keyword is used as
the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet. Repeats of letters in
the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the
keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those
already used in the key.

Encryption: Keyword is "Crypto"

    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    C R Y P T O A B D E F G H I J K L M N Q S U V W X Z


"""

import string


class Crypto:

    def __init__(self, insert_in_alphabet):
        self.insert_in_alphabet = insert_in_alphabet.upper()
        self.alphabet = string.ascii_uppercase
        self.crypto_alphabet = self.insert_in_alphabet + ''.join([char for char in self.alphabet if char not in self.insert_in_alphabet])
        self.dict_ = dict(zip(self.alphabet, self.crypto_alphabet))

    def encode(self, string_to_enc):
        enc = ''
        symbols = (' ', '.', ',', '!')
        for char in string_to_enc.upper():
            if char in symbols:
                enc += char
            else:
                enc += self.dict_[char]
        return enc

    def decode(self, string_to_decode):
        dict_to_dec = dict(zip(self.crypto_alphabet, self.alphabet))
        dec = ''
        symbols = (' ', '.', ',', '!')
        for char in string_to_decode.upper():
            if char in symbols:
                dec += char
            else:
                dec += dict_to_dec[char]
        return dec


a = Crypto('crypto')
print(a.crypto_alphabet)
print(a.encode('Hello world'))
print(a.decode('BTGGJ VJMGP'))
