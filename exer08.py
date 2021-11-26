#objetivo Converter metros em cm e milimetros

#como eu fiz (CERTO)

m = float(input('Quantos metros tem seu percurso? '))
c = m * 100
ml = m * 1000
km = m / 1000
mic = m * 1000000
print('Seu percurso terá {}KM {} metros, {} centímetros e {} melimetros e {} micrometros.'.format(km, m, c, ml, mic))