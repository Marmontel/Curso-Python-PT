#objetivo: faça um programa qe leia a largura e a altura de uma 
#parede em metros. calcule a sua área e a quantidade de tinta necessária
#para pinta-la. sabendo que 1 litro de tinta pinta 2m quadrados

#como eu fiz (CERTO!!)

larg = float(input('Qual a largura da parede?'))
alt = float(input('Qual a altura da parede?'))
diam = larg*alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².'.format(larg, alt, (larg*alt)))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(diam/2))