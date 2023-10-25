
def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    option = input('Please enter an option: ')
    return option


def encode(password):
    password.split()
    new_password = []
    for num in password:
        if int(num) >= 7:
            num = (int(num) + 3) % 10
        else:
            num = int(num) + 3
        new_password.append(str(num))
    new_password = ''.join(new_password)
    print('Your password has been encoded and stored!')
    return new_password


while option != '3':
    option = print_menu()
    if option == '1':
        password = input('Please enter your password to encode: ')
        encode(password)
    elif option == '2':
        password = input('Please enter your password to decode: ')
        decode(password)
