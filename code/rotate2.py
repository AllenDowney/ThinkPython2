"""
Alex Fegatilli
The same rotate.py but without rotate_letter function and with a personal request
"""
def cesare(word, number):
    n = 0
    start = 0
    ciphertext = ""
    while n < len(word):
        if word[n].isupper():
            start = 65 # ord('A')
            letter = ord(word[n]) - start
            c = ((letter+number) % 26) + start
            ciphertext += chr(c)
        
        elif word[n].islower():
            start = 97 # ord('a')
            letter = ord(word[n]) - start
            c = ((letter+number) % 26) + start
            ciphertext += chr(c)
            
        n+=1
    return ciphertext

def request():
    word = input("Write the plaintext: ")
    number = int(input("N. of shifts: "))
    print("\nPlaintext: ",word)
    print("Ciphertext: ",cesare(word,number))

request()
