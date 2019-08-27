'''Joshua'''

min_password = 6


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print('*' * len(password))


def get_password():
    password = input('Enter password of 6 characters:')
    while len(password) < min_password:
        password = input('Enter password of 6 characters:')
    return password


main()
