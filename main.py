from random import *

lista = ['banana','carro','paz','agua','bomba','chocolate','morango']
# A função 'randrange' está sendo importada da bibliote random que esta escolhendo aleatóriamente as 7 palvras presentes na lista
ponteiro = lista[randrange(7)]

# A função 'len' é para visualizar a quatidade de elementos presentes na string
# O video tem uma explicação mais simples e curta para entendimento
# https://www.youtube.com/watch?v=QxjArQ9xZDg&pp=ygUfcHl0aG9uIGNvbW8gc29sZXRyYXIgdW1hIHN0cmluZw%3D%3D

print(len(ponteiro))
print(ponteiro)
palavraSecreta = []
naoContem = []
while True:
	palavra = input('Digite uma letra: ')
	if palavra in ponteiro:
		palavraSecreta.append(palavra)
		print(palavraSecreta)
	else:
		naoContem.append(palavra)
