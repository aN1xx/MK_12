import pygame
import os
import random

pygame.init()
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
size = width, height = 1400, 750
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60 
menu = pygame.image.load(os.path.join('data\misc', 'menu.png'))
characters_menu = pygame.image.load(os.path.join('data\misc', 'characters_menu.png'))
characters = pygame.image.load(os.path.join('data\misc', 'characters.png'))
frame1 = pygame.image.load(os.path.join('data\misc', 'frame_player1.png'))
frame2 = pygame.image.load(os.path.join('data\misc', 'frame_player2.png'))
maps = pygame.image.load(os.path.join('data\misc', 'maps.png'))

Almaty = pygame.image.load(os.path.join('data\maps', 'Almaty.png'))
fizmat = pygame.image.load(os.path.join('data\maps', 'fizmat.png'))
outworld = pygame.image.load(os.path.join('data\maps', 'outworld.png'))
arena = pygame.image.load(os.path.join('data\maps', 'arena.png'))
google = pygame.image.load(os.path.join('data\maps', 'google.png'))


fight = pygame.mixer.Sound('data\sounds\sf_fight.ogg')
punch = pygame.mixer.Sound('data\sounds\punch.ogg')
fatality_snd = pygame.mixer.Sound('data\sounds\sf_fatality.ogg')
finish_him_snd = pygame.mixer.Sound('data\sounds\sf_finish_him.ogg')
scorpion_wins_snd = pygame.mixer.Sound('data\sounds\scorpion_wins.ogg')
sub_zero_wins_snd = pygame.mixer.Sound('data\sounds\sub_zero_wins.ogg')

scorpion = pygame.mixer.Sound('data\sounds\scorpion.ogg')
sub_zero = pygame.mixer.Sound('data\sounds\sub_zero.ogg')
you_suck = pygame.mixer.Sound('data\sounds\you_suck.ogg')


class Scorpion():
    name = 'scorpion'
    
    #images
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
    
    #sounds
    ability_sound = pygame.mixer.Sound('data\sounds\get_over_here.ogg')
    win = pygame.mixer.Sound('data\sounds\scorpion_wins.ogg')
     
    
class Sub_zero():
    name = 'sub-zero'
    
    #images
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

    #sounds
    ability_sound = pygame.mixer.Sound('data\sounds\ice_ball_charge.ogg')  
    win = pygame.mixer.Sound('data\sounds\sub_zero_wins.ogg') 

def game_loop(character1 = Scorpion(), character2 = Sub_zero(), bg_map = fizmat):
    
    player1 = character1
    p1_image = player1.stand
    pressed_d = False
    pressed_a = False
    pressed_s = False
    pressed_w = False
    punch_p1 = False
    stop_p1 = False
    timer1 = 0
    ww = 0
    player1_x = 10
    player1_y = 350
    player1_health = 100
    p1_hp_color = (0, 255, 0)
    kombo_p1 = False
    kombo_time_p1 = 0
    p1_inv_timer = 0
    p1_inv = False
    p1_blocked = False
    p1_ability = False
    projectile_x_p1 = 0
    hooked_p1 = False
    frozen_p1 = False
    pressed_y = False
    cd_p1 = 0
    p1_win = False
    fatality_p1 = False
    fatality_timer_p1 = 200
    frm1 = 10
    stun_p1 = False
    stun_timer_p1 = 0
    snd1 = True
    
    
    player2 = character2
    p2_image = player2.stand
    player2_x = 1200
    player2_y = 350
    player2_health = 100
    p2_hp_color = (0, 255, 0)
    p2_inv = False
    pressed_right = False
    pressed_left = False
    pressed_down = False
    pressed_up = False
    ww2 = 0
    stop_p2 = False
    kombo_time_p2 = 0
    punch_p2 = False
    kombo_p2 = False
    p2_blocked = False
    p2_ability = False
    projectile_x_p2 = 0
    hooked_p2 = False
    frozen_p2 = False
    pressed_p = False
    cd_p2 = 0    
    p2_win = False
    fatality_p2 = False
    fatality_timer_p2 = 200
    frm2 = 10
    stun_p2 = False
    stun_timer_p2 = 0 
    snd2 = True
    
    
    finish_him = pygame.image.load(os.path.join('data\misc', 'finish_him.png'))
    fatality = pygame.image.load(os.path.join('data\misc', 'fatality.png'))
    scorpion_wins = pygame.image.load(os.path.join('data\misc', 'scorpion_wins.png'))
    sub_zero_wins = pygame.image.load(os.path.join('data\misc', 'sub-zero_wins.png'))
    
    sz_fat1 = pygame.mixer.Sound('data\sounds\sz_fat1.ogg')
    sz_fat2 = pygame.mixer.Sound('data\sounds\sz_fat2.ogg')
    sc_fat1 = pygame.mixer.Sound('data\sounds\sc_fat1.ogg')
    sc_fat2 = pygame.mixer.Sound('data\sounds\sc_fat2.ogg')
    
    quit = False
    running = True
    fight.play()
    while running:
        
        screen.fill((255, 255, 255))
        screen.blit(bg_map, (0, 0))
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False 
                quit = True
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_d:
                    pressed_d = True
                    
                if event.key == pygame.K_a:
                    pressed_a = True
                 
                if event.key == pygame.K_w:
                    pressed_w = True                
                    
                if event.key == pygame.K_s:
                    pressed_s = True
                    
                
                    
                if event.key == pygame.K_t and kombo_time_p1 >= 1 and not p1_inv and not kombo_p1:
                    kombo_time_p1 = 0
                    stop_p1 = True
                    kombo_p1 = True
                    ktimer_p1 = 16
                    
                elif event.key == pygame.K_t and not p1_inv:
                    if not punch_p1:
                        punch_p1 = True
                        stop_p1 = True
                        timer1 = 10
                        kombo_time_p1 = 20
                    
                    
                if event.key == pygame.K_LEFT:
                    pressed_left = True
                            
                if event.key == pygame.K_RIGHT:
                    pressed_right = True
                  
                if event.key == pygame.K_UP:
                    pressed_up = True             
                            
                if event.key == pygame.K_DOWN:
                    pressed_down = True                 
                            
                if event.key == pygame.K_o and kombo_time_p2 >= 1 and not p2_inv and not kombo_p2:
                    kombo_time_p2 = 0
                    stop_p2 = True
                    kombo_p2 = True
                    ktimer_p2 = 16
                                
                elif event.key == pygame.K_o and not p2_inv:
                    if not punch_p2:
                        punch_p2 = True
                        stop_p2 = True
                        timer2 = 10
                        kombo_time_p2 = 20
                        
                if pressed_down and pressed_right and event.key == pygame.K_p and not p2_ability and cd_p2 <= 0:
                    p2_ability = True
                    projectile_x_p2 = player2_x - 40
                
                elif event.key == pygame.K_p:
                    pressed_p = True
                 
                if pressed_s and pressed_a and event.key == pygame.K_y and not p1_ability and cd_p1 <= 0:
                    p1_ability = True
                    if player1.name == 'scorpion':
                        projectile_x_p1 = player1_x + 220
                    elif player1.name == 'sub-zero':
                        projectile_x_p1 = player1_x + 150
                    
                elif event.key == pygame.K_y:
                    pressed_y = True
                    
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_d:
                    pressed_d = False
                 
                if event.key == pygame.K_w:
                    pressed_w = False               
                    
                if event.key == pygame.K_s:
                    pressed_s = False            
                    
                if event.key == pygame.K_a:   
                    pressed_a = False  
                    
                if event.key == pygame.K_LEFT:
                    pressed_left = False
                                
                if event.key == pygame.K_RIGHT:
                    pressed_right = False
                
                if event.key == pygame.K_UP:
                    pressed_up = False                    
                
                if event.key == pygame.K_DOWN:
                    pressed_down = False            
                    
                if event.key == pygame.K_p:
                    pressed_p = False
                    p2_blocked = False
                    p2_image = player2.stand
                    stop_p2 = False
                    
                if event.key == pygame.K_y:
                    pressed_y = False
                    p1_blocked = False 
                    p1_image = player1.stand
                    stop_p1 = False
                 
        if p1_win:
            
            p1_image = player1.stand
            p2_image = player2.finish
            
            player1_x = 300
            player2_x = 900
            
            if pressed_a and pressed_w and pressed_d and fatality_timer_p1 > 0:
                fatality_p1 = True
                
                
            if fatality_p1:
                if player1.name == 'scorpion':
                    frame = 'frame' + str(int(frm1 // 10)) + '.png'
                    frm1 += 1
                    
                    if frm1 // 10 <= 9:
                        screen.blit(pygame.transform.flip(p2_image, True, False), (int(player2_x), int(player2_y)))                    
                    
                    if frm1 <= 119:
                        img = pygame.image.load(os.path.join('data\scorpion', frame))
                        
                    if frm1 >= 109:
                        screen.blit(fatality, (300, 110))
                        screen.blit(scorpion_wins, (300, 110))
                        
                    if frm1 == 108:
                        fatality_snd.play()
                            
                    if frm1 == 148:
                        scorpion_wins_snd.play() 
                        
                    if frm1 == 40:
                        sc_fat1.play()
                        
                    if frm1 == 80:
                        sc_fat2.play()
                    
                    screen.blit(img, (300, 50))
                    
                    if frm1 >= 300:
                        return
                    
                elif player1.name == 'sub-zero':
                    frame = 'frame' + str(int(frm1 // 10)) + '.png'
                    frm1 += 1
                        
                    if frm1 // 10 <= 7:
                        screen.blit(pygame.transform.flip(p2_image, True, False), (int(player2_x), int(player2_y)))                    
                        
                    if frm1 <= 129:
                        img = pygame.image.load(os.path.join('data\sub-zero', frame))
                        
                    if frm1 >= 119:
                        screen.blit(fatality, (300, 110))
                        screen.blit(sub_zero_wins, (300, 110))                    
                     
                    if frm1 == 118:
                        fatality_snd.play()
                        
                    if frm1 == 158:
                        sub_zero_wins_snd.play()
                        
                    if frm1 == 40:
                        sz_fat1.play()
                            
                    if frm1 == 115:
                        sz_fat2.play()                    
                        
                    screen.blit(img, (300, 50))
                        
                    if frm1 >= 310:
                        return                
                    
                
                    
            else:
                fatality_timer_p1 -= 1
                if fatality_timer_p1 <= 0:
                    if player1.name == 'scorpion':
                        screen.blit(scorpion_wins, (300, 110))
                        if fatality_timer_p1 == 0:
                            scorpion_wins_snd.play()
                    elif player1.name == 'sub-zero':
                        screen.blit(sub_zero_wins, (300, 110))
                        if fatality_timer_p1 == 0:
                            sub_zero_wins_snd.play()                        
                    if fatality_timer_p1 <= -140:
                        return
                else:
                    if snd1:
                        finish_him_snd.play()
                        snd1 = False
                    screen.blit(finish_him, (300, 150))
        
        elif p2_win:
            
            p2_image = player2.stand
            p1_image = player1.finish
            
            player1_x = 300
            player2_x = 900
            
            if pressed_left and pressed_up and pressed_right and fatality_timer_p2 > 0:
                fatality_p2 = True
                
                
            if fatality_p2:
                if player2.name == 'scorpion':
                    frame = 'frame' + str(int(frm2 // 10)) + '.png'
                    frm2 += 1
                    
                    if frm2 // 10 <= 9:
                        screen.blit(p1_image, (int(player1_x), int(player1_y)))                    
                    
                    if frm2 <= 119:
                        img = pygame.image.load(os.path.join('data\scorpion', frame))
                    
                    if frm2 >= 109:
                        screen.blit(fatality, (300, 110))
                        screen.blit(scorpion_wins, (300, 110))   
                        
                    if frm2 == 108:
                        fatality_snd.play()
                            
                    if frm2 == 148:
                        scorpion_wins_snd.play()  
                        
                    if frm2 == 40:
                        sc_fat1.play()
                            
                    if frm2 == 80:
                        sc_fat2.play()                    
                            
                    screen.blit(pygame.transform.flip(img, True, False), (300, 50))
                    
                    if frm2 >= 300:
                        return
                    
                elif player2.name == 'sub-zero':
                    frame = 'frame' + str(int(frm2 // 10)) + '.png'
                    frm2 += 1
                    
                    if frm2 // 10 <= 7:
                        screen.blit(p1_image, (int(player1_x), int(player1_y)))                    
                    
                    if frm2 <= 129:
                        img = pygame.image.load(os.path.join('data\sub-zero', frame))
                    
                    if frm2 >= 119:
                        screen.blit(fatality, (300, 110))
                        screen.blit(sub_zero_wins, (300, 110))   
                        
                    if frm2 == 118:
                        fatality_snd.play()
                            
                    if frm2 == 158:
                        sub_zero_wins_snd.play()  
                        
                    if frm2 == 40:
                        sz_fat1.play()
                            
                    if frm2 == 115:
                        sz_fat2.play()                    
                    
                    screen.blit(pygame.transform.flip(img, True, False), (300, 50))
                    
                    if frm2 >= 310:
                        return                    
                    
            else:
                fatality_timer_p2 -= 1
                if fatality_timer_p2 <= 0:
                    if player2.name == 'scorpion':
                        screen.blit(scorpion_wins, (300, 110))
                        if fatality_timer_p2 == 0:
                            scorpion_wins_snd.play()                        
                    elif player2.name == 'sub-zero':
                        screen.blit(sub_zero_wins, (300, 110))  
                        if fatality_timer_p2 == 0:
                            scorpion_wins_snd.play()                        
                    if fatality_timer_p2 <= -140:
                        return 
                    
                else:
                    if snd2:
                        finish_him_snd.play()
                        snd2 = False                    
                    screen.blit(finish_him, (300, 150))
        
        else:
            
            dmg_p1 = 0
            dmg_p2 = 0
             
            shift = 0
            
            if player2_health <= 0:
                player2_health = 0
                p1_win = True
            
            if player1_health <= 0:
                player1_health = 0
                p2_win = True        
            
            if cd_p1 > 0:
                cd_p1 -= 1
                
            if cd_p2 > 0:
                cd_p2 -= 1
            
            if pressed_p and not p2_inv:
                p2_blocked = True
                
            if pressed_y and not p1_inv:
                p1_blocked = True
            
            if stun_p1:
                stop_p1 = True
                punch_p1 = False
                kombo_p1 = False
                p1_blocked = False
                p1_ability = False
                p1_image = player1.finish
                stun_timer_p1 -= 1
                if stun_timer_p1 <= 0:
                    stun_p1 = False
                    p1_image = player1.stand
                    stop_p1 = False
                 
            if stun_p2:
                stop_p2 = True
                punch_p2 = False
                kombo_p2 = False
                p2_blocked = False
                p2_ability = False
                p2_image = player2.finish
                stun_timer_p2 -= 1
                if stun_timer_p2 <= 0:
                    stun_p2 = False
                    p2_image = player2.stand
                    stop_p2 = False               
                    
            if frozen_p1:
                stop_p1 = True
                punch_p1 = False
                kombo_p1 = False
                p1_blocked = False
                p1_image = player1.frozen
                freeze_time_p1 -= 1
                if freeze_time_p1 <= 0:
                    frozen_p1 = False
                    p1_image = player1.stand
                    stop_p1 = False
                    
            if frozen_p2:
                shift = 70
                stop_p2 = True
                punch_p2 = False
                kombo_p2 = False
                p2_blocked = False
                p2_image = player2.frozen
                freeze_time_p2 -= 1
                if freeze_time_p2 <= 0:
                    frozen_p2 = False
                    p2_image = player2.stand
                    stop_p2 = False  
                    shift = 0
             
            if p1_ability == True:
                stop_p1 = True
                punch_p1 = False
                kombo_p1 = False
                p1_blocked = False
                
                
                if player1.name == 'scorpion' and not frozen_p1 and not p1_inv:
                    p1_image = player1.ability
                    
                    if snd1:
                        player1.ability_sound.play()
                        snd1 = False
                    
                    if projectile_x_p1 >= player2_x:
                        if (p2_blocked or p2_inv) and not hooked_p2:
                            p1_ability = False
                            stop_p1 = False
                            p1_image = player1.stand
                            projectile_x_p1 = 0
                            cd_p1 = 100
                        elif projectile_x_p1 > player1_x + 270:
                            p2_image = player2.inv
                            hooked_p2 = True
                            stop_p2 = True
                            punch_p2 = False
                            kombo_p2 = False
                            p2_blocked = False
                            p2_ability = False
                            projectile_x_p1 -= 800 / fps
                            player2_x = projectile_x_p1 - 100
                        else:
                            stop_p1 = False 
                            stop_p2 = False
                            hooked_p2 = False
                            p1_ability = False
                            p1_image = player1.stand
                            p2_image = player2.stand
                            stun_p2 = True
                            stun_timer_p2 = 150
                            if not p2_inv:
                                dmg_p2 += 2
                            cd_p1 = 200
                            snd1 = True
                            
                    else:
                        projectile_x_p1 += 800 / fps             
                
                elif player1.name == 'sub-zero' and not frozen_p2 and not frozen_p1 and not p1_inv:
                    p1_image = player1.ability
                    shift = 0
                    
                    if snd1:
                        player1.ability_sound.play()
                        snd1 = False                    
                    
                    if projectile_x_p1 >= player2_x:
                        if (p2_blocked or p2_inv) and not frozen_p2:
                            p1_ability = False
                            stop_p1 = False
                            p1_image = player1.stand
                            projectile_x_p1 = 0
                            cd_p1 = 100
                        elif not frozen_p2:
                            p2_image = player2.frozen
                            stop_p2 = True
                            punch_p2 = False
                            kombo_p2 = False
                            p2_blocked = False
                            p2_ability = False
                            
                            frozen_p2 = True
                            p1_ability = False
                            stop_p1 = False
                            shift = 0
                            p1_image = player1.stand
                            freeze_time_p2 = 200
                            dmg_p2 += 2
                            cd_p1 = 200
                            snd1 = True
                                        
                    else:
                        projectile_x_p1 += 800 / fps                    
                
                else: 
                    p1_ability = False        
                
                
                
            if p2_ability == True:
                stop_p2 = True
                punch_p2 = False
                kombo_p2 = False
                p2_blocked = False
                
                
                if player2.name == 'scorpion' and not frozen_p2 and not p2_inv:
                    p2_image = player2.ability
                    shift = 40
                    
                    if snd2:
                        player2.ability_sound.play()
                        snd2 = False                    
                    
                    if projectile_x_p2 <= player1_x + 190:
                        if (p1_blocked or p1_inv) and not hooked_p1:
                            p2_ability = False
                            stop_p2 = False
                            p2_image = player2.stand
                            projectile_x_p2 = 0
                            cd_p2 = 100
                        elif projectile_x_p2 < player2_x - 70:
                            p1_image = player1.inv
                            stop_p1 = True
                            hooked_p1 = True
                            punch_p1 = False
                            kombo_p1 = False
                            p1_blocked = False
                            p1_ability = False
                            projectile_x_p2 += 800 / fps
                            player1_x = projectile_x_p2 - 100
                        else:
                            stop_p2 = False 
                            stop_p1 = False
                            p2_ability = False
                            hooked_p1 = False
                            p2_image = player2.stand
                            p1_image = player1.stand
                            stun_p1 = True
                            stun_timer_p1 = 150
                            shift = 0
                            if not p1_inv:
                                dmg_p1 += 2
                            cd_p2 = 200
                            snd2 = True
                                        
                    else:
                        projectile_x_p2 -= 800 / fps  
                        
                        
                        
                elif player2.name == 'sub-zero' and not frozen_p1 and not frozen_p2 and not p2_inv:
                    p2_image = player2.ability
                    shift = 0
                    
                    if snd2:
                        player2.ability_sound.play()
                        snd2 = False                    
                    
                    if projectile_x_p2 <= player1_x + 190:
                        if (p1_blocked or p1_inv) and not frozen_p1:
                            p2_ability = False
                            stop_p2 = False
                            p2_image = player2.stand
                            projectile_x_p2 = 0
                            cd_p2 = 100
                        elif not frozen_p1:
                            p1_image = player1.frozen
                            stop_p1 = True
                            punch_p1 = False
                            kombo_p1 = False
                            p1_blocked = False
                            p1_ability = False
                            
                            frozen_p1 = True
                            p2_ability = False
                            stop_p2 = False
                            shift = 0
                            p2_image = player2.stand
                            freeze_time_p1 = 200
                            dmg_p1 += 2
                            cd_p2 = 200
                            snd2 = True
                                        
                    else:
                        projectile_x_p2 -= 800 / fps            
                   
                else: 
                    p2_ability = False
             
            if p1_blocked and not hooked_p1:
                stop_p1 = True
                punch_p1 = False
                kombo_p1 = False
                              
            if p2_blocked and not hooked_p2:
                stop_p2 = True   
                punch_p2 = False
                kombo_p2 = False        
                                    
            if kombo_time_p1:
                kombo_time_p1 -= 1
            
            if punch_p1 and not p1_inv: 
                if snd1:
                    punch.play()
                    snd1 = False
                if timer1 >= 5:
                    p1_image = player1.punch1
                else:
                    p1_image = player1.punch2
                timer1 -= 1
                if timer1 == 0:
                    stop_p1 = False
                    p1_image = player1.stand
                    punch_p1 = False
                    if player1_x + 220 >= player2_x and not p2_inv:
                        freeze_time_p2 = 0
                        dmg_p2 += 3
                    snd1 = True
            
            if kombo_p1 and not p1_inv:
                if snd1:
                    punch.play()
                    snd1 = False                
                if ktimer_p1 >= 10:
                    p1_image = player1.kombo1
                else:
                    p1_image = player1.kombo2
                ktimer_p1 -= 1
                if ktimer_p1 == 0:
                    stop_p1 = False
                    p1_image = player1.stand
                    kombo_p1 = False
                    snd1 = True
                    if player1_x + 210 >= player2_x and not p2_inv:
                        dmg_p2 += 5
                        stun_timer_p2 = 0
                        p2_inv_timer = 50
                        p2_inv = True
            
            if pressed_d and not stop_p1:
                player1_x += 200 / fps
                if 0 < ww % 20 <= 5:
                    p1_image = player1.walk1
                elif 5 < ww % 20 <= 10:
                    p1_image = player1.walk2
                elif 10 < ww % 20 <= 15:
                    p1_image = player1.walk3
                else:
                    p1_image = player1.walk4
                ww += 1        
                        
            if pressed_a and not stop_p1:
                player1_x -= 200 / fps
                if 0 < ww % 20 <= 5:
                    p1_image = player1.walk1
                elif 5 < ww % 20 <= 10:
                    p1_image = player1.walk2
                elif 10 < ww % 20 <= 15:
                    p1_image = player1.walk3
                else:
                    p1_image = player1.walk4
                ww -= 1            
               
            if player1_x < 10:
                player1_x = 10
                
            if player1_x > 1030:
                player1_x = 1030    
                
            if player1_x > player2_x - 170:
                player1_x = player2_x - 170      
                 
            # player 2
            
            if pressed_right and not stop_p2:
                player2_x += 200 / fps
                if 0 < ww2 % 20 <= 5:
                    p2_image = player2.walk1
                elif 5 < ww2 % 20 <= 10:
                    p2_image = player2.walk2
                elif 10 < ww2 % 20 <= 15:
                    p2_image = player2.walk3
                else:
                    p2_image = player2.walk4
                ww2 += 1       
                 
            if pressed_left and not stop_p2:
                player2_x -= 200 / fps
                if 0 < ww2 % 20 <= 5:
                    p2_image = player2.walk1
                elif 5 < ww2 % 20 <= 10:
                    p2_image = player2.walk2
                elif 10 < ww2 % 20 <= 15:
                    p2_image = player2.walk3
                else:
                    p2_image = player2.walk4
                ww2 -= 1    
                 
            if player2_x > 1200:
                player2_x = 1200
                
            if player2_x < 160:
                player2_x = 160    
                
            if player2_x < player1_x + 170:
                player2_x = player1_x + 170     
                 
            if kombo_time_p2:
                kombo_time_p2 -= 1
              
                
            if punch_p2 and not p2_inv:
                if snd2:
                    punch.play()
                    snd2 = False                
                if timer2 >= 5:
                    p2_image = player2.punch1
                    shift = 20
                else:
                    p2_image = player2.punch2
                    shift = 50
                timer2 -= 1
                if timer2 == 0:
                    stop_p2 = False
                    p2_image = player2.stand
                    punch_p2 = False
                    shift = 0
                    if player1_x + 220 >= player2_x and not p1_inv:
                        freeze_time_p1 = 0
                        dmg_p1 += 3
                    snd2 = True
                        
                
            if kombo_p2 and not p2_inv:
                if snd1:
                    punch.play()
                    snd1 = False                
                if ktimer_p2 >= 10:
                    p2_image = player2.kombo1
                    shift = 20
                else:
                    p2_image = player2.kombo2
                    shift = 20
                ktimer_p2 -= 1
                if ktimer_p2 == 0:
                    stop_p2 = False
                    p2_image = player2.stand
                    kombo_p2 = False 
                    shift = 0
                    snd2 = True
                    if player1_x + 210 >= player2_x and not p1_inv:
                        dmg_p1 += 5
                        stun_timer_p1 = 0
                        p1_inv_timer = 50
                        p1_inv = True
              
              
              
            if p1_blocked and not hooked_p1:
                p1_image = player1.block
                if dmg_p1 != 0:
                    dmg_p1 = 1
                p1_inv = False
                        
            if p2_blocked and not hooked_p2:
                p2_image = player2.block
                if dmg_p2 != 0:
                    dmg_p2 = 1
                p2_inv = False
               
            if p1_inv:
                p1_inv_timer -= 1
                player1_x -= 300 / fps
                p1_image = player1.inv
                stop_p1 = True
                if p1_inv_timer == 0:
                    p1_inv = False
                    p1_image = player1.stand 
                    stop_p1 = False    
                 
            if p2_inv:
                shift = 70
                p2_inv_timer -= 1
                stop_p2 = True
                player2_x += 300 / fps
                p2_image = player2.inv
                if p2_inv_timer == 0:
                    p2_inv = False
                    p2_image = player2.stand
                    stop_p2 = False    
            
            player1_health -= dmg_p1
            
            player2_health -= dmg_p2    
                         
            if p1_ability and player1.name == 'scorpion':
                screen.blit(player1.spear, (int(projectile_x_p1), 448))
                pygame.draw.rect(screen, (156, 156, 156), (player1_x + 200, 455, projectile_x_p1 - player1_x - 200, 10), 0)
            
            elif p1_ability and player1.name == 'sub-zero':
                screen.blit(player1.ice_ball, (int(projectile_x_p1), 460))    
                
                
            if p2_ability and player2.name == 'scorpion':
                screen.blit(pygame.transform.flip(player2.spear, True, False), (int(projectile_x_p2), 448))
                pygame.draw.rect(screen, (156, 156, 156), (75 + projectile_x_p2, 455, player2_x - projectile_x_p2 - 50, 10), 0)
                
            elif p2_ability and player2.name == 'sub-zero':
                screen.blit(pygame.transform.flip(player2.ice_ball, True, False), (int(projectile_x_p2), 460))
           
        
                
        pygame.draw.rect(screen, (255, 0, 0), (50, 50, 500, 50), 0)
        pygame.draw.rect(screen, (255, 0, 0), (850, 50, 500, 50), 0)
        
        pygame.draw.rect(screen, p1_hp_color, (50, 50, player1_health * 5, 50), 0)
        pygame.draw.rect(screen, p2_hp_color, (850 + (100 - player2_health) * 5, 50, player2_health * 5, 50), 0)
        
        screen.blit(player1.name_player1, (50, 50))
        screen.blit(player2.name_player2, (850, 50))    
        
        if not fatality_p1 and not fatality_p2:
            screen.blit(p1_image, (int(player1_x), int(player1_y)))
            screen.blit(pygame.transform.flip(p2_image, True, False), (int(player2_x) - shift, int(player2_y)))
        
        pygame.display.flip()
        clock.tick(fps)
    
    if quit:
        pygame.quit()
  
#game_loop()
    
maps_menu = False
chars_menu = False  
is_menu = True
char1 = None
char2 = None
frame_p1 = 1
frame_p2 = 5
frame_map_p1 = 1
frame_map_p2 = 5
current_map = fizmat

while is_menu:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            is_menu = False
            
        if event.type == pygame.MOUSEBUTTONUP:
            (x, y) = event.pos
            if 484 <= x <= 878 and 336 <= y <= 432 and event.button == 1 and not chars_menu and not maps_menu:
                chars_menu = True
                
            elif 554 <= x <= 816 and 506 <= y <= 600 and event.button == 1 and not chars_menu and not maps_menu:
                is_menu = False
                
            elif 400 <= x <= 585 and 470 <= y <= 653 and event.button == 1 and maps_menu:
                current_map = outworld  
                
            elif 619 <= x <= 804 and 470 <= y <= 653 and event.button == 1 and maps_menu:
                current_map = fizmat           
                
            elif 834 <= x <= 1019 and 470 <= y <= 653 and event.button == 1 and maps_menu:
                current_map = Almaty          
            
            elif 179 <= x <= 365 and 470 <= y <= 653 and event.button == 1 and maps_menu:
                current_map = google
            
            elif 1053 <= x <= 1239 and 470 <= y <= 653 and event.button == 1 and maps_menu:
                current_map = arena
                
            elif not chars_menu and not maps_menu and event.button == 2:
                you_suck.play()
                
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE and char1 != None and char2 != None:
                if chars_menu:
                    chars_menu = False
                    maps_menu = True
                    
                elif maps_menu:
                    game_loop(char1, char2, current_map)
                    maps_menu = False
                    char1 = None
                    char2 = None
            
            if event.key == pygame.K_ESCAPE:
                if chars_menu:
                    chars_menu = False
                    char1 = None
                    char2 = None
                    frame_p1 = 1
                    frame_p2 = 5
                
                elif maps_menu:
                    maps_menu = False
                    chars_menu = True                    
                
            if event.key == pygame.K_d and chars_menu:
                frame_p1 += 1
                if frame_p1 > 5:
                    frame_p1 = 5
                    
            if event.key == pygame.K_a and chars_menu:
                frame_p1 -= 1
                if frame_p1 < 1:
                    frame_p1 = 1  
                    
            if event.key == pygame.K_t and chars_menu:
                if frame_p1 == 1 and char1 == None:
                    char1 = Scorpion()
                    scorpion.play()
                
                elif frame_p1 == 2:
                    pass
                
                elif frame_p1 == 3 and char1 == None:
                    if random.randint(0, 1) == 1:
                        char1 = Sub_zero()
                        sub_zero.play()
                    else:
                        char1 = Scorpion()
                        scorpion.play()
                        
                elif frame_p1 == 4:
                    pass
                
                elif frame_p1 == 5 and char1 == None:
                    char1 = Sub_zero() 
                    sub_zero.play()
                    
            if event.key == pygame.K_y and chars_menu:
                char1 = None
                    
            if event.key == pygame.K_RIGHT and chars_menu:
                frame_p2 += 1
                if frame_p2 > 5:
                    frame_p2 = 5
                            
            if event.key == pygame.K_LEFT and chars_menu:
                frame_p2 -= 1
                if frame_p2 < 1:
                    frame_p2 = 1
                    
            if event.key == pygame.K_o and chars_menu:
                if frame_p2 == 1 and char2 == None:
                    char2 = Scorpion()
                    scorpion.play()
                
                elif frame_p2 == 2:
                    pass
                
                elif frame_p2 == 3 and char2 == None:
                    if random.randint(0, 1) == 1:
                        char2 = Sub_zero()
                        sub_zero.play()
                    else:
                        char2 = Scorpion()
                        scorpion.play()
                    
                elif frame_p2 == 4:
                    pass
                
                elif frame_p2 == 5 and char2 == None:
                    char2 = Sub_zero() 
                    sub_zero.play()
                            
            if event.key == pygame.K_p and chars_menu:
                char2 = None            
                        
    

    if chars_menu:
        maps_menu = False
        screen.blit(characters_menu, (0, 0))
        if char1 != None:
            screen.blit(char1.stand, (200, 100))
            
        if char2 != None:
            screen.blit(pygame.transform.flip(char2.stand, True, False), (930, 100))    
            
        screen.blit(characters, (0, 0))
        
        if char1 == None:
            if frame_p1 == 1:
                screen.blit(frame1, (179, 470))
            elif frame_p1 == 2:
                screen.blit(frame1, (400, 470))
            elif frame_p1 == 3:
                screen.blit(frame1, (619, 470))
            elif frame_p1 == 4:
                screen.blit(frame1, (834, 470))
            elif frame_p1 == 5:
                screen.blit(frame1, (1053, 470))     
                
        if char2 == None:
            if frame_p2 == 1:
                screen.blit(frame2, (179, 470))
            elif frame_p2 == 2:
                screen.blit(frame2, (400, 470))
            elif frame_p2 == 3:
                screen.blit(frame2, (619, 470))
            elif frame_p2 == 4:
                screen.blit(frame2, (834, 470))
            elif frame_p2 == 5:
                screen.blit(frame2, (1053, 470))        
        
    elif maps_menu:
        chars_menu = False
        screen.blit(current_map, (0, 0))
        screen.blit(maps, (0, 0))
        
    elif is_menu:
        chars_menu = False
        maps_menu = False
        screen.blit(menu, (0, 0))
    
    pygame.display.flip()
            
pygame.quit()