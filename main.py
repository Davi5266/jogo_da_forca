from random import *

lista = ['banana','carro','paz','agua','bomba','chocolate','morango']
ponteiro = lista[randrange(7)]

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
