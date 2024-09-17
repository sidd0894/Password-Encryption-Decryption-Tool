from cryptography.fernet import Fernet
import sys


def encrypt(password: str, filename: str):
    key = Fernet.generate_key()
    print(f'\n-Secret Key: {key.decode()}')

    # Create a new instance of Fernet class
    cipher_suite = Fernet(key)

    encrypted_pass = cipher_suite.encrypt(password.encode())
    print(f'-Encrypted Password: {encrypted_pass.decode()}')

    # Save encrypted password and its key
    try:
        with open(filename, 'a') as file:
            file.write(f'Encrypted Password: {encrypted_pass.decode()}\n')
            file.write(f'Key: {key.decode()}\n\n')
    except Exception as e:
        print(f'[ERROR] Error occured while saving encrypted password: {e}')



def decrypt(encrypted_pass: str, key: str):
    try:
        cipher_suite = Fernet(key.encode())

        decrypted_password = cipher_suite.decrypt(encrypted_pass.encode())
        print(f'\nOriginal password: {decrypted_password.decode()}')
    except Exception as e:
        print(f'[ERROR] Decryption failed: {e}')



def main():
    try:
        transform_type = input('1. Encrypt\n'+
                               '2. Decrypt\n'+
                               'Choose option (1/2): ').strip().lower()


        if transform_type in ['1', 'e', 'encrypt']:
            while True:
                password = input('Enter password to encrypt: ').strip()
                if password == '':
                    print('[ERROR] Password can\'t be empty')
                else:
                    break

            # Validate file name
            while True:
                filename = input('Enter filename to save encrypted text (e.g., passwords.txt): ').strip()
                if filename == '':
                    filename = 'passwords.txt'
                    break
                elif not (filename.endswith('.txt') and len(filename) > 4 and filename[-4] == '.'):
                    print('[ERROR] Filename should be in format \'filename.txt\'')
                else:
                    break
            

            encrypt(password, filename)
                

        elif transform_type in ['2', 'd', 'decrypt']:
            encrypted_pass = input('\nEnter encrypted password: ').strip()

            if encrypted_pass == '':
                print('[ERROR] Decryption text cannot be empty')
                sys.exit()

            key = input('Enter secret key: ').strip()
            if key == '':
                print('[ERROR] Secret key connot be empty')
                sys.exit()

            decrypt(encrypted_pass, key)


        else:
            print('[ERROR] Invalid option')
            
    except KeyboardInterrupt:
        print('\nKeyboard Interuption')
        print('Exiting...')
        sys.exit()

if __name__ == '__main__':
    main()