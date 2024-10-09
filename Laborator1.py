from time import sleep

name = input('Input your username: ')
password = input('Input password: ')
values = []

if name == password:
    print('\nHaving your password the same as your username isn\'t a good idea...\n')

print(f'\nWelcome {name} with IPv4 address 193.1.81.256')
print('Succesfully logged in.....Or not, i wouldn\'t know')
print('I don\'t check the password at all\n\n')


print('Here\' your username in ascii values for no reason:')
for ch in name:
    print(ord(ch), end = ' ')
    values.append(ord(ch))
print('\n')


print('Here\'s the ascii values in hexadecimal, again, for no reason:')
for i in range(0, len(values)):
    hexed = []
    num = values[i]
    while num > 0:
        if num%16 > 9:
            hexed.insert(0, chr(num%16-10+97))
        else:
            hexed.insert(0, str(num%16).upper())
        num //= 16
    print(''.join(hexed), end = ' ')
    values[i] = ''.join(hexed)
print('\n')


print('And lastly, the hexadecimal values in binary...')
print('...and you\'ll never guess...')
print('...but also for no reason:')
for i in range(0, len(values)):
    n1 = ord(values[i][0])-65+10 if values[i][0].isalpha() else int(values[i][0])
    n2 = ord(values[i][1])-65+10 if values[i][1].isalpha() else int(values[i][1])
    b1 = ['0', '0', '0', '0']
    b2 = ['0', '0', '0', '0']
    for i in range(3, -1, -1):
        b1[i] = str(n1%2)
        n1 //= 2
        b2[i] = str(n2%2)
        n2 //= 2
    print(f'{''.join(b1)} {''.join(b2)}')
    
print('\n')