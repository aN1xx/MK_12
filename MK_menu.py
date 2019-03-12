import pygame
import os

from q import game_loop

pygame.init()
size = width, height = 1400, 750 #[int(j) for j in input().split()]
screen = pygame.display.set_mode(size)

class Scorpion():
    name = 'scorpion'
    stand = pygame.image.load(os.path.join('data\scorpion', 'stand.png'))
    walk1 = pygame.image.load(os.path.join('data\scorpion', 'walk1.png'))
    walk2 = pygame.image.load(os.path.join('data\scorpion', 'walk2.png'))
    walk3 = pygame.image.load(os.path.join('data\scorpion', 'stand.png'))
    walk4 = pygame.image.load(os.path.join('data\scorpion', 'walk2.png'))
    punch1 = pygame.image.load(os.path.join('data\scorpion', 'punch1.png'))
    punch2 = pygame.image.load(os.path.join('data\scorpion', 'punch2.png'))
    kombo1 = pygame.image.load(os.path.join('data\scorpion', 'kombo1.png'))
    kombo2 = pygame.image.load(os.path.join('data\scorpion', 'kombo2.png'))
    inv = pygame.image.load(os.path.join('data\scorpion', 'inv.png'))
    block = pygame.image.load(os.path.join('data\scorpion', 'block.png'))
    ability = pygame.image.load(os.path.join('data\scorpion', 'ability.png'))
    frozen = pygame.image.load(os.path.join('data\scorpion', 'frozen.png'))
    spear = pygame.image.load(os.path.join('data\scorpion', 'spear.png'))
    name_player1 = pygame.image.load(os.path.join('data\scorpion', 'name_player1.png'))
    name_player2 = pygame.image.load(os.path.join('data\scorpion', 'name_player2.png'))
    finish = pygame.image.load(os.path.join('data\scorpion', 'finish.png'))
    
    
class Sub_zero():
    name = 'sub-zero'
    stand = pygame.image.load(os.path.join('data\sub-zero', 'stand.png'))
    walk1 = pygame.image.load(os.path.join('data\sub-zero', 'walk1.png'))
    walk2 = pygame.image.load(os.path.join('data\sub-zero', 'walk2.png'))
    walk3 = pygame.image.load(os.path.join('data\sub-zero', 'stand.png'))
    walk4 = pygame.image.load(os.path.join('data\sub-zero', 'walk2.png'))
    punch1 = pygame.image.load(os.path.join('data\sub-zero', 'punch1.png'))
    punch2 = pygame.image.load(os.path.join('data\sub-zero', 'punch2.png'))   
    kombo1 = pygame.image.load(os.path.join('data\sub-zero', 'kombo1.png'))
    kombo2 = pygame.image.load(os.path.join('data\sub-zero', 'kombo2.png'))
    inv = pygame.image.load(os.path.join('data\sub-zero', 'inv.png'))
    block = pygame.image.load(os.path.join('data\sub-zero', 'block.png'))
    ability = pygame.image.load(os.path.join('data\sub-zero', 'ability.png'))
    frozen = pygame.image.load(os.path.join('data\sub-zero', 'frozen.png'))
    ice_ball = pygame.image.load(os.path.join('data\sub-zero', 'ice_ball.png'))
    name_player1 = pygame.image.load(os.path.join('data\sub-zero', 'name_player1.png'))
    name_player2 = pygame.image.load(os.path.join('data\sub-zero', 'name_player2.png'))
    finish = pygame.image.load(os.path.join('data\sub-zero', 'finish.png'))

    
menu = pygame.image.load(os.path.join('data', 'menu.png'))
characters = pygame.image.load(os.path.join('data', 'characters.png'))
characters_menu_png = pygame.image.load(os.path.join('data', 'characters_menu.png'))


characters_menu = False
controls_menu = False
menu_is = True
char1 = None
char2 = None
char1l = False
char2l = False

while menu_is:
    screen.fill((0, 0, 0))
    screen.blit(menu, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_is = False
    
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if x >= 484 and x <= 878 and y >= 335 and y <= 432 and event.button == 1 and characters_menu == False:
                #pass
                characters_menu = True
            
            elif x >= 554 and x <= 816 and y >= 506 and y <= 600 and event.button == 1:
                menu_is = False
            
            elif x >= 170 and x <= 376 and y >= 460 and y <= 664 and event.button == 1 and characters_menu == True:
                if char1 == None and char1l == False:
                    char1 = Scorpion()
                if char2 == None and char1l == True and char2l == False:
                    char2 = Scorpion()

            elif x >= 1042 and x <= 1250 and y >= 460 and y <= 664 and event.button == 1 and characters_menu == True:
                if char1 == None and char1l == False:
                    char1 = Sub_zero()
                if char2 == None and char1l == True and char2l == False:
                    char2 = Sub_zero()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                if char1l == True and char2l == True:
                    char2l = False
                    char2 = None
                
                elif char1l == True and char2l == False:
                    char1l = False
                    char1 = None
            
        if event.key == pygame.K_SPACE and characters_menu == True:
            #screen.blit
            pass
                    
    if characters_menu == True:
        screen.blit(characters_menu_png, (0, 0))
        screen.blit(characters, (0, 0))
        if char1 != None:
            screen.blit(char1.stand, (200, 100))
            char1l = True
        
        if char2 != None:
            screen.blit(pygame.transform.flip(char2.stand, True, False), (930, 100))
            char2l = True
            
    pygame.display.flip()

pygame.quit()