#trial of stances

from pygame import*
from random import*

screen = display.set_mode((800,600))
RED = (0,128,1)

running = True
walks = ["walk1" + str(x) for x in range(1,7)]
walkpos=0
stances = ["Stance1" + str(x) for x in range(1,6)]
stancepos=0
summons=["summon1" + str(x) for x in range(1,13)]
summonpos=0
attack2= ["attack2" + str(x) for x in range(0,49)]
attack2pos=0
attack3= ["attack3" + str(x) for x in range(0,58)]
jump = ["jump" + str(x) for x in range(0,4)]
crouch = ["crouch0"]
punch = ["punch" + str(x) for x in range(0,4)]
hardpunch = ["hard punch" + str(x) for x in range(0,4)]
combo1=["combo" + str(x) for x in range(0,12)]
keypress=False
direc = "right"
jumppos=50
vu = 50
count=0
count1=1
x=400

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running=False
        elif key.get_pressed():
            keypress=True
    mx,my = mouse.get_pos()
    mb    = mouse.get_pressed()
    screen.fill(RED)
    keys = key.get_pressed()
    if keys[K_t]==1:
        for i in range(0,480):
            screen.fill(RED)
            pic = image.load(summons[summonpos%12]+".jpg")
            y=300-pic.get_size()[1]
            if direc == "right":
                screen.blit(pic,(x,y))
                if summonpos%12>=9:
                    x+=3
            else:
                screen.blit(transform.flip(pic,x,0),(x,y))
                if summonpos%12>=9:
                    x-=3
            if i%40==0:
                summonpos+=1
            display.flip()
    elif keys[K_g]==1 and  keys[K_h]==1 and keypress: #takes some timing of the keys to do this move
        for name in combo1:
            screen.fill(RED)
            pic=image.load(name+".jpg")
            y=300-pic.get_size()[1]
            if direc == "right": screen.blit(pic,(x,y))
            else: screen.blit(transform.flip(pic,x,0),(x,y))
            display.flip()
            time.wait(100)
    elif keys[K_g]==1: #fast attack so no time.wait()
        for name in punch:
            screen.fill(RED)
            pic=image.load(name+".jpg")
            y=300-pic.get_size()[1]
            if direc == "right": screen.blit(pic,(x,y))
            else: screen.blit(transform.flip(pic,x,0),(x,y))
            display.flip()
    elif keys[K_h]==1 and keypress: #hard attack so have to do one at a time
        for name in hardpunch:
            screen.fill(RED)
            pic=image.load(name+".jpg")
            y=300-pic.get_size()[1]
            if direc == "right": screen.blit(pic,(x,y))
            else: screen.blit(transform.flip(pic,x,0),(x,y))
            display.flip()
            time.wait(100)
    
    elif keys[K_u]==1:
        for name in attack3[:43]:
            screen.fill(RED)
            pic = image.load(name+".jpg")
            y=300-pic.get_size()[1]
            if direc == "right": screen.blit(pic,(x,y))
            else: screen.blit(transform.flip(pic,x,0),(x,y))
            display.flip()
            time.wait(100)
        for name in attack3[48:]:
            screen.fill(RED)
            pic = image.load("attack347.jpg")
            y=300-pic.get_size()[1]
            if direc == "right": screen.blit(pic,(x,y))
            else: screen.blit(transform.flip(pic,x,0),(x,y))
            pic = image.load(name+".jpg")
            y=300-pic.get_size()[1]
            if direc == "right": screen.blit(pic,(x+55,y))
            else: screen.blit(transform.flip(pic,x,0),(x-130,y))
            display.flip()
            time.wait(100)
    elif keys[K_y]==1:
        if direc == "right": x1=x+50
        else: x1=x-50
        for name in attack2[:45]:
            screen.fill(RED)
            pic = image.load(name+".jpg")
            y=300-pic.get_size()[1]
            if direc == "right": screen.blit(pic,(x,y))
            else: screen.blit(transform.flip(pic,x,0),(x,y))
            display.flip()
            time.wait(100)
        while x1<800 and x1+50>0:
            for name in attack2[45:]:
                screen.fill(RED)
                pic = image.load("attack242.jpg")
                y=300-pic.get_size()[1]
                if direc == "right": screen.blit(pic,(x,y))
                else: screen.blit(transform.flip(pic,x,0),(x,y))
                pic = image.load(name+".jpg")
                y=300-pic.get_size()[1]
                screen.blit(pic,(x1,y))
                if direc == "right":x1+=30
                else: x1-=30
                display.flip()
                time.wait(100)
    elif keys[K_w]==1 and keypress:
        
        for name in jump:
            screen.fill(RED)
            pic = image.load(name+".jpg")
            jumppos+=vu
            if direc == "right": screen.blit(pic,(x,y-jumppos))
            else: screen.blit(transform.flip(pic,x,0),(x,y-jumppos))
            if keys[K_d] == 1:
                x+=50
            elif keys[K_a] == 1:
                x-=50
            vu-=1
            display.flip()
            time.wait(100)
    elif keys[K_s]==1:
        screen.fill(RED)
        pic = image.load(crouch[0]+".jpg")
        y=300-pic.get_size()[1]
        if direc == "right": screen.blit(pic,(x,y))
        else: screen.blit(transform.flip(pic,x,0),(x,y))
    elif keys[K_d]==1:
        pic = image.load(walks[walkpos%6]+".jpg")
        y=300-pic.get_size()[1]
        screen.blit(pic,(x,y))
        if count%3==0:
            x+=1
        direc="right"
    elif keys[K_a]==1:
        pic = image.load(walks[walkpos%6]+".jpg")
        y=300-pic.get_size()[1]
        screen.blit(transform.flip(pic,x,0),(x,y))
        if count%3==0:
            x-=1
        direc="left"
    elif mb[0]==0:
        pic = image.load(stances[stancepos%5]+".jpg")
        y=300-pic.get_size()[1]
        if direc=="right":
            screen.blit(pic,(x,y))
        else:
            screen.blit(transform.flip(pic,x,0),(x,y))

    
    if count%20==0:
        stancepos+=1
        walkpos+=1
    if x>810:
        x=0
    if x<-10:
        direc="left"
        x=800
    if keys[K_w]!=1:
        jumppos=50
        vu = 50
    count+=1
    keypress=False
    display.flip()
    if keys[K_g]!=1:
        time.wait(3)
quit()
