## Working with data types in Python
number1 = int(input('Digite um número inteiro: '));
numberFloat = float(input('Digite um número real: '));
booleanOptions = False;

print(f'Seu número inteiro foi: {number1}');
print(f'Seu número float foi: {numberFloat}');
print(f'Valor default: {booleanOptions}');

numberToBeSumUp = int(input('Digite seu número: '));
numberToBeSummed = int(input('Digite outro número: '));
result = numberToBeSumUp + numberToBeSummed;

print(f'A soma entre {numberToBeSumUp} e {numberToBeSummed} é: {result}');

## Reading through user input and showing possible functionalitties
something = input('Digite algo: ');
print(f'is alpha numeric: {something.isalnum()}');
print(f'isLower: {something.islower()}');
print(f'isUpper: {something.isupper()}');
print(f'isascii: {something.isascii()}');
print(f'isdigit: {something.isdigit()}');