import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Define the menu items
menu_items = ["Start Game", "Options", "Quit"]
selected_item = 0

# Function to draw the menu items on the screen
def draw_menu():
    screen.fill(WHITE)
    for index, item in enumerate(menu_items):
        text = font.render(item, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + index * 50))
        if index == selected_item:
            pygame.draw.rect(screen, BLACK, text_rect, 2)
        screen.blit(text, text_rect)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item = (selected_item - 1) % len(menu_items)
            elif event.key == pygame.K_DOWN:
                selected_item = (selected_item + 1) % len(menu_items)
            elif event.key == pygame.K_RETURN:
                if selected_item == 0:
                    print("Starting game...")
                    # Add your game code here for starting the game
                elif selected_item == 1:
                    print("Opening options...")
                    # Add your code here for opening the options menu
                elif selected_item == 2:
                    print("Quitting game...")
                    running = False
                    pygame.quit()
                    sys.exit()

    draw_menu()
    pygame.display.update()
    
    
import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Define the menu items
menu_items = ["Start Game", "Options", "Quit"]
selected_item = 0

# Function to draw the menu items on the screen
def draw_menu():
    screen.fill(WHITE)
    for index, item in enumerate(menu_items):
        text = font.render(item, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + index * 50))
        if index == selected_item:
            pygame.draw.rect(screen, BLACK, text_rect, 2)
        screen.blit(text, text_rect)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item = (selected_item - 1) % len(menu_items)
            elif event.key == pygame.K_DOWN:
                selected_item = (selected_item + 1) % len(menu_items)
            elif event.key == pygame.K_space:
              import time

            import random
            pygame.font.init()
            WIDTH, HEIGHT = 800,500
            WIN = pygame.display.set_mode((WIDTH,HEIGHT))
            pygame.display.set_caption("YAHYA SPACE DODGE") 


            BG = pygame.transform.scale(pygame.image.load("sky.jpg"),(WIDTH,HEIGHT))

PLAYER_WIDTH = 30  
PLAYER_HEIGHT = 40
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("cosmics",40)


def draw(player, elapsed_time,stars):
    WIN.blit(BG, (0,0))
    
    time_text = FONT.render(f"Time:{round(elapsed_time)}s" ,1 , "yellow")
    WIN.blit(time_text, (10, 10))
    pygame.draw.rect(WIN,"red", player)
    for star in stars:
        pygame.draw.rect(WIN,"white",star)
    
    pygame.display.update()
    
def main():
    run = True
    
    player = pygame.Rect(200 , HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    
    star_add_increment = 2000
    star_count = 0
    
    stars = []
    hit = False
    
    while run:
        star_count +=  clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > star_add_increment:
            for _ in range(3):
               star_x = random.randint(0,WIDTH - STAR_WIDTH)
               star = pygame.Rect(star_x,-STAR_HEIGHT,STAR_WIDTH,STAR_HEIGHT)
               stars.append(star)   
               
            star_add_increment = max(200,star_add_increment - 50)
            star_count = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >=0:
            player.x -= PLAYER_VEL 
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL +player.width <= WIDTH:
            player.x += PLAYER_VEL 
            
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
            
        if hit:
            lost_text  = FONT.render("You Lost!!", 3, "yellow")
            WIN.blit(lost_text,(WIDTH/2 - lost_text.get_width()/2,HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)
            break               
        draw(player,elapsed_time,stars)
        
    pygame.quit()

if __name__== "__main__":
    main()

                    
    pygame.display.update()
    

