var = input('Number? ')
rav = input('Other? ')

try:
    print(int(var)/int(rav))
    print('hello')
except ZeroDivisionError:
    print('Divide by 0 error')
except ValueError:
    print('Not an Integer')