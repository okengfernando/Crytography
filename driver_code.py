import CipherText as ciph

def main():
    message = str(input('Enter your message to Encrypt or Decrypt: '))
    key = int(input('Enter you key [1 - 26]: '))
    choice = input('Encrypt or Decrypt? Type -> [E or D]: ')

    if choice.lower().startswith('e'):
        print(ciph.encrypt(message, key))
    else:
        print(ciph.decrypt(message, key))

if __name__ == '__main__':
    main()
