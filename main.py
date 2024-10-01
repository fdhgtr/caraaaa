import random
pole = [10,22,31,14,67,6,7,12,9,]
print(pole)
#
pole[5]=34
print(pole)

print(len(pole))
print(sum(pole))

pole1 = [6,2,10,15,7,9,11,4,3,1]
print(pole1)

pole1[3]=4
print(pole1)
#sečtení obou polí a délka obou polí
print(sum(pole+pole1))
print(len(pole+pole1))
#minimální a maximální hodnota obou pole A
print(min(pole))
print(max(pole))
#minimální a maximální hodnota obou dvou polí
print(min(pole + pole1))
print(max(pole + pole1))

pole_auto=list(range(1,51))
random.shuffle(pole_auto)
print(pole_auto)
