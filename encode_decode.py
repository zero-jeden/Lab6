
def encode(password):
    storage_array =[]
    string =''
    for i in range(0, len(password)):
        storage_array.append(3 + int(password[i]))

    for k in range(0, len(storage_array)):
        if storage_array[k] >= 10:
            string += str(storage_array[k] - 10)
        else:
            string += str(storage_array[k])


    return string
# Elijah De Guzman decode function
def decode(data):
    out = ""
    for char in data:
        if (int(char) < 3):
            out += str((10 + int(char)) - 3)
        else:
            out += str(int(char) - 3)
    return out

if __name__ == '__main__':

    while True:

        print('Menu')
        print('------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')



        selection = int(input('Please enter an option: '))
        if selection == 1:
            password = input('Please enter your password to encode: ')
            encrypted = encode(password)
            print('Your password has been encoded and stored!')

        if selection == 2:
            decrypted = decode(encrypted)
            print(f'The encoded  password is {decrypted}, and the original password is {encrypted}.')

        if selection == 3:
            break




'''
Test cases:
password = '00009962'
password1 = '12345555'
print(encode(password))
print(encode(password1))'''
