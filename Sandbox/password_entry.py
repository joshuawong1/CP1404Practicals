'''Joshua'''

min_password = 6

password = input('Enter password of 6 characters')
while len(password) < min_password:
    password = input('Enter password of 6 characters')
print('*' * len(password))
