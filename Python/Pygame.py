import pygame, sys, random, time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Morpion")

image = pygame.image.load("background.jpg").convert_alpha()
image2 = pygame.image.load("croix.png").convert_alpha()
image3 = pygame.image.load("rond.png").convert_alpha()

joueur1 = 0
joueur2 = 1
map = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]





def main():
    joueur_actif = joueur1
    img = image2
    print("call main")
    screen.blit(image, (0, 0))

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        

        if pygame.mouse.get_pressed() == (1,0,0):
            x,y = pygame.mouse.get_pos()
            print(x, y)
            if 600 > x > 400 and 600 > y > 400 :
                if map[2][2] == "_" :
                    map[2][2] = str(joueur_actif)
                    screen.blit(img, (400, 400))
                    if joueur_actif == joueur1 :
                        joueur_actif = joueur2
                        img = image3
                        print("joueur 2")
                    else :
                        joueur_actif = joueur1
                        img = image2
                        print("joueur 1")
            
            if 400 > x > 200  and 600 > y > 400 :
                if map[2][1] == "_" :
                    map[2][1] = str(joueur_actif)
                    screen.blit(img, (200, 400))
                    if joueur_actif == joueur1 :
                        joueur_actif = joueur2
                        img = image3
                        print("joueur 2")
                    else :
                        joueur_actif = joueur1
                        img = image2
                        print("joueur 1")
            
            if 200 > x > 0 and 600 > y > 400 :
                if map[2][0] == "_" :
                    map[2][0] = str(joueur_actif)
                    screen.blit(img, (0, 400))
                    if joueur_actif == joueur1 :
                        joueur_actif = joueur2
                        img = image3
                        print("joueur 2")
                    else :
                        joueur_actif = joueur1
                        img = image2
                        print("joueur 1")
            if 600 > x > 400 and 400 > y > 200 :
                if map[1][2] == "_" :
                    map[1][2] = str(joueur_actif)
                    screen.blit(img, (400, 200))
                    if joueur_actif == joueur1 :
                        joueur_actif = joueur2
                        img = image3
                        print("joueur 2")
                    else :
                        joueur_actif = joueur1
                        img = image2
                        print("joueur 1")
            
            if 400 > x > 200  and 400 > y > 200 :
                if map[1][1] == "_" :
                    map[1][1] = str(joueur_actif)
                    screen.blit(img, (200, 200))
                    if joueur_actif == joueur1 :
                        joueur_actif = joueur2
                        img = image3
                        print("joueur 2")
                    else :
                        joueur_actif = joueur1
                        img = image2
                        print("joueur 1")
            
            if 200 > x > 0 and 400 > y > 200 :
                if map[1][0] == "_" :
                    map[1][0] = str(joueur_actif)
                    screen.blit(img, (0, 200))
                    if joueur_actif == joueur1 :
                        joueur_actif = joueur2
                        img = image3
                        print("joueur 2")
                    else :
                        joueur_actif = joueur1
                        img = image2
                        print("joueur 1")
            if 600 > x > 400 and 200 > y > 0 :
                if map[0][2] == "_" :
                    map[0][2] = str(joueur_actif)
                    screen.blit(img, (400, 0))
                    if joueur_actif == joueur1 :
                        joueur_actif = joueur2
                        img = image3
                        print("joueur 2")
                    else :
                        joueur_actif = joueur1
                        img = image2
                        print("joueur 1")
            
            if 400 > x > 200  and 200 > y > 0 :
                if map[0][1] == "_" :
                    map[0][1] = str(joueur_actif)
                    screen.blit(img, (200, 0))
                    if joueur_actif == joueur1 :
                        joueur_actif = joueur2
                        img = image3
                        print("joueur 2")
                    else :
                        joueur_actif = joueur1
                        img = image2
                        print("joueur 1")
            
            if 200 > x > 0 and 200 > y > 0 :
                if map[0][0] == "_" :
                    map[0][0] = str(joueur_actif)
                    screen.blit(img, (0, 0))
                    if joueur_actif == joueur1 :
                        joueur_actif = joueur2
                        img = image3
                        print("joueur 2")
                    else :
                        joueur_actif = joueur1
                        img = image2
                        print("joueur 1")
            
            print(map)
            
            if map[0][0] == map[0][1] == map[0][2] and map[0][0] != "_":
                
                print("VOILA")
                pygame.quit()
                sys.exit()

            
            if map[1][0] == map[1][1] == map[1][2] and map[1][0] != "_":
                
                print("VOILA")
                pygame.quit()
                sys.exit()
            
            if map[2][0] == map[2][1] == map[2][2] and map[2][0] != "_":
                
                print("VOILA")
                pygame.quit()
                sys.exit()
            
            if map[0][0] == map[1][0] == map[2][0] and map[0][0] != "_":
                
                print("VOILA")
                pygame.quit()
                sys.exit()
            
            if map[0][1] == map[1][1] == map[2][1] and map[0][1] != "_":
                
                print("VOILA")
                pygame.quit()
                sys.exit()
            
            if map[0][2] == map[1][2] == map[2][2] and map[0][2] != "_":
                
                print("VOILA")
                pygame.quit()
                sys.exit()
            
            if map[0][0] == map[1][1] == map[2][2] and map[0][0] != "_":
                
                print("VOILA")
                pygame.quit()
                sys.exit()
            
            if map[0][2] == map[1][1] == map[2][0] and map[0][2] != "_":
                
                print("VOILA")
                pygame.quit()
                sys.exit()
  

        pygame.display.flip()

        clock.tick(60)
    pygame.quit()



main()