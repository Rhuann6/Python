'''1 soma=0
for i in range(1,6):
    valor=int(input('informe o numero: '))
    soma=(soma+valor)
kk=(soma/i)
print(kk)'''

''''2 maior = 0

for i in range(5):
    n = float(input("Digite um número: "))
    if n > maior:
        maior = n

print("O maior número lido foi:", maior)'''

'''3 soma=0
sla=0
for i in range(1,6):
    n1=int(input('digite: '))
    soma=n1+soma
    sla=soma
print('soma de tudo e',sla)
if(soma>0):  
 media=soma/i
print('a media foi',media)'''


'''''4 dentro_intervalo = 0
fora_intervalo = 0
for i in range(3):
    numero = float(input("Digite o número : "))
    
   
    if numero >= 10 and numero <= 20:
        dentro_intervalo =+ 1
    else:
        fora_intervalo += 1


print('Números no intervalo [10, 20]:',dentro_intervalo)
print('Números fora do intervalo:', fora_intervalo)'''



'''9 
m=0
p=0
g=0
gg=0
for i in range(1,8):
    cams=str(input('informe o o tamanho : '))
    if (cams=="m"):
        m=m+1
    if (cams=="p"):
        p=p+1
    if (cams=="g"):
        g=g+1
    if (cams=="gg"):
        gg=gg+1
print('camisetas P são: ',p)
print('camisetas m são: ',m)
print('camisetas gg são: ',gg)
print('camisetas g são: ',g)'''

'''for i in range(1,3):
    nome=str(input('informe o nome: ')) 
    bairro=str(input('informe o bairro:'))
    if (nome=='rhuann')and(bairro=='primavera'):
        valor1=int(input('informe o valor de venda:'))
        if valor1<=50000:
            porcetagem=(valor1/100)*10
        else:
            ('bairro ou nome invalido')
    nome1=str(input('informe o nome: ')) 
    bairro1=str(input('informe o bairro:'))
    if (nome1=='eduardo')and(bairro1=='castelo'):
        valor2=int(input('informe o valor de venda:'))
        if valor2>=50000:
            porcetagem1=(valor2*15)/100
        else:
            ('bairro ou nome invalido')
print('a porcentagem de bonus de edu foi: ',porcetagem1)
print('porcentagem de bonus do rhuann foi: ', porcetagem)'''
#Peça ao usuário para informar o nome e o bairro de duas pessoas.
#Se o nome for "Carlos" e o bairro for "Jardim", peça um valor de venda e calcule 12% desse valor se ele for maior que 60.000. Caso contrário, imprima uma mensagem de erro.
#Se o nome for "Maria" e o bairro for "Centro", peça um valor de venda e calcule 8% desse valor se ele for menor que 40.000. Caso contrário, imprima uma mensagem de erro.
#No final, exiba a porcentagem de bônus de Carlos e de Maria.
'''for i in range(1,3):
    nome=str(input('informe o nome: '))
    bairro=str(input('informe o bairro: '))
    valor=float(input('informe o valor: '))
    if nome=='carlos'and bairro=='jardin':
            if valor>=60000:
                porcetagem=(valor*12)/100
            else:
                print('erro')
    if nome=='maria':
        if bairro=='centro':
            if valor<40000:
                porcetagem1=(valor*8)/100
            else:
                print('erro')
print('valor de venda de maria foi',porcetagem1)
print('valor de venda de carlos foi',porcetagem)'''
'''i=0
while(i<3):
    i+=1
    nome=str(input('informe'))
print(i)'''
'''idade=0
i=0
while(i<2):
    i+=1
    idade1=int(input('informe o idade '))
    peso=int(input('informe o peso: '))
    altura=float(input('informe o altura: '))
    if idade1>50:
        idade+=1
    else:
        idade=idade
print('pessoas com idade superior a 50 anos: ',idade)'''
#•1 ,2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 -
#Jose/ 2- João /3 - Maria/ 4 - Meu nego) 5 -
#Voto Nulo 6 - Voto em Branco
#Faça um programa que calcule e
#mostre:
#•O total de votos para cada
#candidato;
#•O total de votos nulos;
#•O total de votos em branco;
#•A percentagem de votos nulos sobre
#o total de votos;
#A percentagem de votos em branco
#sobre o total de votos. 
#Para finalizar o algoritmo, o valor digitado deve ser igual a 0.
'''i=0
jose=0
joao=0
maria=0
nego=0
nulo=0
branco=0
total=0
while(i<6):
    i+=1
    vote=int(input('informe o voto: '))
    if(vote==1):
        jose+=1
        total+=1
    if(vote==2):
        joao+=1
        total+=1
    if(vote==3):
        maria+=1
        total+=1
    if(vote==4):
        nego+=1
        total+=1
    if(vote==5):
        nulo+=1
    if(vote==6):
        branco+=1
total1=(tonulo)*100
total2=(total/tal/branco)*100
print('jose recebeu o total de: ',jose)
print('joao recebeu o total de: ',joao)
print('maria recebeu o total de: ',maria)       
print('nego recebeu o total de: ',nego)           
print('nulo recebeu o total de: ',nulo)
print('branco recebeu o total de: ',branco)
print('a porcetagem do nulo e dos votos é: %',total1)
print('a porcetagem de brancos e dos votos %é:',total2)'''
#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
#seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
'''n=0
d=0
i=0
j=0
v=0
while(i<3):
    num=int(input('informe: '))
    if num>=0 and num <=25:
        n+=1
    if num>=26 and num <=50:
        d+=1
    if num>=51 and num <=75:
        v+=1
    if num>=76 and num <=100:
        j+=1
    if num<0:
        i+=4
print('numeros no intervalo de 0 a 25: ',n)
print('numeros no intervalo de 26 a 50: ',d)
print('numeros no intervalo de 51 a 75: ',v)
print('numeros no intervalo de 76 a 100: ',j)'''
'''import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura_tela = 900
altura_tela = 900
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo do Cabeça")

# Cores
cor_fundo = (5, 5, 5)
cor_bolinha_jogador = (255, 10, 30)
cor_bolinha_inimiga = (0, 250, 90)

# Propriedades da bolinha do jogador
posicao_bolinha_jogador = [400, 400]  # Posição inicial
raio_bolinha_jogador = 50
velocidade_bolinha_jogador = 14

# Lista de bolinhas que caem
bolinhas_inimigas = []
raio_bolinha_inimiga = 60
velocidade_bolinha_inimiga = 10

# Variáveis de controle do jogo
jogo_acabou = False

# Função para criar uma nova bolinha inimiga
def criar_bolinha_inimiga():
    posicao_x = random.randint(raio_bolinha_inimiga, largura_tela - raio_bolinha_inimiga)
    return [posicao_x, 6]  # Começa no topo da tela

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controle da bolinha do jogador com W, A, S, D
    teclas = pygame.key.get_pressed()
    if not jogo_acabou:
        if teclas[pygame.K_a]:
            posicao_bolinha_jogador[0] -= velocidade_bolinha_jogador  # Move para a esquerda
        if teclas[pygame.K_d]:
            posicao_bolinha_jogador[0] += velocidade_bolinha_jogador  # Move para a direita
        if teclas[pygame.K_w]:
            posicao_bolinha_jogador[1] -= velocidade_bolinha_jogador  # Move para cima
        if teclas[pygame.K_s]:
            posicao_bolinha_jogador[1] += velocidade_bolinha_jogador  # Move para baixo

    # Mantém a bolinha do jogador dentro da tela
    posicao_bolinha_jogador[0] = max(raio_bolinha_jogador, min(posicao_bolinha_jogador[0], largura_tela - raio_bolinha_jogador))
    posicao_bolinha_jogador[1] = max(raio_bolinha_jogador, min(posicao_bolinha_jogador[1], altura_tela - raio_bolinha_jogador))

    # Atualiza as bolinhas que caem
    if not jogo_acabou:
        # Chance de criar uma nova bolinha inimiga
        if random.randint(1, 30) == 1:
            bolinhas_inimigas.append(criar_bolinha_inimiga())

        # Move as bolinhas inimigas para baixo
        for bolinha in bolinhas_inimigas:
            bolinha[1] += velocidade_bolinha_inimiga  # Move a bolinha para baixo

            # Verifica colisão com a bolinha do jogador
            if (posicao_bolinha_jogador[0] - raio_bolinha_jogador) < (bolinha[0] + raio_bolinha_inimiga) and \
               (posicao_bolinha_jogador[0] + raio_bolinha_jogador) > (bolinha[0] - raio_bolinha_inimiga) and \
               (posicao_bolinha_jogador[1] - raio_bolinha_jogador) < (bolinha[1] + raio_bolinha_inimiga) and \
               (posicao_bolinha_jogador[1] + raio_bolinha_jogador) > (bolinha[1] - raio_bolinha_inimiga):
                jogo_acabou = True  # O jogador perdeu

        # Remove bolinhas que saíram da tela
        bolinhas_inimigas = [bolinha for bolinha in bolinhas_inimigas if bolinha[1] < altura_tela]

    # Atualiza a tela
    tela.fill(cor_fundo)
    pygame.draw.circle(tela, cor_bolinha_jogador, (posicao_bolinha_jogador[0], posicao_bolinha_jogador[1]), raio_bolinha_jogador)

    for bolinha in bolinhas_inimigas:
        pygame.draw.circle(tela, cor_bolinha_inimiga, (bolinha[0], bolinha[1]), raio_bolinha_inimiga)

    if jogo_acabou:
        fonte = pygame.font.Font(None, 74)
        texto = fonte.render("você é gay", True, cor_bolinha_jogador)
        tela.blit(texto, (largura_tela // 2 - 200, altura_tela // 2 - 50))
    pygame.display.flip()

    # Controla a taxa de quadros
    pygame.time.Clock().tick(60)'''
#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#Maior e Menor Acerto;
##A Média das Notas da Turma.Gabarito da Prova:

#01 - A
#02 - B
#03 - C
#04 - D
#05 - E
#06 - E
#07 - D
#08 - C
#09 - B
#10 - A

# pergunta 7
'''
i=0
total=0
maior=0
menor=0
menor1=0
usou=0
while (i<1):
    nota1=str(input('informe a resposta da 1 questao: '))
    nota2=str(input('informe a resposta da 2 questao: '))
    nota3=str(input('informe a resposta da 3 questao: '))
    nota4=str(input('informe a resposta da 4 questao: '))
    nota5=str(input('informe a resposta da 5 questao: '))
    nota6=str(input('informe a resposta da 6 questao: '))
    nota7=str(input('informe a resposta da 7 questao: '))
    nota8=str(input('informe a resposta da 8 questao: '))
    nota9=str(input('informe a resposta da 9 questao: '))
    nota10=str(input('informe a resposta da 10 questao: '))
    if nota1=='a':
        total+=1
    else :
        menor1+=1
    if nota2=='b':
        total+=1
    else:
        menor1+=1
    if nota3=='c':
        total+=1
    else:
        menor1+=1
    if nota4=='d':
        total+=1 
    else:
        menor1+=1
    if nota5=='e':
        total+=1
    else:
        menor1+=1
    if nota6=='e':
        total+=1
    else:
        menor1+=1
    if nota7=='d':
        total+=1
    else:
        menor1+=1
    if nota8=='c':
        total+=1 
    else:
        menor1+=1       
    if nota9=='b':
        total+=1
    else:
        menor1+=1
    if nota10=='a':
        total+=1
    else:
        menor1+=1
    if total>=total:
        maior=total
    if menor1>menor:
        menor=menor1
        if menor1<menor:
            menor1=menor
    print('o maior acerto da sala foi',maior)
    print('a sua nota foi : ',total)
    print('o menor acerto da sala foi : ',menor)
    sistema=str(input('vai usar o sistema?'))
    if sistema=='sim':
        menor=menor
        menor1=0
        maior=0
        total=0
    if sistema=='nao':
        i+=2
        usou+=1

    else:
        i==0'''
# pergunta 4 , A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
'''a = 0
b = 1
while a <= 500:
    print(a)
    a,b = b, a + b
'''
#pergunta 1
'''k=int(input('informe 1 para homen e 2 para mulher: '))
a=float(input('informe sua altura: '))
if k==1:
    g=(72,7*a)-58
print('seu peso é ideal é: ',g)
if a==2:
    l=(62,1*a)-58
print('seu peso ideal é:',l)
if k>2:
    print('invalido')
    '''
#pergunta 3
'''n=float(input('informe quanto vc recebe por hora: '))
k=float(input('informe qnts hora vc trabalhou: '))
p=n*k
print('vc ganha por mes',p)'''
'''#pergunta 3
f=str(input('informe seu nome')) 
p=len(f)
if p>4:
    print('seu nome é:',f)  
g=int(input('informe a idade: '))
if g>0 and g<150:
    print('sua idade e',g)
else:
    print('invalido')         
k=str(input('informe o sexo f para femia e h homen: '))
if k=='f':
    print('vc e mulher')
if k=='h':
    print('vc e homen ')
l=str(input('informe o estado civil s,c,v ou d: '))
if l=='s':
    print('solteiro')
if l=='c':
    print('casado')
if l=='v':
    print('viuvo')
if l=='d':
    print('divorciado')
else:
    print('invalido') 
s=float(input('informe o salario'))
print('seu salario é:',s)'''
# pergunta 6 
'''contador = 0
aluno_mais_alto = 0
altura_mais_alta = 0
aluno_mais_baixo = 0
altura_mais_baixa = 999  


while contador < 10:
    numero_aluno = int(input("Digite o número do aluno: "))
    altura = float(input("Digite a altura do aluno em centímetros: "))
    
    if altura > altura_mais_alta:
        altura_mais_alta = altura
        aluno_mais_alto = numero_aluno
        
    if altura < altura_mais_baixa:
        altura_mais_baixa = altura
        aluno_mais_baixo = numero_aluno
        
    contador += 1  

print(f"Aluno mais alto: Número: {aluno_mais_alto}, Altura: {altura_mais_alta} cm")
print(f"Aluno mais baixo: Número: {aluno_mais_baixo}, Altura: {altura_mais_baixa} cm")'''
#pergunta 5
'''n=int(input('digite um numero'))
if n>1 :
    for i in range(2,n):
        print('nao e primo')
        break
    else:
        print('e numero primo')
else:
    print('nao e numero primo')'''
#pergunta 2
'''ganho_por_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))
salario_total = ganho_por_hora * horas_trabalhadas
print("O seu salário total no mês é: R$",salario_total)'''
#Escreva um algoritmo que deverá realizar a função de pedido de pizza que calcule o valor total de acordo com ingredientes e o tamanho escolhido .
#Deverá apresentar as seguintes perguntar:
#- tamanho da pizza : pequena R$20,média R$30,grande R$40.
#- o programa deverá perguntar se deseja adicionar ingredientes extras como: calabresa ,mussarela ,tomate ,cebola ,bacon .cada ingrediente extra tem o valor de R$ 5,00. Por fim , se deseja beber algo(valor de  R$ 8,00)
#- após isso , pergunta se deseja fazer um novo pedido. - dizer qual foi o pedido mais caro 
#- -dizer qual o pedido mais baixo 
#- -quantidade de pedidos
total=0
baixo=0
alto=0
i=0
while i<1:
    piz=str(input('informe M para media,informe P para pequena,informe G para grande :'))
    if piz=='p':
        total+=20
    if piz=='m':
        total+=30
    if piz=='g':
        total+=40
    igre=str(input('adicionamentos:bacon,tomate,mussarela,cebola e calabresa(valor dos adicionamento:R$ 5,00.digite o nome do igrediente,caso se nao querer digite: nao)'))
    if igre=='bacon'or'tomate'or'cebola'or'mussarela'or'calabresa':
        total+=5
    beb=str(input('ira querer refrigerante:'))
    if beb=='sim':
        total+=8
    print('o total do pedido foi: ',total)
    baixo==total
    alto=total
    if total>alto:
        alto==total
    if baixo>total:
        baixo==total
    baixo==total
    deseja=str(input('deseja fazer um novo pedido? '))
    if deseja=='nao':
        i+=2
    print('o total do pedido foi: ',total)
print('o pedido mais caro foi: ',alto)
print('o pedido mais barato foi: ',baixo)








        
    
    
    






























