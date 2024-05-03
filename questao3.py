n= int(input('quantas maçãs vai querer?'))
if n >= 12:
    total = n*1
    print('foram compradas {} maçãs, o total foi {}'.format(n,total))
if n < 12:
 total = n*1.3
print('foram compradas {} maçãs, o total foi {:.1f}'.format(n,total))
    
    