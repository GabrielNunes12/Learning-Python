## Showing the previous and next numbers
import math

actualNumber = int(input('Digite um número: '));
previousNumber = actualNumber - 1;
nextNumber = actualNumber + 1;
print(f'Your number is: {actualNumber}, previous number is: {previousNumber} and the last is: {nextNumber}');

## Square root and Math library
yourNumber = int(input('Digite um número: '));
tripleNumber = yourNumber * 3;
doubleNumber = yourNumber * 2;
squareRoot = math.sqrt(yourNumber);

print(f'Seu numero: {yourNumber}');
print(f'Dobro: {doubleNumber}');
print(f'triplo: {tripleNumber}');
print(f'Raiz quadrada: {format(squareRoot,".2f")}');