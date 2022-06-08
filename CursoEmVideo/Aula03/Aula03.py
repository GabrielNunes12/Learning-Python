## Truncate a value
from math import trunc, hypot;
valueToBeTrucated = float(input('Digite um valor: '));
resultTruncated = trunc(valueToBeTrucated);
print(f'O valor digitado: {valueToBeTrucated} e a sua porção inteira é {resultTruncated}');

## Calculating skeleton and hypotenuse
skeletonOpposite = float(input('Comprimento do cateto oposto: '));
adjacentSkeleton = float(input('Comprimento do cateto adjacente: '));
resultHypotenuse = hypot(skeletonOpposite, adjacentSkeleton);
print(f'A hipotenusa vai medir: {format(resultHypotenuse, ".2f")}');