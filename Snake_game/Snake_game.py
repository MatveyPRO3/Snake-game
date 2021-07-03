import pygame
import random
import time

pygame.init()
pygame.mixer.init()

width = 1200
height = 800

display  = pygame.display.set_mode((width,height))

pygame.display.update()
pygame.display.set_caption("Snake_game")
Icon = pygame.image.load("Icon_for_snake_game.ico")
pygame.display.set_icon(Icon)

game_end = False

clock = pygame.time.Clock()

def clicksound():
    pygame.mixer.music.load("a.mp3")
    pygame.mixer.music.play(loops=0)
colors = {
    "snake_head": (0,255,0),
    "snake_tail": (0,200,0),
    "apple": (255,0,0)
}

snake_pos = {
    "x": width/2-5,
    "y": height/2-5,
    "x_change": 0,
    "y_change": 0
}

snake_size = (10,10)

Pause = False

food_pos = {
    "x": round(random.randrange(0,width - snake_size[0]) / 10)*10,
    "y": round(random.randrange(0,height - snake_size[1]) / 10)*10

}

snake_speed = 10

snake_tails = []



font = pygame.font.SysFont("arial",20)

font_for_pause = pygame.font.SysFont("arial",20)

food_size = (10,10)
food_eaten = 0
score = font.render(str(food_eaten),1,(255,255,0),(150,150,150))




def check_KEYDOWN_events(event):
    if event.key == pygame.K_a and snake_pos["x_change"] == 0:
        snake_pos["x_change"] = -snake_speed
        snake_pos["y_change"] = 0       
    elif event.key == pygame.K_d and snake_pos["x_change"] == 0:
        snake_pos["x_change"] = snake_speed
        snake_pos["y_change"] = 0
    elif event.key == pygame.K_w and snake_pos["y_change"] == 0:
        snake_pos["x_change"] = 0
        snake_pos["y_change"] = -snake_speed
    elif event.key == pygame.K_s and snake_pos["y_change"] == 0:
        snake_pos["x_change"] = 0
        snake_pos["y_change"] = snake_speed 
    

Game_over = False

while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True
        elif event.type == pygame.KEYDOWN:
            check_KEYDOWN_events(event)
       

    display.fill((0,0,0))

    ltx = snake_pos["x"]
    lty = snake_pos["y"]

    for i,v in enumerate(snake_tails):
        _ltx = snake_tails[i][0]
        _lty = snake_tails[i][1]

        snake_tails[i][0] = ltx
        snake_tails[i][1] = lty

        ltx = _ltx
        lty = _lty
    for t in snake_tails:
        pygame.draw.rect(display,colors["snake_tail"],[
            t[0],
            t[1],
            snake_size[0],
            snake_size[1]
            ])    
    snake_pos["x"] += snake_pos["x_change"]
    snake_pos["y"] += snake_pos["y_change"] 

    if snake_pos["x"] < -snake_size[0]:
        snake_pos["x"] = width
    elif snake_pos["x"] > width:
        snake_pos["x"] = 0
    elif snake_pos["y"] < -snake_size[1]:
        snake_pos["y"] = height
    elif snake_pos["y"] > height:
        snake_pos["y"] = 0

    pygame.draw.rect(display, colors["snake_head"], [
        snake_pos["x"],
        snake_pos["y"],
        snake_size[0],
        snake_size[1]
        ])

    pygame.draw.rect(display,colors["apple"],[
        food_pos["x"],
        food_pos["y"],
        food_size[0],
        food_size[1]
    ])

    if (snake_pos["x"] == food_pos["x"]
        and snake_pos["y"] == food_pos["y"]):
        food_eaten+=1
        clicksound()
        snake_tails.append([food_pos["x"],food_pos["y"]])
        food_pos = {
            "x": round(random.randrange(0,width-snake_size[0]) / 10)*10,
            "y": round(random.randrange(0,height-snake_size[1]) / 10)*10
        }

    for i,v in enumerate (snake_tails):
        if(snake_pos["x"]+snake_pos["x_change"] == snake_tails[i][0]
            and snake_pos["y"] + snake_pos["y_change"] == snake_tails[i][1]):
            snake_tails = []
            food_eaten = 0
            break
    if Pause:
        Pause = font.render("PAUSE",1,(0,255,0),(0,0,0))
        display.blit(score,(0,0))
    
    score = font.render("Score: "+str(food_eaten),1,(255,255,0),(0,0,0))
    display.blit(score,(50,50))
    pygame.display.update()


    clock.tick(30)

pygame.quit()
quit()