n1= float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media= (n1+n2)/2
if media >=9:
    print('Nota1: {}\nNota2: {}\nMedia: {}\nConceito: A'.format(n1,n2,media))
elif media >= 7.5 and media < 9:
    print('Nota1: {}\nNota2: {}\nMedia: {}\nConceito: B'.format(n1,n2,media))
elif media >= 6.0 and media < 7.4:
    print('Nota1: {}\nNota2: {}\nMedia: {}\nConceito: C'.format(n1,n2,media))
elif media >= 4.0 and media < 5.9:
    print('Nota1: {}\nNota2: {}\nMedia: {}\nConceito: D'.format(n1,n2,media))
elif media >= 0 and media < 3.9:
    print('Nota1: {}\nNota2: {}\nMedia: {}\nConceito: E'.format(n1,n2,media))