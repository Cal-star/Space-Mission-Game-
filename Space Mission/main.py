import pygame
import time
import random

WIDTH = 1000
HEIGHT = 800
PLAYER_VELOCITY =  5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Mission")
BG = pygame.transform.scale(pygame.image.load('bg.jpeg'), (WIDTH, HEIGHT))
player = pygame.transform.scale(pygame.image.load('rocket.jpeg'), (40, 50))
player_rect = player.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.y = HEIGHT - player.get_height()
FPS = 60
clock = pygame.time.Clock()
enemies = []
ENEMY_VELOCITY = 3
pygame.font.init() #intializing the font module
FONT = pygame.font.SysFont('comicsans', 30) #setting the font style

def draw(elapsed_time):
    screen.blit(BG, (0, 0)) #background setting
    time_text = FONT.render(f'Time: {round(elapsed_time)}s', 1, 'white')
    screen.blit(time_text, (10, 10)) 
    screen.blit(player, player_rect) #drwaing player
    for enemy, enemy_rect in enemies:
        screen.blit(enemy, enemy_rect)
    pygame.display.update()
    
def main():
    enemy_add_increment = 2000
    enemy_count = 0
    run = True
    hit = False
    start_time = time.time()
    
    while run:
        enemy_count += clock.tick(FPS)
        elapsed_time = time.time() - start_time 
        if enemy_count > enemy_add_increment:
            for _ in range(3):
                enemy = pygame.transform.scale(pygame.image.load('space shuttle.jpeg'), (30, 40))
                enemy_rect = enemy.get_rect()
                enemy_rect.x = random.randint(0, WIDTH - enemy.get_width())
                enemy_rect.y = -enemy.get_height()
                enemies.append((enemy, enemy_rect))
            
            enemy_add_increment = max(200, enemy_add_increment - 50)
            enemy_count = 0
                
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        for enemy, enemy_rect in enemies[:]:  # copy of the list for safe removal
            enemy_rect.y += ENEMY_VELOCITY  # move enemy down
            if enemy_rect.y > HEIGHT:
                enemies.remove((enemy, enemy_rect))
            elif enemy_rect.inflate(-10, -10).colliderect(player_rect.inflate(-5, -5)):
                enemies.remove((enemy, enemy_rect))
                hit = True
                break

        if hit:
            lost_text = FONT.render('You Lost!', 1, 'white')
            screen.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        
        draw(elapsed_time)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.x - PLAYER_VELOCITY >= 0:
            player_rect.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player_rect.x + PLAYER_VELOCITY + player_rect.width <= WIDTH:
            player_rect.x += PLAYER_VELOCITY
    pygame.quit()


        
if __name__ == '__main__':
    main()