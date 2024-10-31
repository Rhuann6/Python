#Construa um algoritmo que receba o código e o total de vendas
#do vendedor, calcule
#a comissão conforme a tabela
#e informe o código e a comissão do vendedor:
n1=int(input('informe o codigo:'))
if(n1<100):
    print('o total de venda foi:',n1)
    soma=n1/1
    print('vc vai ganhar',soma)
if(n1>100)and(n1<350):
    print('o total de venda foi:',n1)
    soma=n1/6
    print('vc vai ganhar',soma)
if(n1>350):
    print('o total de venda foi:',n1)
    soma=(n1/10)
    print('vc vai ganhar',soma)
    