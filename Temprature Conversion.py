choose = input("Choose an operator 'fahrenheit' or 'celsius': ").strip().lower()

if choose == 'fahrenheit' or 'Fahrenheit':
    celsius = float(input('Enter temperature in Celsius: '))
    fahrenheit = (celsius * 1.8) + 32
    print('%.2f Celsius is equivalent to: %.2f Fahrenheit' % (celsius, fahrenheit))
elif choose == 'celsius' or 'Celsius':
    fahrenheit = float(input('Enter temperature in Fahrenheit: '))
    celsius = (fahrenheit - 32) / 1.8
    print('%.2f Fahrenheit is equivalent to: %.2f Celsius' % (fahrenheit, celsius))
else:
    print("Invalid choice. Please choose 'fahrenheit' or 'celsius'.")
