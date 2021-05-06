# Typing Speed Game. 
# Cada palavra digitada corretamente acrescenta um ponto. No final, o programa exibe na tela o tempo.

#ACESSANDO UM SITE COM PYTHON
#lista de 10000 palavras https://www.mit.edu/~ecprice/wordlist.10000
#requests permite comunicação com o site. 

import requests
import random
import time

url = 'https://www.mit.edu/~ecprice/wordlist.10000'

resposta = requests.get(url)
palavras = resposta.content.splitlines()
#splitlines transforma essas palavras separadas por linhas do site em uma lista de palavras

#Conversão do formato das palavras.
palavras = [palavra.decode('utf-8') for palavra in palavras]
#print(palavras)

#10 palavras aleatórias da lista
random_words = random.sample(palavras, 10)
#print(random_words)

pontos = 0

tic = time.perf_counter()
for palavra in random_words:
  print(palavra)
  entrada = input()
  if entrada == palavra:
    pontos = pontos + 1

toc=time.perf_counter()

print(pontos, 'points')
print('time = ',toc-tic, 'sec')
