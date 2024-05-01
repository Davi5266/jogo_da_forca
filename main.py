from random import *
import os
import pyfiglet

def limparTela():
	os.system('clear') or None

limparTela()
print(pyfiglet.figlet_format('Jogo da Forca'))

def menu():
	i = input(f'Deseja tentar mais uma vez?')
	match i.lower():
		case 'sim':
			limparTela()
			palavraSorteada = palavraSecreta()
			jogoForca(palavraSorteada)
		case 'nao':
			limparTela()
			print('Tchau!')
		case _:
			limparTela()
			print('Resposta inválida!')
			menu()
def palavraSecreta():
	lista = ['banana','carro','paz','agua','bomba','chocolate','morango']
	# A função 'randrange' está sendo importada da bibliote random que esta escolhendo aleatóriamente as 7 palvras presentes na lista
	j = lista[randrange(7)]
	return j


def jogoForca(palavraEscolhida):
	letrasEscolhidas = []
	tentativas = 0
	fimDeJogo = False
	while True:
		print(pyfiglet.figlet_format('Jogo da Forca'))
		print(' ')
		print('Letra usadas: ',end='')
		print('')
		desenha_forca(tentativas)

		for i in letrasEscolhidas:
			if i.lower() not in palavraEscolhida.lower():
				print(i, end=" ")
		print('\n')

		for letra in palavraEscolhida:
			if letra.lower() in letrasEscolhidas:
				print(letra,end=" ")
			else:
				print("_",end=" ")

		print('\n')

		letraUsuario = input('Digite uma letra: ')

		letrasEscolhidas.append(letraUsuario.lower())

		if letraUsuario.lower() not in palavraEscolhida.lower():
			tentativas += 1	

		fimDeJogo = True
	
		if tentativas >= 7:
			limparTela()
			print(f'Você perdeu a palavra era {palavraEscolhida}!')
			break
	
		for letra in palavraEscolhida:
			if letra.lower() not in letrasEscolhidas:
				fimDeJogo = False

		if fimDeJogo:
			limparTela()
			print('[---}',end=' ')
			print(f'{palavraEscolhida}',end=' ')
			print('{---]')
			print(f'Você venceu o Jogo!')
			print('\n')
			animacao()
			break

		limparTela()
	menu()

#Desenho do personagem e da forca
def desenha_forca(erros):
	print("  _______     ")
	print(" |/      |    ")

	match erros:
		case 1:
			print(" |      (_)   ")
			print(" |            ")
			print(" |            ")
			print(" |            ")

		case 2:
			print(" |      (_)   ")
			print(" |      \     ")
			print(" |            ")
			print(" |            ")

		case 3:
			print(" |      (_)   ")
			print(" |      \|    ")
			print(" |            ")
			print(" |            ")

		case 4:
			print(" |      (_)   ")
			print(" |      \|/   ")
			print(" |            ")
			print(" |            ")

		case 5:
			print(" |      (_)   ")
			print(" |      \|/   ")
			print(" |       |    ")
			print(" |            ")

		case 6:
			print(" |      (_)   ")
			print(" |      \|/   ")
			print(" |       |    ")
			print(" |      /     ")

		case 7:
			print(" |      (_)   ")
			print(" |      \|/   ")
			print(" |       |    ")
			print(" |      / \   ")

	#print(" |            ")
	print("_|___")
	print("")

# Animação de personagem em caso de vitória
def animacao():
	import os, time

	stickman0 = [" O", "/|\\" ,"/ \\"]
	stickman1 = ["_O_", " | " ,"/ \\"]
	stickman2 = ["\\O/", " | " ,"/ \\"]
	i = 0
	while True:
		for i in stickman0:
			print (i)
		time.sleep(.5)
		os.system("clear")  
  
		for i in stickman1:
			print (i) 
		time.sleep(.5)
		os.system("clear") 
  
		for i in stickman2:
			print (i) 
		time.sleep(.5)
		os.system("clear")

		for i in stickman1:
			print (i) 
		time.sleep(.5)
		os.system("clear")   
		if i >= 50:
			break
		i += 1

limparTela()
palavraSorteada = palavraSecreta()
jogoForca(palavraSorteada)
