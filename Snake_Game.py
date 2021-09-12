# Snake? Snaaaaaaake!
import pygame
import time
import random
pygame.init()

#colors
background = (250,223,173)
snake = (0,192,163)
food = (205,25,25)
type_color = (255, 170, 200)

#window details
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake Game by Griffyboi")

#snake body
def ourSnake(block, snakeList):
    for x in snakeList:
        pygame.draw.rect(dis, snake, [x[0], x[1], block, block])

#font
font_style = pygame.font.SysFont(None, 50)

#message positions
position = {'loser': [20, 150], 'endGame': [20, 200], 'highScores': [20, 300], 'score1': [20, 350], 'score2': [20, 400], 'score3': [20,450], 'scoreCounter': [10, 10]}

def messages(msg, color, pos):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, position[pos])

#game loop and variabes
def gameLoop():
    game_over = False
    game_lose = False
    write_score = False
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0
    block = 10
    length = 1
    score = 0
    snakeList = []
    scoreList = []

    #food
    foodx = round(random.randrange(0, dis_width - block)/10)*10
    foody = round(random.randrange(0, dis_height - block)/10)*10

    #speeds
    clock = pygame.time.Clock()
    snake_speed = 30

    #main while loops
    while not game_over:

        while game_lose:

            while not write_score:

                #write high scores
                scoreFile = open("Highscores.txt", "a")
                scoreFile.writelines(str(score) + "\n")
                write_score = True

            #read high scores
            scoreFile = open("Highscores.txt", "r")
            scoreList = scoreFile.readlines()
            for i in range(0, len(scoreList)):
                scoreList[i] = int(scoreList[i])
            scoreList.sort()
            scoreList.reverse()

            #message content
            text = ['Loser.', 'Press Any Key to try again or ESC to quit.', 'High Scores:', str(scoreList[0]), str(scoreList[1]), str(scoreList[2]), 'Score:']

            pygame.display.update()

            #message for-loop
            for (words, keys) in zip(text, position):
                messages(words, type_color, keys)

            pygame.display.update()

            #game over input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_lose = False
                    else:
                        gameLoop()

        #keybindings
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_lose = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = 10
                elif event.key == pygame.K_ESCAPE:
                    game_over = True
                    game_lose = False

        #failstate
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_lose = True

        #location of snake
        x1 += x1_change
        y1 += y1_change

        #draw to display
        dis.fill(background)
        pygame.draw.rect(dis, food, [foodx, foody, block, block])
        pygame.draw.rect(dis, snake,[x1, y1, block, block])
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)

        #snake length
        if len(snakeList) > length:
            del snakeList[0]

        for x in snakeList[:-1]:
            if x == snakeHead:
                game_lose = True

        #snake details
        ourSnake(block, snakeList)

        #food and score counters
        messages("Score: "+str(score), type_color, 'scoreCounter')
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - block)/10)*10
            foody = round(random.randrange(0, dis_height - block)/10)*10
            length += 1
            score += 1

        pygame.display.update()
        clock.tick(snake_speed)

    #playthrough terminus
    pygame.quit()
    quit()

gameLoop()
scoreFile.close()


# OLD CODE

# scoreList = [scores.strip('\n') for scores in scoreList]

# def scoreboard(msg, color, dis_width, dis_height):
#     msg = font_style.render(msg, True, color)
#     dis.blit(msg, [10, 10])

# def loser(msg, color):
#     msg = font_style.render(msg, True, color)
#     dis.blit(msg, [20, 150])

# def endgame(msg, color):
#     msg = font_style.render(msg, True, color)
#     dis.blit(msg, [20, 200])

# def highScores(msg, color):
#     msg = font_style.render(msg, True, color)
#     dis.blit(msg, [20, 300])

# def score1(msg, color):
#     msg = font_style.render(msg, True, color)
#     dis.blit(msg, [20, 350])

# def score2(msg, color):
#     msg = font_style.render(msg, True, color)
#     dis.blit(msg, [20, 400])

# def score3(msg, color):
#     msg = font_style.render(msg, True, color)
#     dis.blit(msg, [20, 450])

# display on game over
# messages("Loser.", type_color, 'loser')
# messages("Press Any Key to try again or ESC to quit.", type_color, 'endGame')
# messages("High Scores:", type_color, 'highScores')
# messages(str(scoreList[0]), type_color, 'score1')
# messages(str(scoreList[1]), type_color, 'score2')
# messages(str(scoreList[2]), type_color, 'score3')
