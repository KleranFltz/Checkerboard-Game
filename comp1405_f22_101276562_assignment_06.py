# Kieran Fitzgerald 101276562

#this game has exact requirements, numbered tiles, snake connections, and double moves

import pygame
import random

#create a function for rolling dice that returns a single value
def roll():
    a = random.randint(1,6)
    b = random.randint(1,6)
    ans = a + b
    print("your roll was "+str(ans))
    if a == b:
        print("You rolled snake eyes, you get to roll again!")
        return (roll() + (ans))
    return ans

def calc_row(playerposition):
    row = 0
    while (playerposition - 11) > 0:
        playerposition = playerposition - 11
        row = row + 1
    return row

def calc_column(playerposition):
    if (playerposition % 11) == 0:
        column = 10
    else:
        column = (playerposition % 11) - 1
    return column

pygame.init()

window = pygame.display.set_mode((374,450))

window.fill((255,255,255))

font = pygame.font.Font('freesansbold.ttf',10)

#create a while loop that terminates when either player reaches the end

player1 = 1
player2 = 1
add2 = 0
endy = False
turn = 1

while endy == False:
    pygame.display.update()
    const = 0
    #determines the turn (if odd number player1, if even number player2)
    if (turn % 2) == 1:
        add1 = roll()
        newpos1 = player1 + add1
        if newpos1 > 110:
            print("You cannot pass the end of the board, you will have to roll again on your next turn.")
            newpos1 = newpos1 - add1
        else:
            player1 = newpos1
    else:
        add2 = roll()
        newpos2 = player2 + add2
        if newpos2 > 110:
            print("you cannot pass the end of the board, you will have to roll again on your next turn.")
            newpos2 = newpos2 - add2
        else:
            player2 = newpos2
    #draw a checkerboard pattern for the game using nested for loops and displaying numbers on each square
    window.fill((255,255,255))
    for i in range(10):
        for j in range(11):
            #draws checkerboard pattern on the entire window 18x42 grid        
            pygame.draw.rect(window,(0,0,0),(j*34,i*34,34,34),3)
            #draws a number correlating to each square
            text = font.render(str(j+1+const),True,(0,0,0),(255,255,255))
            textRect = text.get_rect()
            textRect.center = ((j*34)+15,(i*34)+15)
            window.blit(text, textRect)

        const = const + 11

    roller1 = font.render("player 1(red) roll: "+str(add1),True,(0,0,0),(255,255,255))
    roller2 = font.render("player 2(blue) roll: "+str(add2),True,(0,0,0),(255,255,255))
    rolRect1 = text.get_rect()
    rolRect1.center = (150,400)
    rolRect2 = text.get_rect()
    rolRect2.center = (150,430)
    window.blit(roller1,rolRect1)
    window.blit(roller2,rolRect2)

    pygame.draw.rect(window,(255,0,0),(calc_column(player1)*34,calc_row(player1)*34,34,34),5)
    pygame.draw.rect(window,(0,0,255),(calc_column(player2)*34,calc_row(player2)*34,34,34),5)

    #draw snake
    pygame.draw.rect(window,(0,255,0),(9*35,9*32,12,28))

    #turn variable is to determine who's turn it is
    turn = turn + 1

    pygame.time.delay(3000)

    #snake back 11 squares because if you land on the second last square it is impossible to win
    if player1 == 109:
        player1 = player1 - 11
    if player2 == 109:
        player2 = player2 - 11

    #win condition check
    if player1 == 110:
        print("Player1 you won!")
        endy = True

    if player2 == 110:
        print("Player2 you won!")
        endy = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()