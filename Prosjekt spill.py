
import pygame
pygame.init()

display_width = 800
display_height = 600

win = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Alvens våte drøm")

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (34,139,34)

elfimg = pygame.image.load("elf.png").convert()

'''
nisseimg = pygame.image.load("bilde.png").convert()
'''




def tekst(t, X, Y, F):
    font = pygame.font.Font("freesansbold.ttf", F)
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

Lvl = {"1": True, "2":False, "3":False, "4":False, 
               "5":False, "6":False, "7":False, "8":False}


nakennisse = 0
nisseLvl=0
tabell = 'NISSEN NAKEN = ' + str(nakennisse)
tabell2 = "Du må nå se nissen naken "+str(3-nakennisse)+" ganger til"

 
menu = 1
run = True
game = 0
Level = 0


def nTabell():
    global nakennisse
    global tabell
    global tabell2
    nakennisse +=1
    tabell = 'NISSEN NAKEN = ' + str(nakennisse)
    tabell2 = "Du må nå se nissen naken "+str(3-nakennisse)+" ganger til"

def valgtre(a,b,c):
    global x
    global y
    global nakennisse
    global nisseLvl
    global Lvl
    if Tekst_2xL[1]<x<Tekst_2xL[0] and Tekst_2yL[1]<y<Tekst_2yL[0]:
        x = (display_width*0.45)
        y = (display_height*0.8)
        win.fill(black)
        Lvl[str(c-1)]=False
        Lvl[str(c)]=True
        if b:
            nTabell()
            nisseLvl=True
            Lvl[str(c)]=False
    if Tekst_1xL[1]<x<Tekst_1xL[0] and Tekst_1yL[1]<y<Tekst_1yL[0]:
        x = (display_width*0.45)
        y = (display_height*0.8)
        win.fill(black)
        Lvl[str(c-1)]=False
        Lvl[str(c)]=True
        if a:
            nTabell()
            nisseLvl=True
            Lvl[str(c)]=False

def nisseLvl2(a):
    global nisseLvl
    global Lvl
    global x
    global y
    if 500<x<600 and 400<y<500:
                win.fill(black)
                nisseLvl=False
                Lvl[a] = True
                x = (display_width*0.45)
                y = (display_height*0.8)
            
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
        tekst("Alvens Våte Drøm", hovedtekstx, hovedteksty, 32)
        tekst("Start", Tekst_1x, Tekst_1y, 32)
        tekst("Avslutt", Tekst_2x, Tekst_2y, 32)
        if Tekst_2xL[1]<x<Tekst_2xL[0] and Tekst_2yL[1]<y<Tekst_2yL[0]:
            run=False
        if Tekst_1xL[1]<x<Tekst_1xL[0] and Tekst_1yL[1]<y<Tekst_1yL[0]:
            menu = 0
            game = 1
            x = (display_width*0.45)
            y = (display_height*0.8)
    if game==1:
        win.fill(black)
        if Lvl["1"]:
            Level=2
            tekst("Du befinner deg nå i nissens", hovedtekstx, hovedteksty, 32)
            tekst("Målet: Se nissen naken minst 3 ganger", hovedtekstx, hovedteksty+40, 32)
            tekst("Dør", Tekst_1x, Tekst_1y, 32)
            tekst("Dør 2", Tekst_2x, Tekst_2y, 32)
            valgtre(False, True, 2)
        if Lvl["2"]:
            Level=3
            tekst("hei",100,100, 20)
        if nisseLvl:
            tekst("Du fant nissen naken!", hovedtekstx, hovedteksty, 32)
            elf(display_width//2, display_height//2)
            tekst(tabell2, 200, 550, 15)
            tekst("Løp Videre", 600, 500, 20)
            nisseLvl2(str(Level))
                
            
    
    elf(x,y)
    tekst(tabell, 600, 30, 25)
    
    pygame.display.update()
        
pygame.quit()
quit()          
        