#trial of stances

from pygame import*
from random import*

screen = display.set_mode((800,600))
RED = (0,128,1)

running = True
walks = ["walk" + str(x) for x in range(1,6)]
walkpos=0
stances = ["stance" + str(x) for x in range(0,5)]
stancepos=0
attack1= ["attack2" + str(x) for x in range(0,8)] + ["attack1" +str(x) for x in range(0,14)]
attack2= ["attack2" + str(x) for x in range(0,22)]
attack2pos=0
attack3= ["attack3" + str(x) for x in range(0,26)]
punch = ["punch" + str(x) for x in range(0,7)]
hardpunch = ["hard punch" + str(x) for x in range(0,7)]
jump = ["jump" + str(x) for x in range(0,4)]
combo = ["combo" + str(x) for x in range(0,13)]
crouch = ["crouch0"]
direc ="right"
first=True
count=0
count1=1
x=400

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running=False
        elif key.get_pressed():
            first=True
    mx,my = mouse.get_pos()
    mb    = mouse.get_pressed()
    screen.fill(RED)
    keys = key.get_pressed()
    
    if keys[K_u]==1:
        for name in attack3:
            screen.fill(RED)
            pic = image.load(name+".jpg")
            x1=x-(pic.get_size()[0])/2.0
            y=300-pic.get_size()[1]
            if attack3.index(name)>20:
                y=randint(0,300)
            if direc == "right": screen.blit(pic,(x1,y))
            else: screen.blit(transform.flip(pic,x,0),(x1,y))
            display.flip()
            time.wait(100)
    elif keys[K_y]==1:
        for name in attack2:
            screen.fill(RED)
            pic = image.load(name+".jpg")
            x1=x-((pic.get_size()[0])/2.0)
            y=300-pic.get_size()[1]
            if direc == "right": screen.blit(pic,(x1,y))
            else: screen.blit(transform.flip(pic,x,0),(x1,y))
            display.flip()
            time.wait(50)
    elif keys[K_t]==1:
        x1=x+100
        for name in attack1[:20]:
            screen.fill(RED)
            pic = image.load(name+".jpg")
            x1=x-((pic.get_size()[0])/2.0)
            y=300-pic.get_size()[1]
            if direc == "right": screen.blit(pic,(x,y))
            else: screen.blit(transform.flip(pic,x,0),(x,y))
            display.flip()
            time.wait(50)
        while x1<800 and x1>0:
            for name in attack1[20:]:
                screen.fill(RED)
                pic = image.load("attack27"+".jpg")
                y=300-pic.get_size()[1]
                if direc == "right": screen.blit(pic,(x,y))
                else: screen.blit(transform.flip(pic,x,0),(x,y))
                pic = image.load(name+".jpg")
                y=300-pic.get_size()[1]
                if direc == "right":
                    screen.blit(pic,(x1,y))
                    x1+=50
                else:
                    screen.blit(transform.flip(pic,x,0),(x1,y))
                    x1-=50
                display.flip()
                time.wait(100)
            
    elif keys[K_w]==1:
        for name in jump:
            screen.fill(RED)
            pic = image.load(name+".jpg")
            y=300-pic.get_size()[1]
            if direc == "right": screen.blit(pic,(x,y-70*jump.index(name)))
            else: screen.blit(transform.flip(pic,x,0),(x,y-70*jump.index(name)))
            if keys[K_d]==1:
                x+=50
            elif keys[K_a]==1:
                x-=50
            display.flip()
            time.wait(90)
    elif keys[K_j]==1:
        screen.fill(RED)
        pic = image.load("guard.jpg")
        y=300-pic.get_size()[1]
        if direc == "right": screen.blit(pic,(x,y))
        else: screen.blit(transform.flip(pic,x,0),(x,y))
        
    elif keys[K_h]==1 and keys[K_g]==1:
        for name in combo:
            screen.fill(RED)
            pic = image.load(name+".jpg")
            y=300-pic.get_size()[1]
            if direc == "right": screen.blit(pic,(x,y))
            else: screen.blit(transform.flip(pic,x,0),(x,y))
            display.flip()
            time.wait(95)
    elif keys[K_g]==1:
        for name in punch:
            screen.fill(RED)
            pic = image.load(name+".jpg")
            y=300-pic.get_size()[1]
            if direc == "right": screen.blit(pic,(x,y))
            else: screen.blit(transform.flip(pic,x,0),(x,y))
            display.flip()
    
    elif keys[K_h]==1:
        for name in hardpunch:
            screen.fill(RED)
            pic = image.load(name+".jpg")
            y=300-pic.get_size()[1]
            if direc == "right": screen.blit(pic,(x,y))
            else: screen.blit(transform.flip(pic,x,0),(x,y))
            display.flip()
            time.wait(100)
    elif keys[K_s]==1:
        screen.fill(RED)
        pic = image.load(crouch[0]+".jpg")
        y=300-pic.get_size()[1]
        if direc == "right": screen.blit(pic,(x,y))
        else: screen.blit(transform.flip(pic,x,0),(x,y))
    elif keys[K_d]==1:
        pic = image.load(walks[walkpos%5]+".jpg")
        y=300-pic.get_size()[1]
        if direc == "right": screen.blit(pic,(x,y))
        else: screen.blit(transform.flip(pic,x,0),(x,y))
        if count%3==0:
            x+=1
        direc="right"
    elif keys[K_a]==1:
        pic = image.load(walks[walkpos%5]+".jpg")
        y=300-pic.get_size()[1]
        if direc == "right": screen.blit(pic,(x,y))
        else: screen.blit(transform.flip(pic,x,0),(x,y))
        if count%3==0:
            x-=1
        direc="left"
    else:
        pic = image.load(stances[stancepos%5]+".jpg")
        y=300-pic.get_size()[1]
        if direc == "right": screen.blit(pic,(x,y))
        else: screen.blit(transform.flip(pic,x,0),(x,y))
    
    if count%20==0:
        stancepos+=1
        walkpos+=1
    if x>810:
        x=0
    count+=1
    display.flip()
    if keys[K_g]!=1:
        time.wait(3)
quit()
