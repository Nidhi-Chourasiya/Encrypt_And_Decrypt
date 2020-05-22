def encrypt(message,key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    for letter in message:
        if letter in alphabets: 
            letter_index = (alphabets.find(letter) + key) % len(alphabets)
            result = result + alphabets[letter_index] 
        else:
            result = result + letter
    return result


def decrypt(message,key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    for letter in message:
        if letter in alphabets: 
            letter_index = (alphabets.find(letter) - key) % len(alphabets)
            result = result + alphabets[letter_index] 
        else:
            result = result + letter
            
    return result


message = "hello world!"
encrypted = encrypt(message,3)
print(encrypted)

decrypted = decrypt(encrypted,3)
print(decrypted)
