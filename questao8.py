atual = int(input('a quantidade atual é: '))
maximo = int(input('a quantidade maxima é: '))
minimo = int(input('a quantidade minima é: '))
media  = (maximo + minimo)/2
if atual >= media:
  print(atual,'Não Efetuar comprar')
else:
    print(atual, 'Efetuar compra')