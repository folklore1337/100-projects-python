first_number = int(input('Enter first number: '))
state = (input('Enter the condition for the action (valid: +, -, /, *)'))
second_number = int(input('Enter second number: '))



if state == '+':
    print(first_number + second_number)
elif state == '-':
    print(first_number - second_number)
elif state == '/':
    print(first_number / second_number)
elif state == '*':
    print(first_number * second_number)
else:
    print('Error')
    

print()


