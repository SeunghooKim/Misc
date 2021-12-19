def encrypt(message, shift):
    output = ''

    for x in message:
        if x.isalpha():
            if x.isupper():
                output += chr((ord(x) + shift - 65) % 26 + 65)
            else:
                output += chr((ord(x) + shift - 97) % 26 + 97)
        else:
            output += x

    return output

def decrypt(messagelist):
    with open('dictionary.txt') as f:
        words = f.read().splitlines()

    encryptlist = list()

    for i in range(0, -26, -1):
        encryptlist.clear()
        for x in messagelist:
            if len(x) > 1:
                encryptlist.append(encrypt(x, i).lower())

        if all(word in words for word in encryptlist):
            return i

    raise ValueError("Cannot find the shift")

print('Input the message to encrypt and the desired shift.')
message = str(input('MESSAGE> '))
origshift = int(input('SHIFT> '))
shift = origshift % 26

print(f'\nYour encrypted message with shift {origshift}:\nOUTPUT {encrypt(message, shift)}\n')

print("Input the message to decrypt using brute force")
message = str(input('MESSAGE TO DECRIPT> '))
messagelist = message.split(' ')

decshift = decrypt(messagelist)
print(f'\nThe original message is:\nOUTPUT {encrypt(message, decshift)}')
print(f"The original message was encrypted with a shift of:\nOUTPUT {abs(decshift)}")