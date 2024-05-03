n1 = float(input('Digite a nota 1 do aluno: '))
n2 = float(input('Digite a nota 2 do aluno: '))
media = (n1 + n2) /2
if media >= 6:
    print('a media do aluno {},ele foi aprovado'.format(media))
else:
    print('a media do aluno {}, ele foi reprovado'.format(media))
    
