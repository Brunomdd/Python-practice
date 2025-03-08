#Faça um programa que leia a largura e a altura de uma parede em metros.
#Calcule a sua área e a quantidade de tinta necessária para pinta-lo,sabendo que cada litro de tinta
#é uma área de 2m²

larg = float(input('Digite a largura da parede:'))
alt = float(input('Digite a altura da parede:'))
area = larg * alt
print('Sua parede tem dimensões de {}x{} e sua área é de {}m²'.format(larg,alt,area))
tinta = area / 2
print('Para pintar essa parede, voçe vai precisar de {}L de tinta'.format((tinta)))