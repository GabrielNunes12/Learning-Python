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

## multiplication table
numberToBeMultiplied = int(input('Digite um número: '));
print(f'{numberToBeMultiplied} x 1 = {numberToBeMultiplied * 1}');
print(f'{numberToBeMultiplied} x 2 = {numberToBeMultiplied * 2}');
print(f'{numberToBeMultiplied} x 3 = {numberToBeMultiplied * 3}');
print(f'{numberToBeMultiplied} x 4 = {numberToBeMultiplied * 4}');
print(f'{numberToBeMultiplied} x 5 = {numberToBeMultiplied * 5}');
print(f'{numberToBeMultiplied} x 6 = {numberToBeMultiplied * 6}');
print(f'{numberToBeMultiplied} x 7 = {numberToBeMultiplied * 7}');
print(f'{numberToBeMultiplied} x 8 = {numberToBeMultiplied * 8}');
print(f'{numberToBeMultiplied} x 9 = {numberToBeMultiplied * 9}');
print(f'{numberToBeMultiplied} x 10 = {numberToBeMultiplied * 10}');

## Money conversor
walletReais = float(input('Quanto dinheiro você tem na carteira? R$: '));
americanDolar = 4.77;
result = walletReais / americanDolar;
print(f'com {walletReais} você pode comprar {format(result, ".2f")} dolares');

## Taxes
productPrice = float(input('Qual é o preço do produto? '));
tax = 0.05;
taxes = productPrice * tax;
payingTaxes = productPrice - taxes;
placeHolderTax = 5;
print(f'O produto que custava R${productPrice}, na promoção com desconto de {placeHolderTax}% vai custar R${format(payingTaxes, ".2f")}');