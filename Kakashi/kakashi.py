#Kakashi

from pygame import*
from random import*
screen = display.set_mode((800,600))
COL = (0,0,0)
running = True
walks = ["walk" + str(x) for x in range(0,5)]
walksleft = ["walkl" + str(x) for x in range(0,5)]
walkpos=0
stances = ["stance" + str(x) for x in range(0,4)]
stancepos=0
jumps = ["jump" + str(x) for x in range(0,4)]
jumpsleft = ["jumpl" + str(x) for x in range(0,4)]
jumppos=0
crouches = ["crouch" + str(x) for x in range(0,2)]
crouchesleft = ["crouchl" + str(x) for x in range(0,2)]
incrouch=False
lightningblade= ["lightningblade" + str(x) for x in range(0,28)]
summon= ["summon" + str(x) for x in range(0,16)]
summonpos=12
fsummon= ["fsummon" + str(x) for x in range(0,10)]
fsummonpos=0
cattack=["cattack" + str(x) for x in range(0,13)]
cattackpos=0
count=0
x=400
facing="r"

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running=False
    mx,my = mouse.get_pos()
    mb    = mouse.get_pressed()
    for evt in event.get():
        if evt.type == "QUIT" or keys[K_ESCAPE]:
            running = quit()
    screen.fill(COL)
    keys = key.get_pressed()
    if keys[K_g]==1:
        pic=image.load(stances[0]+".png")
        y=300-pic.get_size()[1]
        screen.blit(pic,(x,y))
        display.flip()
        time.wait(100)
        for i in range(0,260):
            screen.fill(COL)
            pic = image.load(cattack[cattackpos%13]+".png")
            y=300-pic.get_size()[1]
            screen.blit(pic,(x,y))
            if i%20==0:
                cattackpos+=1
            display.flip()    
        
    if keys[K_w]==1 and keys[K_d]==1:
            pic = image.load(stances[0]+".png")
            y=300-pic.get_size()[1]
            screen.blit(pic,(x,y))
            display.flip()
            time.wait(250)
            jy=300-pic.get_size()[1]-145
            for i in range(0,160):
                screen.fill(COL)
                pic = image.load(jumps[jumppos%4]+".png")
                screen.blit(pic,(x,jy))
                if i%40==0:
                    x+=25
                    jumppos+=1
                    jy-=10
                display.flip()
    elif keys[K_w]==1 and keys[K_a]==1:
        pic = image.load(stances[0]+".png")
        y=300-pic.get_size()[1]
        screen.blit(transform.flip(pic,x,0),(x,y))
        display.flip()
        time.wait(250)
        jy=300-pic.get_size()[1]-145
        for i in range(0,160):
            screen.fill(COL)
            pic = image.load(jumps[jumppos%4]+".png")
            screen.blit(transform.flip(pic,x,0),(x,jy))
            if i%40==0:
                x-=25
                jumppos+=1
                jy-=10
            display.flip()
            
    elif keys[K_w]==1:
        pic = image.load(stances[0]+".png")
        y=300-pic.get_size()[1]
        if facing=="r":
            screen.blit(pic,(x,y))
        else:
            screen.blit(transform.flip(pic,x,0),(x,y))
        display.flip()
        time.wait(250)
        for i in range(0,160):
            screen.fill(COL)
            pic = image.load(jumps[jumppos%4]+".png")
            jy=300-pic.get_size()[1]-145
            if facing=="r":
                screen.blit(pic,(x,jy))
            else:
                screen.blit(transform.flip(pic,x,0),(x,jy)) 
            if i%40==0:
                jumppos+=1
                jy-=10
            display.flip()
        
    
    elif keys[K_s]==1:
        screen.fill(COL)
        if incrouch==False:
            incrouch=True
            pic = image.load(crouches[0]+".png")
            y=300-pic.get_size()[1]
            if facing=="r":
                screen.blit(pic,(x,y))
            else:
                screen.blit(transform.flip(pic,x,0),(x,y))
        if incrouch==True:
            pic = image.load(crouches[1]+".png")
            y=300-pic.get_size()[1]
            if facing=="r":
                screen.blit(pic,(x,y))
            else:
                screen.blit(transform.flip(pic,x,0),(x,y))
                
       
    elif keys[K_t]==1:
        summondis=50
        for i in summon:
            if summon.index(i)>11:
                break    
            else:
                screen.fill(COL)
                pic = image.load(i+".png") 
                y=300-pic.get_size()[1]
                if facing=="r":
                    screen.blit(pic,(x,y))
                else:
                    screen.blit(transform.flip(pic,x,0),(x,y))
                display.flip()
                time.wait(100)
        while x+summondis+pic.get_size()[0]<=800:
                screen.fill(COL)
                pic = image.load(summon[summonpos]+".png") 
                y=300-pic.get_size()[1]
                ys=300-image.load(summon[11]+".png").get_size()[1]
                if facing=="r":
                    screen.blit(image.load(summon[11]+".png"),(x,ys))
                    screen.blit(pic,(x+summondis,y))
                else:
                    screen.blit(transform.flip(image.load(summon[11]+".png"),x,0),(x,ys))
                    screen.blit(transform.flip(pic,x,0),(x-summondis,y))
                display.flip()
                time.wait(150)
                summondis+=50
                summonpos+=1
                if summonpos==16:
                    summonpos=12
    elif keys[K_y]:
        fsummondis=50
        for i in summon:
            if summon.index(i)>11:
                break    
            else:
                screen.fill(COL)
                pic = image.load(i+".png") 
                y=300-pic.get_size()[1]
                if facing=="r":
                    screen.blit(pic,(x,y))
                else:
                    screen.blit(transform.flip(pic,x,0),(x,y))
                display.flip()
                time.wait(100)
        if facing=="r":
            while x+fsummondis+pic.get_size()[0]<=800:
                screen.fill(COL)
                pic = image.load(fsummon[fsummonpos]+".png") 
                y=300-pic.get_size()[1]
                ys=300-image.load(summon[11]+".png").get_size()[1]
                screen.blit(image.load(summon[11]+".png"),(x,ys))
                screen.blit(pic,(x+fsummondis,y))
                display.flip()
                time.wait(100)
                fsummondis+=50
                fsummonpos+=1
                if fsummonpos==10:
                    fsummonpos=0
        else:
            while x-fsummondis>=0:
                screen.fill(COL)
                pic = image.load(fsummon[fsummonpos]+".png") 
                y=300-pic.get_size()[1]
                ys=300-image.load(summon[11]+".png").get_size()[1]
                screen.blit(transform.flip(image.load(summon[11]+".png"),x,0),(x,ys))
                screen.blit(transform.flip(pic,x,0),(x-fsummondis,y))                            
                display.flip()
                time.wait(100)
                fsummondis+=50
                fsummonpos+=1
                if fsummonpos==10:
                    fsummonpos=0
    elif keys[K_u]==1:
        d=x
        for i in lightningblade:
            
            if lightningblade.index(i)>21:          
                screen.fill(COL)
                pic = image.load(i+".png") 
                y=300-pic.get_size()[1]
                screen.blit(pic,(d+280,y))
                display.flip()
                time.wait(200)
            else:
                screen.fill(COL)
                pic = image.load(i+".png")
                y=300-pic.get_size()[1]
                xsp = (pic.get_size()[0])/2.0
                screen.blit(pic,(d-xsp,y))
                display.flip()
                time.wait(200)
        x+=280
    elif keys[K_d]==1:
        facing="r"
        if walkpos%5==1 or walkpos%5==4 or walkpos%5==2:
            pic = image.load(walks[walkpos%5]+".png")
            y=300-pic.get_size()[1]
            screen.blit(pic,(x+8,y))    
        else:
            pic = image.load(walks[walkpos%5]+".png")
            y=300-pic.get_size()[1]
            screen.blit(pic,(x,y))
        if count%3==0:
            x+=1
    elif keys[K_a]==1:
        facing="l"
        if walkpos%5==1 or walkpos%5==4 or walkpos%5==2:
            pic = image.load(walks[walkpos%5]+".png")
            y=300-pic.get_size()[1]
            screen.blit(transform.flip(pic,x,0),(x,y))    
        else:
            pic = image.load(walks[walkpos%5]+".png")
            y=300-pic.get_size()[1]
            screen.blit(transform.flip(pic,x,0),(x,y))
        if count%3==0:
            x-=1
    else:
        pic = image.load(stances[stancepos%4]+".png")
        y=300-pic.get_size()[1]
        if facing=="r":
            screen.blit(pic,(x,y))
        else:
            screen.blit(transform.flip(pic,x,0),(x,y))

    if keys[K_s]==0:
        incrouch==True
    if count%20==0:
        stancepos+=1
        walkpos+=1
        
       
    if x>810:
        x=0
    summonpos=12
    fsummonpos=0
    count+=1
    display.flip()
    time.wait(5)
quit()
"""    
            elif lightningblade.index(i)==4 or lightningblade.index(i)==5 or lightningblade.index(i)==6:
                if lightningblade.index(i)==5:
                    screen.fill(COL)
                    pic = image.load(i+".png") 
                    y=300-pic.get_size()[1]
                    screen.blit(pic,(d-5,y+5))
                    display.flip()
                    time.wait(800)
                elif lightningblade.index(i)==6:
                    screen.fill(COL)
                    pic = image.load(i+".png") 
                    y=300-pic.get_size()[1]
                    screen.blit(pic,(d-10,y+5))
                    display.flip()
                    time.wait(800)
                else:
                    screen.fill(COL)
                    pic = image.load(i+".png") 
                    y=300-pic.get_size()[1]
                    screen.blit(pic,(d-5,y+10))
                    display.flip()
                    time.wait(800)
             
            elif lightningblade.index(i)==4:
                screen.fill(COL)
                pic = image.load(i+".png") 
                y=300-pic.get_size()[1]
                screen.blit(pic,(d-5,y+5))
                display.flip()
                time.wait(400)
"""
