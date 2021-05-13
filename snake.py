import pygame
import random

pygame.init()

pygame.mixer.music.set_volume(0.5)  # aceita valores entre 0 e 1
background_music = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

## todos os arquivos de som precisam ser .wav, exceto a música de fundo
colision_noise = pygame.mixer.Sound('smw_coin.wav')


##Cores (https://coolors.co/)
cor_tela = (3, 83, 164)
cor_cobra = (251, 86, 7)
cor_comida = (56, 176, 0)
cor_texto = (255, 190, 11)

dimensoes = (600, 600)

tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake Game')

tela.fill(cor_tela)

clock = pygame.time.Clock()
### VALORES INICIAIS ###
#inicia desenho do retangulo no centro da tela de 600x600
# (0,0) é o canto superior esquerdo

x = 300
y = 300
d = 20  #tamanho inicial do retangulo, em pixels

#lista de posições da cobra
#inicialmente, só tem uma posição: a inicial (x, y)
lista_cobra = [[x, y]]

dx = 0
dy = 0
x_comida = round(random.randrange(0, 600-d)/20) * 20
y_comida = round(random.randrange(0, 600-d)/20) * 20

fonte = pygame.font.SysFont('hack', 35)

### FUNÇÕES ###
def desenhar_cobra(lista_cobra):
    tela.fill(cor_tela)
    for unidade in lista_cobra:
        pygame.draw.rect(tela, cor_cobra, [unidade[0], unidade[1], d, d])
    

# Movimentação da cobra
def mover_cobra(dx, dy, lista_cobra):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d
    
    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy

    lista_cobra.append([x_novo, y_novo])

    del lista_cobra[0]

    return dx, dy, lista_cobra

# Comida
def comida(dx, dy, x_comida, y_comida, lista_cobra):
    head = lista_cobra[-1]
    x_novo = head[0] + dx
    y_novo = head[1] + dy
   

    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo, y_novo])
        x_comida = round(random.randrange(0, 600-d) / 20) * 20
        y_comida = round(random.randrange(0, 600-d) / 20) * 20
        colision_noise.play()
    ##divide e multiplica por 20 para alinhar cobra e comida
    pygame.draw.rect(tela, cor_comida, [x_comida, y_comida, d, d])
   

    return [x_comida, y_comida, lista_cobra]

### verifica colisão com parede
def verifica_parede(lista_cobra):
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]

    if x not in range(600) or y not in range(600):
        raise Exception
        #raise interromope a execução 

# Verifica colisão com a própria cobra
def verifica_mordeu_cobra(lista_cobra):
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()
    del corpo[-1]   #pq esse tem q ser igual a cabeça mesmo
    for x,y in corpo:
        if x==head[0] and y==head[1]:
            
            raise Exception

##pontuação
def atualizar_pontos(lista_cobra):
    pts = str(len(lista_cobra))
    score = fonte.render('Pontuação: ' + pts, True, cor_texto)
    tela.blit(score, [0,0])
# Loop do jogo
while True:
    #jogos sempre trabalham dentro de um loop
    pygame.display.update()  #atualiza a tela
    desenhar_cobra(lista_cobra)
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_comida, y_comida, lista_cobra = comida(dx, dy, x_comida, y_comida, lista_cobra)
        
    
    verifica_parede(lista_cobra)
    verifica_mordeu_cobra(lista_cobra)
    atualizar_pontos(lista_cobra)

    speed=len(lista_cobra) + 4
    clock.tick(speed) 
