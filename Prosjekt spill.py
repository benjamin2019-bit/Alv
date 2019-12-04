
import pygame
pygame.init()

display_width = 800
display_height = 600

win = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Nissen og alven Onkel Edition")

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (34,139,34)

elfimg = pygame.image.load("elf.png").convert()

'''
nisseimg = pygame.image.load("bilde.png").convert()
'''

font = pygame.font.Font("freesansbold.ttf", 32)


def tekst(t, X, Y):
    text = font.render(t, True, red, black)
    textRect = text.get_rect()
    textRect.center = (X, Y)
    win.blit(text, textRect)

def elf(x,y):
    win.blit(elfimg,(x,y))
    
x = (display_width*0.45)
y = (display_height*0.8)
width = 40
height = 60
vel = 15

hovedtekstx = display_width//2
hovedteksty = display_height//4
Tekst_1x = display_width//5
Tekst_1y = display_height*0.6//1
Tekst_2x = display_width*0.7//1
Tekst_2y = display_height*0.6//1
Tekst_1xL = [Tekst_1x, Tekst_1x-100]
Tekst_1yL = [Tekst_1y, Tekst_1y-50]
Tekst_2xL = [Tekst_2x, Tekst_2x-100]
Tekst_2yL = [Tekst_2y, Tekst_2y-50]

Lvl1=True
Lvl2=False
Lvl3=False
Lvl4=False
Lvl5=False
Lvl6=False
Lvl7=False
Lvl8=False

nissegreier = {"Lvl1": True}


nakennisse = 0
nisseLvl=0

 
menu = 1
run = True
game = 0


def valgtre(a,b):
    global x
    global y
    global nakennisse
    global Lvl1
    global Lvl2
    global Lvl3
    global Lvl4
    global Lvl5
    global Lvl6
    global Lvl7
    global Lvl8
    global nisseLvl
    if Tekst_2xL[1]<x<Tekst_2xL[0] and Tekst_2yL[1]<y<Tekst_2yL[0]:
        x = (display_width*0.45)
        y = (display_height*0.8)
        win.fill(black)
        Lvl1=False
        Lvl2=True
        
        if b:
            nakennisse+=1
            nisseLvl=True
            Lvl2=False
                    
    if Tekst_1xL[1]<x<Tekst_1xL[0] and Tekst_1yL[1]<y<Tekst_1yL[0]:
        x = (display_width*0.45)
        y = (display_height*0.8)
        win.fill(black)
        Lvl1=False
        Lvl2=True
        
        if a:
            nakennisse+=1
            nisseLvl=True
            Lvl2=False
            
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 800-width-vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y-=vel
    if keys[pygame.K_DOWN] and y< 600-width-vel:        
        y+=vel
    
    win.fill(black)
    
    if menu==1:
        tekst("Alvens Våte Drøm", hovedtekstx, hovedteksty)
        tekst("Start", Tekst_1x, Tekst_1y)
        tekst("Avslutt", Tekst_2x, Tekst_2y)
        if Tekst_2xL[1]<x<Tekst_2xL[0] and Tekst_2yL[1]<y<Tekst_2yL[0]:
            run=False
        if Tekst_1xL[1]<x<Tekst_1xL[0] and Tekst_1yL[1]<y<Tekst_1yL[0]:
            menu = 0
            game = 1
            x = (display_width*0.45)
            y = (display_height*0.8)
    if game==1:
        win.fill(black)
        if Lvl1:
            tekst("Du befinner deg nå i nissens", hovedtekstx, hovedteksty)
            tekst("Målet: Se nissen naken minst 3 ganger", hovedtekstx, hovedteksty+40)
            tekst("Dør", Tekst_1x, Tekst_1y)
            tekst("Dør 2", Tekst_2x, Tekst_2y)
            valgtre(False, True)
        if Lvl2:
            tekst("hei",100,100)
        if nisseLvl:
            tekst("Du fant nissen naken!", hovedtekstx, hovedteksty )
            win.blit(elfimg, display_width//2, display_height//2)
            
    
    elf(x,y)
    
    tabell = 'NISSEN NAKEN = ' + str(nakennisse)
    tekst(tabell, 600, 30)
    
    pygame.display.update()
        
pygame.quit()
quit()          
        
