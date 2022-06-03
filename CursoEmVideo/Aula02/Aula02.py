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

## Average grade
firstGrade = float(input('Digite sua primeira nota: '));
secondGrade = float(input('Digite a segunda nota: '));
result = (firstGrade + secondGrade) / 2;
print(f'A primeira nota: {firstGrade} e sua segunda foi: {secondGrade}, resultando: {result}');

## converting meters
meters = float(input('Digite a medida em metros: '));
dam = meters / 10;
hm = dam / 10;
km = hm / 10;
dm = meters * 10;
cm = dm * 10;
mm = cm * 10;

print(f'A medida de: {meters}m corresponde a ');
print(f'Km: {km} km');
print(f'Hm: {hm} hm');
print(f'Dam: {dam} dam');
print(f'dm: {dm} dm');
print(f'cm: {cm} cm');
print(f'Mm: {mm} mm');
