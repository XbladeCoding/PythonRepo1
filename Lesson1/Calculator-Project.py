from math import sqrt

firstPrompt = input('Welcome to Python Calculator! What would you like to do? ')

#First we create basic arthmetic operations
try:
    if firstPrompt == 'add' or firstPrompt == 'Add':
        firstNumAdd = float(input('First number? '))
        secNumAdd = float(input('Second number? '))
        print(firstNumAdd + secNumAdd)
    elif firstPrompt == 'subtract' or firstPrompt == 'Subtract':
        firstNumSub = float(input('First number? '))
        secNumSub = float(input('Second Number? '))
        print(firstNumSub - secNumSub)
    elif firstPrompt == 'multiply' or firstPrompt == 'Multiply':
        firstNumMult = float(input('First number? '))
        secNumMult = float(input('Second numbar? '))
        print(firstNumMult * secNumMult)
    elif firstPrompt == 'divide' or firstPrompt == 'Divide':
        firstNumDiv = float(input('First number? '))
        secNumDiv = float(input('Second number? '))
        print(firstNumDiv / secNumDiv)
    elif firstPrompt == 'exponent' or firstPrompt == 'Exponent':
        firstNumExp = float(input('Base? '))
        secNumExp = float(input('Exponent? '))
        print(firstNumExp ** secNumExp)
    elif firstPrompt == 'sqrt' or firstPrompt == 'square root':
        BaseRoot = float(input('Base? '))
        print(sqrt(BaseRoot))

except ZeroDivisionError:
    print('DIVIDE BY 0 ERROR')
except ValueError:
    print('Undefined value')