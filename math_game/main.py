import pygame
import random
import sys


pygame.init()


WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption('Math game')


font = pygame.font.Font(None, 40)


bg = pygame.image.load('grid_bg.png')
bg = pygame.transform.scale(bg,(WINDOW_WIDTH,WINDOW_HEIGHT))






def text_draw(texto,x,y):
    text_surf = font.render(texto, False, (255, 255, 255))
    text_rect = text_surf.get_rect(center=(x, y))
    display_surface.blit(text_surf, text_rect)


def main_game():

    display_surface.fill((0,0,0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                game()

        text_draw('Math game', WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

        text_draw('Press space for play', WINDOW_WIDTH/2, (WINDOW_HEIGHT/2)+50)


        pygame.display.update()


def game():
    

    dado_1_valor = random.randint(1,6)

    dado_1 = pygame.image.load(f"side_{dado_1_valor}_pips.png").convert_alpha()
    dado_1 = pygame.transform.scale(dado_1,(32*2,32*2))

    dado_2_valor = random.randint(1,6)

    dado_2 = pygame.image.load(f"side_{dado_2_valor}_pips.png").convert_alpha()
    dado_2 = pygame.transform.scale(dado_2,(32*2,32*2))

    dado_3_valor = random.randint(1,6)

    dado_3 = pygame.image.load(f"side_{dado_3_valor}_pips.png").convert_alpha()
    dado_3 = pygame.transform.scale(dado_3,(32*2,32*2))

    dado_4_valor = random.randint(1,6)

    dado_4 = pygame.image.load(f"side_{dado_4_valor}_pips.png").convert_alpha()
    dado_4 = pygame.transform.scale(dado_4,(32*2,32*2))

    dado_5_valor = random.randint(1,6)



    dado_5 = pygame.image.load(f"side_{dado_5_valor}_pips.png").convert_alpha()
    dado_5 = pygame.transform.scale(dado_5,(32*2,32*2))

    dado_6_valor = random.randint(1,6)

    dado_6 = pygame.image.load(f"side_{dado_6_valor}_pips.png").convert_alpha()
    dado_6 = pygame.transform.scale(dado_6,(32*2,32*2))

    dado_7_valor = random.randint(1,6)

    dado_7 = pygame.image.load(f"side_{dado_7_valor}_pips.png").convert_alpha()
    dado_7 = pygame.transform.scale(dado_7,(32*2,32*2))

    dado_8_valor = random.randint(1,6)

    dado_8 = pygame.image.load(f"side_{dado_8_valor}_pips.png").convert_alpha()
    dado_8 = pygame.transform.scale(dado_8,(32*2,32*2))

    dado_9_valor = random.randint(1,6)

    dado_9 = pygame.image.load(f"side_{dado_9_valor}_pips.png").convert_alpha()
    dado_9 = pygame.transform.scale(dado_9,(32*2,32*2))

    dado_10_valor = random.randint(1,6)

    dado_10 = pygame.image.load(f"side_{dado_10_valor}_pips.png").convert_alpha()
    dado_10 = pygame.transform.scale(dado_10,(32*2,32*2))

    dado_11_valor = random.randint(1,6)

    dado_11 = pygame.image.load(f"side_{dado_11_valor}_pips.png").convert_alpha()
    dado_11 = pygame.transform.scale(dado_11,(32*2,32*2))

    dado_12_valor = random.randint(1,6)

    dado_12 = pygame.image.load(f"side_{dado_12_valor}_pips.png").convert_alpha()
    dado_12 = pygame.transform.scale(dado_12,(32*2,32*2))

    dado_13_valor = random.randint(1,6)

    dado_13 = pygame.image.load(f"side_{dado_13_valor}_pips.png").convert_alpha()
    dado_13 = pygame.transform.scale(dado_13,(32*2,32*2))

    dado_14_valor = random.randint(1,6)

    dado_14 = pygame.image.load(f"side_{dado_14_valor}_pips.png").convert_alpha()
    dado_14 = pygame.transform.scale(dado_14,(32*2,32*2))

    dado_15_valor = random.randint(1,6)

    dado_15 = pygame.image.load(f"side_{dado_15_valor}_pips.png").convert_alpha()
    dado_15 = pygame.transform.scale(dado_15,(32*2,32*2))

    x_pos = 60

    y_pos = 120

    soma = str(dado_1_valor + dado_2_valor + dado_3_valor + dado_4_valor + dado_5_valor + dado_6_valor + dado_7_valor + dado_8_valor + dado_9_valor + dado_10_valor + dado_11_valor + dado_12_valor + dado_13_valor + dado_14_valor + dado_15_valor)

    see = False



    

    while True:
        display_surface.fill((2,2,2))
        display_surface.blit(bg,(0,0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    see = True

                if event.key == pygame.K_a:
                    dado_1_valor = random.randint(1,6)

                    dado_1 = pygame.image.load(f"side_{dado_1_valor}_pips.png").convert_alpha()
                    dado_1 = pygame.transform.scale(dado_1,(32*2,32*2))

                    dado_2_valor = random.randint(1,6)

                    dado_2 = pygame.image.load(f"side_{dado_2_valor}_pips.png").convert_alpha()
                    dado_2 = pygame.transform.scale(dado_2,(32*2,32*2))

                    dado_3_valor = random.randint(1,6)

                    dado_3 = pygame.image.load(f"side_{dado_3_valor}_pips.png").convert_alpha()
                    dado_3 = pygame.transform.scale(dado_3,(32*2,32*2))

                    dado_4_valor = random.randint(1,6)

                    dado_4 = pygame.image.load(f"side_{dado_4_valor}_pips.png").convert_alpha()
                    dado_4 = pygame.transform.scale(dado_4,(32*2,32*2))

                    dado_5_valor = random.randint(1,6)



                    dado_5 = pygame.image.load(f"side_{dado_5_valor}_pips.png").convert_alpha()
                    dado_5 = pygame.transform.scale(dado_5,(32*2,32*2))

                    dado_6_valor = random.randint(1,6)

                    dado_6 = pygame.image.load(f"side_{dado_6_valor}_pips.png").convert_alpha()
                    dado_6 = pygame.transform.scale(dado_6,(32*2,32*2))

                    dado_7_valor = random.randint(1,6)

                    dado_7 = pygame.image.load(f"side_{dado_7_valor}_pips.png").convert_alpha()
                    dado_7 = pygame.transform.scale(dado_7,(32*2,32*2))

                    dado_8_valor = random.randint(1,6)

                    dado_8 = pygame.image.load(f"side_{dado_8_valor}_pips.png").convert_alpha()
                    dado_8 = pygame.transform.scale(dado_8,(32*2,32*2))

                    dado_9_valor = random.randint(1,6)

                    dado_9 = pygame.image.load(f"side_{dado_9_valor}_pips.png").convert_alpha()
                    dado_9 = pygame.transform.scale(dado_9,(32*2,32*2))

                    dado_10_valor = random.randint(1,6)

                    dado_10 = pygame.image.load(f"side_{dado_10_valor}_pips.png").convert_alpha()
                    dado_10 = pygame.transform.scale(dado_10,(32*2,32*2))

                    dado_11_valor = random.randint(1,6)

                    dado_11 = pygame.image.load(f"side_{dado_11_valor}_pips.png").convert_alpha()
                    dado_11 = pygame.transform.scale(dado_11,(32*2,32*2))

                    dado_12_valor = random.randint(1,6)

                    dado_12 = pygame.image.load(f"side_{dado_12_valor}_pips.png").convert_alpha()
                    dado_12 = pygame.transform.scale(dado_12,(32*2,32*2))

                    dado_13_valor = random.randint(1,6)

                    dado_13 = pygame.image.load(f"side_{dado_13_valor}_pips.png").convert_alpha()
                    dado_13 = pygame.transform.scale(dado_13,(32*2,32*2))

                    dado_14_valor = random.randint(1,6)

                    dado_14 = pygame.image.load(f"side_{dado_14_valor}_pips.png").convert_alpha()
                    dado_14 = pygame.transform.scale(dado_14,(32*2,32*2))

                    dado_15_valor = random.randint(1,6)

                    dado_15 = pygame.image.load(f"side_{dado_15_valor}_pips.png").convert_alpha()
                    dado_15 = pygame.transform.scale(dado_15,(32*2,32*2))

                    x_pos = 60

                    y_pos = 120

                    soma = str(dado_1_valor + dado_2_valor + dado_3_valor + dado_4_valor + dado_5_valor + dado_6_valor + dado_7_valor + dado_8_valor + dado_9_valor + dado_10_valor + dado_11_valor + dado_12_valor + dado_13_valor + dado_14_valor + dado_15_valor)

                    see = False




        if see:
            text_draw(soma,WINDOW_WIDTH/2, WINDOW_HEIGHT/2+200)


        text_draw('Rodada: 1', WINDOW_WIDTH-100, 60)


        
        
            
        display_surface.blit(dado_1,(x_pos,y_pos))

        display_surface.blit(dado_2,(x_pos + 200,y_pos))

        display_surface.blit(dado_3,(x_pos + 400,y_pos))

        display_surface.blit(dado_4,(x_pos + 600,y_pos))

        display_surface.blit(dado_5,(x_pos + 800,y_pos))




        display_surface.blit(dado_6,(x_pos ,y_pos+ 100))
        display_surface.blit(dado_7,(x_pos + 200, y_pos + 100))

        display_surface.blit(dado_8,(x_pos + 400, y_pos + 100))

        display_surface.blit(dado_9,(x_pos + 600, y_pos + 100))

        display_surface.blit(dado_10,(x_pos + 800, y_pos + 100))


        display_surface.blit(dado_11,(x_pos ,y_pos+ 200))

        display_surface.blit(dado_12,(x_pos + 200 ,y_pos+ 200))
        display_surface.blit(dado_13,(x_pos + 400 ,y_pos + 200))
        display_surface.blit(dado_14,(x_pos + 600 ,y_pos + 200))
        display_surface.blit(dado_15,(x_pos + 800 ,y_pos + 200))
        


        pygame.display.update()



main_game()
