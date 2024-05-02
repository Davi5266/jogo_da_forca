from random import *
import os
import pyfiglet
import time
# Função para limpar o terminal
def limparTela():
	os.system('clear') or None

#limparTela()
#print(pyfiglet.figlet_format('Jogo da Forca'))

#Menu de continuação
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
#Função que escolhe uma das palavras na lista de forma aleatória e retorna o valor para a variavel
def palavraSecreta():
	lista = ['banana','carro','paz','agua','bomba','chocolate','morango']
	# A função 'randrange' está sendo importada da bibliote random que esta escolhendo aleatóriamente as 7 palvras presentes na lista
	j = lista[randrange(7)]
	return j

#Função que recebe a palavra como parâmetro e a  coloca na forca
def jogoForca(palavraEscolhida):
	letrasEscolhidas = []
	tentativas = 0
	fimDeJogo = False
	while True:
		#Titulo do Jogo com função da biblioteca pyfiglet
		print(pyfiglet.figlet_format('Jogo da Forca'))
		print(' ')
		print('Letra usadas: ',end='')
		#Letras que foram digitadas e não fazem parte da palavra da forca
		for i in letrasEscolhidas:
			if i.lower() not in palavraEscolhida.lower():
				print(i, end=" ")
		print('\n')
		
		desenha_forca(tentativas)

		#for i in letrasEscolhidas:
		#	if i.lower() not in palavraEscolhida.lower():
		#		print(i, end=" ")
		print('\n')
		#Verifica se a letra digitada pelo usuario pertence a palavra da forca se pertencer a letra sera printada senão um "_" é printado no lugar
		for letra in palavraEscolhida:
			if letra.lower() in letrasEscolhidas:
				print(letra,end=" ")
			else:
				print("_",end=" ")

		print('\n')

		letraUsuario = input('Digite uma letra: ')
		# Adiciona as letras digitadas pelo usuário a uma lista para depois realizar uma verificação
		letrasEscolhidas.append(letraUsuario.lower())
		# Verifica se letra que usuario digito pertence palavra da forca senão pertencer ele tira um ponto 
		if letraUsuario.lower() not in palavraEscolhida.lower():
			tentativas += 1	
		#variavel gerada para finalizar o jogo se verdadeira
		fimDeJogo = True
		#Se atingir o numero máximo de tentativas o jogo se encerra e anuncia a palavra da forca
		if tentativas >= 7:
			limparTela()
			print(pyfiglet.figlet_format('Perdeu a palavra era ' + palavraEscolhida))
			break
		# Se todas as letras digitadas fizerem parte da forca a variavel fimDeJogo permanece verdadeira senão ela recebe o valor False
		for letra in palavraEscolhida:
			if letra.lower() not in letrasEscolhidas:
				fimDeJogo = False
		# Se a variavel fimDeJogo for verdadeira o jogo finaliza e imprime o resultado
		if fimDeJogo:
			limparTela()
			print('[---}',end=' ')
			print(f'{palavraEscolhida}',end=' ')
			print('{---]')
			print(pyfiglet.figlet_format('venceu o Jogo!'))
			print('\n')
			time.sleep(5)
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
	#import os, time

	stickman0 = [" O", "/|\\" ,"/ \\"]
	stickman1 = ["_O_", " | " ,"/ \\"]
	stickman2 = ["\\O/", " | " ,"/ \\"]
	j = 0
	while True:
		for i in stickman0:
			print (i)
		time.sleep(.5)
		limparTela()  
  
		for i in stickman1:
			print (i) 
		time.sleep(.5)
		limparTela() 
  
		for i in stickman2:
			print (i) 
		time.sleep(.5)
		limparTela()

		for i in stickman1:
			print (i) 
		time.sleep(.5)
		limparTela()   
		if j == 5:
			break
		j = j + 1

# Limpa o terminal e inicia o jogo da forca
limparTela()
palavraSorteada = palavraSecreta()
jogoForca(palavraSorteada)
