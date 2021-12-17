alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encode(txt, k):
    shifted_list = ""
    for i in txt:
        if i in alphabet:
            position = alphabet.index(i)
            shifted_list += alphabet[position + k]
    print("Encoded Message is", shifted_list)


def decode(txt, k):
    shifted_list = ""
    for i in txt:
        if i in alphabet:
            position = alphabet.index(i)
            shifted_list += alphabet[position - k]
    print("Decoded Message is", shifted_list)


condition_check = True

while condition_check:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        print("Mission is success")
        text = input("Type your message to encode:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encode(text, shift)
    if direction == "decode":
        print("Mission is success")
        text = input("Type your message to decode:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decode(text, shift)
