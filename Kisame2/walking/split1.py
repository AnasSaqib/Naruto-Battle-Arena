from pygame import*
from random import*
from math import*

running = True
name = "Akatsuki"
newName = "attack1"
pic = image.load(name+".png")
wid,hi = pic.get_size()
cnt = 10
counter = 0
press = False
posx,posy = 127,788
xPos,yPos = 0,0
secPosX,secPosY = 0,0
screen = display.set_mode(pic.get_size())
first =True
first1=False
while running:
    keys = key.get_pressed()
    for evt in event.get():
        if evt.type == "QUIT" or keys[K_ESCAPE]:
            running = quit()
        elif MOUSEBUTTONDOWN:
            first1=True
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    screen.blit(pic,(xPos,yPos))
    if keys[K_UP]:
        yPos-=5
    if keys[K_DOWN]:
        yPos+=5
    if keys[K_LEFT]:
        xPos-=5
    if keys[K_RIGHT]:
        xPos+=5
    if mb[0]==1 and press == False:
        posx,posy = mx,my
        secPosX,secPosY = mx,my
        press = True
    if first:
        yPos-=3500
        first=False
    
    
    print mx,my
    posx,posy = 37,518
    if mb[0]==1 and first1:
        posx=mx
        saveRect = screen.subsurface((posx,posy-100,175,100)).copy()
        saveImage = image.save(saveRect,newName+str(cnt)+".jpg")
        cnt+=1
        print " HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEELL"
    first1=False
    display.flip()
quit()

"""

    screen.blit(pic,(xPos,yPos))
##    draw.image(pic,(100,200))
    if keys[K_UP]:
        yPos-=5
    if keys[K_DOWN]:
        yPos+=5
    if keys[K_LEFT]:
        xPos-=5
    if keys[K_RIGHT]:
        xPos+=5
    if mb[0]==1 and press == False:
        posx,posy = mx,my
        secPosX,secPosY = mx,my
        press = True
    if press == True:
        secPosX,secPosY = mx,my
        draw.rect(screen,(0,0,255),(posx,posy,secPosX-posx,secPosY-posy),1)
    if mb[0] == 0 and press == True:
        press = False
##        newName = name+str(cnt)
        secPosX,secPosY = mx,my
        #saveRect = screen.subsurface((posx,posy,secPosX-posx,secPosY-posy)).copy()
"""
