alphabets = 'abcdefghijklmnopqrstuvwxyz'
def encrypt(message, key):
    encrypted = ''
    for letter in message:
        if letter in alphabets:
            num = alphabets.find(letter)
            num += key
            encrypted += alphabets[num % 26]
        else:
            encrypted += letter
    return encrypted
def decrypt(message, key):
    decrypted = ''
    for letter in message:
        if letter in alphabets:
            num = alphabets.find(letter)
            num -= key
            decrypted += alphabets[num % 26]
        else:
            decrypted += letter
    return decrypted
def main():
    message = input('Enter your message: ')
    key = int(input('Enter the key number (1-26): '))
    print('Your original message is: ', message)
    print('Your encrypted message is: ', encrypt(message, key))
    print('Your decrypted message is: ', decrypt(encrypt(message, key), key))
if __name__ == '__main__':
    main()
